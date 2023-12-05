# so, for the first we need to get our components into lists, 
"""
the first thing is the seeds
then, we have several maps, we are checking, if our one is in one of them, and in every, then we note the final plant, and choose min element from the final list
"""
import re
with open('sample.txt', 'r') as f:
    seeds = f.readline()[7:].split(' ')
    curr = []
    a = ""
    for seed in seeds:
        for line in f:
            if bool(re.match(r"[\d \d \d]", line)):
                curr.append(line.rstrip('\n'))
            elif bool(re.match(r"[^\d]", line)):
                print(curr[0])
                break