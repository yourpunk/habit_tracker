from datetime import date, timedelta


def calculate_streak(completion_dates: list[str]) -> int:
    if not completion_dates:
        return 0

    dates = sorted({date.fromisoformat(d) for d in completion_dates}, reverse=True)
    today = date.today()

    if dates[0] not in (today, today - timedelta(days=1)):
        return 0

    streak = 1

    for i in range(len(dates) - 1):
        gap = (dates[i] - dates[i + 1]).days
        if gap == 1:
            streak += 1
        else:
            break

    return streak
