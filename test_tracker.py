# test_tracker.py
import pytest
from tracker import ExpenseTracker

# `tmp_path` is a built-in pytest fixture that creates a temporary directory
def test_add_expense(tmp_path):
    # 1. Setup: Create a tracker using a temp file
    test_file = tmp_path / "test_data.json"
    tracker = ExpenseTracker(str(test_file))
    
    # 2. Action: Add an expense
    tracker.add_expense(10.50, "Food", "Lunch")
    
    # 3. Assert: Check if it was added correctly
    assert len(tracker.expenses) == 1
    assert tracker.expenses[0]["amount"] == 10.50
    assert tracker.expenses[0]["category"] == "Food"

def test_add_expense_invalid_amount(tmp_path):
    test_file = tmp_path / "test_data.json"
    tracker = ExpenseTracker(str(test_file))
    
    # Check if our custom Exception is raised for bad input
    with pytest.raises(ValueError):
        tracker.add_expense(-5.00, "Food", "Lunch")

def test_delete_expense(tmp_path):
    test_file = tmp_path / "test_data.json"
    tracker = ExpenseTracker(str(test_file))
    tracker.add_expense(10.00, "Food", "Lunch")
    
    # Delete using the 1-based index
    tracker.delete_expense(1)
    
    assert len(tracker.expenses) == 0

def test_delete_invalid_index(tmp_path):
    test_file = tmp_path / "test_data.json"
    tracker = ExpenseTracker(str(test_file))
    
    with pytest.raises(IndexError):
        tracker.delete_expense(99)

def test_monthly_summary(tmp_path):
    test_file = tmp_path / "test_data.json"
    tracker = ExpenseTracker(str(test_file))
    
    # Add expenses
    tracker.add_expense(10.00, "Food", "Lunch")
    tracker.add_expense(20.00, "Food", "Dinner")
    tracker.add_expense(15.00, "Transport", "Bus")
    
    summary = tracker.get_monthly_summary()
    
    assert summary["Food"] == 30.00
    assert summary["Transport"] == 15.00