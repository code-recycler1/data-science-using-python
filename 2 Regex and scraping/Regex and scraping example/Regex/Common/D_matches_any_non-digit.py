import re

pattern = r"\D"
text = "a1b2c3"
matches = re.findall(pattern, text)
print(matches)  # Output: ['a', 'b', 'c']
