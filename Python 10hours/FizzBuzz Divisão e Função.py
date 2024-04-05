escolha = int(input('escolha um número: '))

def função(escolha):
    
    for num in range(1, escolha):

        if num % 3 and num % 5 == 0:
            print(f'{num} fizzbuzz ')

        elif num % 3 == 0:
            print(f'{num}/fizz')
            
        elif num % 5 == 0:
            print(f'{num}/buzz')

                
função(escolha)