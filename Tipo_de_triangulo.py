#Crie um programa que mostre tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes'''

from time import sleep
a = float(input('Digite um segmento: '))
b = float(input('Digite um perímetro: '))
c = float(input('Digite um perímetro: '))
if a < (b + c) and b < (a + c) and c < (a + b):
    print('Os segmentos informados formam um triângulo.')
    print('O triângulo é: ') # aqui poderia acrescentar o ,end='' para unir com o próximo print.
    sleep(1) #Para dar a impressão de que e máquina esta processando as informações.
    if a == b and a == c:
        print('Equilátero')
    elif a == b or a == c or c == b:
        print('Isóceles')
    else:
        print('Escaleno')
else:
    print('Os segmentos informados não são capazes de formar um triângulo.')

#A parte usada para avaliar o tipo de triangulo precisou ir dentro do primeiro if, pois, o código só deverá retornar o
#tipo de triângulo caso os segmentos informados sejam capazes de forma-lo, caso contrário, teriamos uma resposta mesmo
#que os segmentos não formassem um triângulo.

