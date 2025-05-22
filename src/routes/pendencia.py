from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from src.models.pendencia import Pendencia, ItemPendencia, ItemResumo, ItemDecisao
from src.main import db

pendencia_bp = Blueprint('pendencia', __name__)

@pendencia_bp.route('/')
def index():
    """Rota principal que exibe a lista de pendências."""
    return render_template('index.html')

@pendencia_bp.route('/api/pendencias', methods=['GET'])
def listar_pendencias():
    """API para listar todas as pendências."""
    pendencias = Pendencia.query.all()
    return jsonify([pendencia.to_dict() for pendencia in pendencias])

@pendencia_bp.route('/api/pendencias', methods=['POST'])
def criar_pendencia():
    """API para criar uma nova pendência."""
    data = request.json
    
    # Criar a pendência principal
    pendencia = Pendencia(
        uf=data['uf'].upper(),
        situacao=data['situacao']
    )
    db.session.add(pendencia)
    db.session.flush()  # Para obter o ID da pendência
    
    # Adicionar itens de pendência
    for i, item in enumerate(data.get('pendencias', []), 1):
        item_pendencia = ItemPendencia(
            pendencia_id=pendencia.id,
            numero=i,
            descricao=item
        )
        db.session.add(item_pendencia)
    
    # Adicionar itens de resumo
    for i, item in enumerate(data.get('resumos', []), 1):
        item_resumo = ItemResumo(
            pendencia_id=pendencia.id,
            numero=i,
            descricao=item
        )
        db.session.add(item_resumo)
    
    # Adicionar itens de decisão
    for i, item in enumerate(data.get('decisoes', []), 1):
        item_decisao = ItemDecisao(
            pendencia_id=pendencia.id,
            numero=i,
            descricao=item
        )
        db.session.add(item_decisao)
    
    db.session.commit()
    return jsonify(pendencia.to_dict()), 201

@pendencia_bp.route('/api/pendencias/<int:id>', methods=['GET'])
def obter_pendencia(id):
    """API para obter uma pendência específica."""
    pendencia = Pendencia.query.get_or_404(id)
    return jsonify(pendencia.to_dict())

@pendencia_bp.route('/api/pendencias/<int:id>', methods=['PUT'])
def atualizar_pendencia(id):
    """API para atualizar uma pendência existente."""
    pendencia = Pendencia.query.get_or_404(id)
    data = request.json
    
    # Atualizar dados básicos
    pendencia.uf = data['uf'].upper()
    pendencia.situacao = data['situacao']
    
    # Remover itens existentes
    ItemPendencia.query.filter_by(pendencia_id=pendencia.id).delete()
    ItemResumo.query.filter_by(pendencia_id=pendencia.id).delete()
    ItemDecisao.query.filter_by(pendencia_id=pendencia.id).delete()
    
    # Adicionar novos itens de pendência
    for i, item in enumerate(data.get('pendencias', []), 1):
        item_pendencia = ItemPendencia(
            pendencia_id=pendencia.id,
            numero=i,
            descricao=item
        )
        db.session.add(item_pendencia)
    
    # Adicionar novos itens de resumo
    for i, item in enumerate(data.get('resumos', []), 1):
        item_resumo = ItemResumo(
            pendencia_id=pendencia.id,
            numero=i,
            descricao=item
        )
        db.session.add(item_resumo)
    
    # Adicionar novos itens de decisão
    for i, item in enumerate(data.get('decisoes', []), 1):
        item_decisao = ItemDecisao(
            pendencia_id=pendencia.id,
            numero=i,
            descricao=item
        )
        db.session.add(item_decisao)
    
    db.session.commit()
    return jsonify(pendencia.to_dict())

@pendencia_bp.route('/api/pendencias/<int:id>', methods=['DELETE'])
def excluir_pendencia(id):
    """API para excluir uma pendência."""
    pendencia = Pendencia.query.get_or_404(id)
    db.session.delete(pendencia)
    db.session.commit()
    return '', 204

@pendencia_bp.route('/api/pendencias/filtrar', methods=['GET'])
def filtrar_pendencias():
    """API para filtrar pendências por UF e/ou situação."""
    uf = request.args.get('uf', '').upper()
    situacao = request.args.get('situacao', '')
    
    query = Pendencia.query
    
    if uf:
        query = query.filter(Pendencia.uf == uf)
    
    if situacao:
        query = query.filter(Pendencia.situacao == situacao)
    
    pendencias = query.all()
    return jsonify([pendencia.to_dict() for pendencia in pendencias])
