from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.types import StringType
import hashlib
import os


class SparkCSVAnonymizer:
    """
    A class to anonymize specified columns in a CSV file using PySpark.
    """

    def __init__(self, input_filename: str, output_filename: str):
        """
        Initializes the SparkCSVAnonymizer with input and output filenames.

        :param input_filename: The name of the input CSV file.
        :param output_filename: The name of the output CSV file.
        """
        self.input_filename = input_filename
        self.output_filename = output_filename

    @staticmethod
    def _hash_value(value: str) -> str:
        """
        Hashes a single value using MD5. Handles None values by returning an empty string.

        :param value: The value to hash.
        :return: The hashed value.
        """
        if value is None:
            return ''
        return hashlib.md5(value.encode()).hexdigest()

    def _anonymize_column(self):
        """
        Creates a UDF (User Defined Function) to anonymize a column using MD5 hashing.
        """
        return udf(lambda value: self._hash_value(value), StringType())

    def anonymize_csv(self):
        """
        Anonymizes specified columns in the CSV file using PySpark.
        """
        spark = SparkSession.builder.appName("CSV Anonymizer").getOrCreate()

        # Load the CSV file
        df = spark.read.option("header", True).option("delimiter", ",").format("csv").load(self.input_filename)

        df.show(200, truncate=False)

        # Anonymize the columns
        hash_udf = self._anonymize_column()
        df = df.withColumn('first_name', hash_udf(col('first_name')))
        df = df.withColumn('last_name', hash_udf(col('last_name')))
        df = df.withColumn('address', hash_udf(col('address')))

        df.show(10, truncate=False)

        # Save the anonymized CSV file
        df.write.mode("overwrite").csv(self.output_filename, header=True)

        spark.stop()

if __name__ == "__main__":

    generated_file_path = os.getenv('GENERATED_FILE_PATH',
                                    r'C:\Users\karan\Projects\demyst\problem2\data\sample.csv')
    scaled_anonymised_file_path = os.getenv('SCALED_ANONYMISED_FILE_PATH',
                                     r'C:\Users\karan\Projects\demyst\problem2\data\scaled_anonymized_sample.csv')

    anonymizer = SparkCSVAnonymizer(generated_file_path, scaled_anonymised_file_path)
    anonymizer.anonymize_csv()
