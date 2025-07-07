lista_alunos = []

print("Bem vindo!")
print("O sistema irá pedir o nome de 5 alunos e suas 3 notas. (0 a 10)")
print("Depois, retornaremos informações interessantes sobre o desempenho de cada um.")
print ("-" * 125)

# Entrada dos dados
for i in range(5):
    nome = input(f"\nNome do aluno {i + 1}: ")

    nota1 = float(input("Qual foi a sua primeira nota? "))
    nota2 = float(input("Qual foi a sua segunda nota? "))
    nota3 = float(input("Qual foi a sua terceira nota? "))

    lista_alunos.append([nome, [nota1, nota2, nota3]])

# Mostrando lista bruta (opcional, útil para debug)
print("\nalunos adicionados (dados brutos):")
print(lista_alunos)


#Calculando as médias
medias = []

for aluno in lista_alunos:
    notas = aluno[1]
    media = sum(notas) / len(notas)
    medias.append(media)

# Exibindo nome + média com zip()
for aluno, media in zip(lista_alunos, medias):
    nome = aluno [0]
    print(f"{nome} - Média: {media:.2f}")

# Verificando destaque (10 em tudo) ou dificuldade (< 5 em tudo)
for aluno in lista_alunos:
    nome, notas = aluno
    if all(nota == 10 for nota in notas):
        print(f"\nParabéns especial para {nome}, tirou 10 em tudo!")
        break
    elif all(nota < 5 for nota in notas):
        print(f"\nO aluno {nome} não está indo bem (todas as notas abaixo de 5).")

# List comprehension para alunos aprovados
aprovados = [aluno[0] for aluno, media in zip(lista_alunos, medias) if media >= 6]

print("\nAlunos aprovados:", aprovados)
