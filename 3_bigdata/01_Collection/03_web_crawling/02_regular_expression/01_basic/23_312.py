import re

p = re.compile('(ABC)+')
m = p.search('ABCABACABAC OK?')
print(m)

print(m.group(0))

p = re.compile(r'\w+\s+\d+[-]\d+[-]\d+')
m = p.search('park 101-1231-1231')
print(m)

p = re.compile(r'\w+\s+\d+[-]\d+[-]\d+')
m = p.search('park 1011-12111131-1231')
print(m)

p = re.compile(r'(\w+)\s+\d+[-]\d+[-]\d+')
m = p.search('park 101111-1231-1231')
print(m.group(1))
