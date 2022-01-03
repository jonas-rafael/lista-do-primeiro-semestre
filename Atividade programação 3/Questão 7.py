print("============================================")
print("           Questão 7")
print("============================================")
um=0
dois=0
tres=0
cinco=0
nove=0
cod=int



while True:
  cod=int(input("Digite o código do produto: "))
  if cod==1 or cod==2 or cod==3 or cod==5 or cod==9:
    qua=float(input("Digite a quantidade do produto: "))
    if cod==1:
      um=um + 0.50
    if cod==2:
      dois=dois + 1.00
    if cod==3:
      tres=tres + 4.00
    if cod==5:
      cinco=cinco + 7.00
    if cod==9:
      nove=nove + 8.00
    if cod==0:
      break
  else:
    print("Código invalido!")

print(um)
print(dois)
print(tres)
print(cinco)
print(nove)