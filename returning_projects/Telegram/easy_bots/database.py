import sqlite3


def init_db():
    # Создаем подключение к файлу базы данных (если файла нет, он создастся)
    conn = sqlite3.connect("notes_bot.db")
    cursor = conn.cursor()

    # Создаем таблицу для заметок, если её еще нет
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,          -- Сюда будем писать Telegram ID пользователя
            note_text TEXT,           -- Текст самой заметки
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()


def add_note(user_id: int, text: str):
    conn = sqlite3.connect("notes_bot.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO user_notes (user_id, note_text) VALUES (?, ?)", (user_id, text))
    conn.commit()
    conn.close()


def get_notes(user_id: int):
    conn = sqlite3.connect("notes_bot.db")
    cursor = conn.cursor()
    # Забираем только заметки того пользователя, который сделал запрос
    cursor.execute("SELECT id, note_text FROM user_notes WHERE user_id = ?", (user_id,))
    notes = cursor.fetchall()
    conn.close()
    return notes
