from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from ..models import (
    Categoria,
    Item,
    Fornecedor,
    MovimentacaoEstoque,
)


@login_required
def home(request):

    ultimas_movimentacoes = (
        MovimentacaoEstoque.objects
        .order_by('-data_movimentacao')[:5]
    )

    contexto = {
        'total_categorias': Categoria.objects.count(),
        'total_itens': Item.objects.count(),
        'total_fornecedores': Fornecedor.objects.count(),
        'total_movimentacoes': MovimentacaoEstoque.objects.count(),
        'ultimas_movimentacoes': ultimas_movimentacoes,
    }

    return render(
        request,
        'almoxarifado/home.html',
        contexto
    )