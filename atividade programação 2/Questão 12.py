print("--------------------------------------------")
print("              Questão 12")
print("--------------------------------------------")
#
cod=float(input("Digite o código do produto: "))
valor=float
#------------------------------------------------
if cod>=1 and cod<=40:
  quant=float(input("Digite o número e produtos comprados: "))

  if cod>=1 and cod<=10:
    valor=10*quant
  
    print(f"O valor unitário do pruduto com código {cod} 10,00R$.")
    print(" ")
    print(f"O valor total da nota é {valor}")
    if valor<-250:
      desc=(5/100)*valor
      valort=valor-desc
      print(f"o total de desconto em Reais é {desc}R$")
      print("  ")
      print(f"O valor total da nota com o desconto  {valort}R$")  
    elif valor>=250 and valor<=500:
      desc=(10/100)*valor
      valort=valor-desc
      print(f"o total de desconto em Reais é {desc}R$")
      ("  ")
      print(f"O valor total da nota com o desconto é {valort}R$")
    elif valor>=501:
      desc=(15/100)*valor
      valort=valor-desc
      print(f"o total de desconto em Reais é {desc}R$")
      print("  ")
      print(f"O valor total da nota com o desconto é {valort}R$") 
      #-------------------------------------------------------------------
  elif cod>=11 and cod<=20:
    valor=15*quant
    print(f"O valor unitário do produto com codigo {cod} é 15,00R$.")
    print(f"O valor total da nota é {valor}")
    if valor<-250:
      desc=(5/100)*valor
      valort=valor-desc
      print(f"o total de desconto em Reais é {desc}R$")
      print("  ")
      print(f"O valor total da nota com o desconto  {valort}R$")  
    elif valor>=250 and valor<=500:
      desc=(10/100)*valor
      valort=valor-desc
      print(f"o total de desconto em Reais é {desc}R$")
      ("  ")
      print(f"O valor total da nota com o desconto é {valort}R$")
    elif valor>=501:
      desc=(15/100)*valor
      valort=valor-desc
      print(f"o total de desconto em Reais é {desc}R$")
      print("  ")
      print(f"O valor total da nota com o desconto é {valort}R$")

    #---------------------------------------------------------------------- 
  elif cod>=21 and cod<=30:
    valor=20*quant
    print(f"O valor unitário do pruduto com código {cod} 20,00R$.")
    print(" ")
    print(f"O valor total da nota é {valor}")
    if valor<-250:
      desc=(5/100)*valor
      valort=valor-desc
      print(f"o total de desconto em Reais é {desc}R$")
      print("  ")
      print(f"O valor total da nota com o desconto  {valort}R$")  
    elif valor>=25 and valor<=500:
      desc=(10/100)*valor
      valort=valor-desc
      print(f"o total de desconto em Reais é {desc}R$")
      ("  ")
      print(f"O valor total da nota com o desconto é {valort}R$")
    elif valor>=501:
      desc=(15/100)*valor
      valort=valor-desc
      print(f"o total de desconto em Reais é {desc}R$")
      print("  ")
      print(f"O valor total da nota com o desconto é {valort}R$")

    #----------------------------------------------------------------------
  elif cod>=31 and cod<=40:
    valor=30*quant
    print(f"O valor unitário do produto com codigo {cod} é 30,00R$.")
    print(f"O valor total da nota é {valor}") 
    if valor<-250:
      desc=(5/100)*valor
      valort=valor-desc
      print(f"o total de desconto em Reais é {desc}R$")
      print("  ")
      print(f"O valor total da nota com o desconto  {valort}R$")  
    elif valor>=250 and valor<=500:
      desc=(10/100)*valor
      valort=valor-desc
      print(f"o total de desconto em Reais é {desc}R$")
      ("  ")
      print(f"O valor total da nota com o desconto é {valort}R$")
    elif valor>=501:
      desc=(15/100)*valor
      valort=valor-desc
      print(f"o total de desconto em Reais é {desc}R$")
      print("  ")
      print(f"O valor total da nota com o desconto é {valort}R$")

   #---------------------------------------------------------------------- 
else: 
  print("Código não encontrado")




    

   
 


 



