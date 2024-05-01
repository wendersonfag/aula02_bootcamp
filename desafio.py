CONSTANTE_BONUS = 1000
# 1) Solicita ao usuário que digite seu nome
nome_usuario = input("Digite seu nome: ")

if any(char.isdigit() for char in nome_usuario):
    print("O nome não deve conter números.")
elif len(nome_usuario) == 0:
    print("Você não digitou nada")
    exit()
elif nome_usuario.isspace():
    print("Você digitou só espaço")
    exit()
# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
try:
    salario = float(input("Digite o seu salário: "))
except ValueError:
    print("digite um valor de salário válido: ")
# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
try:
    bonus = float(input("Digite o seu bônus: "))
except ValueError:
    print("digite um valor de bônus válido: ")
# 4) Calcule o valor do bônus final
resultado_bonus = CONSTANTE_BONUS + salario * bonus
# 5) Imprima cálculo do KPI para o usuário
#print(resultado_bonus)
# 6) I'mprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"Olá {nome_usuario}, o seu bônus foi de R${resultado_bonus:.2f}")
# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?