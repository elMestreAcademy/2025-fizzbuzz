contador = 100

while (contador >= 1):
    if contador % 3 == 0 and contador % 5 == 0:
        print("fizzbuzz")
    elif contador % 3 == 0:
        print("fizz")
    elif contador % 5 == 0:
        print("buzz")
    else:
        print(contador)
    contador = contador - 1
