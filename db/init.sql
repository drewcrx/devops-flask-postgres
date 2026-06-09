CREATE TABLE IF NOT EXISTS productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio NUMERIC(10, 2) NOT NULL,
    stock INTEGER NOT NULL
);

INSERT INTO productos (nombre, precio, stock)
VALUES
    ('Laptop Lenovo ThinkPad', 850.00, 10),
    ('Mouse Logitech Inalámbrico', 18.50, 35),
    ('Teclado Mecánico Redragon', 45.99, 20),
    ('Monitor Samsung 24 pulgadas', 165.75, 12),
    ('Disco SSD Kingston 1TB', 89.90, 25)
ON CONFLICT DO NOTHING;
