codigo = input("Digite uma frase: ")

lista_de_letras = []
lista_de_numeros = []
lista_de_simbolos = []

for caractere in codigo:
    if caractere.isalpha():
        lista_de_letras.append(caractere)
    elif caractere.isdigit():
        lista_de_numeros.append(caractere)
    else:
        lista_de_simbolos.append(caractere)
        
print(lista_de_letras, "\n")
print(lista_de_numeros, "\n")
print(lista_de_simbolos)