import re

pattern = r"\w"
text = "a_b c!"
matches = re.findall(pattern, text)
print(matches)  # Output: ['a', '_', 'b', 'c']
