import unittest
from database import Database

class TestShowTasks(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")

    def test_show_tasks(self):
        self.db.add_task("Görev 1")
        self.db.add_task("Görev 2")
        tasks = self.db.get_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0][1], "Görev 1")
        self.assertEqual(tasks[1][1], "Görev 2")

    def tearDown(self):
        self.db.close()

if __name__ == "__main__":
    unittest.main()
