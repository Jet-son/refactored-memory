f = open("Day3Input",'r')

geography = [i.strip() for i in f.readlines()]

wrapval = len(geography[0])
xtrav = [1,3,5,7,1]
ytrav = [1,1,1,1,2]
xpos = 0

def checktree(line,xpos):
#    print("xpos in checktree is: ", xpos)
    if line[xpos] == '#':
#        print("return: 1")
        return 1
    else:
#        print("return: 0")
        return 0
totalslist = []
total = 0
for index in range(len(xtrav)):
    xpos = 0
    xval = xtrav[index]
    yval = ytrav[index]
    print("xval is: ",xval)
    print("yval is: ",yval)

    for geolinenum in range(len(geography)):
#        print("geolinenum is: ", geolinenum)
#        print("geolinenum * yval is: ", geolinenum*yval)
#        print("xpos is: ",xpos)
#        print(geography[(geolinenum*yval)])
        if geolinenum*yval > len(geography): break
        else:
            total += checktree(geography[(geolinenum*yval)],xpos)
            xpos += xval
            if xpos > wrapval - 1:
                xpos = xpos - wrapval
            else:
                continue
    print(total)
    totalslist.append(total)
    total = 0

val = 1
for i in totalslist:
    val *= i
print('total trees mult: ', val)
