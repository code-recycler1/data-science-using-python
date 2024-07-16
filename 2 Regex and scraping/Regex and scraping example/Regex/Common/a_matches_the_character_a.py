import re

pattern = r"a"
text = "abc"
matches = re.findall(pattern, text)
print(matches)  # Output: ['a']
