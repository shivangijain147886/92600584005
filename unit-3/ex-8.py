import re

text = "My phone number is 9876543210"

# Search for a pattern
result = re.search(r"\d{10}", text)

if result:
    print("Phone number found:", result.group())
else:
    print("Phone number not found")

# Find all numbers
print("All numbers:", re.findall(r"\d+", text))

# Check whether text starts with a word
print("Starts with My:", bool(re.match(r"My", text)))
