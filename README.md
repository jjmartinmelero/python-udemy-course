# 🐍 Python Learning Path

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0+-orange.svg)](https://www.mysql.com/)

Este repositorio contiene una colección completa de ejercicios y proyectos para aprender Python desde cero hasta un nivel avanzado.

## 📚 Contenido

1. **Fundamentos Básicos**
   - [Hola Mundo y POO Básica](01exercise/)
   - Variables y Tipos de Datos
   - Operadores
   - Estructuras de Control

2. **Estructuras de Datos y Control de Flujo**
   - [Variables y Tipos](02vars/)
   - [Operadores](03operators/)
   - [Sentencias de Control](04sentences/)
   - [Bucles](05loops/)
   - [Colecciones](06collections/)

3. **Funciones y Modularidad**
   - [Funciones](07functions/)
   - Módulos y Paquetes
   - Store App (Ejemplo Práctico)

4. **Programación Orientada a Objetos**
   - [Conceptos POO](08poo/)
   - Clases y Objetos
   - Herencia y Polimorfismo
   - Proyectos Prácticos:
     - Sistema de Empleados
     - PC World App

5. **Características Avanzadas**
   - [Programación Avanzada](09advanced/)
   - Lambda Functions
   - Map, Filter, Reduce
   - Generadores

6. **Manejo de Archivos y Datos**
   - [Operaciones con Archivos](10files/)
   - Proyecto Máquina de Snacks

7. **Bases de Datos**
   - [Conexión a MySQL](11database/)
   - CRUD Operations
   - Pool de Conexiones
   - Proyecto Cliente-DAO

## 🚀 Proyectos Destacados

### 💼 Sistema de Gestión de Empleados
- Gestión de empleados por departamento
- Clases: Employee, Company
- Métodos para añadir, listar y gestionar empleados

### 🖥️ PC World App
- Sistema de gestión de computadoras
- Componentes: Monitor, Teclado, Ratón
- Manejo de órdenes y productos

### 🍫 Máquina de Snacks
- Sistema completo de venta de snacks
- Persistencia en archivos
- Gestión de inventario y ventas

### 👥 Sistema de Gestión de Clientes
- CRUD completo con MySQL
- Patrón DAO
- Pool de conexiones
- Interfaz de consola interactiva

## 🛠️ Tecnologías Utilizadas

- **Python 3.11+**
- **MySQL 8.0+**
- **Bibliotecas:**
  - `mysql-connector-python`
  - `random`
  - `functools`

## 🗂️ Estructura del Proyecto

```
python-ex-1/
├── 01exercise/          # Introducción y POO básica
├── 02vars/             # Variables y tipos de datos
├── 03operators/        # Operadores y expresiones
├── 04sentences/        # Estructuras de control
├── 05loops/            # Bucles y repetición
├── 06collections/      # Colecciones de datos
├── 07functions/        # Funciones y modularidad
├── 08poo/             # Programación Orientada a Objetos
├── 09advanced/        # Características avanzadas
├── 10files/           # Manejo de archivos
└── 11database/        # Conexión a base de datos
```

## 📝 Patrones de Diseño Implementados

- **DAO (Data Access Object)**
  - Separación de lógica de acceso a datos
  - Implementado en el módulo de base de datos

- **Singleton**
  - Usado en la gestión de conexiones a base de datos
  - Pool de conexiones centralizado

- **MVC (Model-View-Controller)**
  - Separación de responsabilidades
  - Implementado en proyectos como PC World y Snack Machine

## 🌟 Características

- ✨ Código limpio y documentado
- 📚 Ejercicios progresivos
- 🎯 Proyectos prácticos reales
- 🔄 Patrones de diseño
- 🗃️ Gestión de datos
- �� Manejo de errores

## 🚀 Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/jjmartinmelero/python-ex-1.git
```

2. Crea un entorno virtual:
```bash
python -m venv .venv
```

3. Activa el entorno virtual:
```bash
# En Windows
.venv\Scripts\activate

# En Unix o MacOS
source .venv/bin/activate
```

4. Instala las dependencias:
```bash
pip install mysql-connector-python
```

## ⚙️ Configuración

Para los proyectos con base de datos, configura las credenciales en `database/project/conexion.py`:

```python
DATABASE = "tu_base_de_datos"
USERNAME = "tu_usuario"
PASSWORD = "tu_password"
HOST = "tu_host"
```

## 👨‍💻 Autor

- [@jjmartinmelero](https://github.com/jjmartinmelero)

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.
