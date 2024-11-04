print("Hola, Liverpool es parte de tu vida")
nombre = input("¿Cuál es tu nombre? ")
print("Muy bien " + nombre + ", ¿qué te gustaría comprar de electrodomésticos?")
print(" ** Selecciona ** ")
print("Refrigerado. Presiona 1")
print("Microondas. Presiona 2")
print("Licuadora. Preiona 3 ")
print("Batidora. Presiona 4")
print("Estufa. Presiona 5")
print("**")
opcion = int(input("Escribe el número del electrodoméstico que deseas comprar: "))
# Selección opción 1 Refrigerador
if opcion == 1:
    print("Perfecto, el Refrigerador cuesta $30,000 pesos.")
    opcion_uno = input(nombre + ", ¿Te gustaría proceder con el pago? ")
    if opcion_uno == "SI":
        print("Muy bien, ¿cuál sería tu método de pago?")
        print("**SELECCIONA**")
        print("Tarjeta BBVA. Presiona 7")
        print("Otra tarjeta (con 10% de intereses). Presiona 8")
        print("Abono. Presiona 9")
        opcion_pago = int(input("Selecciona la opción de tu pago: "))
        
        if opcion_pago == 7:
            print("Perfecto, " + nombre + ". Inserte su tarjeta.")
            PIN = input("Por favor inserte su PIN: ")
            if PIN == "2588":
                print(nombre + ", ¡¡¡¡¡¡FELICIDADES, SU TARJETA HA SIDO APROBADA!!!!!!, ¡¡¡SU REFRIGERADOR VA EN CAMINO!!!")
            else:
                print("PIN incorrecto Transacción no autorizada ☹️.")
        
        elif opcion_pago == 8:
            print(f"Serían $30,000 más el 10%, en total $33,000 pesos.")
            PIN = input("Por favor inserte su tarjeta y su PIN: ")
            if PIN == "2588":
                print(nombre + ", ¡¡¡FELICIDADES, SU TARJETA HA SIDO APROBADA!!! ¡¡¡SU REFRIGERADOR VA EN CAMINO!!!")
            else:
                print("PIN incorrecto. Transacción no autorizada.")
        
        elif opcion_pago == 9:
            saldo = 100000
            print(f"Tu saldo registrado es de {saldo} pesos.")
            abono = float(input("¿Cuál será la cantidad que te gustaría abonar? "))
            if abono <= saldo:
                saldo -= abono
                print(f"Abono registrado exitosamente. Tu nuevo saldo es: {saldo} pesos.")
                print("¡¡¡SU REFRIGERADOR VA EN CAMINO!!!")
            else:
                print("Saldo insuficiente para realizar el abono.")
    else:
        print("Perfecto, " + nombre + ". Puedes volver a iniciar sesión para seleccionar otro.")

# Selección opción 2 Microondas
elif opcion == 2:
    print("El microondas cuesta $20,000 pesos.")
    opcion_dos = input(nombre + "¿Te gustaría proceder con el pago? ")
    if opcion_dos == "SI":
        print("Muy bien, ¿cuál sería tu método de pago?")
        print("**SELECCIONA**")
        print("Tarjeta BBVA. Presiona 7")
        print("Otra tarjeta (con 10% de intereses). Presiona 8")
        print("Abono. Presiona 9")
        opcion_pago = int(input("Selecciona la opción de tu pago: "))
        
        if opcion_pago == 7:
            print("Perfecto, " + nombre + ". Inserte su tarjeta.")
            PIN = input("Por favor inserte su PIN: ")
            if PIN == "2588":
                print(nombre + ", ¡¡¡FELICIDADES, SU TARJETA HA SIDO APROBADA!!! ¡¡¡SU MICROONDAS VA EN CAMINO¡¡¡")
            else:
                print("PIN incorrecto. Transacción no autorizada.")
        
        elif opcion_pago == 8:
            print(f"Serían $20,000 más el 10%, en total $22,000 pesos.")
            PIN = input("Por favor inserte su tarjeta y su PIN: ")
            if PIN == "2588":
                print(nombre + ", ¡¡¡FELICIDADES, SU TARJETA HA SIDO APROBADA!!! ¡¡¡SU MICROONDAS VA EN CAMINO¡¡¡ ")
            else:
                print("PIN incorrecto. Transacción no autorizada.")
        
        elif opcion_pago == 9:
            saldo = 100000
            print(f"Tu saldo registrado es de {saldo} pesos.")
            abono = float(input("¿Cuál será la cantidad que te gustaría abonar? "))
            if abono <= saldo:
                saldo -= abono
                print(f"Abono registrado exitosamente. Tu nuevo saldo es: {saldo} pesos.")
                print("¡¡¡SU MICROONDAS VA EN CAMINO!!!")
            else:
                print("Saldo insuficiente para realizar el abono.")
    else:
        print("Perfecto, " + nombre + ". Puedes volver a iniciar sesión para seleccionar otro.")

