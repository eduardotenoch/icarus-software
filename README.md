Aquí te dejo las instrucciones detalladas para descargar un repositorio de Python desde GitHub, configurarlo con una base de datos MySQL y ejecutarlo. También te explico cómo probar los endpoints personalizados usando Postman o Swagger.

1. Crear una carpeta para el proyecto
   Crea una carpeta donde quieras clonar el repositorio. Puedes nombrarla como el repositorio.

En la terminal, ejecuta:

bash
Copiar código
mkdir icarus-software
cd icarus-software 2. Clonar el repositorio de GitHub
Clona el repositorio desde GitHub usando el comando git clone:

bash
Copiar código
git clone https://github.com/TU_USUARIO/icarus-software.git
Cambia el nombre de TU_USUARIO por tu nombre de usuario en GitHub. Esto descargará todos los archivos del proyecto en la carpeta.

Ve al directorio del proyecto:

bash
Copiar código
cd icarus-software 3. Configurar la base de datos MySQL
Crea una base de datos en MySQL. Asegúrate de que el nombre sea el que especifica tu archivo de configuración.

En MySQL, crea la base de datos:

sql
Copiar código
CREATE DATABASE icarus_db; 4. Configurar la conexión a la base de datos
Edita el archivo de configuración settings.py que se encuentra en la carpeta icarus/settings.py. Asegúrate de que la sección DATABASES esté configurada correctamente:

python
Copiar código
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.mysql',
'NAME': 'icarus_db', # Asegúrate de que esta base de datos exista
'USER': 'root', # Asegúrate de que este usuario sea correcto
'PASSWORD': 'Naruto221101', # La contraseña del usuario root
'HOST': 'localhost', # O usa '127.0.0.1'
'PORT': '3306', # Asegúrate de que el puerto sea correcto
}
} 5. Instalar las dependencias
Instala las dependencias del proyecto. Si hay un archivo requirements.txt en el repositorio, usa el siguiente comando para instalar los paquetes necesarios:

bash
Copiar código
pip install -r requirements.txt 6. Aplicar las migraciones a la base de datos
Aplica las migraciones para crear las tablas en la base de datos MySQL.

Si estás en Linux o macOS, ejecuta:

bash
Copiar código
python3 manage.py makemigrations
python3 manage.py migrate
Si estás en Windows, ejecuta:

bash
Copiar código
python manage.py makemigrations
python manage.py migrate 7. Ejecutar el servidor
Una vez finalizado, inicia el servidor de desarrollo de Django.

En Linux o macOS, ejecuta:

bash
Copiar código
python3 manage.py runserver
En Windows, ejecuta:

bash
Copiar código
python manage.py runserver
Esto iniciará el servidor en http://127.0.0.1:8000.

8. Probar los endpoints personalizados
   Ahora puedes probar los endpoints personalizados de dos formas:

Postman: Abre Postman y envía solicitudes a los endpoints del servidor. Usa http://localhost:8000/tu_endpoint/ como URL base.

Swagger: Si tienes configurado Swagger en tu proyecto, puedes ir a http://127.0.0.1:8000/swagger/ para probar y documentar los endpoints desde la interfaz de Swagger.

¡Con esto deberías tener el proyecto corriendo y los endpoints listos para probar!
