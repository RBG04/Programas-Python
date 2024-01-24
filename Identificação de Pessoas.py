'''
Faça um programa onde sejama digitados o nome , sexo e a idade de 5 pessoas
e ao final o programa calcula e mostra:
-total de homens.
-total de mulheres.
-total de pessoas maiores de idade.
-total de pessoas maiores de 40 sexo feminino.
-total de pessoas do sexo masculino com idade entre 15 e 30 anos.
'''

x=0
totH=0 
totM=0
totP=0 
tot40=0 
totJ=0 
while x<3:
    nome=input("Digite seu nome: ")
    sexo=input("Digite seu sexo: ")
    idade=int(input("Digite sua idade: "))
    if(sexo=="masculino"):
        totH=totH+1
    elif(sexo=="feminino"):
        totM=totM+1 
    if(idade>18):
        totP=totP+1
    if(idade>40):
        tot40=tot40+1 
    if(idade>15 and idade<30):
        totJ=totJ+1
    x+=1 
print("total de homens é: ",totH)
print("total de mulheres é: ",totM)
print("total de pessoas maiores de 18: ",totP)
print("total de mulheres acima de 40: ",tot40)
print("total de jovens: ",totJ)