# Backend - Mini Core Comisiones
---
Link al video:  https://youtu.be/srxaciksG_g

---

repositorio frontend react: https://github.com/der-matt02/mini-core-frontend-comisiones-fastapi-react.git

---
## Descripción

Este proyecto corresponde al backend de una aplicación para el cálculo de comisiones de ventas basado en un conjunto de reglas, fechas y vendedores registrados. La aplicación está desarrollada con FastAPI y expone una API RESTful que permite registrar ventas, gestionar reglas de comisión, y obtener cálculos de comisión por rango de fechas para un vendedor específico.

El sistema está orientado a ofrecer una solución modular y extensible para negocios que requieren evaluar comisiones por desempeño individual, de manera automatizada y conectada a un frontend externo.

## Características

- Arquitectura modular basada en FastAPI.
- Separación clara de capas: routers, servicios, repositorios, esquemas y modelos.
- Cálculo de comisiones por rango de fechas, aplicando reglas configurables según montos.
- Uso de base de datos MySQL (adaptable a SQLite para pruebas locales).
- Conexión a base de datos mediante SQLAlchemy y manejo de entorno con `pydantic-settings`.
- Documentación automática con Swagger UI (`/docs`).
- Soporte CORS para conexión con frontend desplegado por separado.
- Preparado para despliegue en Render con variables de entorno configurables.

## Recursos y Documentación Adicional

A continuación se listan recursos confiables y gratuitos para aprender FastAPI, Python, MVC, modularidad, y conceptos clave como CORS, WSGI y ASGI.

---

### 📘 Documentación oficial y guías de FastAPI

