lineList = input().split()
lineList[0], lineList[1], lineList[2] = float(lineList[0]), float(lineList[1]), float(lineList[2])
if (lineList[0] + lineList[1]) > lineList[2] and (lineList[0] + lineList[2]) > lineList [1] and (lineList[1] + lineList[2]) > lineList[0]:
    per = sum(lineList)
    print("Perimetro = " + "{0:.1f}".format(per))
else:
    are = (lineList[0] + lineList[1])/2 * lineList[2]
    print("Area = " + "{0:.1f}".format(are))