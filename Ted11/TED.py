from random import randint

matriz_a = []
for i in range(10):

    matriz_aux = []

    for j in range(10):
        matriz_aux.append(randint(0, 100))

    matriz_a.append(matriz_aux)

for linha in matriz_a:
    print(linha)

print('\n \n')


resultado_soma = 0
for l in matriz_a:
    for c in l:
        resultado_soma += c

print(f'Resultado da Soma = {resultado_soma}')


matriz_b = []
for l in range(0, len(matriz_a)):
    lista_auxiliar = []

    for c in range(0, len(matriz_a[l])):
        resultado_multiplicacao = matriz_a[l][c] * 3
        lista_auxiliar.append(resultado_multiplicacao)

    matriz_b.append(lista_auxiliar)
print(matriz_b)