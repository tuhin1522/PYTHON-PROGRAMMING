import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('Tuhin', 'Islam')
        self.assertEqual(formatted_name, 'Tuhin Islam')

if __name__ == '___main__':
    unittest.main()