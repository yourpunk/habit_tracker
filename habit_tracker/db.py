import sqlite3
from datetime import date
from pathlib import Path

DB_PATH = Path.home() / ".habit-tracker.db"


def get_db_connection(db_path: Path | str = DB_PATH) -> sqlite3.Connection:
    """Establish a connection to the SQLite database."""
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON")
    _create_tables(conn)
    return conn


def _create_tables(conn: sqlite3.Connection) -> None:
    conn.execute("""CREATE TABLE IF NOT EXISTS habits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        created_at TEXT NOT NULL
    )""")
    conn.execute("""CREATE TABLE IF NOT EXISTS completions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        habit_id INTEGER NOT NULL,
                 completed_on TEXT NOT NULL,
        FOREIGN KEY (habit_id) REFERENCES habits (id) ON DELETE CASCADE,
        UNIQUE (habit_id, completed_on)
    )""")
    conn.commit()


def add_habit(conn: sqlite3.Connection, name: str) -> int:
    """Add a new habit to the database ant return its ID."""
    cursor = conn.execute(
        "INSERT INTO habits (name, created_at) VALUES (?, ?)",
        (name, date.today().isoformat()),
    )
    conn.commit()
    return cursor.lastrowid


def remove_habit(conn: sqlite3.Connection, name: str) -> bool:
    """Remove a habit by its name. Return TRUE if the habit was removed."""
    cursor = conn.execute("DELETE FROM habits WHERE name = ?", (name,))
    conn.commit()
    return cursor.rowcount > 0


def get_habit_by_name(conn: sqlite3.Connection, name: str) -> sqlite3.Row | None:
    conn.row_factory = sqlite3.Row
    return conn.execute("SELECT * FROM habits WHERE name = ?", (name,)).fetchone()

def list_habits(conn: sqlite3.Connection) -> list[sqlite3.Row]:
    """Return all habits, ordered by creation date."""
    conn.row_factory = sqlite3.Row
    return conn.execute("SELECT * FROM habits ORDER BY created_at").fetchall()

def mark_done(
    conn: sqlite3.Connection, habit_id: int, on_date: date | None = None
) -> bool:
    """Mark a habit as done for a specific date (by default - today). Return FALSE if already done."""
    on_date = on_date or date.today()
    try:
        conn.execute(
            "INSERT INTO completions (habit_id, completed_on) VALUES (?, ?)",
            (habit_id, on_date.isoformat()),
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False


def get_completions(conn: sqlite3.Connection, habit_id: int) -> list[str]:
    """Get a list of dates when the habit was completed."""
    rows = conn.execute(
        "SELECT completed_on FROM completions WHERE habit_id = ? ORDER BY completed_on DESC",
        (habit_id,),
    ).fetchall()
    return [row[0] for row in rows]
