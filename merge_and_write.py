import os
import pytest

from tempfile import NamedTemporaryFile


# Функция, которую нужно протестировать.
def merge_and_write(file1_path, file2_path, output_file_path):
    try:
        with open(file1_path, 'r') as file1:
            data1 = file1.read().strip()

        with open(file2_path, 'r') as file2:
            data2 = file2.read().strip()

        merged_data = data1 + ' ' + data2

        with open(output_file_path, 'w') as output_file:
            output_file.write(merged_data)

        with open(output_file_path, 'r') as output_file:
            data = output_file.read()
        return data
    except FileNotFoundError:
        return "Один из файлов не найден"


# Фикстура для создания временных файлов.
@pytest.fixture
def create_temp_files():
    temp_files = []

    def _create_temp_file(initial_content=None):
        temp_file = NamedTemporaryFile(delete=False)
        if initial_content:
            with open(temp_file.name, 'w') as f:
                f.write(initial_content)
        temp_files.append(temp_file.name)
        return temp_file.name

    yield _create_temp_file

    for temp_file in temp_files:
        os.remove(temp_file)


# Тесты
def test_merge_and_write(create_temp_files):
    file1 = create_temp_files("Hello")
    file2 = create_temp_files("World")
    output_file = create_temp_files()

    result = merge_and_write(file1, file2, output_file)
    assert result == "Hello World"


def test_merge_and_write_missing_file(create_temp_files):
    file1 = create_temp_files("Hello")
    missing_file = "missing_file.txt"
    output_file = create_temp_files()

    result = merge_and_write(file1, missing_file, output_file)
    assert result == "Один из файлов не найден"


if __name__ == "__main__":
    pytest.main()