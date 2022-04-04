nota1 = float(input("Escreva a nota 1: "))
nota2 = float(input("Escreva a nota 2: "))
peso1 = float(input("Escreva o peso da nota 1: "))
peso2 = float(input("Escreva o peso da nota 2: "))

somaPeso = peso1 + peso2
mediaPonderada = ((nota1 * peso1) + (nota2 + peso2)) / somaPeso

print(mediaPonderada)