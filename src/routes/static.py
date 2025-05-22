from flask import render_template, send_from_directory
from src.main import app

@app.route('/')
def index():
    """Rota principal que renderiza a página inicial."""
    return send_from_directory('static', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    """Rota para servir arquivos estáticos."""
    return send_from_directory('static', path)
