Instrucciones para Descargar y Configurar un Repositorio de Python

1. Crear carpeta del proyecto:
   mkdir icarus-software
   cd icarus-software

2. Clonar el repositorio:
   git clone https://github.com/TU_USUARIO/icarus-software.git
   cd icarus-software

3. Configurar la base de datos MySQL:
   sql
   CREATE DATABASE icarus_db;

4. Configurar la conexión: Edita settings.py y asegúrate de que DATABASES esté configurado correctamente.
5. Instalar dependencias:
   pip install -r requirements.txt

6. Aplicar migraciones:
   python3 manage.py makemigrations
   python3 manage.py migrate

7. Ejecutar el servidor:
   python3 manage.py runserver

8.Probar endpoints:
Postman: Usa http://localhost:8000/tu_endpoint/.
Swagger: Accede a http://127.0.0.1:8000/swagger/.

¡Listo! Tu proyecto debería estar corriendo y los endpoints listos para probar.
