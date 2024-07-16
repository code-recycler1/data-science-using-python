import re

pattern = r"[^abc]"
text = "dabcde"
matches = re.findall(pattern, text)
print(matches)  # Output: ['d', 'd', 'e']
