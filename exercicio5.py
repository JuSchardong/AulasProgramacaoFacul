#num = float(input("Escreva um numero: "))
soma = 0
for i in range(5):
    num = int(input("Escreva um numero: "))
    soma = int(num+soma)
    
media = float (soma / 5) 
print("A soma é: ",soma,"A media é: ", media)