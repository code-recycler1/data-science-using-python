import re

pattern = r"abc"
text = "abc"
matches = re.findall(pattern, text)
print(matches)  # Output: ['abc']
