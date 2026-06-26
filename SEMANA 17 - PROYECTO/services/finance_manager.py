# services/finance_manager.py
"""
Finance Manager - Core logic of the application.
"""

import json
from datetime import datetime
from typing import List, Dict

from models.category import Category
from models.transaction import Transaction
from utils.validators import validate_date, validate_amount, validate_title


class FinanceManager:
    """Manages categories and transactions."""

    def __init__(self, data_file: str = "data/finance_data.json"):
        self.data_file = data_file
        self.categories: Dict[str, Category] = {}
        self.transactions: List[Transaction] = []
        self.load_data()

    def load_data(self):
        """Load data from JSON file."""
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Load categories
            self.categories.clear()
            for name, info in data.get("categories", {}).items():
                self.categories[name] = Category.from_dict(info)

            # Load transactions
            self.transactions.clear()
            for t in data.get("transactions", []):
                self.transactions.append(Transaction.from_dict(t, self.categories))

        except FileNotFoundError:
            self.categories = {}
            self.transactions = []
        except Exception:
            self.categories = {}
            self.transactions = []

    def save_data(self):
        """Save data to JSON file."""
        data = {
            "categories": {name: cat.to_dict() for name, cat in self.categories.items()},
            "transactions": [t.to_dict() for t in self.transactions]
        }

        import os
        os.makedirs("data", exist_ok=True)

        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    # ====================== CATEGORIES ======================

    def add_category(self, name: str, color: str = "#1E90FF") -> Category:
        """Add a new category."""
        category = Category(name, color)
        if category.name in self.categories:
            raise ValueError(f"Category '{category.name}' already exists.")
        
        self.categories[category.name] = category
        self.save_data()
        return category

    def get_category_names(self) -> List[str]:
        """Return list of category names."""
        return sorted(self.categories.keys())

    # ====================== TRANSACTIONS ======================

    def add_transaction(self, title: str, amount: str, category_name: str, 
                    trans_type: str, date_str: str = None) -> Transaction:
        """Add new income or expense."""
        if not self.categories:
            raise ValueError("No categories available. Please add a category first.")

        if category_name not in self.categories:
            raise ValueError(f"Category '{category_name}' does not exist.")

        validated_amount = validate_amount(amount)
        validated_title = validate_title(title)
        validated_date = validate_date(date_str) if date_str else datetime.now().strftime("%d/%m/%Y")

        transaction = Transaction(
            title=validated_title,
            amount=validated_amount,
            category=self.categories[category_name],
            trans_type=trans_type,
            date_str=validated_date
        )

        self.transactions.append(transaction)
        self.save_data()
        return transaction

    def get_all_transactions(self) -> List[Transaction]:
        """Return all transactions (newest first)."""
        return sorted(self.transactions, key=lambda t: t.date, reverse=True)

    def get_balance(self) -> float:
        return sum(t.amount if t.type == "Income" else -t.amount for t in self.transactions)

    def get_total_income(self) -> float:
        return sum(t.amount for t in self.transactions if t.type == "Income")

    def get_total_expense(self) -> float:
        return sum(t.amount for t in self.transactions if t.type == "Expense")

    def export_to_csv(self):
        """Simple CSV export."""
        import csv
        import os
        os.makedirs("exports", exist_ok=True)

        filepath = "exports/finance_export.csv"

        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Type", "Title", "Category", "Amount"])

            for t in self.get_all_transactions():
                amount_str = f"+{t.amount:.2f}" if t.type == "Income" else f"-{t.amount:.2f}"
                writer.writerow([t.date, t.type, t.title, t.category.name, amount_str])

            # Totals
            writer.writerow([])
            writer.writerow(["TOTAL INCOME", "", "", "", f"+{self.get_total_income():.2f}"])
            writer.writerow(["TOTAL EXPENSE", "", "", "", f"-{self.get_total_expense():.2f}"])
            writer.writerow(["NET BALANCE", "", "", "", f"{self.get_balance():.2f}"])

        return filepath