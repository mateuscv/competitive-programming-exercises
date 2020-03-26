N = int(input())
meuDicionario = {}

'''
    {chave:valor}

    exemplo: dicionario de nomes

    {Mateus:2,
    Jorge:3,
    Ana:8}

'''

for i in range(N):
    number = int(input())
    if number not in meuDicionario:
        meuDicionario[number] = 1
    else:
        meuDicionario[number] += 1

listaDeChaves = list(meuDicionario)
listaDeChaves.sort()

for chave in listaDeChaves:
    print(str(chave) + " aparece " + str(meuDicionario[chave]) + " vez(es)")
