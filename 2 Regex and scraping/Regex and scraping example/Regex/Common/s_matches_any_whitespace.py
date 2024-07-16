import re

pattern = r"\s"
text = "a b c"
matches = re.findall(pattern, text)
print(matches)  # Output: [' ', ' ']
