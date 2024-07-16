import re

pattern = r"a{3}"
text = "aaabbb"
matches = re.findall(pattern, text)
print(matches)  # Output: ['aaa']
