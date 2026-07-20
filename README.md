# ALMOXARIFADO-SEAP

Sistema Web para Controle de Almoxarifado da **Secretaria de Administração Penitenciária e Ressocialização de Pernambuco (SEAP-PE)**.

---

## Sobre o Projeto

O **ALMOXARIFADO-SEAP** foi desenvolvido para modernizar o controle de materiais de consumo utilizados pela SEAP-PE.

O sistema substitui gradualmente controles realizados em planilhas eletrônicas, oferecendo maior confiabilidade das informações, rastreabilidade das movimentações e apoio à tomada de decisão.

---

## Objetivos

* Controlar o estoque de materiais de consumo.
* Registrar entradas e saídas de materiais.
* Gerenciar requisições internas.
* Cadastrar fornecedores, destinos e servidores responsáveis.
* Emitir relatórios gerenciais.
* Servir como base para integração futura com Power BI.

---

## Funcionalidades Implementadas

* Dashboard Inicial
* Controle de Estoque
* Cadastro de Categorias
* Cadastro de Itens
* Cadastro de Fornecedores
* Cadastro de Destinos
* Cadastro de Servidores do Almoxarifado
* Registro de Entradas
* Registro de Saídas
* Requisições de Materiais
* Relatórios
* Sistema de Login

---

## Tecnologias Utilizadas

| Tecnologia | Versão                  |
| ---------- | ----------------------- |
| Python     | 3.13                    |
| Django     | 6                       |
| Bootstrap  | 5                       |
| HTML5      | ✓                       |
| SQLite     | Desenvolvimento         |
| PostgreSQL | Planejado para Produção |
| Git        | Controle de Versão      |
| GitHub     | Hospedagem do Projeto   |

---

## Arquitetura

```text
Usuário
   │
   ▼
Interface Web
   │
   ▼
Views (Django)
   │
   ▼
Models
   │
   ▼
Banco de Dados
```

---

## Estrutura do Projeto

```text
ALMOXARIFADO-SEAP/

├── almoxarifado/
│   ├── migrations/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
│
├── core/
│
├── seap_project/
│
├── manage.py
├── requirements.txt
├── DOCUMENTACAO_PROJETO.md
└── README.md
```

---

## Funcionalidades Planejadas

* Aprovação de Requisições
* Controle Patrimonial
* Assinatura Digital
* Geração de PDF
* QR Code
* Dashboard Gerencial
* Curva ABC
* Inventário Automatizado
* Integração com Power BI

---

## Status do Projeto

**Em desenvolvimento**

Versão atual: **0.1**

---

## Desenvolvedor

**Daniel Albuquerque de Sousa**

Projeto acadêmico e institucional voltado à modernização do controle de almoxarifado da Secretaria de Administração Penitenciária e Ressocialização de Pernambuco (SEAP-PE).

---

## Licença

Este projeto possui finalidade acadêmica e institucional.
