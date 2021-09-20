# Índice de massa corporal by Alex Ribeiro
# O IMC se calcula através da fórmula Peso/altura².
 
print('-='*18)
print()
print('Vamos calcular o IMC das pessoas.')
print()

peso = float(input('Digite o seu peso: '))
print()

altura = float(input('Agora, digite sua altura: '))
print()
print('-='*18)
print()

imc = peso / (altura**2)

if imc < 18.5:
    print('Você está abaixo do peso. IMC {:.2f}.'.format(imc))
elif 18.5 <= imc < 25:
    print('Você está no peso ideal. IMC {:.2f}.'.format(imc))
elif 25 <= imc < 30:
    print('Você está com sobrepeso. IMC {:.2f}.'.format(imc))
elif 30 <= imc < 40:
    print('Você está com obesidade. IMC {:.2f}.'.format(imc))
else:    print('Você está com obesidade Mórbida. IMC {:.2f}.'.format(imc))

print()
print('-='*18)