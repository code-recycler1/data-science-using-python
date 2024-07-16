import re

s = "I went to the zoo and saw _lions_, _tigers_ and _meerkats_."

found = re.search(r"lion", s)
print(found)  # This will print the match object

# To access the matched text, we use the group() method
if found:
    print(found.group(), found.start(), found.end())
else:
    print("Nothing here...")
