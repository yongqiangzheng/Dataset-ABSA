import re

a = 'genius bar staff)'
b = re.search(r'[^a-zA-z\s]', a)
print(b)
