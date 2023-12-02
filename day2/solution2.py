sum = 0

with open('sample.txt' , 'r') as f:
    games = [item.replace(",", "").replace("\n", "") for item in f]
    
    i = [i.split(';') for i in games]
    for j in i:
        max_blue = max_red = max_green = 0
      
        for k in j:
            k = k.split(' ')
            print(k)
            if "red" in k:
                if int(k[k.index("red") - 1]) > max_red:
                    print("sranie")
                    max_red = int(k[k.index("red") - 1])
            if "blue" in k:
               if int(k[k.index("blue") - 1]) > max_blue:
                    print("sranie")
                    max_blue = int(k[k.index("blue") - 1])
            if "green" in k:
                if int(k[k.index("green") - 1]) > max_green:
                    print("sranie")
                    max_green = int(k[k.index("green") - 1])
        
        sum += max_red * max_blue * max_green

        print(sum)
         