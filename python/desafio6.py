# digiritar largura e altura em metros. calcular a area e descobrir quantos litros de tinta para pintar. 
# sabendo que 1 litro de tintar pinta 2metros quadrados!

def calcular_tinta(largura, altura):
    area = largura * altura
    litros = area / 2
    return litros
# testar a função:
largura = float(input("digite a largura em metros: "))
altura = float(input("digite a altura em metros: "))
print(f"serão necessarios {calcular_tinta(largura, altura)} litros de tinta para pintar")