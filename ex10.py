# 10. Apenas aceitar números positivos. O programa deve continuar pedindo um número até o usuário digitar um número negativo.

# Declaração de variáveis

num = 1

# Apresentaçãp de resultados

while num <= 0:
    num = int(input("Digite um número positivo: "))
    if num <= 0:
        print("Número inválido. Digite um número positivo.")
    else:
        print("Número digitado: ", num)
        