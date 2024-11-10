from State import State
class Stage3(State):
    def __init__(self):
        board_size = (8, 8)
        goals = [(4, 2), (6, 6)]  
        initial_states = [(1, 1), (2, 2)]  
        
        super().__init__(board_size=board_size, goals=goals, initial_states=initial_states)
        
        self.board[3][3] = 0
        self.board[4][4] = 0
        self.board[5][5] = 0
        self.board[6][2] = 0
        self.board[2][5] = 0

    def display_stage(self):
        print("Stage 3:")
        self.print_board()

stage3 = Stage3()
stage3.display_stage()
