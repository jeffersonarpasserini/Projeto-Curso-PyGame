def soma(x,y):
    return (x+y)

def multiplicacao(x,y):
    return (x*y)

def subtracao(x,y):
    return (x-y)

def divisao(x,y):
    return (x/y)

def imprimirNome(nome, vezes):
    for n in range(1,vezes):
        print(nome)

#------------- Main ---------------------------
loop = True
while loop:
    print('------------------- Menu Principal ----------------------')
    print('Escolha sua opção: ')
    print('1 - Operação de soma')
    print('2 - Operacao de subtracão')
    print('3 - Operacao de multiplicação')
    print('4 - Operacao de divisão')
    print('5 - Imprimir o seu nome N vezes')
    print('0 - Sair do programa')

    opcao = int(input('Opção:'))

    if (opcao == 1):
        print('----- Operacao de Soma -----')
        n1 = int(input('Entre com o primeiro numero:'))
        n2 = int(input('Entre com o segundo numero:'))
        resultado = soma(n1,n2)
        print("O resultado da soma foi de {}".format(resultado))
    elif (opcao == 2):
        print('----- Operacao de Subtração -----')
        n1 = int(input('Entre com o primeiro numero:'))
        n2 = int(input('Entre com o segundo numero:'))
        resultado = subtracao(n1, n2)
        print("O resultado da substração foi de {}".format(resultado))
    elif (opcao == 3):
        print('----- Operacao de Multiplicação -----')
        n1 = int(input('Entre com o primeiro numero:'))
        n2 = int(input('Entre com o segundo numero:'))
        resultado = multiplicacao(n1, n2)
        print("O resultado da multiplicação foi de {}".format(resultado))
    elif (opcao == 4):
        print('----- Operacao de Divisao -----')
        n1 = int(input('Entre com o primeiro numero:'))
        n2 = int(input('Entre com o segundo numero:'))
        resultado = divisao(n1, n2)
        print("O resultado da divisão foi de {}".format(resultado))
    elif (opcao == 5):
        print('----- Imprimir nome n vezes -----')
        nome = input('Entre com o seu nome:')
        vezes = int(input('Entre com o numero de vezes:'))
        imprimirNome(nome, vezes)
    elif (opcao == 0):
        loop = False


print('Você finalizou a execução do Programa!')



