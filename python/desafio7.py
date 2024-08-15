import random

#sorte nome de uma lista.
alunos = ['Maria', 'Joao', 'Lucas', 'jose']

for c in random.choices(alunos):
    print('o aluno escolhido foi {}'.format(c))



