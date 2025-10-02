#!/bin/bash

# Nombre del proyecto
PROJECT_NAME="mi_proyecto_web"

# Ruta al escritorio (para Linux)
DESKTOP="$HOME/Escritorio"

# Carpeta del proyecto
PROJECT_PATH="$DESKTOP/$PROJECT_NAME"

echo "Creando proyecto en $PROJECT_PATH..."

# Crear carpeta del proyecto
mkdir -p "$PROJECT_PATH"
cd "$PROJECT_PATH" || exit 1

# Crear entorno virtual
python3 -m venv .venv

# Activar entorno virtual
source .venv/bin/activate

# Instalar Flask automáticamente
pip install --upgrade pip
pip install flask

# Crear carpetas para HTML, CSS, JS e imágenes
mkdir -p templates
mkdir -p static/css
mkdir -p static/js
mkdir -p static/img

# Crear archivo app.py básico con Flask
cat <<EOF > app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hola, mundo!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
EOF

# Mensaje final
echo " Proyecto creado en: $PROJECT_PATH"
echo "Para correr la app ejecuta:"
echo "   source .venv/bin/activate && python app.py"