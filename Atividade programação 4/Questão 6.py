print("============================================")
print("                Questão 6")
print("============================================")

lista=[]
quantidade=int(input("Digite a quantidade de intens que terá a lista: "))
maior=0
menor=0
aux=0

for i in range(quantidade):
  
  lista.append(int(input("Digite um  item pra ser adicionado a lista: ")))
  lista.sort()
  print(f"Esta é a lista em ordem crecente{lista}")
  if i==0:
    maior=menor=lista[i]
else:
  if lista[i]>maior:
    maior=lista[i]
  if lista[i]<menor:  
    menor=lista[i]
print("--------------------------------------")
print(f"Este é o maior número: {maior}")
print(f"Este é o menor número: {menor}")
print("---------------------------------------")
#=======================================================
#Multiplicado pelo maior e dividido pelo menor.

for i in range(len(lista)):
  divimul= (i*maior) / menor
  print(f"o resultado da multiplicação do {i} da lista pelo maior número: {maior} e da divisão pelo menor número: {menor} é {divimul}")
  print("---------------------------------------------")