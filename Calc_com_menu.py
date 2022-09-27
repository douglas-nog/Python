'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

n1 = float(input('Informe o primeiro número: '))
n2 = float(input(('Informe o segundo número: ')))
maior = 0
opcao = 0
while opcao != 5:
    print('''Escolha o que deseja fazer
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    opcao = int(input('Digite qual operação deseja realizar: '))
    if opcao == 1:
        soma = n1 + n2
        print('O resultado da soma entre {:.2f} e {:.2f} é {:.2f}.'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O resultado da multiplicação entre {:.2f} e {:.2f} é {:.2f}.'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior número entre {:.2f} e {:.2f} é {:.2f}.'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = float(input('Informe o primeiro número: '))
        n2 = float(input(('Informe o segundo número: ')))
    elif opcao == 5:
        print('Finalizando o programa. ')
    else:
        print('Opção inválida, tente novamente!')
    print('*==*==' * 10)
print('Programa finalizado com sucesso! ')