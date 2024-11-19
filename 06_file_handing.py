### File Handing ###

# .txt file

txt_file = open("my_file.txt", "r+") # Leer y escribir
#print(txt_file.read())
#print(txt_file.read(10))
#print(txt_file.readlines())

for line in txt_file.readlines():
    print(line)