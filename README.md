Running the code:

- run commands
1. source venv/bin/activate
2. python3 main.py

-----------------------------------------------------------------------------------------------------------
Running Unit Tests:

To run the automated test cases for this project, follow these steps:

1. Ensure you have Python installed
   This project requires Python 3.6 or later.

2. (Optional) Create and activate a virtual environment
   It is recommended to use a virtual environment to manage dependencies:

   python3 -m venv venv
   source venv/bin/activate

3. Run all tests
   From the project root directory, execute:

   python -m unittest discover -s tests

   This command will discover and run all tests in the 'tests' directory.

4. Run a single test file
   To run a specific test file, use:

   python3 -m unittest tests/test_input_parser.py

   Replace 'tests/test_input_parser.py' with the module path of the test you want to run.

5. Check test results
   - OK means all tests passed.
   - FAIL or ERROR means one or more tests failed or had errors—review the output for details.
