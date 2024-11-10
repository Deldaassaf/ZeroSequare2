from State import State
class Stage2(State):
    def __init__(self):
        board_size = (8, 8)
        goals = [(6, 2)]  
        initial_states = [(1, 1)]

        super().__init__(board_size=board_size, goals=goals, initial_states=initial_states)
        
        self.board[2][3] = 0
        self.board[3][4] = 0
        self.board[4][5] = 0
        self.board[5][2] = 0
        self.board[6][3] = 0

    def display_stage(self):
        print("Stage 2 :")
        self.print_board()

stage2 = Stage2()
stage2.display_stage()
