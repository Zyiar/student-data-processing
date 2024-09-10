import pandas as pd
from functions import generate_email
from constraints import validate_name
import logging

# Set up logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def main():
    # Load the Excel file
    df = pd.read_excel('test_file.xlsx')
    email_set = set()

    emails = []
    for index, row in df.iterrows():
        student_name = row['Student Name']
        try:
            validate_name(student_name)
            email = generate_email(student_name, email_set)
            emails.append(email)
        except ValueError as e:
            logging.error(f"Validation error for {student_name}: {e}")
            emails.append("Invalid Name")

    # Save the results
    df['Email Address'] = emails
    df.to_csv('students.csv', index=False)
    df.to_csv('students.tsv', sep='\t', index=False)
    logging.info('Processing completed successfully.')

if __name__ == "__main__":
    main()
