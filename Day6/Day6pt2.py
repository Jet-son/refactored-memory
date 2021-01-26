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
    valstring = 'abcdefghijklmnopqrstuvwxyz'
    vallist = ['a','b','c','d','e','f','g',
            'h','i','j','k','l','m','n','o',
            'p','q','r','s','t','u','v','w',
            'x','y','z']
    for group in glist:
        for person in group:
            for i in valstring:
                if  i not in person and i in vallist:
                    vallist.remove(i)
                else: continue
        uniquelist.append(vallist)
        vallist = ['a','b','c','d','e','f','g',
                'h','i','j','k','l','m','n','o',
                'p','q','r','s','t','u','v','w',
                'x','y','z']

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
    print("Sum is: ", sum(counts))
    
    f.close()

#RUN MAIN
main()
