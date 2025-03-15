import unittest
from database import Database

class TestCompleteTask(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")

    def test_complete_task(self):
        self.db.add_task("Tamamlanacak görev")
        task_id = self.db.get_tasks()[0][0]
        self.db.complete_task(task_id)
        task = self.db.get_tasks()[0]
        self.assertTrue(task[2])  # 3. indeks "completed" sütununu temsil ediyor

    def tearDown(self):
        self.db.close()

if __name__ == "__main__":
    unittest.main()
