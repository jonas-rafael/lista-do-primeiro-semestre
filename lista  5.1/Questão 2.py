def vetor( l=[], a=[]):
  tamanho=int(input("Defina quantos itens terá a lista: "))
  for j in range(tamanho):
    valor=int(input("insira um valor pra lista: "))
    l.append(valor)
    print(l)
  exp=1
  for num in l:
    print(f"esse é a lista correndo{num}")
    exp*=num
    a.append(exp)
    print(f" esse é o novo vetor {a}")

    

    
    



print(30*"=")
 
 
vetor()