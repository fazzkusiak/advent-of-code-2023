def check_left(i, index):
    return i[index + 1] != '.'

def check_right(i, index):
    return i[index + 1] != '.'

def check_upper(i, index_start, index_end):
    for j in range(index_start, index_end + 1, 1):
        pass

def check_down(a, b):
    pass

sum = []
line = -1
numb = ''
left = right = up = down = True
with open('sample.txt', 'r') as f:
    arr = ["\n".join(f)] 
    for i in arr:
        line += 1
        print('linia, ', line)
        for j in i:
            print('huj')
            print(j[0])
            if j.isnumeric():
                numb += j
                print(j)
            else:
                numb_length = len(numb)
                numb_id_start = i.index(numb)
                numb_id_end = i.index(numb) + len(numb) - 1
                if numb_id_start == 0:
                    right = check_right(i, numb_id_start)
                elif numb_id_start == len(j) - 1:
                    left = check_left(i, numb_id_start)
                
                if line == 0:
                    down = check_down(i, numb_id_start)

                elif line == 9:
                    up = check_upper(i, numb_id_start)
                else:
                    down = check_down(i,numb_id_start)
                    up = check_upper(i,numb_id_start)

        
                if left and right and up and down == True:
                    print(numb.strip())
                    sum.append(numb)
                    numb = ""

                
                   
        print(sum)

