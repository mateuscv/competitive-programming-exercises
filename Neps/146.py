X = int(input())
Y = int(input())

if X == 0 or Y == 0:
	print("eixos")
elif X > 0:
    if Y>0:
    	print("Q1")
    else:
        print("Q4")
else:
    if Y>0:
	    print("Q2")
    else:
        print("Q3")