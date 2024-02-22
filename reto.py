#varibles para máximos y minimos
min_car = 5
max_car = 50
max_phone_digits = 10
users_data = {}
user_list = []
user_id = 1 # inicio en 1
test = ""


#defino una función por si necesito reutilizar este bloque de código
def new_user():

    global user_id # usamos global para usar la variable definida fuera del scope de la funcion

    name = input("Ingrese el nombre del usuario: ")
    while not(len(name) > min_car and len(name) < max_car):
          name = input('Error ! el NOMBRE debe tener entre 5 y 50 caracteres. Ingrese de nuevo el nombre : ')

    last_name = input("Ingrese los apellidos del usuario: ")
    while not(len(last_name) > min_car and len(last_name) < max_car):
          last_name = input('Error ! el APELLIDO debe tener entre 5 y 50 caracteres. Ingrese de nuevo el apellido : ')

    phone = input("Ingrese el número de teléfono del usuario: ")
    while len(phone) != max_phone_digits:
          phone = input('Error ! el teléfono debe tener 10 caracteres. Ingrese de nuevo el teléfono : ')
    

    mail = input("Ingrese el correo electrónico del usuario: ")
    while not(len(mail) > min_car and len(mail) < max_car):
          mail = input('Error ! el MAIL debe tener entre 5 y 50 caracteres. Ingrese de nuevo el mail : ')

    #users_data.append([user_id, name, last_name, phone, mail])
    # Guardamos los datos en un Diccionario:
    users_data.update({
    "ID" : user_id,
    "Nombre" : name,
    "Apellido" : last_name,
    "Teléfono" : phone,
    "Mail" : mail
    })
          
    user_list.append(users_data.copy())  #Agregamos el diccionario a la lista

    user_id += 1
    return mail

def registro():
    # uso try/catch(except) para capturar errores
    try:
        cantidad_usuarios = int(input("¿Cuántos usuarios desea registrar? "))
        if cantidad_usuarios <= 0:
                print("Por favor, ingrese un número válido de usuarios.")
        # iteramos N veces según el números de usuarios a ingresar    
        for i in range(cantidad_usuarios):
                print(f"\nRegistrando usuario {i+1}:")
                correo = new_user()
                print(f"\n¡Usuario {i+1} registrado con éxito!")
                print(f"Se enviará un mail de confirmación a {correo}")
    except ValueError:
            print("Por favor, ingrese un número entero válido para la cantidad de usuarios.")

    print("--------------------------------")
    print(f"\nSe han registrado {cantidad_usuarios} usuario/s")


def show_user():
            id_user = int(input("Ingrese el ID del usuario que desea ver: "))

            usuario_encontrado = None #

            for user_data in user_list:
                if user_data["ID"] == id_user:
                        usuario_encontrado = user_data
                        break
                
            if usuario_encontrado is not None:
                print("Datos del usuario: ")
                for key, value in usuario_encontrado.items():
                        print(f"{key}: {value}")
            else:
                print(f"NO se encontró usuario con ID: {id_user}")

def edit_user():
            # Modificar un usuario según el ID
            id_usuario = int(input("\nIngrese el ID del usuario que desea modificar: "))
            for user_data in user_list:
                if user_data["ID"] == id_usuario:
                    print("\nModificando usuario...")
                    # Solicitar al usuario que ingrese los nuevos datos
                    name = input("Ingrese el nuevo nombre del usuario: ")
                    last_name = input("Ingrese los nuevos apellidos del usuario: ")
                    phone = input("Ingrese el nuevo número de teléfono del usuario: ")
                    mail = input("Ingrese el nuevo correo electrónico del usuario: ")

                    # Actualizar los datos del usuario en el diccionario
                    user_data["Nombre"] = name
                    user_data["Apellido"] = last_name
                    user_data["Teléfono"] = phone
                    user_data["Mail"] = mail

                    print("\n¡Usuario modificado con éxito!")
                    print("\nNuevos datos del usuario:")
                    for key, value in user_data.items():
                        print(f"{key}: {value}")
                    
                else:
                    print(f"\nNo se encontró ningún usuario con el ID {id_usuario}")

def delete_user():
    # Eliminar un usuario según el ID
    id_usuario = int(input("\nIngrese el ID del usuario que desea eliminar: "))
    for user_data in user_list:
        if user_data["ID"] == id_usuario:
            print("\nEliminando usuario...")
            user_list.remove(user_data)
            print("\n¡Usuario eliminado con éxito!")
            break
    else:
        print(f"\nNo se encontró ningún usuario con el ID {id_usuario}")

def lis_users():
     print("los usuarios registrado son:")
     for user_data in user_list:
          print("Datos de los usuarios:")
          for key, value in user_data.items():
               print(f"{key}: {value}")
          print("---------------")


print("BIENVENIDO!\n")
registro()
# -------------Menu de opciones-----------------
while True:
      option = input("\nQue desea hacer a continuación?:\nA - Agregar un nuevo Usuario\nB - Buscar un usuario por ID\nC - Modifificar un usuario\nD - Borrar Usuario\nE - Listar\nF - Salir\n")

      #Procesamos la opcion seleccionada:
      if option == "A":
            registro()
      elif option == "B":
            show_user()

      elif option == "C":
           edit_user()

      elif option == "D":
           delete_user()

      elif option == "E":
           lis_users()

      elif option == "F":
            # Salir del programa
        print("\nSaliendo del programa...")
        break
      else:
        print("\nOpción no válida. Por favor, seleccione una opción válida.")


# ----------Fin de Menu de opciones-----------------


