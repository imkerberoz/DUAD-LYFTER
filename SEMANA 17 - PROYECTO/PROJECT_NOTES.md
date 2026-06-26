# PROJECT NOTES - Personal Finance Manager

## Project Overview
This is a desktop application to manage personal finances (incomes and expenses) using FreeSimpleGUI.

---

## Project Structure Explanation

### 1. `models/` Folder (The Foundation)
Contains the main classes that represent real-world objects.

- **`category.py`**: Defines the `Category` class
  - Represents a financial category (Food, Salary, Transport, etc.)
  - Has a name and a color

- **`transaction.py`**: Defines the `Transaction` class
  - Represents a financial movement (income or expense)
  - Contains: date, title, amount, type, and category

**Relationship**: Every Transaction needs a Category.

---

### 2. `utils/` Folder (Helper Tools)
- **`validators.py`**: Contains validation functions
  - `validate_date()`, `validate_amount()`, `validate_title()`
  - Ensures user input is correct before processing

---

### 3. `services/` Folder (The Brain / Business Logic)
- **`finance_manager.py`**: Contains the `FinanceManager` class
  - **Core logic** of the entire application
  - Manages categories and transactions
  - Handles saving and loading data (JSON)
  - Calculates balance, total income, and total expenses
  - Exports data to CSV

---

### 4. `ui/` Folder (Graphical User Interface)
- **`main_window.py`**: Contains the `MainWindow` class
  - Controls the entire graphical interface
  - Creates windows, buttons, and the transactions table
  - Communicates with `FinanceManager` when user interacts

---

### 5. `tests/` Folder (Unit Testing)
- **`test_finance.py`**: Contains 10 unit tests
  - Tests the logic without using the graphical interface
  - Helps ensure the program works correctly

---

### Root Files

- **`main.py`** → Main entry point (the file you run to start the app)
- **`README.md`** → Project documentation
- **`requirements.txt`** → List of required libraries

---

## Important Concepts Explained

### `__eq__` and `__hash__` (in `Category` class)

```python
def __eq__(self, other):
    return self.name.lower() == other.name.lower()



---
## 3. Why `__init__.py` is Important

Every folder contains an empty file called **`__init__.py`**.

**Purpose:**
- It tells Python that the folder is a **package**.
- It allows us to import files from that folder using syntax like:
  ```python
  from models.category import Category
  from services.finance_manager import FinanceManager