'''
    Não existe tipos de variavel
    Você vai usar, por exemplo  ->  num = 1
    Declarar usuário para o usuário digitar -> num = int(input("Digite o número que você deseja!"))
    Instalar as estensões Python e CodeRunner no VsCode para rodar Python
'''

num = int(input("Digite o número que você desejar!"))
num2 = int(input("Digite outro número!"))

if num2 == 0:
    print("ERRO!\nERRO!")
else:
    if num > num2:
        print(f"O número {num} é maior que {num2}!")
    elif num < num2:
        print(f"O número {num2} é maior que {num}!")
    else:
        print("Os números são iguais!")

soma = num + num2
subtracao = num - num2
multiplicacao = num * num2

if num2 == 0:
    print("ERRO!\nDigite o segundo número sem ser 0!\nERRO!")
else:
    divisao = num / num2
    print(f"Soma: {soma}\n\nSubtração: {subtracao}\n\nDivisão: {divisao}\n\nMultilpicação: {multiplicacao}")