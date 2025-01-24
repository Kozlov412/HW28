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
        
        
    def write_file(self, filepath: str, *data: str) -> None:
        """Записывает данные в TXT файл.

        Args:
            filepath (str): Путь к файлу.
            *data (str): Строки для записи.
        """
        try:
            with open(filepath, 'w', encoding='utf-8') as file:
                for item in data:
                    file.write(item)
        except Exception as e:
            print(f"Ошибка при записи в файл: {e}")

