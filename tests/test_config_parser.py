import unittest
import os
from main import config_parser


class TestConfigParser(unittest.TestCase):
    """Unit tests for the `config_parser` function."""

    def setUp(self):
        self.test_filename = 'test_network_device_output.txt'

    def test_config_parser_output(self):
        """Test parsing a valid input file."""
        result = config_parser(self.test_filename)

        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

        # Validate the first parsed object
        self.assertEqual(result[0].Id, "ether2")
        self.assertEqual(result[0].Name, "ether2")
        self.assertEqual(result[0].MacAddress, "64:D1:54:87:2D:1F")
        self.assertEqual(result[0].Status, None)

        # Validate the second parsed object
        self.assertEqual(result[1].Id, "ether3")
        self.assertEqual(result[1].Name, "ether3")
        self.assertEqual(result[1].MacAddress, "64:D1:54:87:2D:20")
        self.assertEqual(result[1].Status, None)

    def test_empty_file(self):
        """Test handling of an empty input file."""
        empty_filename = 'empty_test_file.txt'
        with open(empty_filename, 'w', encoding='utf-8') as file:
            pass

        result = config_parser(empty_filename)
        self.assertEqual(result, [])

        os.remove(empty_filename)


if __name__ == '__main__':
    unittest.main()
