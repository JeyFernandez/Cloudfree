# Guía de Despliegue en PythonAnywhere

## Requisitos previos
- Cuenta en [PythonAnywhere.com](https://www.pythonanywhere.com/)
- Acceso a la línea de comandos (Bash console)

## Pasos de instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/tuusuario/CloudFree.git
cd CloudFree
```

### 2. Crear entorno virtual
```bash
python3.10 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Nota:** Si encuentras errores con Pillow, puedes omitirlo temporalmente:
```bash
pip install -r requirements.txt --ignore-installed Pillow
```
```

### 4. Configurar variables de entorno
En **PythonAnywhere**, ve a **Account → Web → Environment variables** y añade:

```env
DJANGO_SETTINGS_MODULE=config.settings
SECRET_KEY=tu-clave-secreta-aqui
DEBUG=False
ALLOWED_HOSTS=tudominio.pythonanywhere.com
```

**Importante:** Genera una `SECRET_KEY` segura ejecutando:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 5. Recolectar archivos estáticos
```bash
python manage.py collectstatic --noinput
```

### 6. Migrar la base de datos
```bash
python manage.py migrate
```

### 7. Crear superusuario (admin)
```bash
python manage.py createsuperuser
```

### 8. Configurar aplicación web en PythonAnywhere
1. Ve a **Web** → **Add a new web app**
2. Elige **Manual configuration** → **Python 3.10**
3. En **Code**, apunta a tu carpeta del proyecto
4. En **WSGI configuration file**, edita el archivo y asegúrate de que apunta correctamente:
#### Opción A: Desde el Dashboard (Recomendado)
1. Ve a **Web** → **Add a new web app**
2. Elige **Manual configuration** → **Python 3.10**
3. En **Source code**, apunta a: `/home/tuusuario/CloudFree`
4. En **Working directory**, apunta a: `/home/tuusuario/CloudFree`
5. En **Virtualenv**, apunta a: `/home/tuusuario/CloudFree/venv`
6. En **WSGI configuration file**, edita el archivo y reemplaza todo con:

```python
import os
import sys

path = '/home/tuusuario/CloudFree'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

5. En **Virtualenv**, apunta a: `/home/tuusuario/CloudFree/venv`
6. Recarga la aplicación web
7. Recarga la aplicación web presionando el botón **Reload**

#### Opción B: Desde la consola Bash
```bash
# Ir a la carpeta de configuración web
cd /var/www/

# O si es usando dominios propios:
cd /var/www/tudominio.pythonanywhere.com/
```

## URLs importantes
## URLs importantes después del despliegue
- **Admin:** `https://tudominio.pythonanywhere.com/admin/`
- **Noticias:** `https://tudominio.pythonanywhere.com/noticias/`
- **Recursos:** `https://tudominio.pythonanywhere.com/recursos/`
- **Feed JSON:** `https://tudominio.pythonanywhere.com/noticias/feed.json`

## Notas sobre imágenes
- Los campos de imagen (`news.image` y `resource.image`) usan **URLs externas**
- Puedes hospedar imágenes en servicios como:
  - **Cloudinary** (con integración en el proyecto)
  - **Imgur**
  - **GitHub** (raw content)
  - Tu propio servidor de imágenes
- No se almacenan archivos en el servidor
- Puedes hospedar imágenes en servicios como:
  - **Imgur** (fácil, sin registro)
  - **Cloudinary** (con integración en el proyecto)
  - **GitHub** (usando raw content)
  - Tu propio servidor de imágenes

## Mantenimiento
- Acceso al admin para gestionar noticias y recursos
- Los scripts `check_images.py` y `update_image.py` son solo para desarrollo local y no se necesitan en producción
## Mantenimiento después del despliegue

### Ver logs
En PythonAnywhere:
- **Web** → **Log files** → Ver el archivo `error.log`

### Actualizar código
```bash
cd ~/CloudFree
git pull
python manage.py migrate
python manage.py collectstatic --noinput
# Luego en dashboard: Reload
```

### Gestionar contenido
- Accede a `https://tudominio.pythonanywhere.com/admin/`
- Usuario y contraseña: los que creaste con `createsuperuser`

## Troubleshooting

### Error: "ModuleNotFoundError: No module named 'django'"
**Solución:** Asegúrate de que el virtualenv está correctamente configurado en el dashboard de PythonAnywhere.

### Error: "No module named 'whitenoise'"
**Solución:** Ejecuta `pip install -r requirements.txt` nuevamente en la consola bash de PythonAnywhere.

### Error: "Secret key is exposed"
**Solución:** Ve a `config/settings.py` y verifica que `SECRET_KEY` use variables de entorno, no un string hardcodeado.

### Imágenes no carga
**Solución:** Verifica que:
1. Las URLs en el admin son válidas (comienzan con https://)
2. Los dominios existen y están activos
3. No hay errores CORS en la consola del navegador

### Database locked
**Solución:** SQLite puede tener problemas en producción. Considera migrar a PostgreSQL:
```bash
# En el dashboard, activa PostgreSQL en Account → Databases
# Actualiza DATABASES en config/settings.py:
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'tuusuario$database_name',
    'USER': 'tuusuario',
    'PASSWORD': 'tu_contraseña',
    'HOST': 'tuusuario.postgres.pythonanywhere-services.com',
    'PORT': 5432,
  }
}
# Ejecuta migraciones nuevamente
```

## Preguntas frecuentes

**P: ¿Cómo cambio el dominio?**
R: En PythonAnywhere dashboard → Web → Principal web app, ajusta el dominio.

**P: ¿Cómo cargo más noticias o recursos?**
R: Accede al admin `/admin/` y usa el formulario para agregarlos.

**P: ¿Puedo usar base de datos MySQL?**
R: Sí, pero SQLite funciona bien para proyectos pequeños. Si necesitas cambiar, ve a Account → Databases.

**P: ¿Cómo configuro HTTPS?**
R: PythonAnywhere proporciona certificados gratuitos. Ve a Web → Security y actívalo.
- Si hay errores de permisos, asegúrate de que el usuario de PythonAnywhere tiene acceso al directorio
- Para ver logs: Ve a **Web** → **Log files**
- Para recargar después de cambios: Presiona **Reload** en **Web**
