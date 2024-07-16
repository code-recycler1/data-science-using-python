import re

pattern = r"\d"
text = "a1b2c3"
matches = re.findall(pattern, text)
print(matches)  # Output: ['1', '2', '3']
