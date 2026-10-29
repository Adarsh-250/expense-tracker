# 💰 Python CLI Expense Tracker

A robust, interactive Command-Line Interface (CLI) application built in Python to track daily expenses, manage budgets by category, and generate monthly summaries. 

This project was built as part of a software engineering roadmap to master core Python concepts, including Object-Oriented Programming (OOP), File I/O, Exception Handling, and Test-Driven Development (TDD).

## ✨ Features

*   **Add Expenses:** Log expenses with an amount, category, and description.
*   **List Expenses:** View all recorded expenses in a beautifully formatted terminal table.
*   **Delete Expenses:** Remove mistakes or old entries by selecting their row number.
*   **Monthly Summary:** Automatically calculate and display total spending per category for the current month.
*   **Data Persistence:** Expenses are automatically saved to and loaded from a local `data.json` file.
*   **Graceful Error Handling:** The app won't crash if you enter invalid data (e.g., negative amounts, text instead of numbers, or corrupted JSON files).
*   **Rich UI/UX:** Uses the `rich` library to provide colored text, formatted tables, and interactive prompts.

## 🛠️ Tech Stack & Concepts

*   **Language:** Python 3.10+
*   **UI/UX:** [`rich`](https://github.com/Textualize/rich) (for terminal formatting and tables)
*   **Testing:** [`pytest`](https://docs.pytest.org/) (for unit testing)
*   **Standard Libraries:** `json`, `pathlib`, `datetime`, `collections` (defaultdict), `typing`
*   **Concepts applied:** Object-Oriented Programming (OOP), Custom Exceptions, File I/O, Type Hinting, TDD.

## 🚀 Getting Started

Follow these steps to run the application on your local machine.

### Prerequisites
*   Python 3.10 or higher installed on your system.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Adarsh-250/expense-tracker.git
   cd expense-tracker
Create and activate a virtual environment:

Windows:

powershell
python -m venv venv
venv\Scripts\activate
macOS/Linux:

bash
python3 -m venv venv
source venv/bin/activate
Install dependencies:

bash
pip install -r requirements.txt
💻 Usage
To start the application, ensure your virtual environment is activated and run:

bash
python main.py
You will be greeted with the interactive menu:

text
Welcome to the Expense Tracker!

💰 Expense Tracker Menu
1. Add Expense
2. List All Expenses
3. Delete Expense
4. Monthly Summary
5. Exit
Choose an option (1-5): 
Example: Viewing the Summary
When you select option 4, the app uses Python's datetime and collections.defaultdict to filter the current month and format a summary table like this:

text
       Current Month Summary       
┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃ Category   ┃         Total Spent┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ Food       │             $45.50 │
│ Transport  │             $15.00 │
│ Utilities  │             $60.00 │
└────────────┴────────────────────┘

Total Spent: $120.50
🧪 Running Tests
This project uses pytest to ensure the core logic is working correctly. The tests use tmp_path fixtures to create temporary JSON files, ensuring your real data is never overwritten during testing.

To run the test suite:

bash
pytest test_tracker.py -v
📁 Project Structure
text
expense-tracker/
│
├── venv/                    # Virtual environment (Ignored by Git)
├── data.json                # Local database for expenses (Ignored by Git)
├── tracker.py               # Core logic (Classes, JSON handling, OOP)
├── main.py                  # CLI Interface (User interaction, UI/UX via Rich)
├── test_tracker.py          # Pytest test suite
├── requirements.txt         # Project dependencies (rich, pytest)
└── .gitignore               # Files to ignore in version control
