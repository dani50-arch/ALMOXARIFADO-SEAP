# CHANGELOG

## Sprint de Hardening — Módulo Nova Entrada

Data: Julho/2026

### Correções implementadas

- Implementada validação para impedir quantidade igual a zero.
- Mantida proteção contra quantidades negativas através do PositiveIntegerField do Django.
- Implementada obrigatoriedade do Documento (Nota Fiscal, Processo ou outro documento oficial).
- Validada atualização automática do estoque.
- Validado registro automático da movimentação de entrada.
- Validado cadastro utilizando fornecedor.

### Resultado

Módulo Nova Entrada considerado estável e aprovado para continuidade do desenvolvimento.

# CHANGELOG

---

## Versão 0.2
Data: 24/07/2026

### Módulo 11 — Nova Saída (Concluído)

#### Implementações

- Cadastro de saídas de materiais.
- Atualização automática do estoque.
- Registro automático das movimentações.
- Registro do responsável pela operação.

#### Hardening

- Validação de quantidade maior que zero.
- Documento obrigatório.
- Destino obrigatório.
- Validação de estoque insuficiente.
- Exibição das mensagens de erro diretamente no formulário.
- Revisão completa da view `nova_saida`.
- Revisão completa do formulário `SaidaForm`.
- Revisão do template `nova_saida.html`.

#### Correções Gerais

- Padronização das validações.
- Correção de inconsistências no `forms.py`.
- Eliminação de todos os Problems reportados pelo VS Code.
- Revisão do fluxo completo de saída de estoque.

### Status

✔ Módulo homologado.

Próximo módulo:
Módulo 12 — Requisições