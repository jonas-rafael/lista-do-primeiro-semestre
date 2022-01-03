print("===========================================")
print("               Questão 8")
print("==========================================")
lista=[]
quantidade=int(input("Digite o tamanho da lista desejado: "))


for i in range(quantidade):
  aux=(input(f"Digite um número para a lista:"))
  lista.append(aux)
  print("--------------------------------------------")
  print(f"Existem >>>>{lista.count(aux)}<<<< deste número na lista")
  print("---------------------------------------------")

print("===========================")
