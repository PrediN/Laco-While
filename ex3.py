# 3. Somar números até o usuário digitar 0. Peça números ao usuário e some-os até que ele digite 0.

# Declaração de variáveis

sum = 0
datainput = 1

# Apresentação de resultados
while datainput != 0:
    datainput = int(input("Digite um número (digite 0 pra sair): "))
    sum += datainput
    print("Soma atual: ", sum)

