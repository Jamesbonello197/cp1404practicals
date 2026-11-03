"""CP1404 Practical - Programming Languages example."""


class ProgrammingLanguage:
    """Represents a Programming Language Object"""

    def __init__(self, language_name: str, typing: str, reflection: str, year: int):
        self.language_name = language_name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == "Dynamic"

    def __str__(self) -> str:
        return f"{self.language_name}, {self.typing}, Reflection={self.reflection}, First appeared in {self.year}"
