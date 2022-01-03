print("------------------------------------------------")
print("               Questão 7 ")
print("------------------------------------------------")
salario=float(input("Digite seu salario: "))
reajuste=float
aumento=float
if salario<300:
 reajuste=(35/100)*salario
 aumento=salario+reajuste
 print(f"seu salario de {salario} receberá um reajuste de  35% no valor de{reajuste} com isso seu novo salário é {aumento}   ")
else: salario>301
reajuste=(15/100)*salario
aumento=salario+reajuste
print(f"seu salario de {salario} receberá um reajuste de  35% no valor de{reajuste} com isso seu novo salário é {aumento}   ")
