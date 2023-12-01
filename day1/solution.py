
curr_number = ""
counter = 0
cnt = 0

index = 0
with open('sample.txt' , 'r') as f:
    for line in f:
        line = line.rstrip('\n')
        for i in range(0, len(line), 1):
            
            if line[i].isnumeric():
                
                curr_number += line[i]

                index = i
                break
        for j in range(len(line) - 1, index - 1, -1):
            
            print(line[j])
            if line[j].isnumeric():
                curr_number += line[j]
                
        
                cnt+=1
                break

        counter += int(curr_number)
        curr_number = ""
        
        print(cnt, "   " , counter)
