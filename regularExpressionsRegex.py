# Topic of the Day: Regular Expressions (Regex)
# Explanation: Regex is a special language for searching text strings. It allows you to find patterns like "any email address" or "any phone number" without writing 50 lines of if/else checks.
# Module: import re
# Common Patterns:
# \d: Any digit (0-9).
# \w: Any word character (a-z, 0-9).
# +: One or more times.


import re

text = "Contact me at test@email.com or call 555-0199."

# 1. Extracting an Email
# Pattern: [chars]@[chars].[chars]
# r"..." stands for 'raw string' (best practice for regex)
email_pattern = r"[\w\.-]+@[\w\.-]+"
email = re.search(email_pattern, text)

if email:
    print(f"Found Email: {email.group()}")

# 2. Extracting Phone Numbers
# Pattern: 3 digits, hyphen, 4 digits
phone_pattern = r"\d{3}-\d{4}"
phones = re.findall(phone_pattern, text)

print(f"Found Phones: {phones}")