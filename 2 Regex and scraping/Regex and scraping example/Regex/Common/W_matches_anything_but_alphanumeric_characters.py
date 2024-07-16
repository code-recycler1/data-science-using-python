import re

pattern = r"\W"
text = "a_b c!"
matches = re.findall(pattern, text)
print(matches)  # Output: [' ', '!']
