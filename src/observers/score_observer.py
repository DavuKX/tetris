from abc import ABC, abstractmethod
import sqlite3
from datetime import datetime
from typing import List, Tuple

DEFAULT_DB_PATH = "data/tetris_scores.db"

class GameObserver(ABC):
    @abstractmethod
    def on_game_over(self, final_score: int):
        pass

class ScoreDatabase:
    _instance = None
    _initialized = False
    
    def __new__(cls, db_path: str = DEFAULT_DB_PATH):
        if cls._instance is None:
            cls._instance = super(ScoreDatabase, cls).__new__(cls)
        return cls._instance
    
    def __init__(self, db_path: str = DEFAULT_DB_PATH):
        if not ScoreDatabase._initialized:
            self.db_path = db_path
            self._init_database()
            ScoreDatabase._initialized = True
    
    @classmethod
    def get_instance(cls, db_path: str = DEFAULT_DB_PATH):
        if cls._instance is None:
            cls._instance = cls(db_path)
        return cls._instance
    
    @classmethod
    def reset_instance(cls):
        cls._instance = None
        cls._initialized = False
    
    def _init_database(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS high_scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                score INTEGER NOT NULL,
                date TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()
    
    def save_score(self, score: int):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute('INSERT INTO high_scores (score, date) VALUES (?, ?)', (score, date_str))
        conn.commit()
        conn.close()
    
    def get_top_scores(self, limit: int = 3) -> List[Tuple[int, str]]:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT score, date FROM high_scores ORDER BY score DESC LIMIT ?', (limit,))
        scores = cursor.fetchall()
        conn.close()
        return scores

class ScoreDatabaseObserver(GameObserver):
    def __init__(self, db_path: str = DEFAULT_DB_PATH):
        self.database = ScoreDatabase(db_path)
    
    def on_game_over(self, final_score: int):
        if final_score > 0: 
            self.database.save_score(final_score)
    
    def get_high_scores(self, limit: int = 3) -> List[Tuple[int, str]]:
        return self.database.get_top_scores(limit)
