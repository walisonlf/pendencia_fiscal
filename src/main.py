import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))  # DON'T CHANGE THIS !!!

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Inicialização do Flask e SQLAlchemy
app = Flask(__name__)

# Configuração do banco de dados
database_url = os.environ.get('DATABASE_URL')
if database_url and database_url.startswith("postgres://"):
    # O Render usa URLs começando com postgres://, mas SQLAlchemy precisa de postgresql://
    database_url = database_url.replace("postgres://", "postgresql://", 1)
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
else:
    # Fallback para SQLite local quando não estiver em produção
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pendencias_fiscais.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Importação dos modelos para garantir que sejam registrados
from src.models.pendencia import Pendencia, ItemPendencia, ItemResumo, ItemDecisao

# Importação dos blueprints
from src.routes.pendencia import pendencia_bp
from src.routes.static import static_files, index

# Registro dos blueprints
app.register_blueprint(pendencia_bp, url_prefix='/api')

# Criação das tabelas do banco de dados
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    # Usar a porta definida pelo ambiente ou 5000 como padrão
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
