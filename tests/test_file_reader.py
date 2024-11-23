import unittest
import logging
import os
from main import read_file

# Configure logging for the test
logging.basicConfig(level=logging.INFO)

class TestReadFile(unittest.TestCase):
    """
    Unit tests for the `read_file` function.
    Verifies parsing and splitting of blocks from configuration files.
    """

    def setUp(self):
        """
        Prepare the environment before each test case.
        Create a temporary test file with sample content.
        """
        self.test_filename = "test_file_reader.txt"
        self.test_content = (
            "jsdfkjdssdfnsdfdsfjkdfsjkfdkjdsf\n"
            "Flags: D - dynamic; X - disabled, R - running; S - slave; P - passthrough\n"
            " 0      name=\"ether1\" default-name=\"ether1\" type=\"ether\" mtu=1500 actual-mtu=1500 l2mtu=1598 max-l2mtu=2028\n"
            "        mac-address=64:D1:54:87:2D:1E ifname=\"eth0\" ifindex=8 id=1 link-downs=0 \n\n"
            " 1      name=\"ether2\" default-name=\"ether2\" type=\"ether\" mtu=1500 actual-mtu=1500 l2mtu=1598 max-l2mtu=2028\n"
            "        mac-address=64:D1:54:87:2D:1F ifname=\"eth1\" ifindex=9 id=2 link-downs=0 \n\n"
            " 2      name=\"ether3\" default-name=\"ether3\" type=\"ether\" mtu=1500 actual-mtu=1500 l2mtu=1598 max-l2mtu=2028\n"
            "        mac-address=64:D1:54:87:2D:20 ifname=\"eth2\" ifindex=10 id=3 link-downs=0 \n"
        )
        with open(self.test_filename, "w", encoding="utf-8") as f:
            f.write(self.test_content)

    def tearDown(self):
        """
        Clean up after each test case.
        Remove the temporary test file.
        """
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_read_file_successful_parsing(self):
        """
        Test successful parsing and splitting of the file into blocks.
        """
        blocks = read_file(self.test_filename)
        self.assertIsNotNone(blocks, "The function should return a non-None value.")
        self.assertEqual(len(blocks), 3, "The file should be split into 3 blocks.")
        self.assertTrue("ether1" in blocks[0], "Block 1 should contain 'ether1'.")
        self.assertTrue("ether2" in blocks[1], "Block 2 should contain 'ether2'.")
        self.assertTrue("ether3" in blocks[2], "Block 3 should contain 'ether3'.")

    def test_read_file_file_not_found(self):
        """
        Test behavior when the specified file does not exist.
        """
        non_existent_file = "non_existent_file.txt"
        with self.assertLogs(level="ERROR") as log:
            result = read_file(non_existent_file)
            self.assertIsNone(result, "The function should return None for a missing file.")
            self.assertIn(f"Файл '{non_existent_file}' не найден.", log.output[0])

    def test_read_file_no_useful_data(self):
        """
        Test behavior when the file contains no useful data.
        """
        empty_filename = "empty_test_file.txt"
        with open(empty_filename, "w", encoding="utf-8") as f:
            f.write("random irrelevant text\n")

        with self.assertLogs(level="ERROR") as log:
            result = read_file(empty_filename)
            self.assertEqual(result, [], "The function should return an empty list for no useful data.")
            self.assertIn("Полезная нагрузка не найдена в файле.", log.output[0])

        os.remove(empty_filename)


if __name__ == "__main__":
    unittest.main()
