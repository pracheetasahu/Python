import re

text = "Contact us at support@gmail.com or admin@yahoo.com"

emails = re.findall(r'[\w.-]+@[\w.-]+\.\w+', text)

print("Original Text:", text)
print("Email Addresses Found:")

for email in emails:
    print(email)

phone = "9876543210"

if re.fullmatch(r'\d{10}', phone):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")
