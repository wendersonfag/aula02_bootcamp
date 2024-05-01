# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

# n1 = 4
# n2= 5
# soma = n1 + n2
# print(f"Soma do valores é : {soma}")


# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

# n = int(input("Digite um numero: "))
# resto = n % 5
# print(f"o resto da divisão por 5 é: {resto}")


# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

# n1 = int(input("Digite o primeiro numero: "))
# n2 = int(input("Digite o segundo numero: "))
# resultado = n1 * n2
# print(f"Resultado da multiplicação é: {resultado}")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

# n1 = int(input("Digite o primeiro numero: "))
# n2 = int(input("Digite o segundo numero: "))
# resultado = n1 // n2
# print(f"O resultado da divisão inteira é: {resultado}")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# n1 = int(input("Digite o primeiro numero: "))

# resultado = n1 ** 2 
# print(f"O quadrado do número é : {resultado}")

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

# n1 = float(input("Digite o primeiro numero: "))
# n2 = float(input("Digite o segundo numero: "))
# resultado = n1 - n2
# print(f"O resultado da adiçãos é: {resultado}")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

# n1 = float(input("Digite o primeiro numero: "))
# n2 = float(input("Digite o segundo numero: "))
# resultado = (n1 + n2)/2
# print(f"A média é: {resultado}")

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

# n1 = float(input("Digite o numero base: "))
# n2 = float(input("Digite o numero expoente: "))
# resultado = n1 ** n2
# print(f"O resultado da potência é:{resultado}")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

# celsius = 30.0  # Exemplo de entrada
# fahrenheit = (celsius * 9/5) + 32
# print(f"{celsius}°C é igual a {fahrenheit}°F")

# celsius = 30.0  # Exemplo de entrada
# fahrenheit = (celsius * 1.8) + 32
# print(f"{celsius}°C é igual a {fahrenheit}°F")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# raio = 5.0
# area = 3.1415 * (raio **2)
# print(f"Área do circulo é : {area}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

# texto = "wenderson"
# texto_maiusculo = texto.upper()
# print(f"Texto em maiúsculas: {texto_maiusculo}")

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

# nome_completo = "Wenderson sinfroni fagundes"
# nome_minusculo = nome_completo.lower()
# print(f"Nome em minúsculas:: {nome_minusculo}")
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

# frase = "Hello World"
# frase_sem_espaco = frase.strip()

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# data = "01/05/2024"
# data_split= data.split("/")
# print(f"O dia é: {data_split[0]}, Mês é {data_split[1]}, O ano é {data_split[2]}")


# data1 = "01/05/2024"
# dia, mes,ano = data.split("/")
# print("Dia:", dia)
# print("Mês:", mes)
# print("Ano", ano)

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# nome = "Wenderson"
# sobrenome = "Fagundes"

# nome_sobrenome = nome + " " + sobrenome
# print("Texto concatenado: ",nome_sobrenome)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# valor1 = True
# valor2 = False
# resultado_and = valor1 and valor2
# print("Resultado do AND lógico:", resultado_and)
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# resultado_or = valor1 or valor2
# print("Resultado do OR lógico:", resultado_or)
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# resulto_not = not valor1
# print("Resultado do NOT lógico: ", resulto_not)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# comparacao = valor1 == valor2
# print("Resultado da comparação: ",comparacao)

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# diferente = valor1 != valor2
# print("Resultado da diferença: ", diferente)

# #### try-except e if

# 21: Conversor de Temperatura

# try:
#     celsius = float(input("Digite um temperatura : "))  # Exemplo de entrada
#     fahrenheit = (celsius * 1.8) + 32
#     print(f"{celsius}°C é igual a {fahrenheit}°F")
# except:
#         print("Por favor digite um numero valido")


# 22: Verificador de Palíndromo

# entrada = input("Digite uma palavra ou frase: ")
# if isinstance(entrada, str):
#     formatado = entrada.replace(" ", "").lower()
#     if formatado == formatado[::-1]:
#         print("É um palíndromo.")
#     else:
#         print("Não é um palíndromo.")
# else:
#     print("Entrada inválida. Por favor, digite uma palavra ou frase.")

# 23: Calculadora Simples
# try:
#     num1 = float(input("Digite o primeiro número: "))
#     num2 = float(input("Digite o segundo número: "))
#     operador = input("Digite o operador (+, -, *, /): ")
#     if operador == '+':
#         resultado = num1 + num2
#     elif operador == '-':
#         resultado = num1 - num2
#     elif operador == '*':
#         resultado = num1 * num2
#     elif operador == '/' and num2 != 0:
#         resultado = num1 / num2
#     else:
#         print("Operador inválido ou divisão por zero.")
#     print("Resultado:", resultado)
# except ValueError:
#     print("Erro: Entrada inválida. Certifique-se de inserir números.")

# 24: Classificador de Números

# try:
#     numero = int(input("Digite um número: "))
#     if numero > 0:
#         print("Positivo")
#     elif numero < 0:
#         print("Negativo")
#     else:
#         print("Zero")
#     if numero % 2 == 0:
#         print("Par")
#     else:
#         print("Ímpar")
# except ValueError:
#     print("Por favor, digite um número inteiro válido.")

# 25: Conversão de Tipo com Validação

entrada_lista = input("Digite uma lista de números separados por vírgula: ")
numeros_str = entrada_lista.split(",")
numeros_int = []
try:
    for num in numeros_str:
        numeros_int.append(int(num.strip()))
    print("Lista de inteiros:", numeros_int)
except ValueError:
    print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")
