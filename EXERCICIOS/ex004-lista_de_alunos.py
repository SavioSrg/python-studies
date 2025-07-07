print("Cria uma lista inicial com 5 nomes de alunos: ")
alunos = ["Carlos", "Amanda", "Bruno", "Fernanda", "Eduardo"]
print(alunos, "\n")

print("Adicionando mais nomes a lista")
alunos.append("Joana")
alunos.append("Lucas")
print(alunos, "\n")

print("Inserir um novo nome em uma posição especifica: ")
alunos.insert(1, "Marina")
print(alunos, "\n")

print("Modificar o nome em uma das posições ('Carlos'|'Carla'): ")
alunos[0] = "Carla"
print(alunos, "\n")

print("Remova o aluno 'Bruno' da lista: ")
alunos.remove("Bruno")
print(alunos, "\n")

print("Use pop() para remover o último aluno e guarde em uma variável: ")
ultimo_removido = alunos.pop(-1)
print(alunos, ultimo_removido, "\n", sep="\n")

print("Inverta a lista original no local: ")
alunos.reverse()
print("Lista invertida:", alunos, "\n")

print("Informações: ")
print("Número total de alunos:", len(alunos))
print("Primeiro aluno (índice 0):", alunos[0])
print("Último aluno (índice -1):", alunos[-1])
print("Fatiamento dos 3 primeiros alunos:", alunos[:3])
print("Fatiamento de 2 em 2:", alunos[::2])
print("Lista invertida com slicing:", alunos[::-1])
