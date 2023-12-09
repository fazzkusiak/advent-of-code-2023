# so, for the first we need to get our components into lists, 
"""
the first thing is the seeds
then, we have several maps, we are checking, if our one is in one of them, and in every, then we note the final plant, and choose min element from the final list
"""
import re
with open('sample.txt', 'r') as f:
    seeds = f.readline()[7:].rstrip()

    print(seeds)
    seeds = [int(s) for s in seeds.split(' ')]
    temp = []
    curr = []
    a = ""
    res = []
    for line in f:
        if bool(re.match(r"[\d \d \d]", line)):
            line = line.rstrip()
            line = [int(s) for s in line.split(' ')]
            temp.append(line)
            
        elif bool(re.match(r"[^\d]", line)):
            curr.append(temp)
            
            temp = []
    curr = [x for x in curr if x != []]

    for seed in seeds:
        place = seed
        for i in curr:
            print('aha')
            for j in i:
                print(j)
                # 50 98 2
                # 52 50 48
                # 50 98 2 case
                # 79 > 50 ? and 79 <= 51 false so > 79 >= 98 not
                # range there is between 50 - 51 and 98 - 99, 79 isnt so its goin to nthe next, however 
                # so should be, first checks 50 - 51and other 98 -99, then 52-99 and 50-97
                if j[1] > j[0]:
                    if ((place >= j[0]) and place <= j[0] + j[2] - 1) or (place >= (j[1] and place <= j[1] + j[2] - 1)):
                        
                        place = seed + j[2]
                        print(place)
                        
                        res.append(place)   

                        break
                else:
                    #j[1] < j[0]
                    #52 50
                    # 79 < 52 f or 79 <= 50 f
                    if ((place <= j[0]) and place >= j[0] + j[2] - 1) or (place <= (j[1] and place >= j[1] + j[2] - 1)):
                        place = seed + j[2]
                        print(place)
                        
                        res.append(place)   

                        break
            place = seed
                  
        res.append(place) 
    print(res)
                #print(j)