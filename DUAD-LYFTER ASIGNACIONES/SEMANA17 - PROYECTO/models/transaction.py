# models/transaction.py
"""
Transaction model - Income and Expense with custom date and color.
"""

from datetime import datetime
from typing import Dict, Any


class Transaction:
    """
    Represents one financial movement (Income or Expense).
    """
    def __init__(self, title: str, amount: float, category, trans_type: str, date_str: str = None):
        if not title or not title.strip():
            raise ValueError("Title cannot be empty.")
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        if trans_type not in ["Income", "Expense"]:
            raise ValueError("Transaction type must be 'Income' or 'Expense'.")

        # Date (default today)
        if date_str is None or not date_str.strip():
            date_str = datetime.now().strftime("%d/%m/%Y")

        self.date = date_str.strip()
        self.title = title.strip()
        self.amount = float(amount)
        self.category = category          # Category object
        self.type = trans_type

    def get_display_amount(self) -> str:
        sign = "+" if self.type == "Income" else "-"
        return f"{sign}${self.amount:,.2f}"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "date": self.date,
            "type": self.type,
            "title": self.title,
            "category": self.category.name,
            "amount": self.amount,
            "color": getattr(self.category, 'color', "#1E90FF")
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any], categories_dict: Dict) -> 'Transaction':
        """Create Transaction from JSON data"""
        from models.category import Category   # import inside method

        cat_name = data.get("category", "Unknown")
        category = categories_dict.get(cat_name)

        if not category:
            color = data.get("color", "#1E90FF")
            category = Category(name=cat_name, color=color)

        return cls(
            title=data["title"],
            amount=data["amount"],
            category=category,
            trans_type=data["type"],
            date_str=data.get("date")
        )