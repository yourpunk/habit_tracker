import click

from rich.console import Console
from rich.table import Table
from habit_tracker import db
from habit_tracker.streaks import calculate_streak


console = Console()


@click.group()
def cli():
    """Habit Tracker CLI"""
    pass


@cli.command()
@click.argument("name")
def add(name: str):
    """Add a new habit"""
    conn = db.get_db_connection()
    existing = db.get_habit_by_name(conn, name)
    if existing:
        console.print(f"[yellow]Habit '{name}' already exists.[/yellow]")
        return
    db.add_habit(conn, name)
    console.print(f"[green]Habit '{name}' added.[/green]")

@cli.command()
@click.argument("name")
def check(name: str):
    """Check off a habit for today"""
    conn = db.get_db_connection()
    habit = db.get_habit_by_name(conn, name)
    if not habit:
        console.print(f"[yellow]Habit '{name}' does not exist.[/yellow]")
        return
    db.check_habit(conn, habit["id"])
    console.print(f"[green]Habit '{name}' checked off for today.[/green]")


@cli.command()
@click.argument("name")
def remove(name: str):
    """Remove a habit"""
    conn = db.get_db_connection()
    removed = db.remove_habit(conn, name)
    if removed:
        console.print(f"[red]Habit '{name}' was removed.[/red]")
    else:
        console.print(f"[yellow]Habit '{name}' does not exist.[/yellow]")


@cli.command()
@click.argument("name")
def done(name: str):
    """Mark a habit as done for today"""
    conn = db.get_db_connection()
    habit = db.get_habit_by_name(conn, name)
    if not habit:
        console.print(
            f'[yellow]Habit "{name}" does not exist. '
            f'Add it first: habit add "{name}"[/yellow]'
        )
        return

    marked = db.mark_done(conn, habit["id"])
    if marked:
        completions = db.get_completions(conn, habit["id"])
        streak = calculate_streak(completions)
        console.print(
            f"[green]✓[/green] '{name}' marked as done for today. "
            f"Current streak: [bold orange3]{streak} 🔥[/bold orange3]"
        )
    else:
        console.print(f'[yellow]"{name}" has already been marked as done today.[/yellow]')

@cli.command(name="list")
def list_cmd():
    """List all habits and its streak"""
    conn = db.get_db_connection()
    habits = db.list_habits(conn)

    if not habits:
        console.print(
            '[dim]No habits found. Add your first one: habit add "read a book"[/dim]'
        )
        return
    table = Table(title="Your Habits")
    table.add_column("Habit", style="cyan", no_wrap=True)
    table.add_column("Streak", justify="right", style="bold orange3")
    table.add_column("Total Completions", justify="right", style="dim")

    for habit in habits:
        completions = db.get_completions(conn, habit["id"])
        streak = calculate_streak(completions)
        total = len(completions)
        streak_display = f"{streak} 🔥" if streak > 0 else "0"
        table.add_row(habit["name"], streak_display, str(total))

    console.print(table)


if __name__ == "__main__":
    cli()
