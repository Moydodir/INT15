import re
import logging

pattern = r'(?=(^|\s)\d+\s+(?:R|RS|X)?\b)'

def read_file(filename):
    """Parses the configuration file, extracts blocks of interest."""
    content = []

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except FileNotFoundError:
        logging.error(f"Файл '{filename}' не найден.")
        return
    except IOError as e:
        logging.error(f"Ошибка при чтении файла '{filename}': {e}")
        return

    for i, line in enumerate(lines):
        stripped_line = line.strip()

        if not stripped_line:
            remaining_content = ''.join(lines[i + 1:])
            if not re.search(pattern, remaining_content):
                logging.info(f"Пустая строка найдена, далее нет паттерна. Обрезаем текст до строки {i}.")
                break

        content.append(line)

    full_content = ''.join(content)

    match = re.search(pattern, full_content)
    if match:
        full_content = full_content[match.start():]
    else:
        logging.error("Полезная нагрузка не найдена в файле.")
        return []

    blocks = re.split(pattern, full_content)
    blocks = [block for block in blocks if block.strip()]  # Удалить пустые блоки

    for i, block in enumerate(blocks, 1):
        logging.info(f'Блок № {i}:\n{block}\n')

    return blocks