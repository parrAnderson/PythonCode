#Simulação de um Caixa Eletrônico Este programa simula um caixa eletrônico, permitindo que o usuário faça depósitos, saques e consulte o saldo da conta, e sair


saque = int(input("Que valor você quer sacar? \n"))
notas = [50, 20, 10, 1]
cedulas = []
counter = 0
deposito=1
while saque > 0:
    for val in notas:
        cedulas.append(saque // val)
        saque = saque % val
        #        print(f"{cedulas[counter]} notas de R${val}")
        counter += 1
    counter = 0

    for item in cedulas:
        if item > 0:
            print(f"{item} cédulas de R${notas[counter]}")
        counter += 1  # teste
print(f' saque realizado com sucesso')

if counter ==1:
    deposito = float (input('Quanto voce deseja depositar?'))
    saldo += deposito
elif counter ==3:
    print(f'seu saldo é {saldo}')