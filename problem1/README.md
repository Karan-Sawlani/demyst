# HOW TO RUN?

## Problem 1

```shell
# cd (change directory) to problem1 folder and run below cmds
docker build -t fixed-width-parser .
docker run --rm -v C:\Users\karan\Projects\demyst\problem1\data:/app/data/ fixed-width-parser
```

```shell
# command to run unit test cases locally
pytest -v .\test_fixed_width_parser.py
```
