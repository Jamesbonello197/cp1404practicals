"""CP1404/CP5632 Practical - Guitar example."""
from datetime import datetime


class Guitar:
    """Represents a Guitar object"""

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self) -> str:
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        current_year = datetime.now().year
        return current_year - self.year

    def is_vintage(self):
        return self.get_age() >= 50
