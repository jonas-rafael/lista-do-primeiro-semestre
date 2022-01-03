print(50*"=")
print("                    Questão 1")
print(50*"=")
lista=[]
tamanho=int(input("insira quantos itens a lista terá: "))
pares=0
impar=0
paim=0

for i in range(tamanho):
  valor= int(input("\nDigite um valor inteiro: "))
  lista.append(valor)
  print(lista)
  if valor % 2 ==0:
    print(f"\no número: {valor} é divisivel por 2")
    pares+= 1
  if valor % 3 ==0:
    print(f"\no número: {valor} é divisivel por 3")
    impar+= 1
  if valor % 2 ==0 and valor % 3==0:
    print(f"\no número: {valor} é divisível por 2")
    paim+= 1
print(f"\nA quantidade de números divisíveis por 2 é: {pares}")
print(f"\nA quantidade de números divisíveis por 3 é: {impar}")
print(f"\nA quantidade de números divisiveis por 2 e 3  é: {paim}")