def Escolher_time(numero_matricula):
    if numero_matricula % 2 == 0:
        print("VOCE ESTÁ NO TIME AZUL")
    else:
        print("VOCÊ ESTÁ NO TIME AMARELO")

numero = int(input("Digite p número de matricula: "))
Escolher_time(numero)           