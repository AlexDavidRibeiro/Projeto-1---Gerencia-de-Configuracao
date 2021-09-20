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

print(f'Seu IMC = {imc:.2f}')