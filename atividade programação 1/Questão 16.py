import math
print("----------------------------")
print("         Questão 16")
print("----------------------------")
catetoa=float(input("Digite o valor do cateto A: "))
catetob=float(input("Digite o valor do cateto B: "))
catetoab= round(math.sqrt((catetoa**2)+(catetob**2)),2)
print(f"a hipotenusa dos conjunto de valores {catetoa} e {catetob} é {catetoab}")