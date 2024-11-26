from State import State

class DFSRecursive:
    def __init__(self):
        self.visited = set()
        self.nodes_visited = 0

    def dfs(self, state_obj, current_position, direction, path=None):
        if not isinstance(state_obj, State):
            raise ValueError("state_obj يجب أن يكون كائن من فئة State.")

        if path is None:
            path = [current_position]
        else:
            path.append(current_position)

        self.visited.add(current_position)
        self.nodes_visited += 1

        new_state = state_obj.move(direction, [current_position])
        if new_state.check_goal():
            print(f"المسار إلى الهدف: {path}")
            print(f"عدد العقد التي تمت زيارتها: {self.nodes_visited}")
            return path

       
        directions_map = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1)
        }

        for d_i, d_j in directions_map.values():
            ni, nj = current_position[0] + d_i, current_position[1] + d_j

            if (0 <= ni < len(state_obj.board) and
                0 <= nj < len(state_obj.board[0]) and
                (ni, nj) not in self.visited and
                state_obj.board[ni][nj] == 1):
                
                result = self.dfs(state_obj, (ni, nj), direction, path)
                if result:  
                    return result

        path.pop()
        return None
