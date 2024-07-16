import re

s = "I went to the zoo and saw _lions_, _tigers_ and _meerkats_."

new_s = re.sub(r"_", r"", s)
print(new_s)

# Replace specific patterns
new_s = re.sub(r"t[a-zA-Z]+", r"X", s)
print(new_s)  # Replaces entire match, not just 't'

# Use groups
new_s = re.sub(r"t([a-zA-Z]+)", r"X\1", s)
print(new_s)
