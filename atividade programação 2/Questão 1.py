print("--------------------------------------------")
print("                Questão 1")
print("--------------------------------------------")
nome=str(input("Insira o nome do aluno: "))
nota1=float(input("Insira a primeira nota: "))
nota2=float(input("Insira a segunda nota: "))
nota3=float(input("Insira a terceira nota: "))
nota4=float(input("Insira a quarta nota: "))
media=(nota1+nota2+nota3+nota4)/2
if media>=7: print(f" O {nome} aprovado com {media} está aprovado")


else: print(f"O(a) {nome} está cm média {media} por tanto terá que repetir o ano.")