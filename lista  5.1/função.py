

def ler_nota(mensagem, l=[]):

  while True:
    nota= float(input(mensagem))
    l.append(nota)
    print(l)

    if 0 <= nota <= 10:
      break
    else:
      print("Nota invalida!")
  return nota
def media(mensagem):  
  global l
  letra=str(input(mensagem))
  if letra == "a" or "A":
    med= (l[1] + l[2] + l[3])/3
    print(med)
  elif letra == "p" or "P":
    med= (l[1]*5 + l[2]*3 + l[3]*2 ) / (5+3+2)
    print(med)
  
  




       
    