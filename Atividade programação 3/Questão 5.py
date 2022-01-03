print("=============================================")
print("                 Questão 5")
print("=============================================")


cont=0
quinze=0
dez=0
trint=0
quent=0
acima=0

while cont<15:
  idade=int(input("Digite a idade: "))
  cont+=1
  if idade<=15:
    quinze+=1
  if idade>=16 or idade<=31:
    dez+=1
  if idade>=31 or idade<=45:
    trint+=1
  if idade>=46 or idade<=60:
    quent
  if idade>=61:
    acima+=1


print(f"na 1º faixa etária até 15 anos tem o total de {quinze} ")
print(f"na 2º faixa etária até 15 anos tem o total de {dez} ")
print(f"na 3º faixa etária até 15 anos tem o total de {trint} ")
print(f"na 4º faixa etária até 15 anos tem o total de {quent} ")
print(f"na 5º faixa etária até 15 anos tem o total de {acima} ")