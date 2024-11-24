from collections import deque
from State import State
class BFS:
    def __init__(self):
        pass

    def bfs(self, state_obj, initial_position, direction):
        if not isinstance(state_obj, State):
            raise ValueError("state_obj يجب أن يكون كائن من فئة State.")
        
        queue = deque([(initial_position, [initial_position])])
        visited = set()
        visited.add(initial_position)
        nodes_visited = 0

        directions_map = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1)
        }

        while queue:
            (i, j), path = queue.popleft()
            nodes_visited += 1

            neighbors = []
            for d_i, d_j in directions_map.values():
                ni, nj = i + d_i, j + d_j
                if 0 <= ni < len(state_obj.board) and 0 <= nj < len(state_obj.board[0]) and state_obj.board[ni][nj] != 0:
                    neighbors.append((ni, nj))

            new_state = state_obj.move(direction, neighbors)

            # تحقق من الوصول إلى الهدف بعد الحركة
            if new_state.check_goal():
                print(f"المسار إلى الهدف: {path}")
                print(f"عدد العقد التي تمت زيارتها: {nodes_visited}")
                return path

            # إضافة الجيران إلى الطابور
            for ni, nj in neighbors:
                if (ni, nj) not in visited:
                    visited.add((ni, nj))
                    queue.append(((ni, nj), path + [(ni, nj)]))

        print("لم يتم العثور على مسار إلى الهدف.")
        return None
