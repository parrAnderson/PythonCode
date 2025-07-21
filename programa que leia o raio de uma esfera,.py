#Escreva um programa que leia o raio de uma esfera,
# e calcule o seu volume e área.

raio = float(input('digite o raio:'))

#calculo do volume e área
V = (4/3) * 3.1415 + raio ** 3
A = 4* 3.1415 * raio ** 2

#RESULTADO
print (f'Volume da esfera: {V:.2f}\nárea da esfera: {A:.2f}')
