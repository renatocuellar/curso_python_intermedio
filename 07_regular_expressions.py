### Regular Expressions ###

import re

# Cómo funciona el Match

my_string = "Esta es la lección número 7: Lección de Expresiones regulares"
my_other_string = "Está no es una clase"

match= re.match("Esta es la lección", my_string, re.I)
# if not(match == nome): 
# if not(match != nome): 
if match is not None:
    print(match)
    start, end = match.span()
    print(my_string[start:end])


print(re.match("Esta es la lección", my_other_string))
print(re.match("Expresiones", my_string))


# Así funciona el search

search = re.search("lección", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])


#Así funciona findall

findall = re.findall("lección", my_string, re.I)
print(findall)


#Así funciona un split

print(re.split("7", my_string))

# sub

print(re.sub("[l|L]ección", "Leccion", my_string))


# patterns

pattern = r"[l|L]ección"
print(re.findall(pattern, my_string))

pattern = r"[l|L]ección|Expresiones"
print(re.findall(pattern, my_string))

pattern = r"[a-z]"
print(re.findall(pattern, my_string))

pattern = r"[0-9]"
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r"\D"
print(re.findall(pattern, my_string))

pattern = r"[l]."
print(re.findall(pattern, my_string))


#email validation reGex

email = "renato.cuellar@gmail.com.co"


pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))
