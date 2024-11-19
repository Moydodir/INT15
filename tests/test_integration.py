import unittest
import os
import xml.etree.ElementTree as ET
from main import config_parser
from xml_writer import write_to_xml_file

class TestIntegration(unittest.TestCase):
    def setUp(self):
        """test config"""
        self.test_input_file = "int_test.txt"
        self.test_output_file = "test_device_settings.xml"

    def tearDown(self):
        """Delete test xml file"""
        if os.path.exists(self.test_output_file):
            os.remove(self.test_output_file)

    def test_integration(self):
        """integration test for all process"""

        # Testing config_parser
        interfaces = config_parser(self.test_input_file)
        self.assertIsInstance(interfaces, list)
        self.assertEqual(len(interfaces), 8)

        # Checking that the objects SettingModel were created correctly
        self.assertEqual(interfaces[0].Id, "ether1")
        self.assertEqual(interfaces[0].Name, "ether1")
        self.assertEqual(interfaces[0].Description, None)
        self.assertEqual(interfaces[0].MacAddress, "64:D1:54:87:2D:1E")
        self.assertEqual(interfaces[0].Status, None)

        # Check that all statuses are processed correctly
        self.assertEqual(interfaces[4].Status, "up")  # Status "R" = "up"
        self.assertEqual(interfaces[5].Status, "up")  # Status "RS" = "up"
        self.assertEqual(interfaces[6].Status, "down")  # Status "X" = "down"

        with self.assertLogs(level='INFO') as log:
            write_to_xml_file(interfaces, self.test_output_file)

            # Check that the file has been recorder
            self.assertTrue(os.path.exists(self.test_output_file))

            # Check that the logs contain a message about a successful recording
            self.assertIn(f"INFO:root:Файл успешно записан: {self.test_output_file}", log.output)

        tree = ET.parse(self.test_output_file)
        root = tree.getroot()
        self.assertEqual(root.tag, "device")
        self.assertEqual(len(root), 8)

        # Checking the data inside the XML for the first interface
        interface1 = root[0]
        self.assertEqual(interface1.find("Id").text, "ether1")
        self.assertEqual(interface1.find("Name").text, "ether1")
        self.assertEqual(interface1.find("Description").text, "N/A")
        self.assertEqual(interface1.find("MacAddress").text, "64:D1:54:87:2D:1E")
        self.assertEqual(interface1.find("Status").text, "N/A")

        # Checking the data inside the XML for the second interface
        interface8 = root[7]
        self.assertEqual(interface8.find("Id").text, "bridge1")
        self.assertEqual(interface8.find("Name").text, "N/A")
        self.assertEqual(interface8.find("Description").text, "N/A")
        self.assertEqual(interface8.find("MacAddress").text, "64:D1:54:87:2D:24")
        self.assertEqual(interface8.find("Status").text, "up")

    def test_invalid_file(self):
        """Test for incorrect file path"""
        with self.assertLogs(level='ERROR') as log:
            interfaces = config_parser("invalid_file.txt")
            self.assertIsNone(interfaces)
            self.assertIn("Файл 'invalid_file.txt' не найден.", log.output[0])

if __name__ == "__main__":
    unittest.main()
