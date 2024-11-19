import re
import sys
import logging
from model import SettingModel
from xml_writer import write_to_xml_file

logging.basicConfig(level=logging.INFO)

reg_dict = {
    'Id': r'(?<![\w-])name="([^"]+)"',
    'Name': r'default-name="([^"]+)"',
    'Description': r';;;\s*(.+)',
    'MacAddress': r'mac-address=([\w:]+)',
    'Status': r'\b(RS|R|X)\b'
}
def config_parser(filename):
    """breaks the text into blocks, calls param_finder, write_to_xml_file and create instance of the class"""
    interfaces = []

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            file.readline()
            content = file.read()
    except FileNotFoundError:
        logging.error(f"Файл '{filename}' не найден.")
        return
    except IOError as e:
        logging.error(f"Ошибка при чтении файла '{filename}': {e}")
        return

    blocks = re.split(r'(?=(^|\s)\d+\s+(?:R|RS|X)?\b)', content)
    blocks = [block for block in blocks if block.strip()]

    for i, block in enumerate(blocks, 1):
        logging.info(f'Обработка блока {i}:\n{block}\n')

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

    interfaces= config_parser(text_file)
    write_to_xml_file(interfaces)