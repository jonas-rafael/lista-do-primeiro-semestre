print("--------------------------------------------")
print("               Questão 2")
print("--------------------------------------------")

aluno=str(input("Digite nome do aluno: "))
nota1=float(input("Digite a primeira nota: "))
nota2=float(input("Digite a segunda nota: "))
media=(nota1+nota2)/2 
if media==0 or media>=4:
  print(f"O(a) {aluno} está reprovado")
elif media==4 or media<7:
  print(f"O(a) {aluno} está na prova final")
elif media>=7 or media>=10:
  print(f"O(a) {aluno} está aprovado")