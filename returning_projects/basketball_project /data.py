import sqlite3

class DatabaseManager:
    def __init__(self, db_name: str = "player_stats.db"):
        self.db_name = db_name
        self.init_db()

    # Метод для создания таблицы (вызывается автоматически при создании менеджера)
    def init_db(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS basket_stats (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,          
                    player_name TEXT,         
                    points INTEGER DEFAULT 0,  
                    assists INTEGER DEFAULT 0, 
                    rebounds INTEGER DEFAULT 0,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()

    # Метод принимает объект класса Player и сохраняет его данные в БД
    def save_player_stats(self, user_id: int, player: Player):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO basket_stats (user_id, player_name, points, assists, rebounds) 
                VALUES (?, ?, ?, ?, ?)
            """, (user_id, player.name, player.points, player.assists, player.rebounds))
            conn.commit()