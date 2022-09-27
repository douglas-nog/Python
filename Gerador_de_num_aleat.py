#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.


#A biblioteca numPy gera um array com número aleatórios, basta definir o intevalo e quantos valores.
from time import sleep
import numpy
from random import randint
print('Gerando número aleatórios...')
sleep(2)

#Na resolução do exercício o programa foi escrito de uma forma mais simples e mais restrita, como abaixo

'''tupla = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))'''
#Ou seja, utilizou o randint 5x, o que pode ser um problema quando se quiser trabalhar com intervalos maiores.

lista = numpy.random.randint(1, 101, (5)) #De 1 a 100 mostrando 5 número aleatórios.
#Neste método basta alterar o intervalo e quantos números quer dentro do Array e depois converter para tupla.

#Utilizei o "tuple" para converter o array em Tupla.
tupla = tuple(lista)

#Mostrar a tupla após a conversão... Aqui ficou como na resolução do exercício!
for n in tupla:
    print(f'{n}', end=' ')

#Tentei através da validação convencional mas não rolou, na resolução do exercício utilizou-se o método min e max.
print(f'\nO menor número do intervalor é o {min(tupla)}.')
print(f'O maior número do intervalo é o {max(tupla)}.')