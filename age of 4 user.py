sam = int( float(input(" Enter Value sam: ")) )
max = int( float(input(" Enter Value max: ")) )
robin = int( float(input(" Enter Value robin: ")) ) 
lilly = int( float(input(" Enter Value lilly: ")) )

if (sam < max) and (sam < robin) and (sam < lilly) :    # if sam is largest
    print(f' {sam} is youngest ')


elif (max < sam) and (max < robin) and (max < lilly):   # if max is largest
    print(f' {max} is youngest')


elif (robin < sam) and (robin < max) and (robin < lilly):   # if robin is largest
    print(f' {robin} is youngest')


elif (lilly < sam) and (lilly < max) and (lilly < robin):   # if lilly is largest
    print(f' {lilly} is youngest')


elif (sam==max) and (sam == robin) and (sam == robin):  # if sam = max = robin = lilly 
    print('All are of equal age')
    

                
                                          