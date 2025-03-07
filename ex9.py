# 9. Contar quantos números pares o usuário digitar. O programa deve contar quantos números pares o usuário inseriu.
# O usuário para digitando -1.

# Declaração de variáveis

dataInput = 0
contador = 0

# Apresentação de resultados

while dataInput != -1:
        
    dataInput = int(input("Digite um número(digite -1 para sair): "))
    print()
    if dataInput % 2 == 0:
        contador += 1

    print("Você digitou", contador, "números pares.")