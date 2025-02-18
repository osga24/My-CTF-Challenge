const WebSocket = require('ws');
const GameRoom = require('./gameRoom');

const wss = new WebSocket.Server({ port: 8080 });
const rooms = new Map();

const ROOM_TIMEOUT = 30 * 60 * 1000;
const CLEANUP_INTERVAL = 5 * 60 * 1000;

function cleanupRooms() {
	const now = Date.now();
	for (const [roomId, room] of rooms.entries()) {
		if (now - room.lastActivity > ROOM_TIMEOUT ||
			room.ws.readyState === WebSocket.CLOSED) {
			rooms.delete(roomId);
			console.log(`Cleaned up room: ${roomId}`);
		}
	}
}

setInterval(cleanupRooms, CLEANUP_INTERVAL);

wss.on('connection', (ws) => {
	const roomId = Date.now().toString();
	const gameRoom = new GameRoom();

	rooms.set(roomId, {
		ws,
		gameRoom,
		lastActivity: Date.now()
	});

	console.log(`New connection established: ${roomId}`);

	ws.send(JSON.stringify({
		status: 'connected',
		message: `Welcome! Room ID: ${roomId}. You have 3 attempts to guess a number between 0-10000.`
	}));

	ws.on('message', (message) => {
		const room = rooms.get(roomId);
		if (!room) return;

		room.lastActivity = Date.now();

		try {
			const data = JSON.parse(message);
			let response;

			if (data.type === 'guess') {
				response = room.gameRoom.guess(data.number);
			} else if (data.type === 'backdoor') {
				response = room.gameRoom.getSecretAnswer(data.command);
			} else {
				response = { status: 'error', message: 'Invalid message type' };
			}

			ws.send(JSON.stringify(response));

			if (response.status === 'win' || response.status === 'lose') {
				room.lastActivity = Date.now() - (ROOM_TIMEOUT - 5 * 60 * 1000);
			}
		} catch (error) {
			ws.send(JSON.stringify({
				status: 'error',
				message: 'Invalid message format'
			}));
		}
	});

	ws.on('close', () => {
		rooms.delete(roomId);
		console.log(`Connection closed: ${roomId}`);
	});

	const pingInterval = setInterval(() => {
		if (ws.readyState === WebSocket.OPEN) {
			ws.ping();
		} else {
			clearInterval(pingInterval);
		}
	}, 30000);
});

console.log('WebSocket server is running on port 8080');
