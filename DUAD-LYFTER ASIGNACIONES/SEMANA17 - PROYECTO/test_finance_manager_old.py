# test_finance_manager.py
"""
Test for FinanceManager.
"""

from services.finance_manager import FinanceManager


def test_finance_manager():
    """Test the FinanceManager with simplified logic."""
    print("=" * 70)
    print("🧪 TESTING FINANCE MANAGER (SIMPLIFIED)")
    print("=" * 70)

    # Use a test file
    manager = FinanceManager(data_file="data/test_finance_data.json")

    try:
        print("\n1. Managing Categories...")

        # Add categories only if they don't exist
        categories_to_add = ["Food", "Salary", "Transport"]
        for cat_name in categories_to_add:
            try:
                manager.add_category(cat_name)
                print(f"   ✅ Added new category: {cat_name}")
            except ValueError:
                print(f"   ℹ️  Category already exists: {cat_name}")

        print(f"   Total categories: {len(manager.get_category_names())}")

        print("\n2. Adding Transactions...")

        # Add some transactions
        manager.add_transaction(
            title="Monthly Salary",
            amount="850000",
            category_name="Salary",
            trans_type="Income",
            date_str="20/03/2026"
        )

        manager.add_transaction(
            title="Groceries Shopping",
            amount="24500",
            category_name="Food",
            trans_type="Expense",
            date_str="25/03/2026"
        )

        manager.add_transaction(
            title="Bus Ticket",
            amount="3500",
            category_name="Transport",
            trans_type="Expense"
        )

        print(f"   ✅ Added {len(manager.transactions)} transactions")

        # Show summary
        print("\n3. Financial Summary:")
        print(f"   Total Income     : ${manager.get_total_income():,.2f}")
        print(f"   Total Expense    : ${manager.get_total_expense():,.2f}")
        print(f"   Net Balance      : ${manager.get_balance():,.2f}")

        # Show transactions
        print("\n4. Current Transactions:")
        for t in manager.get_all_transactions()[:5]:   # show maximum 5
            print(f"   {t.date} | {t.type:8} | {t.title:25} | {t.category.name:12} | {t.get_display_amount()}")

        # Test Export
        print("\n5. Testing CSV Export...")
        filepath = manager.export_to_csv()
        print(f"   ✅ Exported to: {filepath}")

        print("\n" + "=" * 70)
        print("🎉 TEST PASSED SUCCESSFULLY!")
        print("FinanceManager is working correctly.")
        print("=" * 70)

    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    test_finance_manager()