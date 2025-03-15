import sqlite3
import config  

class Database:
    def __init__(self, db_name=config.DATABASE_NAME):  
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                completed BOOLEAN NOT NULL DEFAULT 0
            )
        """)
        self.conn.commit()

    def add_task(self, description):
        """Yeni bir görev ekler"""
        self.cursor.execute("INSERT INTO tasks (description) VALUES (?)", (description,))
        self.conn.commit()

    def delete_task(self, task_id):
        """Belirtilen ID'ye sahip görevi siler"""
        self.cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        self.conn.commit()

    def get_tasks(self):
        """Tüm görevleri getirir"""
        self.cursor.execute("SELECT id, description, completed FROM tasks")
        return self.cursor.fetchall()

    def complete_task(self, task_id):
        """Belirtilen ID'ye sahip görevi tamamlandı olarak işaretler"""
        self.cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
        self.conn.commit()

    def close(self):
        """Veritabanı bağlantısını kapatır"""
        self.conn.close()
