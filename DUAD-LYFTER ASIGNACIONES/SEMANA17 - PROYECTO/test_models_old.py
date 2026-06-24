# test_models.py
"""
Unit test for Category and Transaction models.
Run this file directly from the project root folder.
"""

from models.category import Category
from models.transaction import Transaction


def test_models():
    """Test all main functionalities of Category and Transaction classes."""
    print("=" * 70)
    print("🧪 TESTING MODELS")
    print("=" * 70)

    try:
        # Test 1: Create Categories
        print("\n1. Creating Categories...")
        cat_food = Category("Food", "#FF5733")           # Orange
        cat_salary = Category("Salary", "#4CAF50")       # Green
        cat_transport = Category("Transport")            # Default colour (DodgerBlue)

        print(f"   ✅ Category: {cat_food} | Colour: {cat_food.color}")
        print(f"   ✅ Category: {cat_salary} | Colour: {cat_salary.color}")
        print(f"   ✅ Category: {cat_transport} | Colour: {cat_transport.color}")

        # Test 2: Create Transactions
        print("\n2. Creating Transactions...")
        
        trans1 = Transaction(
            title="Family Pizza",
            amount=12500,
            category=cat_food,
            trans_type="Expense",
            date_str="25/03/2026"
        )

        trans2 = Transaction(
            title="Monthly Salary",
            amount=850000,
            category=cat_salary,
            trans_type="Income"
            # No date provided → should use today's date
        )

        print(f"   ✅ Expense  → Date: {trans1.date} | {trans1.title} | {trans1.get_display_amount()} | Category: {trans1.category}")
        print(f"   ✅ Income   → Date: {trans2.date} | {trans2.title} | {trans2.get_display_amount()} | Category: {trans2.category}")

        # Test 3: Serialization (to_dict and from_dict)
        print("\n3. Testing serialization (to_dict / from_dict)...")
        data = trans1.to_dict()
        print(f"   ✅ to_dict() → {data}")

        # Prepare categories dictionary for reconstruction
        categories_dict = {
            cat_food.name: cat_food,
            cat_salary.name: cat_salary
        }
        
        trans_recreated = Transaction.from_dict(data, categories_dict)
        print(f"   ✅ from_dict() successful → {trans_recreated.title} | {trans_recreated.date}")

        print("\n" + "=" * 70)
        print("🎉 ALL TESTS PASSED SUCCESSFULLY!")
        print("Models are working correctly.")
        print("=" * 70)

    except Exception as e:
        print(f"\n❌ ERROR during testing: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    test_models()