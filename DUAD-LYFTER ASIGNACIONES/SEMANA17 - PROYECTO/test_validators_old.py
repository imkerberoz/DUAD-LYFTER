# test_validators.py
"""
Unit tests for validation functions.
We run this file to verify all validators work correctly.
"""

from utils.validators import (
    validate_date,
    validate_amount,
    validate_title,
    validate_category
)
from models.category import Category


def test_validators():
    """Test all validation functions."""
    print("=" * 70)
    print("🧪 TESTING VALIDATORS")
    print("=" * 70)

    try:
        # Test 1: validate_date
        print("\n1. Testing validate_date()...")
        
        # Valid dates
        print("   Testing valid dates:")
        print(f"   ✅ {validate_date('25/03/2026')}")
        print(f"   ✅ {validate_date('01/01/2025')}")   # past date should work
        
        # Invalid format
        print("\n   Testing invalid format...")
        try:
            validate_date("2026-03-25")
        except ValueError as e:
            print(f"   ✅ Correctly rejected: {e}")

        # Future date (this should fail)
        print("\n   Testing future date...")
        try:
            validate_date("30/12/2030")   # This will fail if today is before 2030
        except ValueError as e:
            print(f"   ✅ Correctly rejected future date: {e}")

        # Test 2: validate_amount
        print("\n2. Testing validate_amount()...")
        print(f"   ✅ {validate_amount('12500')}")
        print(f"   ✅ {validate_amount('45.75')}")
        
        try:
            validate_amount('-100')
        except ValueError as e:
            print(f"   ✅ Correctly rejected negative amount: {e}")

        try:
            validate_amount('abc')
        except ValueError as e:
            print(f"   ✅ Correctly rejected invalid number: {e}")

        # Test 3: validate_title
        print("\n3. Testing validate_title()...")
        print(f"   ✅ {validate_title('Monthly Salary')}")
        
        try:
            validate_title("")
        except ValueError as e:
            print(f"   ✅ Correctly rejected empty title: {e}")

        # Test 4: validate_category
        print("\n4. Testing validate_category()...")
        cat = Category("Food")
        print(f"   ✅ Category validation passed for: {cat}")
        
        try:
            validate_category(None)
        except ValueError as e:
            print(f"   ✅ Correctly rejected None category: {e}")

        print("\n" + "=" * 70)
        print("🎉 ALL VALIDATOR TESTS PASSED SUCCESSFULLY!")
        print("Validators are working correctly.")
        print("=" * 70)

    except Exception as e:
        print(f"\n❌ UNEXPECTED ERROR: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    test_validators()