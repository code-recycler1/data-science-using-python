import re

pattern = r"[abc]"
text = "dabcde"
matches = re.findall(pattern, text)
print(matches)  # Output: ['a', 'b', 'c']
