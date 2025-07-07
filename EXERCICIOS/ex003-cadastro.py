estado_civil = input("Digite seu estado civil (opções possíveis: S, C, D, V): ")

while estado_civil != "S" and estado_civil != "C" and estado_civil != "D" and estado_civil != "V":
  estado_civil = input("Resposta inválida! Digite seu estado civil (opções possíveis: S, C, D, V): ")

print("O estado civil é", estado_civil)