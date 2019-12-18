from year import validate_year
import unittest


class YearTest(unittest.TestCase):
    """
    Tests for year.py
    """
    def test_year(self):
        """
        
        """
        
        self.assertEqual(validate_year(1987), 1987)
        self.assertEqual(validate_year("1987"), 1987)
        self.assertEqual(validate_year("lxlw<kjx"), None)
        self.assertEqual(validate_year("03"), 2003)
        self.assertEqual(validate_year("69"), 1969)
        self.assertEqual(validate_year("20"), 1920)
        self.assertEqual(validate_year("2020"), None)


if __name__ == "__main__":
    unittest.main()
