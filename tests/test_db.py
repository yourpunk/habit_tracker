from datetime import date
import pytest
from habit_tracker import db


@pytest.fixture
def conn():
    # Create a temporary in-memory database for testing
    connection = db.get_db_connection(db_path=":memory:")
    yield connection
    connection.close()


def test_add_habit_creates_entry(conn):
    habit_id = db.add_habit(conn, "Exercise")
    habit = db.get_habit_by_name(conn, "Exercise")

    assert habit is not None
    assert habit["id"] == habit_id
    assert habit["name"] == "Exercise"


def test_list_habits_returns_all(conn):
    db.add_habit(conn, "Exercise")
    db.add_habit(conn, "Read")

    habits = db.list_habits(conn)

    assert len(habits) == 2
    assert {h["name"] for h in habits} == {"Exercise", "Read"}


def test_remove_habit_deletes_entry(conn):
    db.add_habit(conn, "Exercise")
    removed = db.remove_habit(conn, "Exercise")
    assert removed is True
    assert db.get_habit_by_name(conn, "Exercise") is None


def test_remove_nonexistent_habit_returns_false(conn):
    removed = db.remove_habit(conn, "Nonexistent Habit")
    assert removed is False


def test_mark_done_records_completion(conn):
    habit_id = db.add_habit(conn, "Exercise")
    marked = db.mark_done(conn, habit_id, on_date=date(2026, 6, 20))
    assert marked is True
    assert db.get_completions(conn, habit_id) == ["2026-06-20"]


def test_mark_done_twice_same_day_returns_false(conn):
    habit_id = db.add_habit(conn, "Exercise")
    db.mark_done(conn, habit_id, on_date=date(2026, 6, 20))
    marked_again = db.mark_done(conn, habit_id, on_date=date(2026, 6, 20))
    assert marked_again is False
    assert len(db.get_completions(conn, habit_id)) == 1
