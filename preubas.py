# se solicita la cantidad de usuarios 
users = int(input('cuantos usuarios desea regitrar?  '))
for user in range(users):

    #validacion de los datos 
    #Nombres
    names = input('ingrese sus nombres : ')
    while not(5 < len(names) < 50):
        names = input('Error !! ingrese sus nombres de nuevo : ')

    #apellidos 
    last_names = input('ingrese sus apellidos : ')
    while not(5 < len(last_names) < 50):
        last_names = input('Error !! ingrese sus apellidos de nuevo : ')

    #Numeros de telefono 
    phone_number = input('ingrese su numero de teléfono : ')
    while len(phone_number) != 10:
        phone_number = input('Error !! ingrese su numero de nuevo : ')

    #Correo
    emai = input('ingrese su correo electrónico : ')
    while not(5 < len(emai) < 50):
        emai = input('Error !! ingrese su correo de nuevo : ')

    # se muestra un mensaje de registro exixtoso 
    print(f'Usuario {user + 1} {names} {last_names} se registro con exito, en breve recibirá un correo a {emai}, hasta luego')
    users -= 1

print('----Programa  Finalizado----')