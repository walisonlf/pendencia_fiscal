from datetime import datetime
from src.main import db

class Pendencia(db.Model):
    """Modelo para armazenar as pendências fiscais por UF."""
    
    __tablename__ = 'pendencias'
    
    id = db.Column(db.Integer, primary_key=True)
    uf = db.Column(db.String(2), nullable=False)
    situacao = db.Column(db.String(20), nullable=False)  # Normal, Importante, Urgente
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    data_atualizacao = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relacionamentos
    itens_pendencia = db.relationship('ItemPendencia', backref='pendencia', lazy=True, cascade="all, delete-orphan")
    itens_resumo = db.relationship('ItemResumo', backref='pendencia', lazy=True, cascade="all, delete-orphan")
    itens_decisao = db.relationship('ItemDecisao', backref='pendencia', lazy=True, cascade="all, delete-orphan")
    
    def __repr__(self):
        return f'<Pendencia {self.uf} - {self.situacao}>'
    
    def to_dict(self):
        """Converte o objeto para um dicionário."""
        return {
            'id': self.id,
            'uf': self.uf,
            'situacao': self.situacao,
            'pendencias': [item.to_dict() for item in self.itens_pendencia],
            'resumos': [item.to_dict() for item in self.itens_resumo],
            'decisoes': [item.to_dict() for item in self.itens_decisao],
            'data_criacao': self.data_criacao.isoformat(),
            'data_atualizacao': self.data_atualizacao.isoformat()
        }


class ItemPendencia(db.Model):
    """Modelo para armazenar os itens de pendência."""
    
    __tablename__ = 'itens_pendencia'
    
    id = db.Column(db.Integer, primary_key=True)
    pendencia_id = db.Column(db.Integer, db.ForeignKey('pendencias.id'), nullable=False)
    numero = db.Column(db.Integer, nullable=False)  # Número sequencial do item
    descricao = db.Column(db.Text, nullable=False)
    
    def __repr__(self):
        return f'<ItemPendencia {self.numero}. {self.descricao[:20]}...>'
    
    def to_dict(self):
        """Converte o objeto para um dicionário."""
        return {
            'id': self.id,
            'numero': self.numero,
            'descricao': self.descricao
        }


class ItemResumo(db.Model):
    """Modelo para armazenar os itens de resumo da ocorrência."""
    
    __tablename__ = 'itens_resumo'
    
    id = db.Column(db.Integer, primary_key=True)
    pendencia_id = db.Column(db.Integer, db.ForeignKey('pendencias.id'), nullable=False)
    numero = db.Column(db.Integer, nullable=False)  # Número sequencial do item
    descricao = db.Column(db.Text, nullable=False)
    
    def __repr__(self):
        return f'<ItemResumo {self.numero}. {self.descricao[:20]}...>'
    
    def to_dict(self):
        """Converte o objeto para um dicionário."""
        return {
            'id': self.id,
            'numero': self.numero,
            'descricao': self.descricao
        }


class ItemDecisao(db.Model):
    """Modelo para armazenar os itens de decisão interna."""
    
    __tablename__ = 'itens_decisao'
    
    id = db.Column(db.Integer, primary_key=True)
    pendencia_id = db.Column(db.Integer, db.ForeignKey('pendencias.id'), nullable=False)
    numero = db.Column(db.Integer, nullable=False)  # Número sequencial do item
    descricao = db.Column(db.Text, nullable=False)
    
    def __repr__(self):
        return f'<ItemDecisao {self.numero}. {self.descricao[:20]}...>'
    
    def to_dict(self):
        """Converte o objeto para um dicionário."""
        return {
            'id': self.id,
            'numero': self.numero,
            'descricao': self.descricao
        }
