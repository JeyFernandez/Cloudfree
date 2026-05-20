# CloudFree - Guía Rápida para PythonAnywhere

## Cambios Importantes (Mayo 2026)

Este proyecto ha sido actualizado para:
- ✓ Usar URLs externas para imágenes (sin almacenamiento local)
- ✓ Configuración optimizada para PythonAnywhere
- ✓ WhiteNoise para servir archivos estáticos

## Versiones de Dependencias

### Para Desarrollo Local
Usa `requirements.txt` (con Django 6.0.5)

### Para PythonAnywhere  
Usa `requirements-prod.txt` (con Django 5.1.15 - compatible con PythonAnywhere)

**Razón:** PythonAnywhere no tiene acceso a todas las versiones más nuevas de PyPI.

## Pasos Rápidos en PythonAnywhere

### 1. Clonar
```bash
cd ~
git clone https://github.com/JeyFernandez/Cloudfree.git
cd Cloudfree
```

### 2. Setup
```bash
python3.10 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements-prod.txt
python manage.py migrate
python manage.py collectstatic --noinput
```

### 3. Variables de Entorno
En el dashboard → Account → Web → Environment variables:
```
DJANGO_SETTINGS_MODULE=config.settings
DEBUG=False
SECRET_KEY=genera_una_segura_aqui
ALLOWED_HOSTS=tudominio.pythonanywhere.com
```

### 4. WSGI Configuration
En Web → WSGI configuration, reemplaza todo con:
```python
import os
import sys

path = '/home/tuusuario/Cloudfree'
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### 5. Web App Settings
- **Source code:** `/home/tuusuario/Cloudfree`
- **Working directory:** `/home/tuusuario/Cloudfree`
- **Virtualenv:** `/home/tuusuario/Cloudfree/venv`

### 6. Reload
Presiona **Reload** en el dashboard.

### 7. Crear Admin
```bash
python manage.py createsuperuser
```

## URLs Después del Deploy

- Admin: `https://tudominio.pythonanywhere.com/admin/`
- Noticias: `https://tudominio.pythonanywhere.com/noticias/`
- Recursos: `https://tudominio.pythonanywhere.com/recursos/`
- Feed JSON: `https://tudominio.pythonanywhere.com/noticias/feed.json`

## Gestión de Imágenes

Las imágenes se manejan como URLs externas. Para agregar/editar:

1. Ve a `/admin/`
2. News o Resources
3. Pega una URL válida (https://...) en el campo `image`

Ejemplos de hosting:
- Imgur: `https://i.imgur.com/...`
- Cloudinary: Configurar en variables de entorno
- GitHub raw: `https://raw.githubusercontent.com/...`

## Troubleshooting

### Error: Django version not found
→ Usa `requirements-prod.txt` en lugar de `requirements.txt`

### Error: ModuleNotFoundError
→ Verifica que el virtualenv está configurado correctamente en Web settings

### Imágenes no cargan
→ Verifica que las URLs comienzan con `https://` y el dominio existe

### Ver errores
→ Web → Log files → error.log

## Scripts Importantes

- `DEPLOYMENT.md` - Guía detallada
- `CHECKLIST.md` - Verificación previa
- `requirements-prod.txt` - Dependencias para producción
- `setup-pythonanywhere.sh` - Script automatizado (si funciona)

---

¿Preguntas? Revisa DEPLOYMENT.md para instrucciones completas.
