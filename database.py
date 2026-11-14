"""SQLite ma'lumotlar bazasi."""
import sqlite3
from config import DB_PATH

def connect():
    return sqlite3.connect(DB_PATH)

def init_db():
    with connect() as con:
        con.execute("""CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            balance REAL NOT NULL DEFAULT 0
        )""")
        con.execute("""CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            service TEXT NOT NULL,
            link TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            status TEXT NOT NULL DEFAULT 'Yangi',
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        )""")

def save_user(user_id, username):
    with connect() as con:
        con.execute("INSERT OR IGNORE INTO users(user_id, username) VALUES (?, ?)",
                    (user_id, username or ""))

def get_balance(user_id):
    with connect() as con:
        row = con.execute("SELECT balance FROM users WHERE user_id=?", (user_id,)).fetchone()
    return row[0] if row else 0

def create_order(user_id, service, link, quantity):
    with connect() as con:
        cur = con.execute(
            "INSERT INTO orders(user_id, service, link, quantity) VALUES (?, ?, ?, ?)",
            (user_id, service, link, quantity)
        )
        return cur.lastrowid

def user_orders(user_id, limit=10):
    with connect() as con:
        return con.execute(
            "SELECT id, service, quantity, status FROM orders WHERE user_id=? ORDER BY id DESC LIMIT ?",
            (user_id, limit)
        ).fetchall()

def stats():
    with connect() as con:
        users = con.execute("SELECT COUNT(*) FROM users").fetchone()[0]
        total = con.execute("SELECT COUNT(*) FROM orders").fetchone()[0]
        pending = con.execute("SELECT COUNT(*) FROM orders WHERE status='Yangi'").fetchone()[0]
    return users, total, pending

def update_order_status(order_id, status):
    with connect() as con:
        cur = con.execute("UPDATE orders SET status=? WHERE id=?", (status, order_id))
        row = con.execute("SELECT user_id FROM orders WHERE id=?", (order_id,)).fetchone()
    return cur.rowcount, row[0] if row else None
