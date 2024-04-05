nota = input('Escreva sua nota: ')
nota = int(nota)

if (nota) >= 90:
    print('Grade A, parabéns')

if (nota) >= 88:
   print('Grade B')

elif nota >= 78:
    print('Grade C')

if nota >= 68:
    print('Grade D')

if nota <= 68:
    print('Grade F')
    print("da próxima, estude mais!")
