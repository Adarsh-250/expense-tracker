# main.py
from tracker import ExpenseTracker
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, FloatPrompt, IntPrompt

# Initialize the rich console for printing to the terminal
console = Console()
tracker = ExpenseTracker()

def display_menu() -> None:
    """Prints the main menu to the screen."""
    console.print("\n[bold cyan]💰 Expense Tracker Menu[/bold cyan]")
    console.print("1. Add Expense")
    console.print("2. List All Expenses")
    console.print("3. Delete Expense")
    console.print("4. Monthly Summary")
    console.print("5. Exit")

def handle_add_expense() -> None:
    """Prompts user for expense details and adds it."""
    console.print("\n[bold yellow]--- Add New Expense ---[/bold yellow]")
    try:
        amount = FloatPrompt.ask("Enter amount ($)")
        category = Prompt.ask("Enter category (e.g., Food, Transport)")
        description = Prompt.ask("Enter description")
        
        tracker.add_expense(amount, category, description)
        console.print("[bold green]✅ Expense added successfully![/bold green]")
    except ValueError as e:
        # Catch the specific error we raised in tracker.py
        console.print(f"[bold red]❌ Error: {e}[/bold red]")

def handle_list_expenses() -> None:
    """Displays all expenses in a beautiful table."""
    if not tracker.expenses:
        console.print("[bold red]No expenses found.[/bold red]")
        return

    # Create a Rich Table
    table = Table(title="All Expenses", show_header=True, header_style="bold magenta")
    table.add_column("No.", style="dim")
    table.add_column("Date")
    table.add_column("Category", style="cyan")
    table.add_column("Description")
    table.add_column("Amount", justify="right", style="green")

    # Populate the table
    for i, exp in enumerate(tracker.expenses, start=1):
        table.add_row(
            str(i),
            exp["date"],
            exp["category"],
            exp["description"],
            f"${exp['amount']:.2f}"
        )
    
    console.print(table)

def handle_delete_expense() -> None:
    """Prompts user for an index and deletes it."""
    handle_list_expenses()
    if not tracker.expenses:
        return
        
    try:
        index = IntPrompt.ask("\nEnter the [bold]No.[/bold] of the expense to delete")
        removed = tracker.delete_expense(index)
        console.print(f"[bold green]✅ Deleted: {removed['description']} (${removed['amount']})[/bold green]")
    except IndexError as e:
        console.print(f"[bold red]❌ Error: {e}[/bold red]")

def handle_summary() -> None:
    """Displays the monthly summary."""
    summary = tracker.get_monthly_summary()
    
    if not summary:
        console.print("[bold red]No expenses found for this month.[/bold red]")
        return

    table = Table(title="Current Month Summary", show_header=True, header_style="bold blue")
    table.add_column("Category", style="cyan")
    table.add_column("Total Spent", justify="right", style="green")

    total = 0.0
    for category, amount in summary.items():
        table.add_row(category, f"${amount:.2f}")
        total += amount

    console.print(table)
    console.print(f"\n[bold yellow]Total Spent: ${total:.2f}[/bold yellow]")

def main() -> None:
    """Main application loop."""
    console.print("[bold green]Welcome to the Expense Tracker![/bold green]")
    
    while True:
        display_menu()
        choice = Prompt.ask("Choose an option", choices=["1", "2", "3", "4", "5"])
        
        if choice == "1":
            handle_add_expense()
        elif choice == "2":
            handle_list_expenses()
        elif choice == "3":
            handle_delete_expense()
        elif choice == "4":
            handle_summary()
        elif choice == "5":
            console.print("[bold cyan]Goodbye! 👋[/bold cyan]")
            break

if __name__ == "__main__":
    # This ensures the app only runs if this file is executed directly
    main()