from queue import PriorityQueue
from State import State

class UCS:
    def __init__(self):
        pass

    def ucs(self, state_obj, initial_position, direction):
        if not isinstance(state_obj, State):
            raise ValueError("state_obj يجب أن يكون كائنًا من فئة State.")
        pq = PriorityQueue()
        pq.put((0, initial_position, [initial_position]))

        visited = set()
        visited.add(initial_position)
        parents = {}  
        nodes_visited = 0

        directions_map = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1)
        }

        while not pq.empty():
            current_cost, (i, j), path = pq.get()
            nodes_visited += 1

            state_obj.update_initial_position((i, j)) 
            if state_obj.check_goal():
                print(f"المسار إلى الهدف: {path}")
                print(f"عدد العقد التي تمت زيارتها: {nodes_visited}")
                print(f"التكلفة الإجمالية للمسار: {current_cost}")
                return path

            neighbors = []
            for d_i, d_j in directions_map.values():
                ni, nj = i + d_i, j + d_j
                if 0 <= ni < len(state_obj.board) and 0 <= nj < len(state_obj.board[0]) and state_obj.board[ni][nj] == 1:
                    neighbors.append((ni, nj))

            for ni, nj in neighbors:
                if (ni, nj) not in visited:
                    visited.add((ni, nj))
                    parents[(ni, nj)] = (i, j) 
                    pq.put((current_cost + 1, (ni, nj), path + [(ni, nj)]))

        print("لم يتم العثور على مسار إلى الهدف.")
        return None
