'''
    Não existe tipos de variavel
    Você vai usar, por exemplo  ->  num = 1
    Declarar usuário para o usuário digitar -> num = int(input("Digite o número que você deseja!"))
    Instalar as estensões Python e CodeRunner no VsCode para rodar Python
'''

num = int(input("Digite o número que você desejar!"))
num2 = int(input("Digite outro número!"))

if num > num2:
    print(f"O número {num} é maior que {num2}!")
else:
    print(f"O número {num2} é maior que {num}!")

soma = num + num2
subtracao = num - num2
divisao = num / num2
multiplicacao = num * num2