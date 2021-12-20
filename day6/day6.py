with open("test.txt") as file:
    day = 0
    state = file.read().split(",")
    state = [int(x) for x in state]
    #state=[0]
    #result = 0
    #days = 256
    #for fish in state:
    #    exp = (days-fish-1) // 7
    #    
    #    result += (2**(exp+1)) // exp*2
    #print(result)
    #print("26984457539")
    state=[0]
    length = 14

    schedule = [0]*length
    nfish = len(state)
    for num in state:
        schedule[(num+1)%length] += 1
        schedule[(num+10)%length] += 1
    print(schedule)
    while day < 16:
        tomorrow = [0]*length
        for i in range(length):
            if day + i > 80:
                break
            nfish += schedule[i]
            if 10 + i < length:
                schedule[i+10] += schedule[i]
            else:
                tomorrow[(i+10) % length] += schedule[i]
            tomorrow[(i+18) % length] += schedule[i]
        print(schedule)
        print(tomorrow)
        for i in range(len(tomorrow)):
            schedule[i] += tomorrow[i]
            tomorrow[i] = 0
        
        day += length
    print(schedule)
    print(nfish)

    #while day < 55:
    #    nf = 0
    #    for i in range(len(state)):
    #        if state[i] == 0:
    #            state[i] = 6
    #            nf += 1
    #        else:
    #            state[i] -= 1
    #    day += 1
    #    for _ in range(nf):
    #        state.append(8)
    #    print("#"*len(state) + "." * (200-len(state)))

    #print(len(state))