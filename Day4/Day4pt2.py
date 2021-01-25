#FUNCTIONS
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

def checkbyr(by):
    if int(by) >=1920 and int(by) <= 2002:
        return True
    else:
        return False

def checkiyr(iy):
    if int(iy) >= 2010 and int(iy) <=2020:
        return True
    else:
        return False

def checkeyr(ey):
    if int(ey) >= 2010 and int(ey) <= 2030:
        return True
    else:
        return False

def checkhgt(ht):
    if 'cm' in ht:
        if int(ht[:-2]) >= 150 and int(ht[:-2]) <= 193:
            return True
        else:
            return False
    elif 'in' in ht:
        if int(ht[:-2]) >= 59 and int(ht[:-2]) <= 76:
            return True
        else:
            return False
    else:
        return False

def checkhcl(hc):
    if hc[0] != '#':
        return False
    elif len(hc) != 7:
        return False
    else: pass 

    validchars = '0123456789abcdef'

    for c in hc[1:]:
        if c in validchars:
            continue
        else:
            return False
    return True

def checkecl(ec):
    validec = ['amb','blu','brn','gry','grn','hzl','oth']
    if ec in validec:
        return True
    else:
        return False

def checkpid(pi):
    validnum = '0123456789'
    
    if len(pi) != 9:
        return False
    else:
        pass

    for i in pi:
        if i not in validnum:
            return False
        else:
            continue
    return True

def checkpass(dicts):
    checklist = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    keylist = [key for key in dicts]

    for item in checklist:
        if item in keylist:
            continue
        else:
            return 0
    for key in keylist:
        if key == 'byr':
            if checkbyr(dicts[key]):pass
            else: return 0
        elif key == 'iyr':
            if checkiyr(dicts[key]):pass
            else: return 0
        elif key == 'eyr':
            if checkeyr(dicts[key]): pass
            else: return 0
        elif key == 'hgt':
            if checkhgt(dicts[key]): pass
            else: return 0
        elif key == 'hcl':
            if checkhcl(dicts[key]): pass
            else: return 0
        elif key == 'ecl':
            if checkecl(dicts[key]): pass
            else: return 0
        elif key == 'pid':
            if checkpid(dicts[key]): pass
            else: return 0
        elif key == 'cid': pass
        else: return 0

    return 1

def main():
    f = open("Day4Input",'r')

    filelist = [i.split() for i in f.readlines()]
    filelist.append([])
    
    parsedlist = passportparser(filelist)
    
    p = passportparser(filelist)
    d = createdicts(p)

    total = 0

    for pport in d:
        total += checkpass(pport)

    print(total)

    f.close()

#RUN
main()
