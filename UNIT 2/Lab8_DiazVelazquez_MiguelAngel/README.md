# Lab 8 - MVC Login y Registro

## Organización de los cinco archivos del profesor

1. `database/conexion.py` — conexión a MySQL.
2. `models/user_model.py` — consultas de registro y acceso a usuarios.
3. `views/login_view.py` — pantalla principal de inicio de sesión.
4. `views/register_view.py` — ventana de registro.
5. `controllers/authentication.py` — coordina vistas y modelo.

`main.py` inicia la aplicación y `database/login_mvc.sql` prepara la base de datos.

## Pasos para ejecutar

1. Instala y enciende MySQL (por ejemplo, desde XAMPP si lo utilizas).
2. Ejecuta `database/login_mvc.sql` desde MySQL Workbench o phpMyAdmin (pestaña SQL).
3. En `database/conexion.py` modifica `usuario` y `password` si tu MySQL usa otras credenciales.
4. Abre una terminal dentro de la carpeta principal y ejecuta:

   ```bash
   python -m pip install -r requirements.txt
   python main.py
   ```

5. Presiona **Registrarme**, crea una cuenta y después ingresa con el mismo correo y contraseña.

## Pruebas sugeridas

- Campos vacíos en ambas pantallas.
- Correos inválidos.
- Contraseñas que no coinciden.
- Registro correcto.
- Correo duplicado.
- Acceso con credenciales correctas e incorrectas.
- Cancelar o cerrar el registro y volver a abrirlo.

## Nota sobre seguridad

Este laboratorio **conserva el comportamiento SQL original del profesor**, que guarda contraseñas sin cifrar. Solo debe usarse como práctica local y con contraseñas de prueba, nunca con contraseñas reales. Para una aplicación de verdad usa hash de contraseñas (por ejemplo, Argon2 o bcrypt).

## Estado de comprobación

Se verificó la sintaxis/importaciones de los módulos mediante compilación. La conexión a MySQL y la interfaz gráfica requieren ejecutarse en un equipo con MySQL y escritorio disponibles, por lo que deben probarse localmente.
