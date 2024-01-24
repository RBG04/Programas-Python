x=1;
totm=0;
totf=0;
while x<=10:
    nome=input("digite seu nome: ");
    sexo=input("digite seu sexo: ");
    print(nome);
    print(sexo);
    if(sexo=="masculino"):
        resultado="totm";
        totm=totm+1;
    elif(sexo=="feminino"):
        resultado="totf";
        totf=totf+1;
    x+=1
print("soma de pessoas masculina é: ",totm);
print("soma de pessoas feminina é: ",totf);