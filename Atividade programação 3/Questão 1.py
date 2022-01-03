print(30*"=")
print("          Questão 1")
print(30*"=")
cont=0
inte=int
soma=0
media=float
aux=0

while True :
 inte=int(input("Digite qualquer numero inteiro: "))
 
 aux=inte+aux
 cont= cont+1
 
 if inte==0:
   print(" ")
   print(f"a quantidade de numeros digitados foi {cont}")
   print(" ")

   print(f"a soma dos números digitados são {aux}")
   print("")
   media=(cont+aux)/2
   print(" ")
   print(f"a media da contagem e da soma dos números digitados é {media}")


   break



    

  