from django.shortcuts import render, redirect
from django.db.models import Sum

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout


from .forms import (
    EntradaForm,
    SaidaForm,
    ItemForm,
    FornecedorForm,
    ServidorAlmoxarifadoForm,
    DestinoForm,
    RequisicaoForm,
    ItemRequisicaoForm,
)

from .models import (
    Categoria,
    Setor,
    ServidorAlmoxarifado,
    Destino,
    Requisicao,
    Item,
    Fornecedor,
    MovimentacaoEstoque,
    ItemRequisicao,
)


class MeuLoginView(LoginView):
    template_name = 'almoxarifado/login.html'


def logout_view(request):
    logout(request)
    return redirect('/login/')


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


@login_required
def estoque(request):

    itens_estoque = []

    for item in Item.objects.all():

        entradas = (
            MovimentacaoEstoque.objects
            .filter(item=item, tipo='E')
            .aggregate(total=Sum('quantidade'))
        )['total'] or 0

        saidas = (
            MovimentacaoEstoque.objects
            .filter(item=item, tipo='S')
            .aggregate(total=Sum('quantidade'))
        )['total'] or 0

        saldo = item.saldo_atual()

        situacao = "✅ Normal"

        if saldo <= item.estoque_minimo:
            situacao = "⚠ Repor Estoque"

        itens_estoque.append({
            'codigo': item.codigo,
            'descricao': item.descricao,
            'entradas': entradas,
            'saidas': saidas,
            'saldo': saldo,
            'estoque_minimo': item.estoque_minimo,
            'situacao': situacao,
        })

    return render(
        request,
        'almoxarifado/estoque.html',
        {
            'itens_estoque': itens_estoque
        }
    )


@login_required
def movimentacoes(request):

    movimentacoes = (
        MovimentacaoEstoque.objects
        .select_related(
            'item',
            'destino',
            'fornecedor',
        )
        .order_by('-data_movimentacao')
    )

    return render(
        request,
        'almoxarifado/movimentacoes.html',
        {
            'movimentacoes': movimentacoes
        }
    )


@login_required
def nova_entrada(request):

    if request.method == 'POST':

        form = EntradaForm(request.POST)

        if form.is_valid():

            entrada = form.save(commit=False)

            entrada.tipo = 'E'

            entrada.responsavel = request.user.username

            entrada.save()

            return redirect('/movimentacoes/')

    else:

        form = EntradaForm()

    return render(
        request,
        'almoxarifado/nova_entrada.html',
        {
            'form': form
        }
    )


@login_required
def nova_saida(request):

    if request.method == "POST":

        form = SaidaForm(request.POST)

        if form.is_valid():

            saida = form.save(commit=False)

            saida.tipo = "S"

            saida.responsavel = request.user.username

            saida.save()

            return redirect("movimentacoes")

    else:

        form = SaidaForm()

    return render(
        request,
        "almoxarifado/nova_saida.html",
        {
            "form": form,
        },
    )


@login_required
def novo_item(request):

    if request.method == "POST":

        form = ItemForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("home")

    else:

        form = ItemForm()

    return render(
        request,
        "almoxarifado/novo_item.html",
        {
            "form": form
        }
    )


@login_required
def novo_fornecedor(request):

    if request.method == 'POST':

        form = FornecedorForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('/')

    else:

        form = FornecedorForm()

    return render(
        request,
        'almoxarifado/novo_fornecedor.html',
        {
            'form': form
        }
    )


@login_required
def novo_destino(request):

    if request.method == 'POST':

        form = DestinoForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('/')

    else:

        form = DestinoForm()

    return render(
        request,
        'almoxarifado/novo_destino.html',
        {
            'form': form
        }
    )


@login_required
def nova_requisicao(request):

    if request.method == 'POST':

        form = RequisicaoForm(request.POST)

        if form.is_valid():

            requisicao = form.save(commit=False)

            requisicao.status = 'SOLICITADA'

            requisicao.save()

            return redirect(
                'adicionar_itens_requisicao',
                requisicao.id
            )

    else:

        form = RequisicaoForm()

        print(form)
        print(form.fields)

    return render(
        request,
        'almoxarifado/nova_requisicao.html',
        {
            'form': form
        }
    )


@login_required
def relatorio_estoque(request):

    itens = Item.objects.all()

    return render(
        request,
        'almoxarifado/relatorio_estoque.html',
        {
            'itens': itens
        }
    )


@login_required
def relatorio_movimentacoes(request):

    movimentacoes = (
        MovimentacaoEstoque.objects
        .select_related('item', 'destino', 'fornecedor')
        .order_by('-data_movimentacao')
    )

    return render(
        request,
        'almoxarifado/relatorio_movimentacoes.html',
        {
            'movimentacoes': movimentacoes
        }
    )


@login_required
def novo_servidor(request):

    if request.method == 'POST':

        form = ServidorAlmoxarifadoForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('/')

    else:

        form = ServidorAlmoxarifadoForm()

    return render(
        request,
        'almoxarifado/novo_servidor.html',
        {
            'form': form
        }
    )


@login_required
def adicionar_itens_requisicao(request, pk):

    requisicao = Requisicao.objects.get(id=pk)

    if request.method == "POST":

        form = ItemRequisicaoForm(request.POST)

        if form.is_valid():

            item = form.save(commit=False)

            item.requisicao = requisicao

            item.save()

            return redirect(
                'adicionar_itens_requisicao',
                pk=requisicao.id
            )

    else:

        form = ItemRequisicaoForm()

    itens = ItemRequisicao.objects.filter(
        requisicao=requisicao
    )

    return render(
        request,
        'almoxarifado/adicionar_itens_requisicao.html',
        {
            'requisicao': requisicao,
            'form': form,
            'itens': itens,
        }
    )


@login_required
def listar_requisicoes(request):

    requisicoes = Requisicao.objects.all().order_by(
        '-data_requisicao'
    )

    return render(
        request,
        'almoxarifado/listar_requisicoes.html',
        {
            'requisicoes': requisicoes
        }
    )