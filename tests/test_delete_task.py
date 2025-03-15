import unittest
from database import Database

class TestDeleteTask(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")

    def test_delete_task(self):
        self.db.add_task("Silinecek görev")
        task_id = self.db.get_tasks()[0][0]
        self.db.delete_task(task_id)
        tasks = self.db.get_tasks()
        self.assertEqual(len(tasks), 0)

    def tearDown(self):
        self.db.close()

if __name__ == "__main__":
    unittest.main()
