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

## URLs importantes
- **Admin:** `https://tudominio.pythonanywhere.com/admin/`
- **Noticias:** `https://tudominio.pythonanywhere.com/noticias/`
- **Recursos:** `https://tudominio.pythonanywhere.com/recursos/`

## Notas sobre imágenes
- Los campos de imagen (`news.image` y `resource.image`) usan **URLs externas**
- Puedes hospedar imágenes en servicios como:
  - **Cloudinary** (con integración en el proyecto)
  - **Imgur**
  - **GitHub** (raw content)
  - Tu propio servidor de imágenes

## Mantenimiento
- Acceso al admin para gestionar noticias y recursos
- Los scripts `check_images.py` y `update_image.py` son solo para desarrollo local y no se necesitan en producción

## Troubleshooting
- Si hay errores de permisos, asegúrate de que el usuario de PythonAnywhere tiene acceso al directorio
- Para ver logs: Ve a **Web** → **Log files**
- Para recargar después de cambios: Presiona **Reload** en **Web**
