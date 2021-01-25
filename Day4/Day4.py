f = open("Day4Input",'r')

filelist = [i.split() for i in f.readlines()]
filelist.append([])

def passportparser(filelist):
    testlist = [sublist for sublist in filelist]
    for i in testlist:
        if i == []:
            i.append('')
        else:
            continue
    flatlist = [item for sublist in testlist for item in sublist]

    tmplist = []
    parselist = []
    for i in flatlist:
        if i != '':
            tmplist.append(i)
        else:
            parselist.append(tmplist)
            tmplist = []

    return parselist

parsedlist = passportparser(filelist)

def createdicts(plist):
    returnlist = []
    tempdict = {}
    for i in plist:
        for j in i:
            a,b = j.split(':')
            tempdict.update({a:b})
        returnlist.append(tempdict)
        tempdict = {}
    return returnlist

def checkpass(dicts):
    checklist = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    keylist = [key for key in dicts]

    for item in checklist:
        if item in keylist:
            continue
        else:
            return 0
    return 1

p = passportparser(filelist)
d = createdicts(p)

total = 0

for pport in d:
    total += checkpass(pport)

print(total)
