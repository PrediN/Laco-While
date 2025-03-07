# 5. Some todos os números de 1 a 500 e mostre o resultado.

# Declaração de variáveis

sum = 0
i = 1

# Apresentação de resultados

while i <= 500:
    sum += i
    i += 1
    print(f"Soma atual: {sum:,}")

print()
print(f"Soma de 1 a 500: {sum:,}")