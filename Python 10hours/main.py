def calculator_room():

    altura = float(input('digite a altura do quarto: '))
    largura = float(input('digite a largura do quarto: '))
    calculo = (altura * largura)
    
    return calculo

area_quarto = calculator_room()

print(f'a área do quarto é: {area_quarto:.2f} metros quadrados')