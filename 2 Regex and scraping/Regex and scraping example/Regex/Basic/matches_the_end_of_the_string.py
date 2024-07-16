import re

pattern = r"b$"
text = "aaab"
matches = re.findall(pattern, text)
print(matches)  # Output: ['b']
