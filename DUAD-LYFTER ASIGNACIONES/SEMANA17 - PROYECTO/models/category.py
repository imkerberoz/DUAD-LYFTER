# models/category.py
"""
Category model with custom color support.
"""

from typing import Dict


class Category:
    """
    Represents a financial category with a name and custom color.
    Colors are stored as hex strings (e.g., '#FFA500').
    """
    def __init__(self, name: str, color: str = "#1E90FF"):
        """
        Initialize a new Category.

        Args:
            name (str): Name of the category (e.g., "Food", "Salary")
            color (str): Hex color code (default: DodgerBlue)
        """
        if not name or not name.strip():
            raise ValueError("Category name cannot be empty.")

        self.name = name.strip().capitalize()
        self.color = self._validate_color(color)

    def _validate_color(self, color: str) -> str:
        """Validate and normalize hex color. Return default if invalid."""
        if not color or not isinstance(color, str):
            return "#1E90FF"
        color = color.strip().upper()
        if color.startswith("#") and len(color) in (4, 7):
            return color
        return "#1E90FF"  # fallback

    def __str__(self) -> str:
        return self.name

    def __eq__(self, other) -> bool:
        if isinstance(other, Category):
            return self.name.lower() == other.name.lower()
        return False

    def __hash__(self) -> int:
        return hash(self.name.lower())

    def to_dict(self) -> Dict:
        """Convert category to dictionary for JSON saving."""
        return {
            "name": self.name,
            "color": self.color
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Category':
        """Create Category from dictionary (used when loading from JSON)."""
        return cls(
            name=data.get("name", "Unknown"),
            color=data.get("color", "#1E90FF")
        )