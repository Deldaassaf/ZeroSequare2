from State import State
class Stage1(State):
    def __init__(self):
        board_size = (8, 8)
        goals = [(6, 6)]  
        initial_states = [(1, 1)]  
        
        super().__init__(board_size=board_size, goals=goals, initial_states=initial_states)
    
    def display_stage(self):
        print("Stage One")
        self.print_board()


stage1 = Stage1()
stage1.display_stage()
