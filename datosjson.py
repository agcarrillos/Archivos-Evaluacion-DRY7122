import json

# Abrir archivo JSON
with open("myfile.json") as json_file:
    ourjson = json.load(json_file)

# Mostrar datos
print("Token:", ourjson["token"])
print("Tiempo restante:", ourjson["expires_in"])
