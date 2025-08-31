# Consumo de API de Moodle

> [!IMPORTANT]
> Se están usando configuraciones no adecuadas para producción.

## Levantar Moodle con Docker
Comando para levantar Moodle con Docker:
```
$ docker-compose up -d
```

## Interacción con la instancia de Moodle

Con las configuraciones actuales, Moodle estará disponible en `http://localhost:8085` y `https://localhost:443`.

## API de Moodle

La API de Moodle se puede utilizar para interactuar con la plataforma de manera programática. La dirección de la API con las configuraciones actuales es `http://localhost:8085/moodle/webservice/rest/server.php` o `https://localhost:443/moodle/webservice/rest/server.php`.
