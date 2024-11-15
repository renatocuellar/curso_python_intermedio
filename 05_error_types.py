### Error Types ###

# SyntaxError

#print "Hola Comunidad" #Error
print("Hola comunidad")

# NameError

# print(languaje) # La variable no esta definida


# IndexError

my_list = ["Python", "Swift", "Kotlin", "Dart", "Javascript"]
print(my_list[0])
print(my_list[4])
print(my_list[-1])
print(my_list[1])
#print(my_list[6]) Como no existe en la lista
# genera error


# ModuleNotFoundError
# import maths => No existe
import math


# AttributeError

print(math.pi)
# print(math.Pi) # => Pi en mayus no existe


# KeyError

my_dict = {"Name":"Matt", "Surname":"Cue", "Edad":35}
print(my_dict["Edad"])
# print(my_dict["Apellido"]) Es surname


#TypeError

# print(my_list["Nombre"]) El dict se llama con la variable creada, no es una lista
print(my_list[0])

# ImportError

# from math import Pi => Como Pi esta en mayus, no puede importarlo bien
from math import pi
print(pi)


# ValueError

# my_int = int("10 años")
# print(my_int)


# ZeroDivisionError

# print(4/0)

