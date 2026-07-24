# ALMOXARIFADO-SEAP

<p align="center">

**Sistema Integrado de Gestão de Materiais**

Sistema desenvolvido em **Python** e **Django** para gerenciamento de estoque, movimentações e requisições de materiais da Secretaria de Administração Penitenciária e Ressocialização de Pernambuco.

> Organização • Controle • Eficiência

</p>

---

# Índice

* Sobre o Projeto
* Objetivos
* Funcionalidades
* Tecnologias Utilizadas
* Arquitetura do Sistema
* Estrutura do Projeto
* Capturas de Tela
* Instalação
* Como Executar
* Roadmap
* Contribuição
* Licença
* Autor

---

# Sobre o Projeto

O **ALMOXARIFADO-SEAP** foi desenvolvido para modernizar o controle de materiais de consumo da Secretaria de Administração Penitenciária e Ressocialização de Pernambuco (SEAP-PE).

O sistema substitui controles realizados em planilhas eletrônicas por uma aplicação web capaz de registrar todas as movimentações de estoque, garantindo maior rastreabilidade, segurança e apoio à tomada de decisão.

---

# Objetivos

* Controlar materiais de consumo
* Registrar entradas e saídas
* Controlar saldo de estoque
* Gerenciar fornecedores
* Gerenciar destinos
* Gerenciar requisições
* Emitir relatórios
* Preparar integração com Power BI

---

# Funcionalidades

### Cadastros

* Categorias
* Itens
* Fornecedores
* Destinos
* Requisições

### Controle de Estoque

* Entradas
* Saídas
* Saldo Atual
* Estoque Mínimo

### Relatórios

* Estoque Atual
* Movimentações
* Consumo por Unidade

### Dashboard

* Indicadores Gerais
* Quantidade de Itens
* Quantidade de Movimentações
* Informações Gerenciais

---

# Tecnologias Utilizadas

## Backend

* Python 3.13
* Django 6

## Banco de Dados

* SQLite (Desenvolvimento)
* PostgreSQL (Planejado)

## Frontend

* HTML5
* Bootstrap 5
* CSS3

## Ferramentas

* VS Code
* Git
* GitHub

---

# Arquitetura do Sistema

```text
Usuário
      │
      ▼
Interface Web
      │
      ▼
Views Django
      │
      ▼
Models
      │
      ▼
SQLite / PostgreSQL
```

---

# Estrutura do Projeto

```text
ALMOXARIFADO-SEAP/

├── almoxarifado/
├── core/
├── seap_project/
│
├── assets/
│   ├── banner/
│   ├── logo/
│   ├── screenshots/
│   └── icons/
│
├── README.md
├── DOCUMENTACAO_PROJETO.md
├── requirements.txt
├── manage.py
└── .gitignore
```

---

# Capturas de Tela

Em breve serão adicionadas imagens do sistema contendo:

* Dashboard
* Estoque
* Entradas
* Saídas
* Requisições
* Relatórios

---

# Instalação

```bash
git clone https://github.com/dani50-arch/ALMOXARIFADO-SEAP.git

cd ALMOXARIFADO-SEAP

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

---

# Roadmap

## Concluído

* Cadastro de Categorias
* Cadastro de Itens
* Cadastro de Fornecedores
* Cadastro de Destinos
* Controle de Estoque
* Entradas
* Saídas
* Requisições
* Dashboard
* Relatórios

## Em Desenvolvimento

* Inventário
* Curva ABC
* API REST
* Power BI
* PostgreSQL
* Docker
* Deploy

---

# Contribuição

Este projeto encontra-se em constante evolução.

Sugestões e melhorias são bem-vindas.

---

# Licença

Projeto desenvolvido para fins acadêmicos e institucionais.

---

# Autor

**Daniel Albuquerque de Sousa**

Projeto desenvolvido para a modernização do controle de materiais da Secretaria de Administração Penitenciária e Ressocialização de Pernambuco.
