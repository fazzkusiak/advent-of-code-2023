#...#...... 
#.......#..
# for exmaple here, we are looking for 5 difference, index of the first galaxy is 3, the others 7, so its 7 - 3 == 4, + the difference between x dimension + 1 == 5
arr = []
sum = 0
count = 0
with open('sample.txt', 'r') as f:
    for i in f:
        if '#' not in i:
            arr.append(i.strip('\n'))
            arr.append(i.strip('\n'))
        else:
            arr.append(i.strip('\n'))

    for i in arr:
        print(i)

    for i in range(0, len(arr)):
        if '#' in arr[i]:
            
            galaxy_start_index = arr[i].index('#')
            for j in range(i + 1, len(arr)):
                if '#' in arr[j]:
                    
                    galaxy_end_index = arr[j].index('#')
                    count+=1
                    print(count)
                    print("znaleziono: ", galaxy_start_index, ' ,', galaxy_end_index, '  ', i, ' ', j)
                    if (i - j > 1):
                        sum += 1
                    sum += abs(galaxy_end_index - galaxy_start_index) + (j - i)
                    print(sum)
   