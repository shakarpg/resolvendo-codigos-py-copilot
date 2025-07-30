
# desafios_python_copilot_chatgpt.py

# ==========================================
# 1 - Concatenando Dados 🐾
# ==========================================
print("1 - Concatenando Dados 🐾")
dado1 = input("Digite o primeiro dado: ")
dado2 = input("Digite o segundo dado: ")
resultado_concatenacao = dado1 + " " + dado2
print("Resultado da concatenação:", resultado_concatenacao)

print("\n---------------------------\n")

# ==========================================
# 2 - Repetindo Textos ✏️
# ==========================================
print("2 - Repetindo Textos ✏️")
texto = input("Digite o texto: ")
vezes = int(input("Digite o número de vezes que deseja repetir: "))
resultado_repeticao = texto * vezes
print("Texto repetido:", resultado_repeticao)

print("\n---------------------------\n")

# ==========================================
# 3 - Operações Matemáticas Simples 📐
# ==========================================
print("3 - Operações Matemáticas Simples 📐")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
soma = num1 + num2
print("A soma é:", soma)

print("\n---------------------------\n")

# ==========================================
# 4 - Verificando Números Pares e Ímpares 🧮
# ==========================================
print("4 - Verificando Números Pares e Ímpares 🧮")
numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

print("\n---------------------------\n")

# ==========================================
# 5 - Calculando Média de Notas 📚
# ==========================================
print("5 - Calculando Média de Notas 📚")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
print("A média das notas é:", round(media, 2))

print("\n---------------------------\n")

# ==========================================
# 6 - Verificando Palíndromos 🔄
# ==========================================
print("6 - Verificando Palíndromos 🔄")
palavra = input("Digite uma palavra: ")
if palavra == palavra[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
