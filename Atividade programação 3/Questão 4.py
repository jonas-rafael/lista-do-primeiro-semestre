print("=============================================")
print("               Questão 4")
print("=============================================")

N=int(input("Digite a quantidade de numeros que deseja ver: "))
cont=0
n1=0
n2=1
while cont<N: 
  cont+=1
  n3=n1+n2
  n1=n2
  n2=n3
  print(f"esse é o proximo termo da sequncia {n3}\n")