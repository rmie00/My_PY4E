import re

fhand = open('mbox.txt')

for lines in fhand:
    if lines.startswith('From: '):
        continue
    line = lines.strip().split()
    domain = re.findall('@([^ ]*)', line)
    print(domain)