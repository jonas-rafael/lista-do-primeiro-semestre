
def ler_nota():
  global letra
  if letra == "a" or "A":
    med= (n1 + n2 + n3)/3
    print(med)
  elif letra == "p" or "P":
    med= (n3*5 + n2*3 + n3*2 ) / (5+3+2)
    print(med)
  

#-----------------------------------------------------
n1=int(input("Digite a primeira nota: ")) 
n2=int(input("Digite a segunda nota: "))
n3=int(input("Digite a terceira nota: "))

print("escolha o parâmetro para calculo das notas\n 'A' para media aritimetica\n 'P' para media ponderada. " )
letra=str(input(">> "))

ler_nota()
 

