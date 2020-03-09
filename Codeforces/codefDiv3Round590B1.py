#inputs
n_k = [int(x) for x in input().split()]
ids = input().split()
n = n_k[0]
k = n_k[1]
tela = []
for i in range(n):
    if ids[i] not in tela:
        if len(tela) == k:
            del tela[k-1]
        tela.insert(0,ids[i])
print(len(tela))
print_string = ""
for id in tela:
    print_string = print_string + id + " "
print_string.rstrip()
print(print_string)