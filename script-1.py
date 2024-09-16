from itertools import product

# testar a função product
print("Vamos ver o que a função product faz (spoiler: é o produto cartesiano)")
conjunto = product((0,1,2), repeat=4)
numero_de_iteracoes = 0
for vetor in conjunto:
    numero_de_iteracoes += 1
    print(vetor)

print(f"No total há {numero_de_iteracoes} elementos, como esperado\n")

# 3 10 20
conjunto = product((0,1,2),repeat=10)
lista_com_os_00 = []
for vetor in conjunto:
    for indice in range(0,9):
        if vetor[indice] == 0 and vetor[indice+1] == 0:
            lista_com_os_00.append(vetor)
            break

print(f"o total de numeros na lista com 00 é {len(lista_com_os_00)}")
print(f"O set em python não tem elementos repetidos, transformando a lista em set, temos {len(set(lista_com_os_00))} elementos")
print("ou seja todos são únicos. Vamos ver eles\n")
print("------------------------------------------")


for vetor in lista_com_os_00:
    print(vetor)

