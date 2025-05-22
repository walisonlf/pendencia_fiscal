# Requisitos para Aplicação de Controle de Pendências Fiscais

## Visão Geral
Desenvolver uma aplicação web para controle de pendências fiscais por estado (UF), permitindo o registro, acompanhamento e gerenciamento de pendências fiscais em diferentes unidades federativas. A aplicação deve permitir o trabalho colaborativo, com persistência de dados para consulta por múltiplos usuários.

## Requisitos Funcionais

### 1. Gerenciamento de Pendências
- Cadastrar pendências fiscais por UF (estado)
- Permitir múltiplas pendências para uma mesma UF
- Numeração automática das pendências (1., 2., 3., etc.)
- Categorizar pendências por situação (Normal, Importante, Urgente)
- Permitir edição e exclusão de pendências existentes

### 2. Detalhamento de Ocorrências
- Registrar resumo detalhado das ocorrências para cada UF
- Permitir múltiplos resumos para uma mesma UF
- Numeração automática dos resumos (1., 2., 3., etc.)
- Vincular resumos às pendências correspondentes

### 3. Decisões Internas
- Registrar decisões internas para resolução das pendências
- Permitir múltiplas decisões para uma mesma UF
- Numeração automática das decisões (1., 2., 3., etc.)
- Vincular decisões às pendências correspondentes

### 4. Visualização e Filtros
- Visualizar todas as pendências em formato de tabela
- Filtrar pendências por UF
- Filtrar pendências por situação (Normal, Importante, Urgente)
- Busca por texto em qualquer campo

### 5. Persistência de Dados
- Salvar automaticamente as alterações
- Manter histórico de última atualização
- Permitir acesso aos dados por múltiplos usuários

## Requisitos Não-Funcionais

### 1. Interface de Usuário
- Design responsivo (adaptável a diferentes dispositivos)
- Interface intuitiva e amigável
- Cores diferenciadas por situação:
  - Urgente: Vermelho (#f72585)
  - Importante: Laranja (#f8961e)
  - Normal: Azul (#4cc9f0)

### 2. Desempenho
- Tempo de resposta rápido para operações de CRUD
- Carregamento eficiente de dados

### 3. Segurança
- Proteção básica contra injeção de SQL
- Validação de entradas de usuário

## Estrutura de Dados

### Entidade: Registro de Pendência
- ID (chave primária)
- UF (estado - 2 caracteres)
- Situação (Normal, Importante, Urgente)
- Lista de Pendências (texto, múltiplas entradas)
- Lista de Resumos (texto, múltiplas entradas)
- Lista de Decisões (texto, múltiplas entradas)
- Data de Criação
- Data de Última Atualização

## Interface do Usuário

### Tela Principal
- Cabeçalho com título da aplicação
- Cards de resumo mostrando contagem por situação (Normal, Importante, Urgente)
- Barra de pesquisa e filtros
- Tabela principal com colunas:
  - Situação (com badge colorido)
  - UF
  - Filial/Pendências (com múltiplos itens numerados)
  - Resumo da Ocorrência (com múltiplos itens numerados)
  - Decisão Interna (com múltiplos itens numerados)
  - Ações (editar, excluir)

### Formulário de Cadastro/Edição
- Seleção de situação (Normal, Importante, Urgente)
- Campo para UF
- Campos para adicionar múltiplas pendências
- Campos para adicionar múltiplos resumos
- Campos para adicionar múltiplas decisões
- Botões para adicionar novos itens em cada seção
- Botões para salvar ou cancelar

## Tecnologias
- Backend: Flask (Python)
- Frontend: HTML, CSS, JavaScript, Bootstrap
- Banco de Dados: SQLite (para facilitar a implantação)
- Persistência: SQLAlchemy ORM
