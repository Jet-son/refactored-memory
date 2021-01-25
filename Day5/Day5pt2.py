# DEFINE FUNCTIONS
def checkrow(rowsegment):
    upper = 127
    lower = 0
    for i in rowsegment:
        if i == 'F':
            upper = int((upper-lower)/2)+lower
            lower = lower
        elif i == 'B':
            lower = int((upper - lower)/2) + lower+1
            upper = upper
        else:
            print('not valid')
        #print(i, lower, upper)
    if lower == upper:
        #print('Row: ', lower)
        return lower
    else:
        print('no consensus reached on row')

def checkcol(colseg):
    upper = 7
    lower = 0
    for i in colseg:
        if i == 'L':
            upper = int((upper-lower)/2)+lower
            lower = lower
        elif i == 'R':
            lower = int((upper-lower)/2)+lower+1
            upper = upper
        else:
            print('not valid')
        #print(i, lower, upper)
    if lower == upper:
        #print('Col: ', lower)
        return lower
    else:
        print('no consensus reached on col')

def seatid(row,col):
    return (row*8)+col

def main():
    f = open('Day5Input')
    tickets = [i.strip() for i in f.readlines()]
    seatlist = []

    for t in tickets:
       row =  checkrow(t[:7])
       col =  checkcol(t[7:])
       seatlist.append(seatid(row,col))
    
    seatlist.sort()
    
    for i in range(len(seatlist)-1):
        if seatlist[i+1] != seatlist[i]+1:
            print('Your seat id: ', seatlist[i]+1)

# RUN MAIN
main()
        
