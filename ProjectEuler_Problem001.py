def multipleOf3and5(limit):   
    counter = 1
    theSum = 0
    while(True):
        threePro = 3 * counter
        fivePro = 5 * counter
        counter +=1
        if(threePro < limit):
            theSum +=threePro
            print(threePro)
        if(fivePro <limit):
            theSum +=fivePro
            print(fivePro)
        if(threePro >=limit and fivePro >=limit):
            print(theSum)
            break
multipleOf3and5(1000)
