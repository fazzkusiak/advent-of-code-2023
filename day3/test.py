numb = ""

with open('sample.txt', 'r') as f:
    data = f.read().replace('\n', '')
    for i in range(0, 10, 1): # first line
        if data[i].isnumeric():
            numb += data[i]
        else:
            if numb != "":
                len_numb = len(numb)
                # looks, if the number is on first index possible, 
                if data.index(numb) == 0:
                    if data[len_numb] != ".":
                        sum += int(numb)
                        break
                    else:
                        for j in range(10, 10 + len_numb + 1, 1):
                            if j != ".":
                                sum += int(numb)
                                break
                            
    

                        # cases:
# [0][0], [end][end], [end][0], [0][end], 
                        # sample case, no borders
                        # should be : 
                    