- [Sitio oficial de FastAPI](https://fastapi.tiangolo.com/)
- [Guía para aprender FastAPI paso a paso](https://fastapi.tiangolo.com/learn/)
- [Estructura modular para proyectos grandes en FastAPI](https://fastapi.tiangolo.com/tutorial/bigger-applications/)
- [Referencia rápida de FastAPI](https://fastapi.tiangolo.com/reference/)

---


## Tecnologías y Versiones

A continuación se listan las tecnologías y librerías utilizadas en el backend, junto con sus versiones específicas:
## Recursos adicionales

- **How FastAPI Handles Requests Behind the Scenes**  
  https://www.youtube.com/watch?v=tGD3653BrZ8

- **WSGI vs ASGI, Uvicorn, Daphne, Hypercorn, uWSGI Simplified! #3**  
  https://www.youtube.com/watch?v=i8soiRGK6Dk

- **Miniconda / Conda for Python – Environment and Package Management**  
  https://www.youtube.com/watch?v=hDGSZMLS5F4&t=67s

- **Anaconda Beginners Guide for Linux and Windows**  
  https://www.youtube.com/watch?v=MUZtVEDKXsk

- **Object Oriented Programming with Python – Full Course for Beginners**  
  https://www.youtube.com/watch?v=Ej_02ICOIgs

- **WSGI vs ASGI for Python Web Development**  
  https://medium.com/@commbigo/wsgi-vs-asgi-for-python-web-development-9d9a3c426aa9

- **Learn Python 3 – Codecademy**  
  https://www.codecademy.com/learn/learn-python-3

- **Aprende a programar en Python desde cero – Curso completo gratis (FreeCodeCamp)**  
  https://www.freecodecamp.org/espanol/news/aprende-a-programar-en-python-desde-cero-curso-completo-gratis/

- **MySQL SQL Tutorial – W3Schools**  
  https://www.w3schools.com/mysql/mysql_sql.asp

- **Documentación oficial de FastAPI**  
  https://fastapi.tiangolo.com/

- **Guía “Learn” de FastAPI**  
  https://fastapi.tiangolo.com/learn/
  
> Estos recursos te van a ayudar a comprender mejor los conceptos utilizados en el proyecto, como FastAPI, ASGI, WSGI, Python, SQL y arquitectura modular.  
>  
> Cabe destacar que **estos no son mis videos ni artículos**, solo son enlaces recomendados por su utilidad educativa.

### Lenguaje y framework

- Python 3.11+
- FastAPI 0.115.13
- Uvicorn 0.34.3 (servidor ASGI)

### Conectividad y ORM

- SQLAlchemy 2.0.41
- PyMySQL 1.1.1

### Configuración y validación

- pydantic 2.11.7
- pydantic-settings 2.10.0
- python-dotenv 1.1.0

## Librerías Necesarias

Estas son las dependencias que requiere el backend, junto con las versiones exactas empleadas en el entorno de desarrollo. Todas ellas se encuentran en el archivo `requirements.txt`.

| Paquete              | Versión |
|----------------------|---------|
| alembic              | 1.16.2  |
| annotated-types      | 0.7.0   |
| anyio                | 4.9.0   |
| click                | 8.2.1   |
| fastapi              | 0.115.13|
| greenlet             | 3.2.3   |
| h11                  | 0.16.0  |
| idna                 | 3.10    |
| Mako                 | 1.3.10  |
| MarkupSafe           | 3.0.2   |
| pydantic             | 2.11.7  |
| pydantic-core        | 2.33.2  |
| pydantic-settings    | 2.10.0  |
| PyMySQL              | 1.1.1   |
| python-dotenv        | 1.1.0   |
| sniffio              | 1.3.1   |
| SQLAlchemy           | 2.0.41  |
| starlette            | 0.46.2  |
| typing-inspection    | 0.4.1   |
| typing_extensions    | 4.14.0  |
| uvicorn[standard]    | 0.34.3  |

> Nota: Si optas por usar SQLite en vez de MySQL, no necesitas `PyMySQL`; en su lugar puedes instalar `aiosqlite` si trabajas con SQLAlchemy asíncrono.

---

## Base de Datos

El backend está preparado para funcionar con **MySQL**
### Conexión MySQL

Variables de entorno necesarias:

| Variable      | Descripción                          |
|---------------|--------------------------------------|
| `DB_USER`     | Usuario de la base de datos          |
| `DB_PASSWORD` | Contraseña del usuario               |
| `DB_HOST`     | Hostname o IP del servidor MySQL     |
| `DB_PORT`     | Puerto (por defecto 3306 en MySQL)   |
| `DB_NAME`     | Nombre de la base de datos           |

La cadena de conexión (`SQLALCHEMY_DATABASE_URL`) se construye dinámicamente en `app/core/config.py`.

### Opción alternativa: SQLite local

Para desarrollo rápido se puede usar un archivo `database.db` en la raíz del proyecto. En tal caso, basta con definir `SQLITE_PATH` en el archivo `.env` y ajustar la URL a `sqlite:///ruta_al_archivo`.

---

## Query de Creación de la BD

A continuación se proporciona el script SQL completo para crear la base de datos y poblarla con datos de ejemplo.

```sql
-- Crear base de datos
CREATE DATABASE mini_core_comisiones_db;
USE mini_core_comisiones_db;

-- Tabla vendedores
CREATE TABLE vendedores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL
);

-- Tabla ventas
CREATE TABLE ventas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    vendedor_id INT NOT NULL,
    fecha DATE NOT NULL,
    monto DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (vendedor_id) REFERENCES vendedores(id)
);

-- Tabla reglas
CREATE TABLE reglas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    monto_min DECIMAL(10,2) NOT NULL,
    monto_max DECIMAL(10,2),
    porcentaje DECIMAL(5,2) NOT NULL
);

-- Reglas de ejemplo
INSERT INTO reglas (monto_min, monto_max, porcentaje) VALUES
(0.00, 500.00, 5.00),        -- 5 % para ventas hasta $500
(500.01, 1000.00, 10.00),    -- 10 % para ventas entre $500.01 y $1000
(1000.01, NULL, 15.00);      -- 15 % para ventas mayores a $1000

-- Vendedores de ejemplo
INSERT INTO vendedores (nombre, apellido) VALUES
('Carlos', 'Perez'),
('Ana', 'Martinez'),
('Luis', 'Ramirez'),
('María', 'Lopez'),
('Jorge', 'Sanchez'),
('Lucía', 'Vera'),
('Andrés', 'Mora'),
('Sofía', 'Reyes'),
('Mateo', 'Torres'),
('Valentina', 'Flores');

-- Ventas de ejemplo
INSERT INTO ventas (vendedor_id, fecha, monto) VALUES
(1, '2024-01-10', 300.00),
(1, '2024-02-15', 350.00),
(1, '2024-03-20', 400.00),
(2, '2024-01-25', 500.00),
(2, '2024-03-05', 250.00),
(2, '2024-04-10', 700.00),
(3, '2024-02-12', 600.00),
(3, '2024-03-18', 800.00),
(3, '2024-05-22', 450.00),
(4, '2024-01-08', 200.00),
(4, '2024-02-20', 300.00),
(4, '2024-06-14', 100.00),
(5, '2024-03-03', 500.00),
(5, '2024-04-07', 200.00),
(5, '2024-06-29', 650.00),
(6, '2024-02-01', 700.00),
(6, '2024-05-05', 550.00),
(6, '2024-07-15', 800.00),
(7, '2024-04-12', 400.00),
(7, '2024-06-10', 600.00),
(7, '2024-08-22', 900.00),
(8, '2024-05-30', 300.00),
(8, '2024-07-18', 500.00),
(8, '2024-09-04', 250.00),
(9, '2024-06-11', 1000.00),
(9, '2024-07-27', 400.00),
(9, '2024-08-19', 200.00),
(10, '2024-03-06', 350.00),
(10, '2024-06-21', 750.00),
(10, '2024-09-15', 950.00);

-- Verificar tablas
SELECT * FROM vendedores;
SELECT * FROM ventas;

```
## Instalación Local

Para ejecutar este proyecto en tu máquina local se recomienda utilizar Miniconda para aislar las dependencias. A continuación se detallan los pasos completos para preparar el entorno de desarrollo.

### Crear entorno con Miniconda

Asegúrate de tener instalado Miniconda o Anaconda. Si no lo tienes, descárgalo desde:

https://docs.conda.io/en/latest/miniconda.html

Una vez instalado, abre una terminal y navega a la carpeta raíz del proyecto (donde se encuentra el archivo `requirements.txt`).

Crea un entorno virtual llamado `core-backend-env` con Python 3.11:

```bash
conda create -n core-backend-env python=3.11
```

Activa el entorno:

```bash
conda activate core-backend-env
```

Comprueba la versión de Python (opcional):

```bash
python --version
```

### Instalar dependencias con pip

Instala todas las librerías del proyecto mediante el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

Esto instalará FastAPI, SQLAlchemy, PyMySQL, Uvicorn y el resto de dependencias necesarias.

### (Opcional) Instalar algunas dependencias con conda

Si prefieres instalar ciertos paquetes desde Conda Forge, ejecuta:

```bash
conda install -c conda-forge fastapi uvicorn sqlalchemy pymysql pydantic
```

Posteriormente, para igualar las versiones exactas requeridas, ejecuta de nuevo:

```bash
pip install -r requirements.txt
```

### Ejecutar el servidor

Configura el archivo `.env` con las variables necesarias y arranca la API localmente:

```bash
uvicorn app.main:app --reload --port 8000
```

Accede a la documentación interactiva en:

http://localhost:8000/docs

## Configuración del Archivo .env

En la raíz del proyecto backend, se requiere un archivo `.env` para definir las variables de entorno necesarias.  
Este archivo **no debe subirse a GitHub** (ya está incluido en `.gitignore`).

Ejemplo de contenido del archivo `.env`:

```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=mini_core_comisiones_db
DB_USER=tu_usuario_mysql
DB_PASSWORD=tu_contraseña_mysql
```

Asegúrate de reemplazar `tu_usuario_mysql` y `tu_contraseña_mysql` por tus credenciales locales.

---

## Estructura del Proyecto

El backend está organizado según una arquitectura basada en FastAPI, con módulos separados para lógica de negocio, rutas y acceso a datos.

```
CoreBackend/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── comision_router.py
│   │       ├── regla_router.py
│   │       ├── vendedor_router.py
│   │       └── venta_router.py
│   ├── core/
│   │   ├── config.py
│   │   └── database.py
│   ├── crud/
│   │   ├── crud_comisiones.py
│   │   ├── crud_reglas.py
│   │   ├── crud_vendedores.py
│   │   └── crud_ventas.py
│   ├── models/
│   │   ├── regla.py
│   │   ├── vendedor.py
│   │   └── venta.py
│   ├── schemas/
│   │   ├── regla_schema.py
│   │   ├── vendedor_schema.py
│   │   └── venta_schema.py
│   └── main.py
├── .env
├── requirements.txt
└── README.md
```

---

## Qué guarda cada carpeta

- `app/api/v1/`: Define las rutas del API REST para cada recurso (vendedores, ventas, reglas, comisiones).
- `app/core/`: Configuración general del proyecto. Incluye el archivo `.env` y la conexión a la base de datos.
- `app/crud/`: Lógica de acceso a datos. Aquí se encuentran las funciones que interactúan directamente con la base de datos.
- `app/models/`: Modelos ORM que definen la estructura de las tablas.
- `app/schemas/`: Esquemas Pydantic utilizados para validación y serialización de datos.
- `app/main.py`: Punto de entrada de la aplicación FastAPI.
## Qué hace cada archivo principal

A continuación se describen las funciones clave de los archivos principales del backend:

- `main.py`: Inicializa la aplicación FastAPI, incluye las rutas y lanza el servidor.
- `config.py`: Carga y gestiona las variables de entorno definidas en el archivo `.env`.
- `database.py`: Configura la conexión a MySQL mediante SQLAlchemy y define la sesión de base de datos (`SessionLocal`).
- `regla.py`, `vendedor.py`, `venta.py`: Definen los modelos de datos ORM que representan las tablas en la base de datos.
- `*_schema.py`: Esquemas de validación con Pydantic que se usan para validar la entrada y salida de datos.
- `crud_*.py`: Contienen la lógica de negocio relacionada con cada modelo (crear, leer, actualizar, borrar, calcular).
- `*_router.py`: Rutas RESTful para exponer la funcionalidad del backend a través de la API.

---

## Uso

1. Asegúrate de tener MySQL ejecutándose con la base de datos creada correctamente y los datos precargados.
2. Llena tu archivo `.env` con las credenciales correctas.
3. Activa el entorno virtual de conda:

```bash
conda activate core-backend-env
```

4. Ejecuta el servidor FastAPI:

```bash
uvicorn app.main:app --reload --port 8000
```

5. Accede a la documentación Swagger en:

[http://localhost:8000/docs](http://localhost:8000/docs)

---

## Endpoints Disponibles

Una vez levantado el servidor, estos son algunos de los endpoints accesibles:

### Vendedores
- `GET /api/v1/vendedores/`  
  Lista todos los vendedores.

- `POST /api/v1/vendedores/`  
  Crea un nuevo vendedor.

### Ventas
- `GET /api/v1/ventas/`  
  Lista todas las ventas.

- `POST /api/v1/ventas/`  
  Crea una nueva venta.

### Reglas
- `GET /api/v1/reglas/`  
  Lista todas las reglas de comisión.

- `POST /api/v1/reglas/`  
  Crea una nueva regla.

### Comisiones
- `GET /api/v1/comisiones/?fecha_inicio=YYYY-MM-DD&fecha_fin=YYYY-MM-DD`  
  Calcula las comisiones por vendedor dentro del rango de fechas especificado.

Todos los endpoints devuelven datos en formato JSON.

## Ejemplo de Flujo

A continuación se muestra un flujo típico de uso de la API. Los ejemplos se asumen en `localhost:8000` usando las rutas de `api/v1`.

1. Crear un vendedor  
   `POST /api/v1/vendedores/`  
   ```json
   {
     "nombre": "Juan",
     "apellido": "García"
   }
   ```

2. Registrar una venta  
   `POST /api/v1/ventas/`  
   ```json
   {
     "vendedor_id": 1,
     "fecha": "2024-07-15",
     "monto": 750.00
   }
   ```

3. Consultar la comisión del vendedor entre dos fechas  
   `GET /api/v1/comisiones/?vendedor_id=1&fecha_inicio=2024-07-01&fecha_fin=2024-07-31`

4. El backend devuelve algo como:  
   ```json
   {
     "vendedor_id": 1,
     "total_ventas": 750.00,
     "porcentaje_aplicado": 10.0,
     "comision": 75.00
   }
   ```

---

## Contacto

Para consultas, sugerencias o reportes de errores, puedes contactar al desarrollador:

- **Autor**: Mathew Baquero
- **Correo electrónico**: dermatt02@gmail.com


**Suerte en tu aprendizaje y proyecto.**
