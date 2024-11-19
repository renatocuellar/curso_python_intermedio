### File Handing ###

import os

# .txt file

txt_file = open("my_file.txt", "r+") # Leer y escribir
#print(txt_file.read())
#print(txt_file.read(10))
#print(txt_file.readlines())

for line in txt_file.readlines():
    print(line)

txt_file.close()

#txt_file.write("\n Aunque también me gusta JavaScript")


import json

json_file = open("my_file.json", "r+")

json_test = {"Name":"Renato",
             "Surname": "Cuellar",
             "Age": 35, 
             "Languages": ["Python", "JavaScript", "Kotlin", "Java", "Swift", "TypeScript", "Php", "Ruby"],
             "Website": "https://renatocuellar.com"
             }

json.dump(json_test, json_file, indent = 4)
print(json_file.read())

# .cvs file

import csv

csv_file = open("my_csv.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerows(["name", "surname", "Age", "Language", "Website"])
csv_writer.writerows(["Renato", "Cuéllar", 35, "Python", "https://renatocuellar.com"])

# .xml file

import xml