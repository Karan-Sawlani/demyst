import csv
import os
import random
from faker import Faker
from dotenv import load_dotenv


class CSVGenerator:
    """
    A class to generate a CSV file with specified columns and random data.
    """

    def __init__(self, filename: str, num_records: int):
        """
        Initializes the CSVGenerator with a filename and number of records.

        :param filename: The name of the CSV file to be generated
        :param num_records: The number of records to generate
        """
        self.filename = filename
        self.num_records = num_records
        self.fake = Faker()

    def generate_csv(self):
        """
        Generates a CSV file with random data.
        """
        with open(self.filename, 'w') as csvfile:
            fieldnames = ['first_name', 'last_name', 'address', 'date_of_birth']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for _ in range(self.num_records):
                writer.writerow({
                    'first_name': self.fake.first_name(),
                    'last_name': self.fake.last_name(),
                    'address': self.fake.address().replace(",", ";").replace('\n', ' '),
                    'date_of_birth': self.fake.date_of_birth().isoformat()
                })


if __name__ == "__main__":
    load_dotenv()  # Load environment variables from .env file
    generated_file_path = os.getenv('GENERATED_FILE_PATH', r'C:\Users\karan\Projects\demyst\problem2\data\sample.csv')
    generator = CSVGenerator(generated_file_path, 10000)  # Generate 1,000,000 records
    generator.generate_csv()
