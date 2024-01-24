#entrada de dados
idade=int(input("digite sua idade: "));

#processamento
if(idade<16):
    resultado="não eleitor";
elif(idade>16 and idade <18):
    resultado="eleitor facultativo";
elif(idade>=18 and idade<=65):
    resultado="eleitor obrigatório";
else:
    resultado="eleitor facultativo";
    
#saída de dados
print(resultado)