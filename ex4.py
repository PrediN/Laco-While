# 4. O usuário deve digitar a senha correta (1234). Enquanto errar, o programa deve pedir novamente.

# Declaração de variáveis

senha = 1234
datainput = 0

# Apresentação de resultados
while datainput != senha:
    datainput = int(input("Digite a senha: "))
    if datainput != senha:
        print("Senha incorreta.")
    
print("Senha correta.")