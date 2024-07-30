import pytest
import os
from src.fixed_width_parser import FixedWidthParser

# Paths are static for local unit testing, if we need to add them in CICD we can variablize them too
spec_file = r'C:\Users\karan\Projects\demyst\problem1\data\fixed_width_spec.txt'
input_file = r'C:\Users\karan\Projects\demyst\problem1\data\input.txt'
test_output_file = r'C:\Users\karan\Projects\demyst\problem1\test\data\output.csv'
generated_test_file = r'C:\Users\karan\Projects\demyst\problem1\test\data\test_input.txt'

parser = FixedWidthParser(spec_file)


def test_generate_fixed_width():
    data = [
        ['Alice', '27', 'Los Angeles'],
        ['Bob', '22', 'Chicago']
    ]
    parser.generate_fixed_width_file(data, generated_test_file)
    with open(generated_test_file, 'r') as file:
        lines = file.readlines()
    assert lines[0] == 'Alice     27 Los Angeles    \n'
    assert lines[1] == 'Bob       22 Chicago        \n'


def test_parse_fixed_width():
    parser.parse_fixed_width_file(input_file, test_output_file)
    parser.parse_fixed_width_file(input_file, test_output_file)
    with open(test_output_file, 'r') as file:
        lines = file.readlines()
    assert lines[0].strip() == 'Name,Age,City'
    assert lines[1].strip() == 'John Doe,025,New York'
    assert lines[2].strip() == 'Jane Smith,030,San Francisco'


@pytest.fixture(autouse=True)
def cleanup_files():
    yield
    if os.path.exists(test_output_file):
        os.remove(test_output_file)
    if os.path.exists(generated_test_file):
        os.remove(generated_test_file)
