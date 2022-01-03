print("=============================================")
print("                Questão 5")
print("=============================================")
lista=[]
copia=[]
tamanho=int(input("Digite quantos itens terá a lista: "))
for i in range(tamanho):
  aux=float(input(f" Digite o {i} número para a lista: "))
  lista.append(aux)
  print(lista)

for i in range(len(lista)):
  for j in range(len(lista)):
    soma= i + j
    #print(soma)
    print("------------------------")
    print(f"A soma dos itens da lista é: {lista[i]+ lista[j]}")

print("===================================")

for i in range(len(lista)):
  for j in range(len(lista)):
     print("------------------------")
    print(f" O produto dos itens da lista é: {lista[i]* lista[j]}")
