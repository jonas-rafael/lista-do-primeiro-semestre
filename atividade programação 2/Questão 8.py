print("--------------------------------------------")
print("                 Questão 8")
print("--------------------------------------------")

smedio=float(input("Digite saldo medio: "))
credito=float
scred=float
if smedio>400:
  credito=(30/100)*smedio
  scred=smedio+credito
  print(f"Seu saldo medio foi {smedio} com isso recebera um crédito no valor de {credito:,.2f}, e seu saldo reajustado ficará {scred:,.2f}")
if smedio<400 and smedio>300:
  credito=(25/100)*smedio
  scred=smedio+credito
  print(f"Seu saldo medio foi {smedio} com isso recebera um crédito no valor de {credito:,.2f}, e seu saldo reajustado ficará {scred:,.2f}")
if smedio<300 and smedio>200:
  credito=(20/100)*smedio
  scred=smedio+credito
  print(f"Seu saldo medio foi {smedio} com isso recebera um crédito no valor de {credito:,.2f}, e seu saldo reajustado ficará {scred:,.2f}")
if smedio<200:
  credito=(10/100)*smedio
  scred=smedio+credito
  print(f"Seu saldo medio foi {smedio} com isso recebera um crédito no valor de {credito:,.2f}, e seu saldo reajustado ficará {scred:,.2f}")