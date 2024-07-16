import re

s = "I went to the zoo and saw _lions_, _tigers_ and _meerkats_."

found = re.search(r"flamingo", s)
print(found)
print("We found it!") if found else print("Nothing here...")

found = re.match(r"tiger", s)
print(found)

found = re.match(r"I\s", s)
print(found)
