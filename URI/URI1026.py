#encoding = UTF-8

while True:
    try:
        lista = input().split(" ")
    except EOFError:
        break
    val1 = int(lista[0]) 
    val2 = int(lista[1]) 
    Mofiz = int(val1 ^ val2) # ^ IS PYTHON'S XOR OPERATOR! (2x 1s => 0 ... SO IT'S A XOR!)
    print(Mofiz)

# LEGACY (WORKS BUT URI GIVES RUNTIME ERROR):

'''while True:
        # READING INPUT & CONVERTING TO 32-BIT BINARY

        line = input()

        line = line.split()
        a = format(int(line[0]), '032b')
        b = format(int(line[1]), '032b')

        # LIST ITERATION TO COMPARE EACH BIT

        a = list(a)
        b = list(b)
        a.reverse()
        b.reverse()
        result = list()

        for i, j in zip(a, b):
            if i == "0" and j == "0":
                result.insert(0, "0")
            elif (i == "0" and j == "1") or (i == "1" and j == "0"):
                result.insert(0, "1")
            elif (i == "1" and j == "1"):
                result.insert(0, "0")

        result = "".join(result)
        print(int(result, 2))'''
