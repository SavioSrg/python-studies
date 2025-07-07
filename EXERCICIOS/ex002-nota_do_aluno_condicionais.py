media = float(input("Digite a média do aluno (digite de 0 a 10): "))
frequencia = float(input("Digite a frequência do aluno (em %): "))

if media >= 9 or (media >=6 and frequencia >= 75):
    print("Aprovado")
elif (media >= 6 and frequencia < 75) or (media < 6 and frequencia >= 75):
    print("Recuperação")
else:
    print("Reprovado")

"""Está é uma versão mais recomendada: 

if media >= 9:
  print("Aprovado")
elif media >= 6 and frequencia >= 75:
  print("Aprovado")
elif media >= 6 and frequencia < 75:
  print("Recuperação")
elif media < 6 and frequencia >= 75:
  print("Recuperação")
else:
  print("Reprovado")
"""
