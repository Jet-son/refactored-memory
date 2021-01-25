def parsegroup(filelist):
    filelist.append('')
    groupedlist = []
    templist = []
    for i in filelist:
        if i != '':
            templist.append(i)
        else:
            groupedlist.append(templist)
            templist = []

    return groupedlist

def uniqueanswers(glist):
    uniquelist = []
    templist = []
    for g in glist:
        for p in g:
            for a in p:
                if a not in templist:
                    templist.append(a)
                else: continue
        uniquelist.append(templist)
        templist = []

    return uniquelist

def countanswers(ulist):
    countlist = []

    for a in ulist:
        countlist.append(len(a))

    return countlist


def  main():
    f = open('Day6Input','r')
    flist = [i.strip() for i in f.readlines()]
    
    groupans = parsegroup(flist)
    uniqueans = uniqueanswers(groupans)
    counts = countanswers(uniqueans)

    print(counts)
    print("Sum is: ", sum(counts))

#RUN MAIN
main()
