summ = 0
with open('sample.txt', 'r') as f:
    winnings = []
    own = []
    final = []
    arr = [f.replace('\n', '') for f in f]
    
    arr = [x for x in arr if x != '']
    arr = [arr.split(' ') for arr in arr]

    for i in range(0, len(arr)):
        final.append(arr[i][2:])
    print(final[i])
    for i in range(0, len(final)):
        j = 0
        while final[i][j] != "|":
            winnings.append(final[i][j])
            j += 1
        j += 1
        while j < len(final[i]):
            own.append(final[i][j])
            j += 1
        print("wins:", winnings)
        print("owned:", own)
        winnings = [x for x in winnings if x != '']
        own = [x for x in own if x != '']

        cnt = sum(el in winnings for el in own)
        winnings = []
        own = []
        if cnt != 0:
            summ += 2 ** (cnt - 1)

        print(2 ** (cnt - 1))
    print(summ)
        #1 == 1 
        #2 == 2
        #3 == 4
        #4 == 8
        #5 == 16
        # sum 
        #while i != "|"