import random
import sys
from secret import FLAG

class MazeGame:
    def __init__(self):
        self.inner_size = 7
        self.size = self.inner_size + 2
        self.player_pos = [1, 1]
        self.game_over = False
        self.generate_maze()

    def generate_maze(self):
        while True:
            self.maze = [[1 for _ in range(self.size)] for _ in range(self.size)]
            stack = []
            current = [1, 1]
            visited = set()

            self.maze[1][1] = 0
            self.maze[self.size-2][self.size-2] = 0

            stack.append(current)
            visited.add(tuple(current))

            while stack:
                current = stack[-1]
                possible_moves = []

                for dx, dy in [(0, 2), (2, 0), (0, -2), (-2, 0)]:
                    new_x = current[0] + dx
                    new_y = current[1] + dy

                    if (1 <= new_x < self.size-1 and
                        1 <= new_y < self.size-1 and
                        tuple([new_x, new_y]) not in visited):
                        possible_moves.append((dx, dy))

                if possible_moves:
                    dx, dy = random.choice(possible_moves)
                    new_x = current[0] + dx
                    new_y = current[1] + dy

                    self.maze[current[0] + dx//2][current[1] + dy//2] = 0
                    self.maze[new_x][new_y] = 0

                    stack.append([new_x, new_y])
                    visited.add(tuple([new_x, new_y]))
                else:
                    stack.pop()

            if self.check_path():
                break

    def check_path(self):
        visited = set()
        stack = [(1, 1)]

        while stack:
            current = stack.pop()
            if current == (self.size-2, self.size-2):
                return True

            if current not in visited:
                visited.add(current)
                x, y = current

                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    new_x, new_y = x + dx, y + dy
                    if (1 <= new_x < self.size-1 and
                        1 <= new_y < self.size-1 and
                        self.maze[new_x][new_y] == 0):
                        stack.append((new_x, new_y))

        return False

    def display(self):
        # os.system('clear')
        for i in range(self.size):
            for j in range(self.size):
                if [i, j] == self.player_pos:
                    print('P', end=' ')
                elif [i, j] == [self.size-2, self.size-2]:
                    print('E', end=' ')
                elif self.maze[i][j] == 1:
                    print('█', end=' ')
                else:
                    print(' ', end=' ')
            print()

    def move(self, direction):
        new_pos = self.player_pos.copy()

        if direction == 'w':
            new_pos[0] -= 1
        elif direction == 's':
            new_pos[0] += 1
        elif direction == 'a':
            new_pos[1] -= 1
        elif direction == 'd':
            new_pos[1] += 1

        # 檢查新位置
        if (0 <= new_pos[0] < self.size and
            0 <= new_pos[1] < self.size):
            if self.maze[new_pos[0]][new_pos[1]] == 0:
                self.player_pos = new_pos
                return True
            else:
                self.game_over = True  # 碰到牆壁，遊戲結束
        return False

    def is_complete(self):
        return self.player_pos == [self.size-2, self.size-2]

def Start():
    game = MazeGame()
    while True:
        game.display()

        if game.game_over:
            print("You hit a wall! Game over!")
            break

        if game.is_complete():
            print("\nNEXT Challenge！\n")
            break

        move = input("move: ").lower()

        if move == 'q':
            print("GAME OVER！")
            sys.exit()
        elif move in ['w', 'a', 's', 'd']:
            game.move(move)
            print('='*30)
        else:
            print("Invalid input! Please use W/A/S/D to move or Q to quit.")


def main():
    print("""\033[33m
███╗   ███╗ █████╗ ███████╗███████╗     ██████╗  █████╗ ███╗   ███╗███████╗
████╗ ████║██╔══██╗╚══███╔╝██╔════╝    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
██╔████╔██║███████║  ███╔╝ █████╗      ██║  ███╗███████║██╔████╔██║█████╗
██║╚██╔╝██║██╔══██║ ███╔╝  ██╔══╝      ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝
██║ ╚═╝ ██║██║  ██║███████╗███████╗    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
        """)
    print('\033[32m='*30)
    print("Welcome to the Maze Game!")
    print("Use W/A/S/D to move, Q to quit")
    print("P is the player's position, E is the endpoint")
    print("Note: The game ends immediately if you hit a wall!")
    print('='*30)
    print("\033[0m")

    for i in range (100):
        print('='*8,f"challenge {i+1} ",'='*8,'\n')
        Start()

    print("\033[33m\n")
    print("+----------------------------+")
    print(f"| {FLAG} |")
    print("+----------------------------+")

try:
    main()
except:
    sys.exit()
