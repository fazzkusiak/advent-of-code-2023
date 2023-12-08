import math
with open('sample.txt', 'r') as f:
    multi = 1
    cnt = 0
    time = [int(word) for word in f.readline().split() if word.isdigit()]
    distance = [int(word) for word in f.readline().split() if word.isdigit()]
    minimal = []
    temp = []
    for i in range(0, len(time)):
        for j in range(1, time[i]):
            if j * (time[i] - j) > distance[i]:
                cnt += 1
        multi *= cnt
        cnt = 0
    
    print(multi)