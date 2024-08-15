from random import randint

carro = randint(1, 120)
print(carro)
multa = carro >= 60
valor = (carro-60) * 7
if carro >=60:
    print("Você foi multado")
    print(f"Você foi multado em R${valor:.2f}")
