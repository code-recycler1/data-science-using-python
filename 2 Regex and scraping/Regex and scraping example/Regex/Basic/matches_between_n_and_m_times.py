import re

pattern = r"a{2,3}"
text = "aaaaabbb"
matches = re.findall(pattern, text)
print(matches)  # Output: ['aaa', 'aa']
