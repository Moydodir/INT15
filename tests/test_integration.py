import unittest
import os
import xml.etree.ElementTree as ET
from main import config_parser, read_file, write_to_xml_file

class TestIntegration(unittest.TestCase):

    def setUp(self):
        """Prepare the test environment before each test."""
        # Path to the test file
        self.test_file = 'int_test.txt'

        # Ensure the test file exists before running the test
        self.assertTrue(os.path.exists(self.test_file), f"Test file '{self.test_file}' not found.")

    def test_integration(self):
        """Test the entire flow from reading the file to generating the XML output."""

        # Read blocks from the test file
        blocks = read_file(self.test_file)

        # Ensure that blocks were extracted properly
        self.assertIsNotNone(blocks)
        self.assertGreater(len(blocks), 0, "No blocks were extracted from the file.")

        # Apply the config_parser to create SettingModel objects
        interfaces = config_parser(blocks)

        # Ensure there are exactly 8 interfaces, including those that are active, down, or disabled
        self.assertEqual(len(interfaces), 8, "Number of interfaces does not match the expected count.")

        # Ensure some interfaces have status "up"
        self.assertEqual(interfaces[4].Status, "up", "The status of interface ether5 should be 'up'.")
        self.assertEqual(interfaces[5].Status, "up", "The status of interface wlan1 should be 'up'.")

        # Serialize the interfaces to XML
        output_file = 'test_output.xml'
        write_to_xml_file(interfaces, filename=output_file)

        # Ensure the XML file was created
        self.assertTrue(os.path.exists(output_file), "XML file was not created.")

        # Open the file and check its content (e.g., the presence of the <device> tag)
        tree = ET.parse(output_file)
        root = tree.getroot()
        self.assertEqual(root.tag, "device", "The root element of the XML should be 'device'.")

        # Ensure there are at least 8 interfaces in the XML
        interfaces_xml = root.findall("interface")
        self.assertEqual(len(interfaces_xml), 8, "Number of interfaces in the XML does not match the expected count.")

        # Check some fields in the first interface
        first_interface = interfaces_xml[0]
        self.assertEqual(first_interface.find("Id").text, "ether1", "The Id of the first interface is incorrect.")
        self.assertEqual(first_interface.find("Status").text, "N/A", "The Status of the first interface is incorrect.")

    def tearDown(self):
        """Clean up after the test."""
        # Remove the XML file after the test
        if os.path.exists('test_output.xml'):
            os.remove('test_output.xml')


if __name__ == "__main__":
    unittest.main()