# Selección opción 3: Licuadora
elif opcion == 3:
    print("La licuadora cuesta $2,000 pesos.")
    opcion_tres = input(nombre + ", ¿Te gustaría proceder con el pago?")
    if opcion_tres == "SI":
        print("Muy bien, ¿Cuál sería tu método de pago?")
        print("**SELECCIONA**")
        print("Tarjeta BBVA. Presiona 7")
        print("Otra tarjeta (con 10% de intereses). Presiona 8")
        print("Abono. Presiona 9")
        opcion_pago = int(input("Selecciona la opción de tu pago: "))
        
        if opcion_pago == 7:
            print("Perfecto, " + nombre + ". Inserte su tarjeta.")
            PIN = input("Por favor inserte su PIN: ")
            if PIN == "2588":
                print(nombre + ", ¡¡¡FELICIDADES, SU TARJETA HA SIDO APROBADA!!! ¡¡¡SU LICUADORA VA EN CAMINO!!!")
            else:
                print("PIN incorrecto. Transacción no autorizada.")
        
        elif opcion_pago == 8:
            print(f"Serían $2,000 más el 10%, en total $2,200 pesos.")
            PIN = input("Por favor inserte su tarjeta y su PIN: ")
            if PIN == "2588":
                print(nombre + ", ¡¡¡FELICIDADES, SU TARJETA HA SIDO APROBADA!!! ¡¡¡SU LICUADORA VA EN CAMINO!!!")
            else:
                print("PIN incorrecto. Transacción no autorizada.☹️")
        
        elif opcion_pago == 9:
            saldo = 100000
            print(f"Tu saldo registrado es de {saldo} pesos.")
            abono = float(input("¿Cuál será la cantidad que te gustaría abonar? "))
            if abono <= saldo:
                saldo -= abono
                print(f"Abono registrado exitosamente. Tu nuevo saldo es: {saldo} pesos.")
                print("¡¡¡SU LICUADORA VA EN CAMINO!!!")
            else:
                print("Saldo insuficiente para realizar el abono.☹️")
    else:
        print("Perfecto, " + nombre + ". Puedes volver a iniciar sesión para seleccionar otro.")

# Selección opción 4 Batidora
elif opcion == 4:
    print("La batidora cuesta $1,000 pesos.")
    opcion_cuatro = input(nombre + ", ¿Te gustaría proceder con el pago?")
    if opcion_cuatro == "SI":
        print("Muy bien, ¿Cuál sería tu método de pago?")
        print("**SELECCIONA**")
        print("Tarjeta BBVA. Presiona 7")
        print("Otra tarjeta (con 10% de intereses). Presiona 8")
        print("Abono. Presiona 9")
        opcion_pago = int(input("Selecciona la opción de tu pago: "))
        
        if opcion_pago == 7:
            print("Perfecto, " + nombre + ". Inserte su tarjeta.")
            PIN = input("Por favor inserte su PIN: ")
            if PIN == "2588":
                print(nombre + ", ¡¡¡FELICIDADES, SU TARJETA HA SIDO APROBADA!!! ¡¡¡SU BATIDORA VA EN CAMINO!!!")
            else:
                print("PIN incorrecto. Transacción no autorizada ☹️.")
        
        elif opcion_pago == 8:
            print(f"Serían $1,000 más el 10%, en total $1,100 pesos.")
            PIN = input("Por favor inserte su tarjeta y su PIN: ")
            if PIN == "2588":
                print(nombre + ", ¡¡¡FELICIDADES, SU TARJETA HA SIDO APROBADA!!! ¡¡¡SU BATIDORA VA EN CAMINO!!!")
            else:
                print("PIN incorrecto. Transacción no autorizada.")
        
        elif opcion_pago == 9:
            saldo = 100000
            print(f"Tu saldo registrado es de {saldo} pesos.")
            abono = float(input("¿Cuál será la cantidad que te gustaría abonar? "))
            if abono <= saldo:
                saldo -= abono
                print(f"Abono registrado exitosamente. Tu nuevo saldo es: {saldo} pesos.")
                print("¡¡¡SU BATIDORA VA EN CAMINO!!!😁")
            else:
                print("Saldo insuficiente para realizar el abono.☹️")
    else:
        print("Perfecto, " + nombre + ". Puedes volver a iniciar sesión para seleccionar otro.")

# Selección opción 5 Estufa
elif opcion == 5:
    print("La estufa cuesta $7,000 pesos.")
    opcion_cinco = input(nombre + ", ¿Te gustaría proceder con el pago?")
    if opcion_cinco == "SI":
        print("Muy bien, ¿Cuál sería tu método de pago?")
        print("**SELECCIONA**")
        print("Tarjeta BBVA. Presiona 7")
        print("Otra tarjeta (con 10% de intereses). Presiona 8")
        print("Abono. Presiona 9")
        opcion_pago = int(input("Selecciona la opción de tu pago: "))
        
        if opcion_pago == 7:
            print("Perfecto, " + nombre + ". Inserte su tarjeta.")
            PIN = input("Por favor inserte su PIN: ")
            if PIN == "2588":
                print(nombre + ", ¡¡¡FELICIDADES, SU TARJETA HA SIDO APROBADA!!! ¡¡¡SU ESTUFA VA EN CAMINO!!!😁")
            else:
                print("PIN incorrecto. Transacción no autorizada.")
        
        elif opcion_pago == 8:
            print(f"Serían $7,000 más el 10%, en total $7,700 pesos.")
            PIN = input("Por favor inserte su tarjeta y su PIN: ")
            if PIN == "2588":
                print(nombre + ", ¡¡¡FELICIDADES, SU TARJETA HA SIDO APROBADA!!! ¡¡¡SU ESTUFA VA EN CAMINO!!!😁")
            else:
                print("PIN incorrecto. Transacción no autorizada.")
        
        elif opcion_pago == 9:
            saldo = 100000
            print(f"Tu saldo registrado es de {saldo} pesos.")
            abono = float(input("¿Cuál será la cantidad que te gustaría abonar? "))
            if abono <= saldo:
                saldo -= abono
                print(f"Abono registrado exitosamente. Tu nuevo saldo es: {saldo} pesos.")
                print("¡¡¡SU ESTUFA VA EN CAMINO!!!")
            else:
                print("Saldo insuficiente para realizar el abono.")
else:
    print("Perfecto, " + nombre + ". Puedes volver a iniciar sesión para seleccionar otro.")