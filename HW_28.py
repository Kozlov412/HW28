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

    def append_file(self, filepath: str, *data: str) -> None:
        """Добавляет данные в конец TXT файла.

        Args:
            filepath (str): Путь к файлу.
            *data (str): Строки для добавления.
        """
        try:
            with open(filepath, 'a', encoding='utf-8') as file:
                for item in data:
                    file.write(item)
        except Exception as e:
            print(f"Ошибка при добавлении в файл: {e}")


if __name__ == "__main__": # Тестирование
    handler = TxtFileHandler()

    # Запись в файл
    handler.write_file("test.txt", "This is a test string.\n", "Another test string.\n")

    # Добавление в файл
    handler.append_file("test.txt", "This is an appended string.\n")

    # Чтение из файла
    content = handler.read_file("test.txt")
    print(content)
    
    # Проверка на несуществующий файл
    empty_content = handler.read_file("nonexistent_file.txt")
    print(f"Содержимое несуществующего файла: '{empty_content}'")        

