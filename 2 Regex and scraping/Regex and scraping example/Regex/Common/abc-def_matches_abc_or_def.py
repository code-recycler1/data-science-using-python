import re

pattern = r"abc|def"
text = "abcdef"
matches = re.findall(pattern, text)
print(matches)  # Output: ['abc', 'def']
