import unittest
from State import State
from dfs1 import DFS
from bfs1 import BFS

class TestState(unittest.TestCase):
    def setUp(self):
        # إعداد الحالة الأولية مع لوحة، أهداف، وحالات أولية
        board = [
            [1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 1, 1, 1]
        ]
        goals = [(1, 3)]
        initial_states = [(1, 1)]
        self.state = State(board, goals, initial_states)

    def test_dfs_with_move(self):
        dfs_solver = DFS()
        initial_position = (1, 1)
        direction = "right"
        
        path = dfs_solver.dfs(self.state, initial_position, direction)
        print(f"المسار إلى الهدف: {path}")
        
        # التأكد من أن المسار يصل إلى الهدف
        self.assertTrue(self.state.check_goal(), "الحالة النهائية لم تحقق الهدف.")
        self.assertEqual(path[-1], (1, 3), "المسار لا يصل إلى الهدف المتوقع.")

if __name__ == "__main__":
    unittest.main()
