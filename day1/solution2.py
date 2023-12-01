import re
zz = 0
cnt = 0
help_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}

curr_number = ""
with open('sample.txt' , 'r') as f:
    for line in f:
        line = line.rstrip('\n')
        reg = '(?=(f(ive|our)|s(even|ix)|[t](hree|wo)|(ni|o)ne|eight|\d))'
        a = re.split(reg, line)
        a = [i for i in a if i is not None]

        print(a)
        for i in a:
            if i.isnumeric():
                curr_number += i
                break
            else:
                if i in help_dict:
                    curr_number += help_dict.get(i)
                    break
        for j in reversed (a):
            print(j)
            if j.isnumeric():
                curr_number += j
                break
            else:
                if j in help_dict:
                    curr_number += help_dict.get(j)
                    break
        cnt += 1
        print("countline: ", cnt)
        print(curr_number)
        zz+= int(curr_number)
        curr_number = ""
        print(zz)
    #     for i in range(0, len(line), 1):
    #         if line[i].isnumeric():
    #             curr_number += line[i]
    #         else:

 
   