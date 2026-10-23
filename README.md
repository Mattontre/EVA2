# Seguridad LTDA — Sistema de Inventario

## 📋 Descripción del proyecto

Sistema web de gestión de inventario desarrollado con **Python y Django**, como parte del proyecto académico de Desarrollo Seguro (DevSecOps).

El objetivo es gestionar productos, controlar las entradas y salidas de bodega y mantener registros de auditoría de las operaciones realizadas.

## 🛠️ Tecnologías utilizadas

- Python
- Django
- HTML
- CSS
- SQLite
- Git y GitHub

## ✅ Funcionalidades implementadas

### Gestión de productos
- Listar productos.
- Crear productos.
- Editar productos.
- Eliminar productos.
- Validar los datos ingresados.
- Gestionar código, nombre, código de barras, grupo, subgrupo, ficha técnica, unidad de medida, cantidad y precio.

### Movimientos de bodega
- Registrar entradas de productos.
- Registrar salidas de productos.
- Actualizar automáticamente el stock.
- Evitar salidas superiores al stock disponible.
- Consultar el historial de movimientos.

### Seguridad y auditoría
- Inicio y cierre de sesión.
- Restricción de operaciones administrativas mediante grupos de usuarios.
- Registro de acciones sobre productos.
- Registro de movimientos de bodega.
- Almacenamiento de usuario, acción, detalle y fecha en los registros de auditoría.

## 🚀 Instalación y ejecución

### 1. Clonar el repositorio

Abre una terminal y ejecuta:

```bash
git clone https://github.com/Mattontre/EVA2.git
cd EVA2
```

### 2. Crear un entorno virtual

En Windows, ejecuta:

```powershell
python -m venv .venv
```

Activa el entorno virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

Si utilizas CMD en lugar de PowerShell:

```cmd
.venv\Scripts\activate.bat
```

### 3. Instalar Django

```bash
python -m pip install django
```

### 4. Crear la base de datos

Ejecuta las migraciones:

```bash
python manage.py migrate
```

### 5. Crear un usuario administrador

```bash
python manage.py createsuperuser
```

Django solicitará un nombre de usuario y una contraseña. Introduce las credenciales que quieras utilizar.

**Importante:** no se garantiza que exista una cuenta con usuario `admin` y contraseña `admin`. Cada integrante debe crear su propia cuenta si no existe una previamente configurada.

### 6. Iniciar el servidor

```bash
python manage.py runserver
```

Abre el sistema en el navegador:

- Aplicación: http://127.0.0.1:8000/
- Inicio de sesión: http://127.0.0.1:8000/login/
- Panel de administración: http://127.0.0.1:8000/admin/

## 🔑 Usuarios y permisos

### Administrador de Django

Para acceder al panel `/admin/`, utiliza el usuario y la contraseña creados mediante `createsuperuser`.

### Administrador de inventario

Para crear, editar o eliminar productos y registrar movimientos de bodega, el usuario debe pertenecer al grupo:

`AdministradoresInventario`

Para configurar este permiso:

1. Inicia sesión en el panel de administración de Django.
2. Entra en **Grupos**.
3. Crea el grupo `AdministradoresInventario` si todavía no existe.
4. Entra en **Usuarios**.
5. Selecciona el usuario autorizado y agrégalo al grupo.

El acceso al panel de administración y los permisos para gestionar el inventario son independientes.

## 📦 Estructura del proyecto

```text
EVA2/
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── inventario/
│   ├── migrations/
│   ├── static/
│   │   └── inventario/
│   │       └── estilos.css
│   ├── templates/
│   │   └── inventario/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
├── .gitignore
├── manage.py
└── README.md
```

## 🧪 Comprobar el funcionamiento

Para verificar la configuración de Django:

```bash
python manage.py check
```

Para ejecutar las pruebas automatizadas:

```bash
python manage.py test
```

Las pruebas deben revisarse y ampliarse a medida que se incorporen nuevas funcionalidades.

## 🔒 Buenas prácticas de seguridad

- No subir contraseñas, tokens ni claves privadas a GitHub.
- No subir archivos `.env` con información sensible.
- No subir la carpeta `.venv`.
- No subir la base de datos local `db.sqlite3`.
- Validar los datos recibidos en los formularios.
- Mantener protegidas las vistas que requieren permisos administrativos.
- Revisar los cambios antes de incorporarlos a la rama principal.
- No utilizar contraseñas débiles en entornos compartidos o de producción.

## 👨‍💻 Trabajo en equipo con Git

Antes de comenzar, actualiza tu copia local:

```bash
git pull origin main
```

Crea una rama para tu tarea:

```bash
git checkout -b feature/nombre-de-la-tarea
```

Después de realizar los cambios y comprobar que funcionan:

```bash
git add .
git commit -m "Descripción de los cambios"
git push origin feature/nombre-de-la-tarea
```

Luego, crea un **Pull Request** en GitHub para revisar los cambios antes de incorporarlos a `main`.

No trabajes directamente sobre `main` sin coordinarte con el equipo.

## 📌 Tareas pendientes

- Ampliar las pruebas automatizadas.
- Verificar los permisos y las validaciones de seguridad.
- Configurar SonarQube y SonarScanner.
- Analizar el código y corregir los problemas detectados.
- Documentar los resultados de las pruebas.
- Preparar evidencias para la evaluación de Desarrollo Seguro (DevSecOps).

## 📚 Información académica

**Proyecto:** ERP Seguridad LTDA — Módulo de Inventario  
**Asignatura:** Desarrollo Seguro (DevSecOps)  
**Repositorio GitHub:** https://github.com/Mattontre/EVA2