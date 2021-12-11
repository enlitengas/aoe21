with open("input.txt") as file:
    lines = file.readlines()
    lines = [x.replace("\n", "") for x in lines]
    lines2 = lines.copy()
    filt = ""
    filt2 = ""
    for i in range(len(lines[0])):
        oc = len([x for x in lines if x[i] == '1'])
        oc2 = len([x for x in lines2 if x[i] == '1'])
        if len(lines) > 1:
            if len(lines)/2 > oc:
                filt += "0"
            elif len(lines)/2 <= oc:
                filt += "1"
            lines = [x for x in lines if x[i] == filt[i]]
        if len(lines2) > 1:
            if len(lines2)/2 <= oc2:
                filt2 += "1"
            elif len(lines2)/2 > oc2:
                filt2 += "0"
            lines2 = [x for x in lines2 if x[i] != filt2[i]]
    num = 0
    num2 = 0
    for i in range(len(lines[0])):
        num += (2**(len(lines[0])-1-i))*int(lines[0][i])
        num2 += (2**(len(lines2[0])-1-i))*int(lines2[0][i])
    print(num*num2)
