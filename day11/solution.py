#...#...... 
#.......#..
# for exmaple here, we are looking for 5 difference, index of the first galaxy is 3, the others 7, so its 7 - 3 == 4, + the difference between x dimension + 1 == 5
arr = []
new_arr = []
sum = 0
count = 0
with open('sample.txt', 'r') as f:
    for i in f:
        if '#' not in i:
            arr.append(i.strip('\n'))
            arr.append(i.strip('\n'))
            count += 1
        else:
            arr.append(i.strip('\n'))

    print(arr)
 
    #other approach, just skim over all indexes and check if its #, if so, note the index of x and y into list, after all just loop over this list and make difference between these, like abs(x2-x1) + abs(y2-y1), if diff (x2 - x1) then add 1 to the sum

    for i in range(0, len(arr)):
        for j in range(0, len(arr) - count ):
            print(arr[i][j])
            if arr[i][j] == '#':
                new_arr.append([i,j])
    for x in range(0, len(new_arr)):
        print(new_arr[x][0])
   
    # print(new_arr)
    # for i in range(0, len(arr)):
    #     if '#' in arr[i]:
            
    #         galaxy_start_index = arr[i].index('#')
    #         for j in range(i + 1, len(arr)):
    #             print(arr[j])
    #             if arr[j].count('#') == 1:
                    
    #                 galaxy_end_index = arr[j].index('#')
    #                 count+=1
    #                 print(count)
    #                 print("znaleziono: ", galaxy_start_index, ' ,', galaxy_end_index, '  ', i, ' ', j)
    #                 if (j - i > 1):
    #                     sum += 1
    #                 sum += abs(galaxy_end_index - galaxy_start_index) + (j - i)
    #                 print(sum)
    #             elif arr[j].count('#') > 1:
    #                 # find all indexes of these and count them also
    #                 for k in (0, len(arr[j])):
    #                     if arr[j][k] == '#':

   