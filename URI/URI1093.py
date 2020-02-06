#encoding=UTF-8

def splitInput(x):
    x = x.split()
    return x[0], x[1], x[2], x[3]

def floatenize(tupleArg):
    x, y, z, w = tupleArg
    x = float(x)
    y = float(y)
    z = float(z)
    w = float(w)
    return x,y,z,w
    
while True:
    inputLine = input()

    if inputLine == "0 0 0 0":
        break

    EV1, EV2, AT, D = floatenize(splitInput(inputLine))
    
    # CONDIÇÕES DE MORTE DE CADA VAMPIRO:

    tmp = EV1
    EV1 = 0
    while (tmp > 0):
      tmp -= D
      EV1+=1

    tmp = EV2
    EV2 = 0
    while (tmp > 0):
      tmp -= D
      EV2 += 1
    
    # TEORIA GAMBLER'S RUIN:
    
    if (AT == 3):
        # FAIR COIN FLIP!
        prob = (EV1 / (EV1 + EV2))
    else:
        # UNFAIR COIN FLIP!
        prob = (1-((1-(AT/6))/(AT/6))**EV1) / (1 - ((1-(AT/6))/(AT/6))**(EV1+EV2))

    prob *= 100
    print("{:.1f}".format(prob))