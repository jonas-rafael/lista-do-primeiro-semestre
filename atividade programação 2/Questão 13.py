print("-----------------------------------------------")
print("               Questão 13")
print("-----------------------------------------------")

categ=str(input("Digite a categria do produto ex:(alimentação): "))
valor=float(input("Digite o preço do produto: "))
situa=str(input("Digite a situação R ou S, R significa produto que precisa de refrigeração e S se não precisar: "))








if categ=="alimentação" or categ=="limpeza" or categ=="vestuario":
 




    if categ=="alimentação" and valor<=25:
      aument=(8/100)*valor
      aument1=valor+aument
      print(f"O preço da categoria {categ}\n teve um amumento de 8% no valor de {aument}\n e o preço final do produto é {aument1}")
    elif categ=="alimentação" and valor>25:
      aument=(15/100)*valor
      aument1=valor+aument
      print(f"O preço da categoria {categ} teve um amumento de 15% no valor de {aument} e o preço final do produto é {aument1}")
      if situa=="r" or situa=="R" or categ=="alimentação":
        imposto=(5/100)*valor
        fvalor=aument1+imposto
        print(f"Será aplicado um imposto seguindo as regras de tributação um imposto de  5% no valor de {imposto:,.2f}\n sobre o produto alimentício refrigerado, o valor final do produto com os impostos e reajustes será de {fvalor} ")
      





  #==============================================================
    if categ=="limpeza" and valor<=25:
      aument=(5/100)*valor
      aument1=valor+aument
      print(f"O preço da categoria {categ}\n teve um amumento de 5% no valor de {aument} e o preço final do produto é {aument1}")
    elif categ=="limpeza" and valor>25:
      aument=(12/100)*valor
      aument1=valor+aument
      print(f"O preço da categoria {categ}\n teve um amumento de 12% no valor de {aument} e o preço final do produto é {aument1}")
      if situa=="r" or situa=="R":
        imposto=(5/100)*valor
        fvalor=aument1+imposto
        print(f"Será aplicado um imposto seguindo as regras de tributação, o imposto de  5% no valor de {imposto:,.2f}\n sobre o produto refrigerado, o valor final do produto com os impostos e reajustes será de {fvalor} ")
      elif situa=="s" or situa=="S":
        imposto=(8/100)*valor
        fvalor=aument1+imposto
        print(f"será aplicado um imposto seguindo as regras de tributação, o imposto no valor {imposto:,.2f}\n sobre o produto, com os imposto e reajustes será de {fvalor}.  ")

  #==============================================================
    if categ=="vestuário" and valor<=25:
      aument=(10/100)*valor
      aument1=valor+aument
      print(f"O preço da categoria {categ} teve um amumento de 10% no valor de {aument} e o preço final do produto é {aument1}")
    elif categ=="alimentação" and valor>25:
      aument=(18/100)*valor
      aument1=valor+aument
      print(f"O preço da categoria {categ} teve um amumento de 18% no valor de {aument} e o preço final do produto é {aument1}")
      if situa=="r" or situa=="R":
        imposto=(5/100)*valor
        fvalor=aument1+imposto
        print(f"Será aplicado um imposto seguindo as regras de tributação, o imposto de  5% no valor de {imposto:,.2f}\n sobre o produto refrigerado, o valor final do produto com os impostos e reajustes será de {fvalor} ")
      elif situa=="s" or situa=="S":
        imposto=(8/100)*valor
        fvalor=aument1+imposto
        print(f"será aplicado um imposto seguindo as regras de tributação, o imposto no valor {imposto:,.2f}\n sobre o produto, com os imposto e reajustes será de {fvalor}.  ")
else: 
  print("Aumento de 0%")        