class GameRoom {
	constructor() {
		this.answer = Math.floor(Math.random() * 10001);
		this.attempts = 0;
		this.maxAttempts = 3;
		this.isGameOver = false;
	}

	guess(number) {
		if (this.isGameOver || this.attempts >= this.maxAttempts) {
			return { status: 'error', message: 'Game Over!' };
		}

		this.attempts++;
		const guess = parseInt(number);

		if (isNaN(guess) || guess < 0 || guess > 10000) {
			return { status: 'error', message: 'Invalid number! Please enter a number between 0-10000.' };
		}

		if (guess === this.answer) {
			this.isGameOver = true;
			return {
				status: 'win',
				message: `Congratulations! The answer is ${this.answer}`,
				flag: process.env.FLAG
			};
		}

		if (this.attempts >= this.maxAttempts) {
			this.isGameOver = true;
			return {
				status: 'lose',
				message: `Game Over! You've used all ${this.maxAttempts} attempts. The answer was ${this.answer}`
			};
		}

		return {
			status: 'continue',
			message: `Wrong! The number is ${guess < this.answer ? 'bigger' : 'smaller'}. ${this.maxAttempts - this.attempts} attempts remaining.`
		};
	}

	getSecretAnswer(command) {
		if (command === 'SHOW_ME_THE_ANSWER_PLZ') {
			return { status: 'secret', answer: this.answer };
		}
		return { status: 'error', message: 'Invalid command' };
	}
}

module.exports = GameRoom;
