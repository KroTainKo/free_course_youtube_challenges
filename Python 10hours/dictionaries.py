#create a dictionary that will let you add a student and their grade
#you will need a while loop to complete this task

cont = 1

while cont <=1:
    student = input('digite o nome do estudante: ')
    grade = int(input('Digite a nota do estudante: '))

    dict = dict({'aluno': student, 'nota': grade})
    print(dict)
    cont =+1