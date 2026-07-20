# ALMOXARIFADO-SEAP

## Visão Geral

O ALMOXARIFADO-SEAP é um sistema web desenvolvido para auxiliar o controle de materiais de consumo da Secretaria de Administração Penitenciária e Ressocialização de Pernambuco (SEAP-PE).

O sistema tem como objetivo substituir gradualmente controles manuais realizados em planilhas Excel, permitindo maior rastreabilidade, confiabilidade das informações e apoio à tomada de decisão.

---

## Objetivos

* Controlar materiais armazenados no almoxarifado.
* Registrar entradas e saídas de materiais.
* Acompanhar níveis de estoque.
* Gerar informações para auditoria e prestação de contas.
* Apoiar gestores na tomada de decisão.
* Servir de base para integração futura com Power BI.

---

## Tecnologias Utilizadas

### Backend

* Python 3.13
* Django 6

### Banco de Dados

* SQLite (ambiente de desenvolvimento)
* PostgreSQL (planejado para produção)

### Frontend

* HTML
* Bootstrap 5

### Ferramentas

* VS Code
* Git (planejado)
* Power BI (planejado)

---

## Estrutura Atual

### Aplicação Almoxarifado

#### Categoria

Responsável por classificar os materiais.

Exemplos:

* Expediente
* Limpeza
* Informática
* Manutenção

#### Item

Representa cada material controlado pelo almoxarifado.

Campos:

* Código
* Descrição
* Categoria
* Unidade de Medida
* Estoque Mínimo
* Ativo

#### Fornecedor

Responsável pelo cadastro dos fornecedores.

Campos:

* Razão Social
* CNPJ
* Telefone
* E-mail

#### Movimentação de Estoque

Responsável pelo registro de entradas e saídas.

Tipos:

* Entrada
* Saída

Campos:

* Tipo
* Item
* Quantidade
* Data da Movimentação
* Observação

---

## Funcionalidades Implementadas

* Cadastro de Categorias
* Cadastro de Itens
* Cadastro de Fornecedores
* Cadastro de Movimentações
* Painel Administrativo Django
* Dashboard Inicial

---

## Funcionalidades Planejadas

### Controle de Estoque

* Saldo Atual
* Estoque Mínimo
* Alerta de Reposição

### Entradas

* Nota Fiscal
* Data de Recebimento
* Fornecedor
* Responsável

### Saídas

* Unidade Solicitante
* Responsável pela Retirada
* Justificativa

### Relatórios

* Entradas por Período
* Saídas por Período
* Consumo por Unidade
* Inventário

### Business Intelligence

* Dashboard Power BI
* Indicadores Gerenciais
* Curva ABC
* Consumo Mensal

---

## Histórico do Projeto

### Versão 0.1

Data: Junho/2026

Primeira versão funcional contendo:

* Estrutura Django
* Banco SQLite
* Categorias
* Itens
* Fornecedores
* Movimentações
* Dashboard Inicial

---

## Responsável pelo Desenvolvimento

Daniel Albuquerque de Sousa

Projeto acadêmico e institucional voltado para modernização do controle de almoxarifado da SEAP-PE.
---------------------------------------------------------

# ALMOXARIFADO-SEAP

## Versão Atual

### Funcionalidades Implementadas

* Dashboard gerencial
* Cadastro de categorias
* Cadastro de itens
* Cadastro de fornecedores
* Movimentações de estoque
* Controle de entradas
* Controle de saídas
* Cálculo automático de saldo
* Controle de estoque mínimo
* Histórico de movimentações
* Navegação entre telas

### Próximas Funcionalidades

* Pesquisa por item
* Filtro por período
* Relatórios PDF
* Exportação Excel
* PostgreSQL
* API REST
* Aplicativo mobile

### Tecnologias

* Python
* Django
* SQLite
* Bootstrap

### Responsável pelo Projeto

Daniel Albuquerque de Sousa
---------------------------------------------------

### Versão Atual: v0.4

Módulos Concluídos:
- Autenticação
- Dashboard
- Itens
- Estoque
- Entradas
- Saídas
- Movimentações
- Administração
------------------------------------------------------

## Versão 0.7 – Relatórios

### Funcionalidades implementadas

* Relatório de Estoque Atual
* Exibição de saldo calculado automaticamente
* Integração com método saldo_atual()
* Acesso através do menu principal

### Status do Sistema

Módulos concluídos:

* Autenticação
* Dashboard
* Estoque
* Movimentações
* Entradas
* Saídas
* Itens
* Fornecedores
* Relatório de Estoque

Próximo módulo:

* Relatório de Movimentações por Período
--------------------------------------------------------

# SPRINT 3 — Controle de Destinação de Materiais

## Objetivo

Registrar para qual servidor e para qual setor cada saída de material foi destinada.

## Funcionalidades

- Cadastro de Setores
- Cadastro de Servidores
- Vinculação do Servidor na Saída
- Vinculação do Setor
- Histórico por Servidor
- Recibo de Entrega
- Relatórios por Servidor
- Relatórios por Setor

## Benefícios

