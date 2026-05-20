#!/bin/bash
# Script de setup rápido para PythonAnywhere
# Ejecutar: bash setup-pythonanywhere.sh

echo "=== CloudFree - Setup para PythonAnywhere ==="

# 1. Crear venv si no existe
if [ ! -d "venv" ]; then
    echo "📦 Creando entorno virtual..."
    python3.10 -m venv venv
fi

# 2. Activar venv
echo "✓ Activando venv..."
source venv/bin/activate

# 3. Instalar dependencias
echo "📥 Instalando dependencias..."
pip install -r requirements.txt

# 4. Migrar base de datos
echo "🗄️  Migrando base de datos..."
python manage.py migrate

# 5. Recolectar estáticos
echo "🎨 Recolectando archivos estáticos..."
python manage.py collectstatic --noinput

echo ""
echo "✅ Setup completado!"
echo ""
echo "⚠️  Próximos pasos manuales:"
echo "1. Configura variables de entorno en PythonAnywhere (Account → Web → Environment variables)"
echo "2. Crea un superusuario: python manage.py createsuperuser"
echo "3. Configura la app web en PythonAnywhere"
echo "4. Recarga la aplicación web"
echo ""
echo "📖 Ver DEPLOYMENT.md para instrucciones detalladas"
