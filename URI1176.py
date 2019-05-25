#encoding = UTF-8

test_cases = int(input())

cont = 0

while cont < test_cases:

    n = int(input())

    if n == 0:
        print("Fib(" + str(n) + ") = 0")
    else:
        Fib = []
        Fib.append(0)
        Fib.append(1)

        forRange = range(n+1)

        for i in forRange[2:]:
            Fib.append(Fib[i-1] + Fib[i-2])

        print("Fib(" + str(n) + ") = " + str(Fib[-1]))

    cont += 1