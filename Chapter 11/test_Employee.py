import unittest
from Employee import Employee


class TestEmployee(unittest.TestCase):
    """Test for the Employee class."""

    def setUp(self):
        """
        Create an Employee for use in all test methods.
        """
        self.base_salary = 40000
        self.employee = Employee('John', 'Doe', self.base_salary)

    def test_give_default_raise(self):
        """Test default raise is applied."""
        self.employee.give_raise()
        self.assertEqual(self.base_salary+5000, self.employee.salary)

    def test_give_custom_raise(self):
        """Test custom raise is applied."""
        custom_raise = 20000
        self.employee.give_raise(custom_raise)
        self.assertEqual(self.base_salary + custom_raise, self.employee.salary)


if __name__ == '__main__':
    unittest.main()
