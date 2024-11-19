import logging
from model import SettingModel
import xml.etree.ElementTree as ET


def write_to_xml_file(interfaces, filename="device_settings.xml"):
    """write xml tree in file """
    if not isinstance(interfaces, list) or not all(isinstance(i, SettingModel) for i in interfaces):
        raise ValueError("Входные данные должны быть списком объектов SettingModel.")

    root = ET.Element("device")
    tree = ET.ElementTree(root)

    for interface in interfaces:
        interface_element = interface.serialization().getroot()
        root.append(interface_element)

    tree.write(filename, encoding="utf-8", xml_declaration=True)
    logging.info(f"Файл успешно записан: {filename}")
