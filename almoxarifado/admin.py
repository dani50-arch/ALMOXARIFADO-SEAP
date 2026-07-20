from django.contrib import admin

from .models import (
    Categoria,
    Setor,
    ServidorAlmoxarifado,
    Destino,
    Item,
    Fornecedor,
    MovimentacaoEstoque
)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):

    list_display = (
        'nome',
    )

    search_fields = (
        'nome',
    )


@admin.register(Setor)
class SetorAdmin(admin.ModelAdmin):

    list_display = (
        'nome',
        'sigla',
        'ativo',
    )

    list_filter = (
        'ativo',
    )

    search_fields = (
        'nome',
        'sigla',
    )


@admin.register(ServidorAlmoxarifado)
class ServidorAlmoxarifadoAdmin(admin.ModelAdmin):

    list_display = (
        'nome',
        'matricula',
        'cargo',
        'setor',
        'ativo',
    )

    list_filter = (
        'setor',
        'ativo',
    )

    search_fields = (
        'nome',
        'matricula',
    )


@admin.register(Destino)
class DestinoAdmin(admin.ModelAdmin):

    list_display = (
        'nome',
        'tipo',
        'cidade',
        'responsavel',
        'ativo',
    )

    list_filter = (
        'tipo',
        'ativo',
    )

    search_fields = (
        'nome',
        'cidade',
        'responsavel',
    )


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):

    list_display = (
        'codigo',
        'descricao',
        'categoria',
        'estoque_minimo',
        'ativo',
    )

    list_filter = (
        'categoria',
        'ativo',
    )

    search_fields = (
        'codigo',
        'descricao',
    )


@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):

    list_display = (
        'razao_social',
        'cnpj',
        'telefone',
    )

    search_fields = (
        'razao_social',
        'cnpj',
    )


@admin.register(MovimentacaoEstoque)
class MovimentacaoEstoqueAdmin(admin.ModelAdmin):

    list_display = (
        'tipo',
        'item',
        'quantidade',
        'responsavel',
        'documento',
        'data_movimentacao',
    )

    list_filter = (
        'tipo',
        'item',
    )

    search_fields = (
        'item__descricao',
        'documento',
        'responsavel',
    )