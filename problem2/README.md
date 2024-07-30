# HOW TO RUN?

## Problem 2

```shell
# cd (change directory) to problem2 folder and run below cmds
docker build -t generate-and-analyse-csv .
docker run --rm -v C:\Users\karan\Projects\demyst\problem2\data:/app/data/ generate-and-analyse-csv
```

```shell
# command to run unit test cases locally
pytest -v .\test_generate_csv.py
pytest -v .\test_anonymise_csv.py
```

***Note***:
- In order to run the scaled version of the code we can use distributed library like spark.
  We can run it locally or we can also have the Dockerfile for this solution as well
- The code is under the path: `problem2/src/scaled_anonymise_csv.py`. 
  Command to run the scaled versioned file: `spark-submit problem2/src/scaled_anonymise_csv.py`
