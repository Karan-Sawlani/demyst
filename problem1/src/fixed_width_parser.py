import csv
import os
from dotenv import load_dotenv


class FixedWidthParser:
    """
    A class to parse fixed-width files and generate delimited files.
    """
    def __init__(self, spec_file: str):
        """
        Initializes the FixedWidthParser with a specification file.

        :param spec_file: Path to the specification file containing field names and lengths.
        """
        self.spec = self._parse_spec_file(spec_file)

    def _parse_spec_file(self, spec_file: str) -> dict:
        """
        Parses the specification file to extract field names and lengths.

        :param spec_file: Path to the specification file.
        :return: Dictionary with field names as keys and lengths as values.
        """
        spec = {}
        with open(spec_file, 'r') as file:
            for line in file:
                field, length = line.strip().split()
                spec[field] = int(length)
        return spec

    def parse_fixed_width_file(self, input_file: str, output_file: str):
        """
        Parses a fixed-width file and generates a delimited file (CSV).

        :param input_file: Path to the fixed-width input file.
        :param output_file: Path to the output CSV file.
        """
        with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
            csv_writer = csv.writer(outfile)
            headers = list(self.spec.keys())
            csv_writer.writerow(headers)

            for line in infile:
                start = 0
                row = []
                for field in headers:
                    length = self.spec[field]
                    print(
                        f"line: {line}, "
                        f"field: {field}, "
                        f"start_from_char: {start}, "
                        f"end_till_char: {length}, "
                        f"line_parsed: {line[start:start + length].strip()}"
                    )
                    row.append(line[start:start + length].strip())
                    start += length
                    print(f"new_start: {start}")
                print("==========================")
                csv_writer.writerow(row)

    def generate_fixed_width_file(self, data: list, output_file: str):
        """
        Generates a fixed-width file from given data.

        :param data: List of lists containing data to be written to the fixed-width file.
        :param output_file: Path to the output fixed-width file.
        """
        with open(output_file, 'w') as file:
            for row in data:
                line = ''.join([str(value).ljust(self.spec[field]) for field, value in zip(self.spec.keys(), row)])
                file.write(line + '\n')


if __name__ == "__main__":
    load_dotenv() # Load environment variables from .env file
    spec_file = os.getenv('SPEC_FILE_PATH', r'C:\Users\karan\Projects\demyst\problem1\data\fixed_width_spec.txt')
    input_file = os.getenv('INPUT_FILE_PATH', r'C:\Users\karan\Projects\demyst\problem1\data\input.txt')
    output_file = os.getenv('OUTPUT_FILE_PATH', r'C:\Users\karan\Projects\demyst\problem1\data\output.csv')

    parser = FixedWidthParser(spec_file)
    parser.parse_fixed_width_file(input_file, output_file)

    # For testing generation
    data = [
        ['Alice', '27', 'Los Angeles'],
        ['Bob', '22', 'Chicago']
    ]
    generated_file = os.getenv('GENERATE_TEST_INPUT_FILE_PATH', r'C:\Users\karan\Projects\demyst\problem1\data\test_input.txt')
    parser.generate_fixed_width_file(data, generated_file)
