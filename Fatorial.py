
def Factorial (n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * (n-1) 

n=int(input("Digite um número: "))
resultado=Factorial(n)
print(resultado)
