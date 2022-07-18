
nome = input('Olá, qual o seu nome? \n')
n1 = float(input(f'Olá {nome}, por favor informe o primeiro número: '))
n2 = float(input('Agora informe o segundo número: '))


def Menu():
    print(f'''
    Agora {nome}, ecolha o que quer que eu faça com esses números, suas opcao são:

    [1] Somar
    [2] Multiplicar
    [3] Verificar qual é o maior número
    [4] Divisão
    [5] Novos números
    [6] Subtrair
    [7] Exponenciação
    [8] Fechar o programa
    ''')
Menu()

def Soma():
    soma = n1 + n2
    print(f'A soma de {n1} e {n2} é igual a {soma}')

def Multiplicação():
    produto = n1 * n2
    print(f'O resultado da multiplicação entre {n1} e {n2} é {produto}')

def MaiorMenor():
    if n1 > n2:
        print(f'O número {n1} é maior que {n2}.')
    else:
        print(f'O número {n1} é menor que {n2}.')

def Dividir():
    divisão = n1 / n2
    print(f'A divisão de {n1} por {n2} é de {divisão:.2f}')

def novos_numeros():
    n1 = float(input('Qual o número que você gostaria de usar agora?: \n'))
    n2 = float(input('Qual o segundo numero que você gostaria de utilizar agora?: \n'))

def subtração():
    subtração = n1 - n2
    print(f'O resultado da subtração de {n1} entre {n2} é de {subtração}')

def potência():
    exponenciação = n1 ** n2
    print(f'A exponenciação de {n1} elevado a {n2} é de {exponenciação:.2f}')

def fim():
    print('Obrigado por utilizar nossos serviços, volte sempre!')

def Opção():
    opcao = 0
    while opcao != 8:
        opcao = int(input('Selecione a opção desejada: '))
        if opcao == 1:
            Soma()
        elif opcao == 2:
            Multiplicação()
        elif opcao == 3:
            MaiorMenor()
        elif opcao == 4:
            Dividir()
        elif opcao == 5:
            novos_numeros()
        elif opcao == 6:
            subtração()
        elif opcao == 7:
            potência()
        elif opcao ==8:
            fim()
        else:
            print('Opção inválida, por favor selecione somente as opções informadas!')
Opção()
