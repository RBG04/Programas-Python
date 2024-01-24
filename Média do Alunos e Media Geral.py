x=1;
totalNotas=0
mediaAluno=0
mediaGeral=0
while x<=5:
    nota1=float(input("digite a primeira nota: "));
    nota2=float(input("digite a segunda nota: "));
    totalNotas=nota1+nota2;
    mediaAluno=totalNotas/2;
    print("a media do aluno é: ",mediaAluno);
    mediaGeral=mediaGeral+mediaAluno;
    x+=1;
print("a mediaGeral é: ",mediaGeral);