# 8. Encontrando o maior número inserido pelo usuário. Peça números ao usuário e, ao digitar 0, exiba o maior número inserido.

# Declaração de variáveis

datainput = 1
maior = 0

# Apresentação de resultados

while datainput != 0:
        
    datainput = int(input("Digite um número(digite 0 para sair): "))
    print()
    if datainput > maior:
        maior = datainput

    print("O maior número digitado até agora é: ", maior)
    print()
