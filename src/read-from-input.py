import sys

l = []

for line in sys.stdin:
    #print(line.rstrip())
    l.append(line.rstrip())

print(l)
