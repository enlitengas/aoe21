from collections import defaultdict

def calc_score(board, check, num):
    result = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if check[i][j] == False:
                result += board[i][j]
    return result * num
with open("test.txt") as file:
    lines = file.readlines()
    drawn = lines[0].split(",")
    drawn = [int(x) for x in drawn]
    

    d = defaultdict(bool)
    boards = []
    checks = []
    start_new = True
    current = -1
    for line in lines[1:]:
        if line == "\n":
            start_new = True
            continue
        elif start_new:
            current += 1
            boards.append([])
            checks.append([])
            start_new = False
        nline = line.split()
        nline = [int(x) for x in nline]
        boards[current].append(nline)
        checks[current].append([False] * len(nline))
    found = False
    winner = -1
    for num in drawn:
       for (n, board) in enumerate(boards):
           for (i,row) in enumerate(board):
               for (j,cell) in enumerate(row):
                   if cell == num:
                        if d[n] == True:
                            continue
                        checks[n][i][j] = True  
                        if all(checks[n][i]):
                            winner = calc_score(board, checks[n], num)
                            print(winner)
                            d[n] = True
                            #exit(0)
                        if all([x[j] for x in checks[n]]):
                            winner = calc_score(board, checks[n], num)
                            print(winner)
                            d[n] = True
                            #print("Winner col")
                            #print("Number drawn: " +str(num))
                            #for line in board:
                            #    print(line)
                            #calc_score(board, checks[n], num)
                            #exit(0)
    print("WINNER!")
    print(winner)
    exit(0)
    for board in boards:
        for line in board:
            print(line)
        print()

