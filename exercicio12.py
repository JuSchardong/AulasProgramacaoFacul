# distancia = int (520)
# consome = int (12)
# preco = float(4,50)

distancia = int(input("Digite a distancia: "))
consome = int(input("Digite o consumo: "))
preco = float(input("Digite o preço: "))

litros = distancia / consome
custo = litros * preco

print("Utilizará: ", litros, " litros")
print("Custará: ", custo, "Reais")
