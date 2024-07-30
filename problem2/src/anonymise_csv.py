import csv
import hashlib
import os
from dotenv import load_dotenv

class CSVAnonymizer:
    """
    A class to anonymize specified columns in a CSV file.
    """

    def __init__(self, input_filename: str, output_filename: str):
        """
        Initializes the CSVAnonymizer with input and output filenames.

        :param input_filename: The name of the input CSV file.
        :param output_filename: The name of the output CSV file.
        """
        self.input_filename = input_filename
        self.output_filename = output_filename

    def _hash_value(self, value: str) -> str:
        """
        Hashes a single value using MD5.

        :param value: The value to hash.
        :return: The hashed value.
        """
        return hashlib.md5(value.encode()).hexdigest()

    def anonymize_csv(self):
        """
        Anonymizes specified columns in the CSV file.
        """
        with open(self.input_filename, 'r') as infile, open(self.output_filename, 'w', newline='') as outfile:
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)

            writer.writeheader()
            for row in reader:
                row['first_name'] = self._hash_value(row['first_name'])
                row['last_name'] = self._hash_value(row['last_name'])
                row['address'] = self._hash_value(row['address'])
                writer.writerow(row)

if __name__ == "__main__":
    load_dotenv()  # Load environment variables from .env file

    generated_file_path = os.getenv('GENERATED_FILE_PATH', r'C:\Users\karan\Projects\demyst\problem2\data\sample.csv')
    anonymised_file_path = os.getenv('ANONYMISED_FILE_PATH', r'C:\Users\karan\Projects\demyst\problem2\data\anonymized_sample.csv')

    anonymizer = CSVAnonymizer(generated_file_path, anonymised_file_path)
    anonymizer.anonymize_csv()
