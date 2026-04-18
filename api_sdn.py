import requests

def obtener_dispositivo(device_id):
    url = f"https://jsonplaceholder.typicode.com/users/{device_id}"
    respuesta = requests.get(url)
    respuesta.raise_for_status()
    return respuesta.json()

if __name__ == "__main__":
    dispositivo = obtener_dispositivo(1)
    print(dispositivo)
