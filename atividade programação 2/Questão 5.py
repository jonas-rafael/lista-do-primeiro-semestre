import math
print("----------------------------------------------")
print("                   Questão 5")
print("----------------------------------------------")
print("  ")
print("instruções: escolha dois números e depois selecione uma das operações sitadas abaixo: ")
print("  ")
print("      escolha uma operação")
print("         ")
print("1 Média entre os números digitados")
print("2 Diferença do maior pelo menor")
print("3 Produto entre os números digitados")
print("4 Divisão do primeiro pelo segundo")
print("5 O primeiro número elevado ao segundo número")
print("6 Raiz quadrada de cada um dos números")
print("7 Raiz cúbica de cada um dos números")
print(" ")

n1=float(input("Digite o primeiro número: "))
n2=float(input("Digite o segundo número: "))
escolha=int(input("escolha uma das opções: "))
opera=float
raiz=float


if escolha == 1:
  opera=(n1+n2)/2
  print(f"a média entre os dois números é {opera}")
if escolha==2 and n1>n2: 
  opera= n1
else: opera=n2
if escolha== 3:
  opera=n1*n2
  print(f"O produto dos dois números é {opera}")
if escolha==4:
  opera= n1/n2
  print(f"A divisão do primeiro pelo segundo é {opera}")
if escolha==5:
  opera=(n1**n2)
  print(f"O primeiro número elevado pelo segundo é {opera}")
if escolha==6:
  opera= math.sqrt(n1)
  raiz=math.sqrt(n2)
  print(f"A raiz Quadrada do primeiro é{opera} e do segundo é {raiz}")
if escolha==7:
  opera=(n1 **(1/3))
  raiz=(n2**(1/3))
  print(f"a cúbica do rprimeiro número é {opera} a cúbica do segundo é {raiz}")

