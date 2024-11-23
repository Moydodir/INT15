import re
import sys
import logging
from model import SettingModel
from xml_writer import write_to_xml_file
from file_reader import read_file

logging.basicConfig(level=logging.INFO)

reg_dict = {
    'Id': r'(?<![\w-])name="([^"]+)"',
    'Name': r'default-name="([^"]+)"',
    'Description': r';;;\s*(.+)',
    'MacAddress': r'mac-address=([\w:]+)',
    'Status': r'\b(RS|R|X)\b'
}

def config_parser(blocks):
    """breaks the text into blocks, calls param_finder, write_to_xml_file and create instance of the class"""
    interfaces = []

    for i, block in enumerate(blocks, 1):
        logging.info(f'Обработка блока {i}')

        interface_settings = param_finder(block)
        if interface_settings:
            interfaces.append(SettingModel(**interface_settings))
        else:
            logging.warning(f'Не удалось извлечь параметры для блока {i}')

    return interfaces

def param_finder(block):
    """looking for useful parameters in block"""
    params = {}

    for key in reg_dict:
        param = re.search(reg_dict[key], block)
        params[key] = param.group(1) if param else None

    if params["Status"]:
        if 'R' in params["Status"]:
            params["Status"] = "up"
        else:
            params["Status"] = "down"

    return params

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Пожалуйста, укажите путь к текстовому файлу как аргумент командной строки.")
        sys.exit(1)

    text_file = sys.argv[1]

    blocks = read_file(text_file)
    interfaces= config_parser(blocks)
    write_to_xml_file(interfaces)