def coinToss(flips):
    import random
    tails = 0
    heads = 0
    for i in range(1, flips+1):
        flip = round(random.random())
        if flip == 0.0:
            tails += 1
            print"Attempt #",i, "Throwing a coin... It's tails! ... Got",tails, "tails so far and ",heads, "heads so far."
        elif flip == 1.0:
            heads += 1
            print"Attempt #",i, "Throwing a coin... It's heads! ... Got",tails, "tails so far and ",heads, "heads so far."

coinToss(5001)
