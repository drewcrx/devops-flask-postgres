import os
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "Examen DevOps Flask")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "devops_db")
DB_USER = os.getenv("DB_USER", "devops_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "devops_pass")


def get_connection():
    """Crea una conexión con PostgreSQL usando variables de entorno."""
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        cursor_factory=RealDictCursor
    )


def check_database_connection():
    """Verifica si Flask puede conectarse correctamente a PostgreSQL."""
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT 1 AS estado;")
        cur.fetchone()
        cur.close()
        conn.close()
        return True
    except Exception:
        return False


@app.route("/")
def home():
    db_connected = check_database_connection()
    status_text = "Conectado correctamente a PostgreSQL" if db_connected else "Error de conexión con PostgreSQL"
    status_class = "ok" if db_connected else "error"

    html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>{{ app_name }}</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f4f6f8;
                margin: 0;
                padding: 40px;
                color: #222;
            }
            .card {
                background: white;
                max-width: 720px;
                margin: auto;
                padding: 30px;
                border-radius: 16px;
                box-shadow: 0 8px 24px rgba(0,0,0,.12);
            }
            h1 {
                margin-top: 0;
                color: #1f2937;
            }
            .item {
                font-size: 18px;
                margin: 14px 0;
            }
            .ok {
                color: #15803d;
                font-weight: bold;
            }
            .error {
                color: #b91c1c;
                font-weight: bold;
            }
            a {
                display: inline-block;
                margin-top: 20px;
                background: #2563eb;
                color: white;
                padding: 12px 18px;
                border-radius: 10px;
                text-decoration: none;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Examen Práctico de DevOps</h1>
            <p class="item"><strong>Nombre de la aplicación:</strong> {{ app_name }}</p>
            <p class="item"><strong>Versión actual:</strong> {{ app_version }}</p>
            <p class="item"><strong>Estado de conexión con PostgreSQL:</strong>
                <span class="{{ status_class }}">{{ status_text }}</span>
            </p>
            <a href="/productos">Ver productos</a>
        </div>
    </body>
    </html>
    """
    return render_template_string(
        html,
        app_name=APP_NAME,
        app_version=APP_VERSION,
        status_text=status_text,
        status_class=status_class
    )


@app.route("/productos")
def productos():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT id, nombre, precio, stock
            FROM productos
            ORDER BY id;
        """)
        productos_db = cur.fetchall()
        cur.close()
        conn.close()

        html = """
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <title>Productos</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background: #f4f6f8;
                    margin: 0;
                    padding: 40px;
                    color: #222;
                }
                .card {
                    background: white;
                    max-width: 900px;
                    margin: auto;
                    padding: 30px;
                    border-radius: 16px;
                    box-shadow: 0 8px 24px rgba(0,0,0,.12);
                }
                table {
                    width: 100%;
                    border-collapse: collapse;
                    margin-top: 20px;
                }
                th, td {
                    border: 1px solid #ddd;
                    padding: 12px;
                    text-align: left;
                }
                th {
                    background: #2563eb;
                    color: white;
                }
                tr:nth-child(even) {
                    background: #f9fafb;
                }
                a {
                    display: inline-block;
                    margin-top: 20px;
                    background: #111827;
                    color: white;
                    padding: 12px 18px;
                    border-radius: 10px;
                    text-decoration: none;
                }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>Productos almacenados en PostgreSQL</h1>
                <table>
                    <thead>
                        <tr>
                            <th>Id</th>
                            <th>Nombre</th>
                            <th>Precio</th>
                            <th>Stock</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for producto in productos %}
                        <tr>
                            <td>{{ producto.id }}</td>
                            <td>{{ producto.nombre }}</td>
                            <td>${{ "%.2f"|format(producto.precio) }}</td>
                            <td>{{ producto.stock }}</td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
                <a href="/">Volver al inicio</a>
            </div>
        </body>
        </html>
        """
        return render_template_string(html, productos=productos_db)

    except Exception as error:
        return jsonify({
            "mensaje": "Error al consultar productos",
            "error": str(error)
        }), 500


@app.route("/api/productos")
def productos_json():
    """Ruta adicional en JSON para evidencias técnicas o pruebas con Postman."""
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT id, nombre, precio, stock
            FROM productos
            ORDER BY id;
        """)
        productos_db = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(productos_db)
    except Exception as error:
        return jsonify({
            "mensaje": "Error al consultar productos",
            "error": str(error)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
