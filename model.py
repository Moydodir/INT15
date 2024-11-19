import xml.etree.ElementTree as ET

class SettingModel:
    """
    Represents a model for a network device's interface settings.

    Attributes:
        Id (str): The identifier of the interface.
        Name (str): The name of the interface.
        Description (str): The description of the interface, if available.
        MacAddress (str): The MAC address of the interface.
        Status (str): The status of the interface ('up', 'down', or 'N/A').
    """

    __slots__ = ('Id', 'Name', 'Description', 'MacAddress', 'Status')

    def __init__(self, Id: str, Name: str, Description, MacAddress: str, Status: str):
        self.Id = Id
        self.Name = Name
        self.Description = Description
        self.MacAddress = MacAddress
        self.Status = Status

    def serialization(self) -> ET.ElementTree:
        """Serializes the object to an XML tree."""
        root = ET.Element("interface")
        for name_attr in self.__slots__:
            value = getattr(self, name_attr)
            ET.SubElement(root, name_attr).text = value if value is not None else "N/A"
        return ET.ElementTree(root)