# 7. Adivinhe o número secreto (de 1 a 10). O usuário deve tentar adivinhar um número até acertar. (Declare um valor e receba outro)

# Declaração de variáveis

segredo = 7
n = 0

# Apresentação de resultados

print()
print("Adivinhe o número secreto (de 1 a 10).")
print()

while n != segredo:
    
    n = int(input("Digite um número: "))
    print()
    if n == segredo:
        print("Parabéns! Você acertou.")
        print()
    else:
        print("Você errou. Tente novamente.")
        print()
