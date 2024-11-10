import heapq

class State:
    def __init__(self, board_size=(6, 6), goals=[], initial_states=[]):
        self.board = [[1 for _ in range(board_size[1])] for _ in range(board_size[0])]
        self.goals = goals  # Goals
        self.initial_states = initial_states  # Initial States
        self.game_over = False
        
        # Barrier
        for i in range(board_size[0]):
            for j in range(board_size[1]):
                if i == 0 or i == board_size[0] - 1 or j == 0 or j == board_size[1] - 1:
                    self.board[i][j] = 0
        self.board[1][4] = 0 
        self.board[3][2] = 0 
        self.board[4][4] = 0 
        
        for goal in goals:
            self.board[goal[0]][goal[1]] = "W"
        for initial in initial_states:
            self.board[initial[0]][initial[1]] = "I"

    # Print Board
    def print_board(self):
        for row in self.board:
            print(" ".join(str(cell) for cell in row))
        print("n" + "-"*20 + "n")

    # Find Neighbors
    def next_state(self, i, j):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(self.board) and 0 <= nj < len(self.board[0]) and self.board[ni][nj] != 0:
                neighbors.append((ni, nj))
        return neighbors
    
    # Check if all initial states are at goals
    def check_goal(self):
        return all((i, j) in self.goals for i, j in self.initial_states)

    # Move
    def move(self, direction):
        if self.game_over:
            print("The game is done, You cannot move.")
            return
        
        directions_map = {
            "right": (0, 1),
            "left": (0, -1),
            "up": (-1, 0),
            "down": (1, 0)
        }
        di, dj = directions_map[direction]

        new_positions = []
        for idx, (i, j) in enumerate(self.initial_states):
            if (i, j) in self.goals:
                new_positions.append((i, j))
                continue

            while 0 <= i + di < len(self.board) and 0 <= j + dj < len(self.board[0]):
                ni, nj = i + di, j + dj
                if self.board[ni][nj] == 0 or (ni, nj) in new_positions:
                    break
                if (ni, nj) in self.goals:  
                    i, j = ni, nj
                    self.board[self.initial_states[idx][0]][self.initial_states[idx][1]] = 1
                    self.board[i][j] = "I"
                    new_positions.append((i, j))
                    self.board[self.goals[self.goals.index((ni, nj))][0]][self.goals[self.goals.index((ni, nj))][1]] = 1
                    break
                if self.board[ni][nj] == 1:
                    i, j = ni, nj

            self.board[self.initial_states[idx][0]][self.initial_states[idx][1]] = 1
            self.board[i][j] = "I"
            new_positions.append((i, j))

        self.initial_states = new_positions

        print("After move")
        self.print_board()

        if self.check_goal():
            self.game_over = True
            print("Congratulations! All goals have been reached.")

        return self.initial_states
