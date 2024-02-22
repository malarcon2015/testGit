# Estructuras de control
# if (elif), match (switch), 
# foreach -> Cuando sepamos cuantas iteraciones se necesitan
# while -> Cuando no sepamos cuantas iteraciones se necesitan (Condicion)

""" age = int( input("Ingrese su edad: "))

if age < 100:
    if age < 44:
        print("Sos un pendejo")
    elif age == 44:
        print("Que guapo!")
    else:
        print("Sos un viejo choto")
else:
    print("TE moriste") """


#estructura IF

""" color = input("Ingrese un color para el semáforo: ")

if color == "green":
    print("Puede pasar")
elif color == "yellow":
    print("Guarda!!")
elif color == "red":
    print("ALTOOO!!!!")
else:
    print("No corresponde!") """

# Match (switch)

""" color = input("Ingrese un color para el semáforo: ")

match color:
    case "green":
        print("PASA")
    case "red":
        print("Alto")
    case "yellow":
        print("GUARDAAA")
    case _:
        print("Color invalido") """

# FOREACH

""" for number in range(1, 101):
    if not(number % 2 == 0):
        print(number) """

# WHILE
""" random = 5
number = 0
max_attends = 5
attends = 0

while number != random and attends < 5:
    number = int(input("Ingresa un numero: "))
    attends +=1
else:
    if number == random:
        print("Ganaste!!!")
    else:
        print("Se te acabaron las oportunidades") """

# Listas = estructuras de datos

""" courses = ["Python", "Django", "Flask", "Ruby", "Ruby on Rails", "C#"] """

# EL usuario ingresa el indice que quiera averiguar
""" indice = int(input("Ingresa el valor para el indice: "))
total_indices = len(courses) - 1

if indice <= 5:
    print(courses[indice])
else:
    print("No hay tantos cursos") """

#---------------------------------------------------------------------

# Sublista
""" new_list = courses[::-1] # estructura[start:end:jump]
print(new_list) """

#---------------------------------------------------------------------

# METODOS (append, insert, extend, remove, count, index)

#---------------------------------------------------------------------

#extend: permite insetar toda una lista nueva al final de otra lista

""" new_courses = ["Java", "Docker", "Unix"]

courses.extend( new_courses)

print(courses)
 """
#---------------------------------------------------------------------

# append: agrega un elemento al final de la lista
""" courses.append("Javascript")
courses.append("Php")
courses.append("html") """

#---------------------------------------------------------------------

#insert: inserta un elemento en la lista en un indice en particular
""" courses.insert(2,"SQL")

print(courses)
print(courses[-1]) """

#---------------------------------------------------------------------

# remove: Elimina un elemento de la lista

""" courses.remove("Ruby")
courses.remove("Ruby on Rails")

print(courses) """

#---------------------------------------------------------------------

# count: permite ver cuantas veces está un elemento en la lista

""" print(courses.count("Ruby"))
 """

#---------------------------------------------------------------------

# index: permite ver en que incide se encuentra un valor

""" value = "Ruby"

if value in courses:
    print(f"El indice del valor es: {courses.index(value)}")
else:
    print("No existe") """


#---------------------------------------------------------------------
# Podemos iterar las listas con bucles
""" for course in courses:
    print(course) """

# Si necesitasemos saber ademas del valor, el indice, podemos utilizar "enumerate(VALOR)"

""" for index, course in enumerate(courses):
    print("El indice para el valor: ", course, "es: ", index) """

#----------------------------------------------------------------------------------------------------------------------

# TUPLAS - DICCIONARIOS

# TUPLAS: son inmutables, se pueden iterar

#indices         0         1     2         3           4
""" settings = ("localhost", 3306, "root", "password", "database") """

# desempaquetado de tupla:

# Se asignan en orden correlativo, si no se desea un valor se utiliza _ ej.: host, port, _, _, _ = settings. si tiene muchos valores: host, port, *_ = settings
""" host, port, user, passowrd, name = settings
 """
# Tuplas anidada

""" tuples =(
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

for _tuple in tuples:
    print(_tuple)


print(name) """

""" print(len(settings))
print(settings[2]) """


# -------------------------------
# DICCIONARIOS
# Llave != String - Llaves = Objetos inmutables (String, Enteros, Flotantes, Bool, Tuplas)
""" 
user = {
    # llave : valor,
    "name" : "Matias",
    "age" : 44,
    "email" : "alarcon.matiasj@gmail.com",
    "active" : True
 } """

# Metodo GET: get(KEY, Custom Message)

""" value = user.get("name")
print(value)

print(user["email"]) #para acceder a un valor específico
print(type(user)) """

# keys, values, items

""" print(user.keys())
print(user.values())
print(user.items()) """

#------------------------------------------FUNCIONES-----------------------------------------


# Los datos de entrada de una funcion = ARGUMENTOS -> Parametros
""" def suma(a, b):
    return a + b


def resta(c, d):
    result = c - d
    return result


def multiplicacion(e,f):
    result = e * f
    return result


print(suma(10, 90))
resta(80, 60)
multiplicacion(20,20) """

# Pedimos ingresa 5 notas
# Aprueba con >=7

scores = []

for option in range(0, 5):
    score = int(input("Ingresa una calificacion: "))
    scores.append(score)

average = sum(scores) / len(scores)

print(average)