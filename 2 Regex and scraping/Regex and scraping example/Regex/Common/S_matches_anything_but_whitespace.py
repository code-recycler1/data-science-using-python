import re

pattern = r"\S"
text = "a b c"
matches = re.findall(pattern, text)
print(matches)  # Output: ['a', 'b', 'c']
