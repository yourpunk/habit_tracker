# 🔥 Habit Tracker 💪

[![Tests](https://github.com/yourpunk/habit_tracker/actions/workflows/tests.yml/badge.svg)](https://github.com/yourpunk/habit_tracker/actions/workflows/tests.yml)

**Habit Tracker** is a tiny terminal companion that keeps score of the habits you swear you'll stick to this time.  
💫 No app, no account, no ads, just you, your terminal, and a streak counter judging you.

## Preview

![habit-tracker preview](docs/preview.ipg)

## 🫧 Features
- ✅ Add, remove, and check off habits in seconds
- 🔥 Tracks your streak: consecutive days, no cheating
- 📊 Clean table view of every habit and how loyal you've been to it
- 🎨 Color-coded terminal output (powered by `rich`)
- 🧪 Fully tested, CI-checked on every push

## 🧰 Built With
- **Python 3.11+** - main staff
- **Click** - CLI commands that don't fight you
- **Rich** - because terminal output doesn't have to look like 1998
- **SQLite** - your habits, saved locally, no cloud nonsense
- **Pytest + GitHub Actions** - tests that actually run themselves

## 🛠️ How to Set It Up

### Requirements
- Python 3.11+
- `pip install -e ".[dev]"`
- (Optional) The will to actually do the habit, not just track it

### 🦾 Quickstart
```bash
git clone https://github.com/yourpunk/habit_tracker.git
cd habit_tracker
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux

pip install -e ".[dev]"
```

Then:
```bash
habit add "read a book"
habit done "read a book"
habit list
```

You **also can**:
- Run `habit remove "habit name"` to retire a habit you've outgrown (or gave up on, we don't judge)
- Run `pytest -v` to see all tests pass like they're supposed to

## 🧪 Tests
```bash
pytest -v
```
Tests also run automatically on every push via GitHub Actions — check the badge up top.

## 📁 Project Structure
```
habit_tracker/
├── habit_tracker/
│   ├── cli.py        # CLI commands (add, done, remove, list)
│   ├── db.py         # SQLite persistence layer
│   └── streaks.py    # Streak calculation logic
├── tests/
│   ├── test_db.py
│   └── test_streaks.py
└── .github/workflows/tests.yml
```

## 👤 Author
🦾 Crafted by Aleksandra Kenig (aka [yourpunk](https://github.com/yourpunk)).<br>
💌 Wanna collab or throw some feedback? You know where to find me.
