with open("Day1Input",'r') as f:
    vals = [i.strip() for i in f.readlines()]
    #print(vals)

    for i in range(len(vals)):
        #print(vals[i])
        num1 = int(vals[i])
        for j in range(len(vals)-i-1):
            #print(vals[i+j+1])
            num2 = int(vals[i+j+1])
            for k in range(len(vals)-i-j-2):
                num3 = int(vals[i+j+k+2])
                #print(j+k+1)
                #print("num1 = val[",i,"]")
                #print("num2 = val[",i+j+1,"]")
                #print("num3 = val[",i+j+k+2,"]")
                if num1 + num2 + num3 == 2020:
                    print(num1*num2*num3)
                else:
                    continue


