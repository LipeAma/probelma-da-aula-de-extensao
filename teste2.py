from itertools import product

vetor = [1,2,6,0] # esse vetor é para uma sequencia de dois numeross
def recorrencia(vetor):
    a,b,c,d = vetor
    resposta = [a+b+d,c,2*(b+c),2*(a+d)]
    return resposta

#vamos iterar aquele vetor que começa em n=2 até que n=10
for n in range(2,10):
    vetor = recorrencia(vetor)

a,b,c,d = vetor
print(f"resultado é {a+d}")


