arr = []
with open('sample.txt', 'r') as f:
    for a in f:
        arr.append(a.rstrip())
    new_arr = [0] * len(arr) 
    for i in range(0, len(arr)):
        new_arr[i] = [0] * len(arr)
    
    #for first u have to find S

    for i in range(0, len(arr)):
        for j in (0, i):
            if 'S' in arr[i]:
                #coords of starting point (S)
                start_x = i
                start_y = arr[i].index('S')
                
                print(start_x)
                print(start_y)

    new_arr[start_x][start_y] = 'S'
    print(new_arr)

    #check upper records, then same line, then below
    for i in range(start_x, -1, -1):
        for j in range(start_y, -1, -1):
            if arr[i][j] == '.':
                new_arr[i][j] = '.'
            elif arr[i] 
