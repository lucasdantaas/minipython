#digite quanto dinheira a pessoa tem na carteira e quantos dolares ela pode comprar!

dinheiro = float(input("Quantos reais você tem na carteira? R$ "))
dolar = 5.50
preco_dolar = 5.50
#calcule quanto dinheiro a pessoa pode comprar com o dinheiro que ela tem na carteira!
dinheiro_comprado = dinheiro / preco_dolar
print(f"Com R${dinheiro:.2f} você pode comprar R${dinheiro_comprado:.2f}")


