# DevOps Flask PostgreSQL

Proyecto práctico de DevOps desarrollado con Flask, PostgreSQL, pgAdmin, Docker Compose, GitHub Actions y GitHub Container Registry.

## Descripción

La aplicación permite visualizar información general del sistema y consultar productos almacenados en una base de datos PostgreSQL.

La ruta principal muestra:

* Nombre de la aplicación.
* Versión actual.
* Estado de conexión con PostgreSQL.

Además, cuenta con una ruta para listar los productos registrados en la base de datos.

## Tecnologías utilizadas

* Python
* Flask
* PostgreSQL
* pgAdmin
* Docker
* Docker Compose
* GitHub Actions
* GitHub Container Registry

## Estructura del proyecto

```text
devops-flask-postgres/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── VERSION
├── README.md
│
├── db/
│   └── init.sql
│
└── .github/
    └── workflows/
        └── docker-ghcr.yml
```

## Variables de entorno

La aplicación utiliza variables de entorno configuradas desde Docker Compose:

```text
APP_NAME
APP_VERSION
DB_HOST
DB_PORT
DB_NAME
DB_USER
DB_PASSWORD
```

Estas variables permiten configurar el nombre de la aplicación, la versión y los datos de conexión a PostgreSQL.

## Base de datos

Se crea una base de datos PostgreSQL con una tabla llamada `productos`.

La tabla contiene los siguientes campos:

* `id`
* `nombre`
* `precio`
* `stock`

El archivo `db/init.sql` crea la tabla e inserta cinco registros iniciales.

## Ejecución del proyecto

Para levantar los servicios, ejecutar:

```bash
docker compose up --build
```

El proyecto levanta tres servicios:

* Aplicación Flask
* PostgreSQL
* pgAdmin

## Rutas disponibles

Ruta principal:

```text
http://localhost:5000
```

Ruta para visualizar productos:

```text
http://localhost:5000/productos
```

pgAdmin:

```text
http://localhost:8080
```

## Acceso a pgAdmin

Credenciales de acceso:

```text
Email: admin@admin.com
Password: admin123
```

Datos para registrar el servidor PostgreSQL en pgAdmin:

```text
Host: postgres
Port: 5432
Database: devops_db
Username: devops_user
Password: devops_pass
```

## Docker

El proyecto incluye un `Dockerfile` para construir la imagen de la aplicación Flask.

También se utiliza `docker-compose.yml` para levantar todos los servicios necesarios y configurar la persistencia de datos mediante volúmenes.

## GitHub Actions

El proyecto incluye un workflow en:

```text
.github/workflows/docker-ghcr.yml
```

Este workflow se ejecuta automáticamente al realizar un `push` sobre la rama `main`.

El proceso realiza las siguientes acciones:

* Construye la imagen Docker.
* Inicia sesión en GitHub Container Registry.
* Publica la imagen en GHCR.
* Genera tags de versión y `latest`.

## Versionamiento

La versión inicial del proyecto es:

```text
1.0.0
```

Posteriormente se actualiza a:

```text
2.0.0
```

El archivo `VERSION` se utiliza para definir la versión publicada de la imagen Docker.

## Autor

Andrew Carrera
