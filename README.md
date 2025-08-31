# Consumo de API de Moodle

> [!IMPORTANT]
> Se están usando configuraciones no adecuadas para producción.

## Levantar Moodle con Docker
Comando para levantar Moodle con Docker:
```bash
$ docker-compose up -d
```

## Interacción con la instancia de Moodle

Con las configuraciones actuales, Moodle estará disponible en:
- `http://localhost:8085`
- `https://localhost:443`.

## API de Moodle

La API de Moodle se puede utilizar para interactuar con la plataforma de manera programática.

La dirección de la API con las configuraciones actuales son
- `http://localhost:8085/moodle/webservice/rest/server.php`
- `https://localhost:443/moodle/webservice/rest/server.php`.

### Ejemplo de uso
Se debe seguir las instrucciones indicadas en la documentación que permite habilitar las llamadas a la API de Moodle. Disponible en: <https://supportus.moodle.com/support/solutions/articles/80001016973-using-the-web-services-application-programming-interface-api-in-moodle>

Despues de seguir las instrucciones, ejecutar archivo de python `request.py` usando los siguientes comandos:

Clona el repositorio
```bash
$ git clone https://github.com/CarlosGunter/moodle_api_example
cd moodle_api_example
```
Crear entorno virtual (opcional)
```bash
$ python -m venv venv
$ source venv/bin/activate
```
Instalar dependencias
```bash
$ pip install -r requirements.txt
```
Ejecutar script
```bash
$ python request.py
```