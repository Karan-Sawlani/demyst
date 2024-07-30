import os
import pytest
import hashlib
from src.generate_csv import CSVGenerator


test_generated_file_path = r'C:\Users\karan\Projects\demyst\problem2\test\data\test_sample.csv'


def hash_value(value):
    return hashlib.md5(value.encode()).hexdigest()


def test_generate_csv():
    generator = CSVGenerator(test_generated_file_path, 10)
    generator.generate_csv()

    with open(test_generated_file_path, 'r', newline="\n") as file:
        lines = file.readlines()

    assert len(lines) == 11  # 10 data lines + 1 header line
    header = lines[0].strip().split(',')
    assert header == ['first_name', 'last_name', 'address', 'date_of_birth']


@pytest.fixture(autouse=True)
def cleanup_files():
    yield
    if os.path.exists(test_generated_file_path):
        os.remove(test_generated_file_path)
