'''
- código 1 - Alimento não-perecível 
- código 2,3 ou 4 - Alimento perecível 
- código 5 ou 6 - Vestuário
- código de 8 até 15 - Limpeza e utensílios domésticos
- Qualquer outro código - Invalido
'''
#entrada de dados
produto=int(input("digite o número do código: "));

#processamento 
if(produto<=0 or produto==7 or produto>15):
    resultado="Invalido";
elif(produto==1):
    resultado="alimento não perecível";
elif(produto<=4):
    resultado="alimento perecível";
elif(produto<=6):
    resultado="vestuário";
elif(produto>=8 and produto<=15):
    resultado="Limpeza e utensílios domésticos";
    
#saída de dados 
print(resultado);