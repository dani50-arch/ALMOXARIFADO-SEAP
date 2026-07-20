from django.urls import path

from .views import (
    home,
    estoque,
    movimentacoes,

    MeuLoginView,
    logout_view,

    nova_entrada,
    nova_saida,

    novo_item,
    novo_fornecedor,
    novo_servidor,
    novo_destino,

    relatorio_estoque,
    relatorio_movimentacoes,

    nova_requisicao,
    adicionar_itens_requisicao,

)

urlpatterns = [

    # ==========================
    # Autenticação
    # ==========================

    path(
        'login/',
        MeuLoginView.as_view(),
        name='login'
    ),

    path(
        'logout/',
        logout_view,
        name='logout'
    ),

    # ==========================
    # Dashboard
    # ==========================

    path(
        '',
        home,
        name='home'
    ),

    # ==========================
    # Estoque
    # ==========================

    path(
        'estoque/',
        estoque,
        name='estoque'
    ),

    # ==========================
    # Movimentações
    # ==========================

    path(
        'movimentacoes/',
        movimentacoes,
        name='movimentacoes'
    ),

    path(
        'entrada/nova/',
        nova_entrada,
        name='nova_entrada'
    ),

    path(
        'saida/nova/',
        nova_saida,
        name='nova_saida'
    ),

    # ==========================
    # Cadastros
    # ==========================

    path(
        'item/novo/',
        novo_item,
        name='novo_item'
    ),

    path(
        'fornecedor/novo/',
        novo_fornecedor,
        name='novo_fornecedor'
    ),

    path(
        'servidor/novo/',
        novo_servidor,
        name='novo_servidor'
    ),

    path(
        'destino/novo/',
        novo_destino,
        name='novo_destino'
    ),

    # ==========================
    # Requisições
    # ==========================

    path(
        'requisicao/nova/',
        nova_requisicao,
        name='nova_requisicao'
    ),

    path(
        'requisicao/<int:pk>/itens/',
        adicionar_itens_requisicao,
        name='adicionar_itens_requisicao'
    ),

    # ==========================
    # Relatórios
    # ==========================

    path(
        'relatorios/estoque/',
        relatorio_estoque,
        name='relatorio_estoque'
    ),

    path(
        'relatorios/movimentacoes/',
        relatorio_movimentacoes,
        name='relatorio_movimentacoes'
    ),

]