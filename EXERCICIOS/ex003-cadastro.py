estado_civil = input("Digite seu estado civil (opções possíveis: S, C, D, V): ").upper()

while estado_civil not in ["S", "C", "D", "V"]:
  
  estado_civil = input("Resposta inválida! Digite seu estado civil (opções possíveis: S, C, D, V): ").upper()

print("O estado civil é", estado_civil)