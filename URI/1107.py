while True:
    dimensions = [int(x) for x in input().split()]
    A = dimensions[0]
    C = dimensions[1]
    if dimensions == [0,0]:
        break
    finalheights = [int(x) for x in input().split()]
    
    summer = 0
    for i in range(C):
        if i !=0:
            if finalheights[i] < finalheights[i-1]:
                summer += (finalheights[i-1] - finalheights[i])
        else:
            summer += A - finalheights[i]
    
    print(summer)