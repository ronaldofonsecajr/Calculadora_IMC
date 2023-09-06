cm = float(input('Qual é a sua Altura?: '))
kg = float(input('Qual é a seu peso?: '))

calculo = kg / (cm/100)**2

print(calculo)

if calculo < 18.5:
    print('Magreza')
elif calculo >= 18.6 and calculo < 24.9:
    print('Normal')

elif calculo >= 25.0 and calculo < 29.9:
    print('Sobrepeso')

elif calculo >= 30.0 and calculo < 39.9:
    print('Obesidade')

else:
    print('Obesidaade Grave')