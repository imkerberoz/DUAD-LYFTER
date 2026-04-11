# utils/validators.py
"""
Validation utilities for the Personal Finance Manager application.
Contains functions to validate dates, amounts, titles, and categories.
"""

from datetime import datetime
import re


def validate_date(date_str: str) -> str:
    """
    Validate that the date is in dd/mm/yyyy format and is not in the future.

    Args:
        date_str (str): Date string in dd/mm/yyyy format

    Returns:
        str: Validated date string in dd/mm/yyyy format

    Raises:
        ValueError: If the date format is invalid or the date is in the future
    """
    if not date_str or not date_str.strip():
        raise ValueError("Date cannot be empty.")

    date_str = date_str.strip()

    # Check correct format dd/mm/yyyy
    if not re.match(r"^\d{2}/\d{2}/\d{4}$", date_str):
        raise ValueError("Date must be in the format dd/mm/yyyy (example: 25/03/2026)")

    try:
        date_obj = datetime.strptime(date_str, "%d/%m/%Y")
        
        # Prevent future dates
        today = datetime.now().date()
        if date_obj.date() > today:
            raise ValueError("Date cannot be in the future.")

        return date_str

    except ValueError as e:
        if "time data" in str(e):
            raise ValueError("Invalid date. Please use dd/mm/yyyy format.")
        raise


def validate_amount(amount_input: str) -> float:
    """
    Validate and convert amount to float. Must be greater than zero.

    Args:
        amount_input (str): Amount as string from user input

    Returns:
        float: Valid positive amount

    Raises:
        ValueError: If amount is invalid or not positive
    """
    if not amount_input or not amount_input.strip():
        raise ValueError("Amount cannot be empty.")

    try:
        amount = float(amount_input.strip())
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        return amount
    except ValueError:
        raise ValueError("Amount must be a valid number (e.g., 12500 or 45.50)")


def validate_title(title: str) -> str:
    """
    Validate that the title is not empty.
    """
    if not title or not title.strip():
        raise ValueError("Title cannot be empty.")
    return title.strip()


def validate_category(category) -> bool:
    """
    Check if a category was selected.
    """
    if not category:
        raise ValueError("You must select a category.")
    return True