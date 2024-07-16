import re
from extract_the_data import cards

for card in cards:
    job = re.search(r'-5">(.+)</h2>', str(card))
    company = re.search(r'y">(.+)</h3>', str(card))
    location = re.search(r'ion">\s(.+),\s(.+)', str(card))
    print(job.group(1), ' @ ', company.group(1))
    print(location.group(1).strip(), ',', location.group(2))
    print()
