# 6. Some todos os números pares de 1 a 100 e mostre o resultado.

# Declaração de variáveis

sum = 0
i = 1

# Apresentação de resultados

while i <= 100:
    if i % 2 == 0:
        sum += i
    i += 1
    print(f"Soma atual: {sum}")

print()
print("A soma de todos os números pares de 1 à 100 é:", sum)