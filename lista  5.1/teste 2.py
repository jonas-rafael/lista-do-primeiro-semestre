def ler_nota(mensagem):
    
  while True:
    nota= float(input(mensagem))

    if 0 <= nota <= 10:
      break
    else:
      print("Nota invalida!")
  return nota

    