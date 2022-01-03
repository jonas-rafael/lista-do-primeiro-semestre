print("----------------------------------------------")
print("              Questão 11")
print("----------------------------------------------")
cod=int(input("Digite o codigo do produto: "))
if cod==1:
  print(f"Produto com codigo {cod} tem procedência no Sul.")
elif cod==2:
  print(f"Produto com codigo {cod} tem procedência no Norte.")
elif cod==3:
  print(f"Produto com codigo {cod} tem procedência no Leste.")
elif cod==4:
  print(f"Produto com codigo {cod} tem procedência no Oeste.")
elif cod==5 or cod==6 or cod==21 or cod>=21 and cod<31:
  print(f"Produto com codigo {cod} tem procedência no Nordeste.")
elif cod==7 or cod==8 or cod==9:
  print(f"Produto com codigo {cod} tem procedência no Sudeste.")
elif cod>=10 and cod<=20:
  print(f"Produto com codigo {cod} tem procedência Centro-Oeste.")