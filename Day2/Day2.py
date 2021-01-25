f = open("Day2Input",'r')

passwords = [i for i in f.readlines()]

def parser(item):
    plist = item.split()
    finallist = []
    tmp = plist[0].replace('-',' ')
    tmp = tmp.split()
    finallist.append(tmp[0])
    finallist.append(tmp[1])
    tmp2 = plist[1].replace(':','')
    finallist.append(tmp2)
    finallist.append(plist[2])
    #item[1] = item[1][0]
    return finallist
def lettercheck(parselist):
    lower = int(parselist[0])
    upper = int(parselist[1])
    letter = parselist[2]
    passwd = parselist[3]

    if passwd.count(letter) >= lower and passwd.count(letter) <= upper:
        return 1
    else:
        return 0

total = 0

for i in passwords:
    total += lettercheck(parser(i))
#print(parser(passwords[0]))
#print(lettercheck(parser(passwords[0])))

print(total)
