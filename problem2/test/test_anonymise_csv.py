import os
import pytest
import hashlib
from src.generate_csv import CSVGenerator
from src.anonymise_csv import CSVAnonymizer


test_generated_file_path = r'C:\Users\karan\Projects\demyst\problem2\test\data\test_sample.csv'
test_anonymised_file_path = r'C:\Users\karan\Projects\demyst\problem2\test\data\test_anonymised_sample.csv'


def hash_value(value):
    return hashlib.md5(value.encode()).hexdigest()


def test_anonymize_csv():
    generator = CSVGenerator(test_generated_file_path, 10)
    generator.generate_csv()

    anonymizer = CSVAnonymizer(test_generated_file_path, test_anonymised_file_path)
    anonymizer.anonymize_csv()

    with open(test_anonymised_file_path, 'r', newline="\n") as file:
        lines = file.readlines()

    assert len(lines) == 11  # 10 data lines + 1 header line
    header = lines[0].strip().split(',')
    assert header == ['first_name', 'last_name', 'address', 'date_of_birth']

    original_lines = open(test_generated_file_path, 'r', newline="\n").readlines()[1:]
    anonymized_lines = lines[1:]

    for original, anonymized in zip(original_lines, anonymized_lines):
        orig_data = original.strip().split(',')
        anon_data = anonymized.strip().split(',')

        assert hash_value(orig_data[0]) == anon_data[0]
        assert hash_value(orig_data[1]) == anon_data[1]
        assert hash_value(orig_data[2]) == anon_data[2]


@pytest.fixture(autouse=True)
def cleanup_files():
    yield
    if os.path.exists(test_generated_file_path):
        os.remove(test_generated_file_path)
    if os.path.exists(test_anonymised_file_path):
        os.remove(test_anonymised_file_path)
