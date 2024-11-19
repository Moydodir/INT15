import unittest
from model import SettingModel

class TestSettingModel(unittest.TestCase):
    """
    Unit tests for the `SettingModel` class.
    Verifies the initialization and serialization of the class.
    """

    def setUp(self):
        """
        Set up a test instance of `SettingModel` for use in tests.
        """
        self.interface = SettingModel(
            Id="1",
            Name="ether1",
            Description="description",
            MacAddress="00:11:22:33:44:55",
            Status="up"
        )

    def test_init(self):
        """
        Test the initialization of the `SettingModel` instance.
        Checks if all attributes are set correctly.
        """
        self.assertEqual(self.interface.Id, "1")
        self.assertEqual(self.interface.Name, "ether1")
        self.assertEqual(self.interface.Description, "description")
        self.assertEqual(self.interface.MacAddress, "00:11:22:33:44:55")
        self.assertEqual(self.interface.Status, "up")

    def test_serialization(self):
        """
        Test the `serialization` method of the `SettingModel` class.
        Verifies that the object is serialized into an XML tree with correct tags and values.
        """
        tree = self.interface.serialization()
        root = tree.getroot()

        # Verify the root tag and its children
        self.assertEqual(root.tag, "interface")
        self.assertEqual(root.find("Id").text, "1")
        self.assertEqual(root.find("Name").text, "ether1")
        self.assertEqual(root.find("Description").text, "description")
        self.assertEqual(root.find("MacAddress").text, "00:11:22:33:44:55")
        self.assertEqual(root.find("Status").text, "up")


if __name__ == "__main__":
    unittest.main()
