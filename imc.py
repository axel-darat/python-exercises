def imc(estatura, peso):
    
    return peso / estatura**2

peso = float(input('Escriba su peso (Kg): '))
estatura = float(input('Escriba su estatura (m): '))

indice = imc(estatura, peso)

print('Su IMC es: {}'.format(indice))