print("=============================================")
print("               Questão 3")
print("=============================================")


while True:
 N=int(input("Digite um número que seja (>=1) : "))
 if N>=1:
   break
 else: 
   print("Valor invalido!")

cont=N
fat=1
while cont>1:
  fat=fat* cont
  cont-=1
  print(" ")
  print(fat)
  print("  ")

print(f"O fatorial é {fat}")