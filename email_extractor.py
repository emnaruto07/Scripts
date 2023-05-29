import re
import sys

def extract_emails(filename):
    with open(filename, 'r') as f:
        data = f.read()
        email_pattern = r'[\w\.-]+@[\w\.-]+'
        emails = re.findall(email_pattern, data)
        return emails

if len(sys.argv) != 2:
    print("Usage: python3 email_extractor.py <filename>")
    sys.exit(1)

filename = sys.argv[1]
emails = extract_emails(filename)
for email in emails:
    print(email)
