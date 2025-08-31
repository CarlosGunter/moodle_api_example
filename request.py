import requests
import json

# URL de la API de Moodle
moodle_url = "http://localhost:8085/webservice/rest/server.php"

# Credenciales de autenticación
token = "c40730522c735d9bfd44fc247fa9223c"
username = "user"

# Datos del nuevo usuario
new_user = {
    "username": "testAPI",
    "password": "newpassword",
    "firstname": "API",
    "lastname": "User",
    "email": "api_user@example.com"
}

# Parámetros de la solicitud
params = {
    "wstoken": token,
    "wsfunction": "core_user_create_users",
    "moodlewsrestformat": "json"
}

# Datos de la solicitud
data = {
    "users [0]": json.dumps(new_user)
}

# Enviar la solicitud
response = requests.post(moodle_url, params=params, data=data)

# Verificar la respuesta
print("Respuesta de Moodle:", response.json())