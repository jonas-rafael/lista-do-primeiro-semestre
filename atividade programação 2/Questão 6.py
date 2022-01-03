print("----------------------------------------------")
print("                 Questão 6")
print("----------------------------------------------")

salario=int(input("Digite seu salario: "))
aumento=int
reajuste=int
if salario<=500:
  reajuste=(30/100)*salario
  aumento=salario+reajuste
  print(f"Seu salario de {salario} entra no reajuste, e receberá um aumento de 30% no valor de {reajuste}, no total ficará: {aumento} ")
else:
  print(f"Seu salário é de {salario}, logo não receberáa reajuste.")
