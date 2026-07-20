from django import forms

from .models import (
    MovimentacaoEstoque,
    Item,
    Fornecedor,
    Destino,
    ServidorAlmoxarifado,
    Requisicao,
    ItemRequisicao,
)


class EntradaForm(forms.ModelForm):

    class Meta:

        model = MovimentacaoEstoque

        fields = [
            'item',
            'fornecedor',
            'quantidade',
            'documento',
            'observacao',
        ]


class SaidaForm(forms.ModelForm):

    class Meta:

        model = MovimentacaoEstoque

        fields = [
            'destino',
            'item',
            'quantidade',
            'documento',
            'observacao',
        ]


        labels = {
            'destino': 'Destino',
            'item': 'Item',
            'quantidade': 'Quantidade',
            'documento': 'Documento',
            'observacao': 'Observação',
        }


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item

        fields = [
            'codigo',
            'descricao',
            'categoria',
            'unidade_medida',
            'estoque_minimo',
            'ativo',
        ]


class FornecedorForm(forms.ModelForm):

    class Meta:

        model = Fornecedor

        fields = [
            'razao_social',
            'cnpj',
            'telefone',
            'email',
        ]


class DestinoForm(forms.ModelForm):

    class Meta:

        model = Destino

        fields = [
            'nome',
            'tipo',
            'telefone',
            'email',
            'responsavel',
            'ativo',
        ]


class ServidorAlmoxarifadoForm(forms.ModelForm):

    class Meta:

        model = ServidorAlmoxarifado

        fields = [
            'nome',
            'matricula',
            'cargo',
            'setor',
            'telefone',
            'email',
            'ativo',
        ]


class RequisicaoForm(forms.ModelForm):

    class Meta:

        model = Requisicao

        fields = [
            'numero',
            'destino',
            'solicitante',
            'telefone',
            'observacao',
            'servidor_almoxarifado',
        ]

        widgets = {

            'observacao': forms.Textarea(
                attrs={
                    'rows': 3
                }
            )

        }


class ItemRequisicaoForm(forms.ModelForm):

    class Meta:

        model = ItemRequisicao

        fields = [
            'item',
            'quantidade_solicitada',
        ]

        widgets = {
            'item': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'quantidade_solicitada': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }

        labels = {
            'quantidade_solicitada': 'Quantidade',
        }