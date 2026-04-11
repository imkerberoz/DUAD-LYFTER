# tests/test_finance.py
"""
Unit Tests for Personal Finance Manager
10 tests - Clean and independent
"""

import sys
import os
import unittest

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.category import Category
from models.transaction import Transaction
from services.finance_manager import FinanceManager
from utils.validators import validate_date, validate_amount, validate_title


class TestCategory(unittest.TestCase):

    def test_category_creation(self):
        """Test 1: Create a valid category"""
        cat = Category("Food", "#FF5733")
        self.assertEqual(cat.name, "Food")
        self.assertEqual(cat.color, "#FF5733")

    def test_category_default_color(self):
        """Test 2: Default color is applied"""
        cat = Category("Transport")
        self.assertEqual(cat.color, "#1E90FF")


class TestTransaction(unittest.TestCase):

    def setUp(self):
        self.food_cat = Category("Food")

    def test_transaction_creation(self):
        """Test 3: Create valid transaction"""
        trans = Transaction("Pizza", 12500, self.food_cat, "Expense", "25/03/2026")
        self.assertEqual(trans.title, "Pizza")
        self.assertEqual(trans.amount, 12500)
        self.assertEqual(trans.type, "Expense")

    def test_display_amount(self):
        """Test 4: Display amount with correct sign"""
        expense = Transaction("Bus", 5000, self.food_cat, "Expense")
        income = Transaction("Salary", 100000, Category("Salary"), "Income")
        
        self.assertIn("-", expense.get_display_amount())
        self.assertIn("+", income.get_display_amount())


class TestValidators(unittest.TestCase):

    def test_validate_date(self):
        """Test 5: Valid date format"""
        self.assertEqual(validate_date("25/03/2026"), "25/03/2026")

    def test_validate_amount(self):
        """Test 6: Valid positive amount"""
        self.assertEqual(validate_amount("12500"), 12500.0)

    def test_validate_title(self):
        """Test 7: Valid title"""
        self.assertEqual(validate_title("Monthly Salary"), "Monthly Salary")


class TestFinanceManager(unittest.TestCase):

    def setUp(self):
        """Fresh FinanceManager for each test"""
        self.manager = FinanceManager(data_file="data/unit_test_temp.json")
        # Force clean state
        self.manager.categories = {}
        self.manager.transactions = []

    def test_add_category(self):
        """Test 8: Add new category"""
        self.manager.add_category("Entertainment")
        self.assertIn("Entertainment", self.manager.get_category_names())

    def test_balance_calculation(self):
        """Test 9: Balance calculation"""
        self.manager.categories = {}
        self.manager.transactions = []
        
        self.manager.add_category("Salary")
        self.manager.add_category("Food")
        
        self.manager.add_transaction("March Salary", "500000", "Salary", "Income", "20/03/2026")
        self.manager.add_transaction("Lunch", "15000", "Food", "Expense", "25/03/2026")
        
        self.assertEqual(self.manager.get_balance(), 485000)

    def test_total_income_and_expense(self):
        """Test 10: Total income and expense calculation"""
        self.manager.categories = {}
        self.manager.transactions = []
        
        self.manager.add_category("Salary")
        self.manager.add_transaction("Salary Payment", "300000", "Salary", "Income", "21/03/2026")
        
        self.assertEqual(self.manager.get_total_income(), 300000)
        self.assertEqual(self.manager.get_total_expense(), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)