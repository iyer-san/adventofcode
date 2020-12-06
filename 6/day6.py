import re

def getgrouplength(group):
    simgroup = group.replace('\n', "")
    groupset = set(simgroup)
    return len(groupset)

def getcommonlength(group):
    splitgroup = re.split('\n', group)
    commonset = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
    for passanger in splitgroup:
        passanger = set(passanger)
        commonset = commonset.intersection(passanger)
    return len(commonset)


filename = "adventofcode/6/input.txt"
customsblocks = []
with open(filename) as f:
    content = f.read()
    customsblocks = re.split('\n\n', content)

allgroupslength = 0
commongrouplength = 0

for group in customsblocks:
    allgroupslength += getgrouplength(group)
    commongrouplength += getcommonlength(group)

print(allgroupslength)
print(commongrouplength)
