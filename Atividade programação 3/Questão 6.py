print("==============================================")
print("              Questão 6")
print("==============================================")


valv=0
valp=0
valoref=0
mai=0
men=0
cont=0
tipo=str
while cont<15:
  cont+=1
  tipo=str(input("Digite o tipo da compra, V para compras a vistas e P para compras a prazo: ")) 
  valor=float(input("Digite o valor da compra"))
  if tipo=="V" or "v":
    valv=valv+valor
    valoref=valv+valoref  
    
  if tipo=="P" or "p":
    valp=valp+valor
   
    valoref=valv+valoref
  if valor>mai:
    mai=valor
  if valor<men:
    men=valor
 
print(f"O valor totl das compra a vistas é {valv}")  
print(f"O valor total das compras a prazo é {valp}")
print(f"Valor total das compras foi {valp}")
print(f"A menor compra foi no valor de {men}")
print(f" val d maior compra foi {mai}")