sum = 0
game_number = 0
isPossible = True
with open('sample.txt' , 'r') as f:
    games = [item.replace(",", "").replace("\n", "") for item in f]
  
    i = [i.split(';') for i in games]
    for j in i:
        game_number += 1
        isPossible= True
        print("numer gry: ", game_number)
        for k in j:
            k = k.split(' ')
            print(k)
            if "red" in k:
                if int(k[k.index("red") - 1]) > 12:
                    print("sranie")
                    isPossible = False
                    break
            if "blue" in k:
                if int(k[k.index("blue") - 1]) > 14:
                    print("niebieskie")
                    isPossible = False
                    break
            if "green" in k:
                if int(k[k.index("green") - 1]) > 13:
                    print("zielone")
                    isPossible = False
                    break
            print("dopuszcenie") 
        if isPossible:
            sum += game_number 

        print(sum)
            # print(j[1])
                
            #     if int(j.index("green") - 1) > 13:
            #         print(game_number, " can't be") 
            #         break
            # if "red" in j:
                
            #     if int(j.index("red") - 1) > 12:
            #         print(game_number, " can't be") 
            #         break
            # if "blue"  in j:
            #     if int(j.index("blue") - 1) > 14:
            #         print(game_number, " can't be") 
            #         break
            # sum += int(game_number)
        #     for k in j:
        #         k = k.split(' ')
        #         print(k)
        #         

    #print(sum)
                