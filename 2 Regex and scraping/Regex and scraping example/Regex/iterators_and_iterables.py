import re

s = "I went to the zoo and saw _lions_, _tigers_ and _meerkats_."

found = re.finditer(r"_[a-zA-Z]*_", s)
for f in found:
    print(f.group())

# Using findall
found = re.findall(r"_[a-zA-Z]*_", s)
[print(f) for f in found]

# To remove unwanted characters from the matches, use groups
found = re.findall(r"_([a-zA-Z]*)_", s)
[print(f) for f in found]
