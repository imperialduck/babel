import year
import unittest


class YearTest(unittest.TestCase):
    """
    Tests for year.py
    """
    def test_year(self):
        """Test that input_year is INT"""
        self.assertEqual(type(year.validate_year(1987)), int)
        self.assertEqual(type(year.validate_year("1987")), int)
        self.assertNotEqual(type(year.validate_year("lxlw<kjx")), int)


if __name__ == "__main__":
    unittest.main()