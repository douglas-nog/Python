#Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros
#elementos de uma Sequência de Fibonacci.

n = int(input('Quantos números você deseja mostrar? '))
primeiro = 0
segundo = 1
print(' {} - {} -'.format(primeiro, segundo), end='')
c = 3
while c < n:
    terceiro = primeiro + segundo
    primeiro = segundo
    segundo = terceiro
    c += 1
    print(' {} -'.format(terceiro), end='')
print(' Fim')