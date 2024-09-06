import pandas as pd
import re

df = pd.read_excel('test_file.xlsx')


def generate_email(full_name, existing_emails):
    name_parts = full_name.split()

    if len(name_parts) == 1:
        # If there's only one part, use it as the first name
        f_name_clean = re.sub(r"[^a-zA-Z]", "", name_parts[0]).lower()
        l_name_clean = ""
    else:
        # Use the first part as the first name and the last part as the last name
        f_name_clean = re.sub(r"[^a-zA-Z]", "", name_parts[0]).lower()
        l_name_clean = re.sub(r"[^a-zA-Z]", "", name_parts[-1]).lower()

    email_base = f"{f_name_clean[0]}{l_name_clean}"

    email = f"{email_base}@gmail.com"
    count = 1
    while email in existing_emails:
        email = f"{email_base}{count}@gmail.com"
        count += 1

    existing_emails.add(email)

    return email


existing_emails = set()

df['Email Address'] = df['Student Name'].apply(lambda name: generate_email(name, existing_emails))

df.to_excel('students_with_emails.xlsx', index=False)

print("Emails generated and added to 'Email Address' column successfully.")
