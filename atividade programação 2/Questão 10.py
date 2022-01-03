print("----------------------------------------------")
print("             Questão 10")
print("----------------------------------------------")
altura=float(input("Digite  altura em metros ex(x.xx): "))
sexo=str(input("Defina o sexo sendo M para masculino e F para feminino: "))
peso=float

if sexo=="M" or sexo=="m":
  peso=(72.7*altura)-58
  print(f"Peso ideal para sua altura é {peso:,.2f}")
if sexo=="F" or sexo=="f":
  peso=(62.1*altura)-44.7
  print(f"Peso ideal para sua altura é {peso:,.2f}")

