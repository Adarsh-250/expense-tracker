# tracker.py
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict
from typing import List, Dict, Any

class ExpenseTracker:
    """Manages expenses, saving/loading from a JSON file."""

    def __init__(self, file_path: str = "data.json"):
        # Pathlib handles file paths beautifully across OS
        self.file_path = Path(file_path)
        self.expenses: List[Dict[str, Any]] = []
        self._load_data()

    def _load_data(self) -> None:
        """Private method: Loads data from JSON file. Handles missing files and bad JSON."""
        try:
            if self.file_path.exists():
                with open(self.file_path, 'r') as file:
                    self.expenses = json.load(file)
            else:
                # Create the file if it doesn't exist
                self.expenses = []
                self._save_data()
        except json.JSONDecodeError:
            # Exception handling if file is corrupted
            print("Warning: Data file is corrupted. Starting fresh.")
            self.expenses = []
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def _save_data(self) -> None:
        """Private method: Saves current expenses to JSON file."""
        with open(self.file_path, 'w') as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, amount: float, category: str, description: str) -> None:
        """Adds a new expense to the list and saves it."""
        # Validate input (raising our own errors)
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        if not category.strip() or not description.strip():
            raise ValueError("Category and description cannot be empty.")

        new_expense = {
            "date": datetime.now().strftime("%Y-%m-%d"), # Standard library
            "amount": round(amount, 2),
            "category": category.capitalize(),
            "description": description
        }
        self.expenses.append(new_expense)
        self._save_data()

    def delete_expense(self, index: int) -> None:
        """Deletes an expense by its index (1-based index from UI)."""
        try:
            # Convert 1-based UI index to 0-based list index
            list_index = index - 1 
            removed = self.expenses.pop(list_index)
            self._save_data()
            return removed
        except IndexError:
            # Handle bad input gracefully
            raise IndexError("Invalid expense number.")

    def get_monthly_summary(self) -> Dict[str, float]:
        """Calculates total expenses per category for the current month."""
        current_month = datetime.now().strftime("%Y-%m")
        summary = defaultdict(float) # Standard library: collections
        
        for exp in self.expenses:
            if exp["date"].startswith(current_month):
                summary[exp["category"]] += exp["amount"]
                
        return dict(summary)