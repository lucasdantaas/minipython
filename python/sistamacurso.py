def selecionar_curso():
    print("Selecione o curso que deseja assistir:")
    print("1 - Python")
    print("2 - Java")
    print("3 - C++")
    curso = input("Digite o número do curso: ")
    
    if curso == "1":
        return "curso_python"
    elif curso == "2":
        return "curso_java"
    else:
        print("Curso não encontrado")
    return selecionar_curso()

def curso_python():
    python = str(input('bem vindo! sera presencial ou a distancia:'))
    if python == 'presencial':
        print('você escolheu o curso python presencial')
    elif python == 'a distancia':
        print('você escolheu o curso python a distancia')
      
def curso_java():
    print('seja bem vindo!')
    java = str(input('você deseja fazer o curso java presencial ou a distancia:'))
    if java == 'presencial':
        print('você escolheu o curso java presencial')
    elif java == 'a distancia':
        print('você escolheu o curso java a distancia')


# Chamada da função
curso = selecionar_curso()
if curso == "curso_python":
    curso_python()
elif curso == "curso_java":
    curso_java()



        