- Rastreabilidade completa
- Auditoria
- Controle administrativo
- Impressão de recibos
- Redução de erros

Status: Em desenvolvimento
--------------------------------------------------------

SPRINT 04 – Sistema de Autenticação e Controle de Acesso
Objetivo

Implementar o sistema de autenticação de usuários, garantindo que apenas servidores autorizados possam acessar o Sistema de Almoxarifado da SEAP.

Funcionalidades implementadas
Tela de Login personalizada.
Logout seguro utilizando requisição POST.
Proteção das páginas através do decorator @login_required.
Exibição do usuário autenticado na barra superior.
Redirecionamento automático para login quando necessário.
Correção do erro HTTP 405 no logout.
Resultado

O sistema passou a possuir controle de acesso, aumentando a segurança das informações.

SPRINT 05 – Controle de Movimentações de Estoque
Objetivo

Implementar o cadastro de entradas e saídas de materiais.

Funcionalidades implementadas
Cadastro de Entrada de Material.
Cadastro de Saída de Material.
Registro do usuário responsável pela movimentação.
Histórico completo das movimentações.
Validação para impedir saídas superiores ao saldo disponível.
Cálculo automático do saldo de estoque.
Refatoração do método saldo_atual() no modelo Item.
Resultado

O sistema passou a controlar corretamente todas as movimentações do estoque.

SPRINT 06 – Cadastros Básicos
Objetivo

Permitir o gerenciamento dos principais cadastros utilizados pelo sistema.

Funcionalidades implementadas
Cadastro de Itens
Inclusão de novos itens.
Código interno.
Categoria.
Unidade de medida.
Estoque mínimo.
Situação (ativo/inativo).
Cadastro de Fornecedores
Razão Social.
CNPJ.
Telefone.
E-mail.
Melhorias
Organização do menu.
Criação das telas de cadastro.
Integração completa com Bootstrap.
Resultado

O sistema passou a possuir uma base cadastral própria, eliminando a necessidade de utilizar apenas o Django Admin.

SPRINT 07 – Relatórios e Organização Administrativa
Objetivo

Disponibilizar consultas gerenciais e melhorar a organização do sistema.

Funcionalidades implementadas
Relatório de Estoque
Código do item.
Descrição.
Categoria.
Saldo Atual.
Relatório de Movimentações
Histórico completo das entradas.
Histórico completo das saídas.
Ordenação cronológica.
Melhorias
Reestruturação do menu superior.
Agrupamento por:
Operações
Cadastros
Relatórios
Resultado

O sistema passou a oferecer recursos de consulta para apoio à gestão do Almoxarifado.

SPRINT 08 – Cadastro de Destinos
Objetivo

Cadastrar os locais que poderão receber materiais do Almoxarifado.

Motivação

Os materiais distribuídos pelo Almoxarifado possuem como destino:

Unidades Prisionais.
Setores Administrativos.
Gerências.
Diretorias.
Outros órgãos vinculados.

O cadastro de Destinos permitirá rastrear todas as entregas realizadas.

Funcionalidades implementadas
Novo modelo

Destino

Campos:

Nome
Tipo
Telefone
E-mail
Responsável
Ativo
Administração
Registro no Django Admin.
Pesquisa.
Filtros.
Ordenação.
Sistema
Criação do formulário.
Criação da View.
Criação da URL.
Criação da tela de cadastro.
Integração com Bootstrap.
Resultado

O sistema passou a possuir uma base oficial de destinos para distribuição dos materiais.

SPRINT 09 – Evolução da Movimentação de Saída
Objetivo

Relacionar cada saída de estoque ao seu respectivo destino.

Funcionalidades implementadas
Banco de Dados

Inclusão do relacionamento:

Movimentação de Estoque → Destino

Formulário de Saída

Novo campo:

Destino
View

Atualização da lógica para salvar automaticamente o destino da movimentação.

Interface

Reestruturação da tela de Nova Saída.

Nova sequência operacional:

Destino
Item
Quantidade
Documento
Observação
Melhorias planejadas
Exibição do saldo disponível do item durante a saída.
Pesquisa inteligente de itens.
Seleção de servidor responsável pela entrega.
Geração automática de recibos.
Resultado

A movimentação de saída passou a registrar não apenas o material entregue, mas também o local para onde ele foi destinado, preparando o sistema para emissão automática de recibos e rastreabilidade completa das distribuições.

Resumo Geral até a Sprint 09
Módulos concluídos
✅ Autenticação de Usuários
✅ Dashboard
✅ Controle de Estoque
✅ Entradas
✅ Saídas
✅ Cadastro de Itens
✅ Cadastro de Fornecedores
✅ Cadastro de Destinos
✅ Relatório de Estoque
✅ Relatório de Movimentações
✅ Django Admin Personalizado
Módulos em desenvolvimento
🟡 Cadastro de Servidor do Almoxarifado
🟡 Evolução da Movimentação de Saída
🟡 Geração Automática de Recibos
🟡 Impressão em PDF
🟡 Histórico de Entregas por Destino
🟡 Histórico de Entregas por Servidor

