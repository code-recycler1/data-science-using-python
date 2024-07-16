import re

s = "I went to the zoo and saw _lions_, _tigers_ and _meerkats_."

found = re.search(r"_.*_", s)
print(found.group())  # This might not give the expected result

found = re.search(r"_[a-zA-Z]*_", s)
print(found.group())

found = re.search(r"_[^_]*_", s)
print(found.group())
