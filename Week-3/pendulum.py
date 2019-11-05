def period():
    import math
    L = input()
    g = input()

    while (int(L)*int(g)) < 0:
        print('ValueError')
        L = input()
        g = input()

        
        
    
    
    else:
        T = (2 * math.pi) * (math.sqrt(int(L) * (1/int(g))))
        print(T)

period()



# while isinstance(L, str) == True and isinstance(g, str) == True:
       
      # print('please enter valid integers')
      # L = input()
      # g = input()
