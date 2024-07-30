#!/bin/bash

# Run generate_csv.py inside docker
python /app/src/generate_csv.py

# Run anonymize_csv.py inside docker
python /app/src/anonymise_csv.py

# Run any additional scripts as needed after installing JAVA in the image
# python scaled_anonymize_csv.py
