# tests/test_param_finder.py
import unittest
from main import param_finder

class TestParamFinder(unittest.TestCase):
    """
    Unit tests for the `param_finder` function.
    Verifies the correct parsing of input blocks into expected parameter dictionaries.
    """

    def test_param_finder_valid_data(self):
        """
        Test parsing a block of valid data with all expected fields.
        Checks if all parameters are correctly extracted and transformed.
        """
        block = """0 RS ;;; LAN
                   name="LAN" default-name="ether2" mtu=1500 mac-address=50:00:00:31:00:01"""
        expected = {
            "Id": "LAN",
            "Name": "ether2",
            "Description": "LAN",
            "MacAddress": "50:00:00:31:00:01",
            "Status": "up"
        }
        result = param_finder(block)
        self.assertEqual(result, expected)

    def test_param_finder_invalid_data(self):
        """
        Test parsing a block of data with missing optional fields.
        Ensures that missing fields are handled gracefully with default `None` values.
        """
        block = """0 X  name="LAN" default-name="ether2" mtu=1500 """
        expected = {
            "Id": "LAN",
            "Name": "ether2",
            "Description": None,
            "MacAddress": None,
            "Status": "down"
        }
        result = param_finder(block)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
