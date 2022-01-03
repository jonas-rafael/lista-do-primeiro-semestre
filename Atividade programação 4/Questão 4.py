print(50*"=")
print("                 Questão 4")
print(50*"=")

lista1=[]
lista2=[]
lista1_2=[]
aux=str


tamanho=int(input("Digite quantos itens terá a primeira lista"))
for i in range(tamanho):
  aux=str(input("Digite um nome para ser adcionado a primeira lista: "))
  lista1.append(aux)
  print(lista1)


tamanho1=int(input("Digite quantos itens terá a primeira lista"))

for j in range(tamanho1):
  aux=str(input("Digite um nome para ser adcionado a primeira lista: "))
  lista2.append(aux)
  print(lista2)

lista1.sort()
lista1_2.append(lista1)
lista2.sort()
lista1_2.append(lista2)


print(lista1)
print("========================================")
print(lista2)
print("========================================")
print(lista1_2)
