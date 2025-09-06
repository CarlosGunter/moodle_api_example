import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

url = "http://localhost:8085/webservice/rest/server.php"
token = os.getenv("MOODLE_API_TOKEN")
# Verificar si se obtuvo el token
print('Token:', token)

# Definición del payload para crear un usuario
payload = {
    "wstoken": token, # Token de acceso
    "wsfunction": "core_user_create_users", # Función para crear usuarios
    "moodlewsrestformat": "json", # Formato de respuesta
    # Datos del nuevo usuario
    "users[0][username]": "python@example.com",
    "users[0][password]": "Password123*",
    "users[0][firstname]": "python",
    "users[0][lastname]": "request",
    "users[0][email]": "python@example.com",
    "users[0][auth]": "manual"
}
# La API de Moodle requiere que los datos se envíen como formulario
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

response = requests.post(url, data=payload, headers=headers)

print(response.json())
