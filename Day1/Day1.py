with open("Day1Input",'r') as f:
    vals = [i.strip() for i in f.readlines()]
    #print(vals)

    for i in range(len(vals)):
        #print(vals[i])
        num1 = int(vals[i])
        for j in range(len(vals)-i-1):
            #print(vals[i+j+1])
            num2 = int(vals[i+j+1])
            if num1 + num2 == 2020:
                print(num1*num2)
            else:
                continue


