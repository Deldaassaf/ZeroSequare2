import heapq
from State import State

class AStar:
    def __init__(self):
        pass

    def heuristic(self, current, goal):
        return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

    def a_star(self, state_obj, initial_position, goal_position):
        if not isinstance(state_obj, State):
            raise ValueError("state_obj يجب أن يكون كائن من فئة State.")
        open_list = []
        heapq.heappush(open_list, (0, initial_position, [initial_position])) 
        visited = set()
        visited.add(initial_position)

        nodes_visited = 0

        directions_map = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1)
        }

        while open_list:
            _, (i, j), path = heapq.heappop(open_list)
            nodes_visited += 1

            if (i, j) == goal_position:
                print(f"المسار إلى الهدف: {path}")
                print(f"عدد العقد التي تمت زيارتها: {nodes_visited}")
                return path

            neighbors = []
            for d_i, d_j in directions_map.values():
                ni, nj = i + d_i, j + d_j
                if 0 <= ni < len(state_obj.board) and 0 <= nj < len(state_obj.board[0]) and state_obj.board[ni][nj] == 1:
                    neighbors.append((ni, nj))

            for ni, nj in neighbors:
                if (ni, nj) not in visited:
                    visited.add((ni, nj))
                    g_cost = len(path)  
                    h_cost = self.heuristic((ni, nj), goal_position)  
                    f_cost = g_cost + h_cost  
                    heapq.heappush(open_list, (f_cost, (ni, nj), path + [(ni, nj)]))

        print("لم يتم العثور على مسار إلى الهدف.")
        return None


import unittest

class TestAStar(unittest.TestCase):
    def setUp(self):
        self.board = [
            [1, 1, 0, 0, 0],
            [0, 1, 0, 1, 1],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 1, 1],
            [1, 1, 1, 0, 1]
        ]
        self.initial_position = (0, 0)  
        self.goal_position = (4, 4)    

        self.goals = [self.goal_position]
        self.initial_states = [self.initial_position]
        self.state = State(self.board, self.goals, self.initial_states)
        self.astar = AStar()

    def test_a_star_path(self):
        path = self.astar.a_star(self.state, self.initial_position, self.goal_position)

        self.assertIsNotNone(path, "الخوارزمية لم تجد مساراً بالرغم من وجوده.")

        self.assertEqual(path[-1], self.goal_position, "المسار لا ينتهي عند الهدف.")

        print(f"المسار الناتج: {path}")

    def test_a_star_no_path(self):
        self.state.board[4][3] = 0
        self.state.board[3][3] = 0
        self.state.board[3][4] = 0

        path = self.astar.a_star(self.state, self.initial_position, self.goal_position)
        self.assertIsNone(path, "الخوارزمية وجدت مساراً بالرغم من عدم وجوده.")

if __name__ == "__main__":
    unittest.main()
