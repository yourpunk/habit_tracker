from datetime import date, timedelta
from habit_tracker.streaks import calculate_streak

TODAY = date.today()


def iso(days_ago: int) -> str:
    """Helper function to get ISO format date string for a given number of days ago."""
    return (TODAY - timedelta(days=days_ago)).isoformat()


def test_empty_history_has_zero_streaks():
    assert calculate_streak([]) == 0


def test_single_completion_has_streak_one():
    assert calculate_streak([iso(0)]) == 1


def test_completion_yesterday_keeps_streak_alive():
    assert calculate_streak([iso(1)]) == 1


def test_consecutive_days_count_correctly():
    history = [iso(0), iso(1), iso(2), iso(3)]
    assert calculate_streak(history) == 4


def test_gap_in_history_breaks_streak():
    history = [iso(0), iso(1), iso(5), iso(6)]
    assert calculate_streak(history) == 2


def test_old_completion_without_recent_activity_resets_to_zero():
    history = [iso(7), iso(8), iso(9)]
    assert calculate_streak(history) == 0


def test_duplicate_dates_are_handled_gracefully():
    history = [iso(0), iso(0), iso(1)]
    assert calculate_streak(history) == 2
