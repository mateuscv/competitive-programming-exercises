t = int(input())
t = 2*t
for testcase in range(t):
    try:
        number_of_elements_in_a = int(input())
        a = [int(x) for x in input().split()]
        # into a testcase:
        imparcount = False
        parcount = False
        for element in a:
            if element%2 != 0:
                #impar
                imparcount = True
            else:
                parcount = True
        if (imparcount is True and (number_of_elements_in_a%2 != 0 or parcount is True)):
            print("YES")
        else:
            print("NO")
    except EOFError:
        break