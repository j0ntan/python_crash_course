import unittest
from city_functions import get_formatted_city


class CitiesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_city_country(self):
        """Does a standard city-country pair work?"""
        formatted_city = get_formatted_city('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago, Chile')

    def test_city_country_population(self):
        """Does a  city-country pair w/ population work?"""
        formatted_city = get_formatted_city('santiago', 'chile', 5000000)
        self.assertEqual(
            formatted_city, 'Santiago, Chile - population 5000000')


if __name__ == '__main__':
    unittest.main()
