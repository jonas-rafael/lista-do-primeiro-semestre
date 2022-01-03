quantidade=int(input("Digite a quantidade de alunos na lista"))
alunos=[]

for i in range(quantidade):
  nome=input("Digite o nome do aluno")
  nota1=float(input("Digite a primeira nota do aluno:"))
  nota2=float(input("Digite a segunda nota do aluno:"))
  nota3=float(input("Digite a terceira nota do aluno:"))
  nota4=float(input("Digite a quarta nota do aluno:"))
  alunos.append([nome, nota1, nota2, nota3, nota4 ] )
  print('=============================================')

for aluno in (alunos):
    media=(aluno[1] + aluno[2] + aluno[3] + aluno[4]) /4
    print(f"a média de {aluno[0]}, {media}")


    if media >= 7:
      print("O aluno(a) foi aprovado(a)!")
    elif media< 3:
      print("O aluno(a) foi reprovado(a)")
    else:
      print("Aluno(a) em  recuperação")
  

  