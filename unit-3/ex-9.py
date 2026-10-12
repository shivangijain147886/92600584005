import re

text = "Python is easy. Python is powerful."

# Using match()
print("Match:", re.match("Python", text).group())

# Using search()
print("Search:", re.search("easy", text).group())

# Using findall()
print("Find All:", re.findall("Python", text))
