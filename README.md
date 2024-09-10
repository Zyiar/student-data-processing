# Student Email Generator

## Description
This project generates unique email addresses for students based on their names. The emails are formatted as `firstinitiallastname@gmail.com`. The program ensures that email addresses are unique and do not contain special characters.

## Files
- `functions.py`: Contains functions for generating and validating email addresses.
- `constraints.py`: Contains constraints and validation functions.
- `main.py`: Main program file for executing the email generation process.
- `students.xlsx`: Input file containing student names.
- `students.csv`: Output file with generated email addresses in CSV format.
- `students.tsv`: Output file with generated email addresses in TSV format.
- `app.log`: Log file for recording computation details and warnings.

## How to Run
1. Ensure you have the required packages installed (`pandas`, `openpyxl`).
2. Place the `students.xlsx` file in the same directory.
3. Run the `main.py` script.

## Logging
All computational details and warnings are saved in `app.log`.
