# Examen Práctico de DevOps - Flask + PostgreSQL + Docker + GHCR

Este proyecto cumple los parámetros del examen práctico de DevOps usando:

- Flask
- PostgreSQL
- pgAdmin
- Dockerfile
- Docker Compose
- GitHub Actions
- GitHub Container Registry, GHCR

## 1. Estructura del proyecto

```text
devops-flask-postgres/
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── VERSION
├── db/
│   └── init.sql
└── .github/
    └── workflows/
        └── docker-ghcr.yml
```

## 2. Variables de entorno usadas

La aplicación usa variables de entorno para configurar:

- Nombre de la aplicación: `APP_NAME`
- Versión de la aplicación: `APP_VERSION`
- Nombre de base de datos: `DB_NAME`
- Usuario de base de datos: `DB_USER`
- Contraseña de base de datos: `DB_PASSWORD`
- Host de base de datos: `DB_HOST`
- Puerto de base de datos: `DB_PORT`

Estas variables están configuradas en `docker-compose.yml`.

## 3. Levantar el proyecto

Ejecuta:

```bash
docker compose up --build
```

Servicios disponibles:

```text
Aplicación Flask: http://localhost:5000
Productos:        http://localhost:5000/productos
Productos JSON:   http://localhost:5000/api/productos
pgAdmin:          http://localhost:8080
PostgreSQL:       localhost:5432
```

## 4. Credenciales de pgAdmin

```text
Email: admin@admin.com
Password: admin123
```

## 5. Conexión desde pgAdmin hacia PostgreSQL

Dentro de pgAdmin, crea un nuevo servidor con estos datos:

```text
Name: Examen PostgreSQL
Host: postgres
Port: 5432
Maintenance database: devops_db
Username: devops_user
Password: devops_pass
```

## 6. Tabla productos

La tabla se crea automáticamente desde `db/init.sql`.

```sql
CREATE TABLE IF NOT EXISTS productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio NUMERIC(10, 2) NOT NULL,
    stock INTEGER NOT NULL
);
```

También se insertan cinco registros iniciales.

## 7. Dockerfile

El `Dockerfile` crea una imagen de la aplicación Flask usando Python 3.12 y Gunicorn.

## 8. Docker Compose

El archivo `docker-compose.yml` levanta tres servicios:

- `postgres`
- `pgadmin`
- `flask_app`

También configura volúmenes para persistencia:

- `postgres_data`
- `pgadmin_data`

## 9. GitHub Actions y GHCR

El workflow está en:

```text
.github/workflows/docker-ghcr.yml
```

Se ejecuta automáticamente cuando haces push sobre la rama `main`.

Publica la imagen en GHCR con estos tags:

```text
1.0.0
latest
```

El tag versionado sale del archivo:

```text
VERSION
```

## 10. Subir a GitHub

Crea un repositorio en GitHub, por ejemplo:

```text
devops-flask-postgres
```

Luego ejecuta:

```bash
git init
git add .
git commit -m "Versión inicial 1.0.0"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/devops-flask-postgres.git
git push -u origin main
```

## 11. Actualizar a versión 2.0.0

Edita el archivo `VERSION`:

```text
2.0.0
```

Edita también `docker-compose.yml` y cambia:

```yaml
APP_VERSION: "1.0.0"
image: devops-flask-postgres:1.0.0
```

por:

```yaml
APP_VERSION: "2.0.0"
image: devops-flask-postgres:2.0.0
```

Luego ejecuta:

```bash
git add .
git commit -m "Actualizar aplicación a versión 2.0.0"
git push origin main
```

GitHub Actions volverá a ejecutarse automáticamente y publicará:

```text
ghcr.io/TU_USUARIO/devops-flask-postgres:2.0.0
ghcr.io/TU_USUARIO/devops-flask-postgres:latest
```

## 12. Evidencias recomendadas para entregar

Toma capturas de:

1. `docker compose up --build` sin errores.
2. `docker ps` mostrando PostgreSQL, pgAdmin y Flask.
3. Ruta principal: `http://localhost:5000`.
4. Ruta de productos: `http://localhost:5000/productos`.
5. pgAdmin mostrando la tabla `productos`.
6. GitHub Actions ejecutado correctamente.
7. GHCR mostrando los tags `1.0.0`, `2.0.0` y `latest`.
