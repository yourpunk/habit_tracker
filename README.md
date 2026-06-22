# habit-tracker

[![Tests](https://github.com/yourpunk/habit_tracker/actions/workflows/tests.yml/badge.svg)](https://github.com/yourpunk/habit_tracker/actions/workflows/tests.yml)

A simple, fast habit tracker for your terminal. Add habits, mark them done each day, and watch your streak grow.

## Preview

![habit-tracker preview](docs/preview.png)

## Installation

```bash
git clone https://github.com/yourpunk/habit_tracker.git
cd habit_tracker
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux

pip install -e ".[dev]"
```

## Usage

```bash
habit add "read a book"
habit done "read a book"
habit list
habit remove "read a book"
```

## Running tests

```bash
pytest -v
```

Tests also run automatically on every push via GitHub Actions (see the badge above).

## Tech stack

- Python 3.11+
- [click](https://click.palletsprojects.com/) — CLI interface
- [rich](https://rich.readthedocs.io/) — terminal tables and colored output
- SQLite — local storage, no external database needed
- pytest — unit tests
- GitHub Actions — CI on every push

## Project structure

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
