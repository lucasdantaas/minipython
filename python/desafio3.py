# Um numero em metros e converter em centimentros e milimetros.

# 1 metro = 100 centimetros
# 1 metro = 1000 milimetros
def converter_metros_para_centimetros_e_milimetros(metros):
    centimetros = metros * 100
    milimetros = metros * 1000
    return centimetros, milimetros
# Testar a função com um exemplo
metros = 5
centimetros, milimetros = converter_metros_para_centimetros_e_milimetros(metros)
print(f"{metros} metros é igual a {centimetros} centimetros e {milimetros} milimetros")