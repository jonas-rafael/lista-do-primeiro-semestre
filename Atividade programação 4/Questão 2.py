#========================
listaAP=[]
listaREP=[]
media=[]
listaREC=[]

#========================
while True: 
  aluno=str(input("Digite nome do aluno ou digite (sair) para finalizar: "))
  if aluno == "sair" :
    break
    
  else:
    valor=int(input("Digite a média do aluno: "))
    if valor <=6:
      listaAP.append(aluno)
      listaAP.append(valor)
      print(listaAP)
    if valor <=2:
      listaREP.append(aluno)
      listaREP.append(valor)
      print(listaREP)
    if valor ==3 or valor <=5:
      listaREC.append(aluno)
      listaREC.append(valor)
      print(listaREC)
    if valor<0 or valor>11:
      print("Valor da média não permitido!")



print(f"Lista de aprovados: \n{listaAP}")
print(f"Lista dos alunos que terão que repetir o ano: \n{listaREP}")
print(f"Lista de alunos /n{listaREC}")
      



