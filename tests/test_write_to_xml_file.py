import unittest
import logging
from main import write_to_xml_file, SettingModel
import os

# Configure logging for tests
logging.basicConfig(level=logging.INFO)

class TestWriteToXmlFile(unittest.TestCase):
    """
    Unit tests for the `write_to_xml_file` function.
    Verifies correct file creation and handling of invalid input.
    """

    def setUp(self):
        """
        Prepare test data before each test case.
        Creates sample SettingModel objects and defines a test filename.
        """
        self.interfaces = [
            SettingModel(Id="1", Name="ether1", Description="desc1", MacAddress="00:11:22:33:44:55", Status="up"),
            SettingModel(Id="2", Name="ether2", Description="desc2", MacAddress="00:11:22:33:44:66", Status="down")
        ]
        self.test_filename = "test_device_settings.xml"

    def tearDown(self):
        """
        Clean up after each test case.
        Removes the test file if it was created.
        """
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_write_to_xml_file_creates_file(self):
        """
        Test that `write_to_xml_file` successfully creates an XML file.
        """
        write_to_xml_file(self.interfaces, filename=self.test_filename)
        self.assertTrue(os.path.exists(self.test_filename))

    def test_invalid_input(self):
        """
        Test handling of invalid input data.
        Ensures an appropriate exception is raised for invalid input.
        """
        with self.assertRaises(ValueError) as context:
            write_to_xml_file("invalid_input")

        self.assertEqual(
            str(context.exception),
            "Входные данные должны быть списком объектов SettingModel."
        )

if __name__ == "__main__":
    unittest.main()
