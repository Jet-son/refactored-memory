f = open("Day3Input",'r')

geography = [i.strip() for i in f.readlines()]

wrapval = len(geography[0])
xtrav = 3
ytrav = 1
xpos = 0

def checktree(line,xpos):

    if line[xpos] == '#':
        return 1
    else: return 0

total = 0

for line in geography:
    total += checktree(line,xpos)
    xpos += xtrav
    if xpos > wrapval - 1:
        xpos = xpos - wrapval
    else:
        continue

print(total)
