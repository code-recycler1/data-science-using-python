import re

text = "abc123def456ghi789"

# Match any digit
pattern = r"\d+"
matches = re.findall(pattern, text)
print("Digits:", matches)  # Output: ['123', '456', '789']

# Match any word character (alphanumeric + underscore)
pattern = r"\w+"
matches = re.findall(pattern, text)
print("Word characters:", matches)  # Output: ['abc123def456ghi789']

# Match any non-word character
pattern = r"\W+"
matches = re.findall(pattern, text)
print("Non-word characters:", matches)  # Output: []

# Match sequences of letters
pattern = r"[a-zA-Z]+"
matches = re.findall(pattern, text)
print("Letters:", matches)  # Output: ['abc', 'def', 'ghi']
