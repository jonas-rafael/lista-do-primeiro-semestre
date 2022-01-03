print("-----------------------------------------------")
print("              Questão 9")
print("-----------------------------------------------")

preco=float(input("Digite o novo preço: "))
aumento=float
npreco=float

if preco<50:
  aumento=(5/100)*preco
  npreco=preco+aumento
  print(f"O preço antigo era {preco} com o aumento de {aumento:,.2f}, o novo preço do produto é {npreco} ")
  #
if preco>50 and preco<100:
    aumento=(10/100)*preco
    npreco=preco+aumento
    print(f"o preço antigo do produto é {preco} e com o aumento de {aumento:,.2f}, o novo preço do produto é {npreco} ")
    #
if preco>100:
  aumento=(15/100)*preco
  npreco=preco+aumento
  print(f"o preço antigo do produto é {preco} e com o aumento de {aumento:,.2f}, o novo preço do produto é {npreco} ")
  #
if npreco<80:
  print("Classificação: Barato")
elif npreco>80 and npreco<120:
  print("Classificação> normal")
elif npreco>120 and npreco<200:
  print("Classificação: Caro")
elif npreco>200:
 print("Classificação: Muito caro!")

    
    

    