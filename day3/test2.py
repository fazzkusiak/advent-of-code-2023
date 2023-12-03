import re
summ = []
num = ""
with open('sample.txt', 'r') as f:
    arr = [f.replace("\n", '') for f in f]

    arr = ['.' + a for a in arr]
    arr = [a + '.' for a in arr]
    arr.insert(0, '.'*14)
    arr.insert(13, '.'*14)
    print(arr)
    for i in range(0, len(arr)):
        print(arr[i])
        for j in arr[i]:
        
            if j.isnumeric():
                num += j
                print(num)
            else:
                if num != "":
                    
                    ind_num = arr[i].index(num)
                    
                    if j != "." or arr[i][ind_num + len(num)] != ".":
                        summ.append(num)
                        num = ""
                    else:
                        for x in range(ind_num - 1, ind_num + len(num) + 1, 1):
                            if not bool(re.search('/d|.', arr[i - 1][x] ) )or( not (bool(re.search('/d|.', arr[i + 1][x] )))):
                                print(arr[i - 1][x])
                                print(num)
                                summ.append(num)
                                num = ""
                                break
                    num = ""
        #            else:
                
        print(sum(map(int, summ)))            

    #dots = ['.' + suit for suit in arr]
    
   # print(dots)
    
#    arr.insert(arr[0][0], '.')
