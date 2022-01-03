print("=============================================")
print("                Questão 2")
print("=============================================")

I=int(input("Digite o número inicial da tabuada: "))
L=int(input("Digite o número limitante da tabuada: "))
cont=0
soma=0
mult=0
aux=0
while cont<L:
  cont+=1
  aux+=1
  soma=I+aux
  mult=I*aux
  
  print(f"{I} + {aux} = {soma}| {I} x {aux} = {mult}")

  
