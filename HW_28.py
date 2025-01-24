from typing import List

class TxtFileHandler:
    """Класс для работы с TXT файлами."""

    def read_file(self, filepath: str) -> str:
        """Читает данные из TXT файла.

        Args:
            filepath (str): Путь к файлу.

        Returns:
            str: Содержимое файла или пустая строка, если файл не найден.
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                data = file.read()
            return data
        except FileNotFoundError:
            return ""
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            return ""
