# Checklist Pre-Deployment

Verificar antes de desplegar en PythonAnywhere:

## ✓ Configuración Django
- [ ] `DEBUG = False` en producción
- [ ] `SECRET_KEY` configurada como variable de entorno
- [ ] `ALLOWED_HOSTS` incluye dominio de PythonAnywhere
- [ ] `MIDDLEWARE` incluye `WhiteNoiseMiddleware`
- [ ] `STATIC_ROOT` configurado correctamente

## ✓ Base de datos
- [ ] Migraciones aplicadas (`python manage.py migrate`)
- [ ] Superusuario creado (`python manage.py createsuperuser`)
- [ ] No hay referencias a archivos locales en la base

## ✓ Archivos estáticos
- [ ] `collectstatic` ejecutado exitosamente
- [ ] Carpeta `staticfiles/` poblada
- [ ] `whitenoise` instalado en requirements.txt

## ✓ Código limpio
- [ ] No hay `print()` statements de debug
- [ ] No hay archivos temporales sin commitar
- [ ] `.gitignore` configurado correctamente
- [ ] Datos sensibles no están hardcodeados

## ✓ Documentación
- [ ] `DEPLOYMENT.md` actualizado
- [ ] `requirements.txt` actualizado
- [ ] README tiene instrucciones básicas

## ✓ URLs e imágenes
- [ ] Campos de imagen usan URLs externas
- [ ] `media/` está vacío en producción
- [ ] No hay referencias a `.image.url` en templates

## ✓ Seguridad
- [ ] HTTPS configurado en PythonAnywhere
- [ ] CSRF cookies aseguradas
- [ ] Session cookies aseguradas
- [ ] No hay credenciales en el repo

## ✓ Testing
- [ ] `python manage.py check` sin errores
- [ ] Aplicación funciona en `DEBUG=False` localmente
- [ ] Admin accesible
- [ ] Noticias y recursos cargan correctamente

---

**Después del deployment:**
1. Verifica logs en PythonAnywhere
2. Accede a `/admin/` y confirma que funciona
3. Verifica que los templates cargan correctamente
4. Prueba crear/editar una noticia o recurso
