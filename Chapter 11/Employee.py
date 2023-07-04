class Employee:
    """Represents an employee."""

    def __init__(self, first, last, salary):
        """Collect basic employee information."""
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, raise_amount=0):
        """Give nice raise!"""
        if raise_amount == 0:
            raise_amount = 5000
        self.salary += raise_amount
