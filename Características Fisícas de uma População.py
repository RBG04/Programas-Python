'''
Faça um programa onde é realizada uma pesquisa
sobre algumas características fisicas da população de uma certa
região, a qual coletou os seguintes dados referentes a cada habitantes para análise:
-sexo('M' masculino ou 'F' feminino);
-cor dos olhos('A' azuis,'V' verdes ou 'C' castanhos);
-cor dos cabelos('L' loiros,'C' castanhos ou 'P' pretos);
-idade
Faça um algoritmo que determine e escreva:
-a maior idade dos habitantes;
-a porcentagem entre os indivíduos do sexo masculino, cuja idade está entre 18 e 35 anos;
-a porcentagem do total de individuos do sexo feminino, cuja idade está entre 18 e 35 anos, inclusive,
e que tenham olhos verdes e cabelos loiros.
O final do conjunto de habitantes é reconhecido pelo valor -1 entrando como idade.

=>#Sexo      =>#Cor dos Olhos   =>#Cor do cabelo
M=masculino    A=azuis            C=castanhos
F=feminino     V=verdes           L=loiro 
               C=castanhos        P=pretos
               '''
x=0 
idade=0 
maiorIdade=0
masc=0
porM=0
fem=0 
porF=0 

while x<3:
    idade=int(input("Qual a sua idade: "))
    sexo=str(input("Qual o seu sexo[M/F]: ")).strip()
    olhos=str(input("Qual a cor dos seus olhos[A/C/V]: ")).strip()
    cabelos=str(input("Qual a cor do seu cabelo[C/L/P]: ")).strip()
    if(idade>maiorIdade):
        maiorIdade=idade 
    if(sexo in 'Mm' and idade>17 and idade <36):
        masc+=1
        porM=masc/100
    if(sexo in 'Ff' and idade>17 and idade <36):
        fem+=1
    if(sexo in 'Ff' and olhos=='v' and cabelos=='l'):
        fem+=1 
        porF=fem/100
    x+=1 

print('homem mais velho tem {} anos'.format(maiorIdade))
print('{}% de pessoas do sexo masculino de 18 á 35 anos'.format(porM))
print('{}% de pessoas do sexo feminino de 18 á 35 anos com os olhos verdes e cabelos loiros'.format(porF))
