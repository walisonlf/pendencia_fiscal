# Manual do Usuário - Controle de Pendências Fiscais

## Introdução

Este manual descreve como utilizar a aplicação web de Controle de Pendências Fiscais, desenvolvida para gerenciar pendências fiscais por estado (UF), permitindo o registro, acompanhamento e gerenciamento de múltiplas pendências, resumos e decisões internas.

## Requisitos do Sistema

- Navegador web moderno (Chrome, Firefox, Edge, Safari)
- Conexão com a internet

## Iniciando a Aplicação

Para iniciar a aplicação, siga os passos abaixo:

1. Acesse a pasta do projeto: `cd /caminho/para/controle-pendencias-fiscais`
2. Ative o ambiente virtual: `source venv/bin/activate`
3. Execute a aplicação: `python src/main.py`
4. Acesse a aplicação no navegador: `http://localhost:5000`

## Funcionalidades Principais

### Visão Geral da Interface

A interface principal da aplicação é composta por:

- **Cards de Resumo**: Exibem a contagem de pendências por situação (Urgente, Importante, Normal)
- **Filtros**: Permitem filtrar pendências por situação, UF ou texto
- **Tabela de Pendências**: Exibe todas as pendências cadastradas com suas informações

### Cadastro de Pendências

Para cadastrar uma nova pendência:

1. Clique no botão "Nova Pendência" no canto superior direito
2. Preencha os campos obrigatórios:
   - **Situação**: Selecione entre Urgente, Importante ou Normal
   - **UF**: Digite a sigla do estado (2 letras)
   - **Pendências**: Descreva as pendências (pode adicionar múltiplas)
   - **Resumo da Ocorrência**: Descreva os resumos (pode adicionar múltiplos)
   - **Decisão Interna**: Descreva as decisões (pode adicionar múltiplas)
3. Clique em "Salvar"

### Adição de Múltiplos Itens

Para adicionar múltiplos itens em qualquer seção (Pendências, Resumos ou Decisões):

1. Preencha o primeiro item
2. Clique no botão "Adicionar [Tipo]" abaixo da seção
3. Um novo campo será adicionado com numeração automática
4. Repita o processo para adicionar quantos itens forem necessários

### Edição de Pendências

Para editar uma pendência existente:

1. Localize a pendência na tabela
2. Clique no botão "Editar" na coluna de ações
3. Modifique os campos desejados
4. Clique em "Salvar"

### Exclusão de Pendências

Para excluir uma pendência:

1. Localize a pendência na tabela
2. Clique no botão "Excluir" na coluna de ações
3. Confirme a exclusão na caixa de diálogo

### Filtros e Busca

Para filtrar as pendências:

- **Por Situação**: Selecione uma situação no filtro "Filtrar por Situação"
- **Por UF**: Selecione um estado no filtro "Filtrar por UF"
- **Por Texto**: Digite um termo na caixa de busca

Você também pode clicar nos cards de resumo (Urgente, Importante, Normal) para filtrar rapidamente por situação.

## Recursos Adicionais

### Salvamento Automático

Todas as alterações são salvas automaticamente no banco de dados. A data e hora do último salvamento são exibidas no rodapé da tabela.

### Notificações

Após cada operação (salvar, editar, excluir), uma notificação será exibida no canto inferior direito da tela, confirmando o sucesso da operação.

## Solução de Problemas

Se encontrar algum problema ao utilizar a aplicação:

1. Verifique se o servidor está em execução
2. Atualize a página do navegador
3. Verifique os logs do servidor para identificar possíveis erros

## Suporte

Para obter suporte ou relatar problemas, entre em contato com o administrador do sistema.
