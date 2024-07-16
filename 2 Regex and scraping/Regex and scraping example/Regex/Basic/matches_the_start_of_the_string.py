import re

pattern = r"^a"
text = "aaabbb"
matches = re.findall(pattern, text)
print(matches)  # Output: ['a']
