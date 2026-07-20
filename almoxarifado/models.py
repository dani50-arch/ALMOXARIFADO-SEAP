from django.db import models
from django.db.models import Sum


class Categoria(models.Model):

    nome = models.CharField(
        max_length=100,
        unique=True
    )

    descricao = models.TextField(
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Setor(models.Model):

    nome = models.CharField(
        max_length=100,
        unique=True
    )

    sigla = models.CharField(
        max_length=20,
        blank=True
    )

    descricao = models.TextField(
        blank=True
    )

    ativo = models.BooleanField(
        default=True
    )

    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class ServidorAlmoxarifado(models.Model):

    nome = models.CharField(
        max_length=150
    )

    matricula = models.CharField(
        max_length=30,
        unique=True
    )

    cargo = models.CharField(
        max_length=100
    )

    setor = models.ForeignKey(
        Setor,
        on_delete=models.PROTECT
    )

    telefone = models.CharField(
        max_length=20,
        blank=True
    )

    email = models.EmailField(
        blank=True
    )

    ativo = models.BooleanField(
        default=True
    )

    class Meta:
        verbose_name = 'Servidor do Almoxarifado'
        verbose_name_plural = 'Servidores do Almoxarifado'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Destino(models.Model):

    TIPO_CHOICES = (
        ('SA', 'Setor Administrativo'),
        ('UP', 'Unidade Prisional'),
        ('OU', 'Outro'),
    )

    tipo = models.CharField(
        max_length=2,
        choices=TIPO_CHOICES
    )

    nome = models.CharField(
        max_length=150,
        unique=True
    )

    cidade = models.CharField(
        max_length=100,
        blank=True
    )

    responsavel = models.CharField(
        max_length=150,
        blank=True
    )

    telefone = models.CharField(
        max_length=20,
        blank=True
    )

    email = models.EmailField(
        blank=True
    )

    ativo = models.BooleanField(
        default=True
    )

    class Meta:
        verbose_name = 'Destino'
        verbose_name_plural = 'Destinos'
        ordering = ['nome']

    def __str__(self):
        return f'{self.nome} ({self.get_tipo_display()})'


class Requisicao(models.Model):

    STATUS_CHOICES = (
        ('SOLICITADA', 'Solicitada'),
        ('SEPARACAO', 'Em Separação'),
        ('ATENDIDA', 'Atendida'),
        ('CANCELADA', 'Cancelada'),
    )

    numero = models.CharField(
        max_length=20,
        unique=True
    )

    data_requisicao = models.DateTimeField(
        auto_now_add=True
    )

    destino = models.ForeignKey(
        Destino,
        on_delete=models.PROTECT,
        related_name='requisicoes',
        verbose_name='Destino'
    )

    solicitante = models.CharField(
        max_length=150
    )

    telefone = models.CharField(
        max_length=20,
        blank=True
    )

    observacao = models.TextField(
        blank=True
    )

    servidor_almoxarifado = models.ForeignKey(
        ServidorAlmoxarifado,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='requisicoes_atendidas'
    )

    data_atendimento = models.DateTimeField(
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='SOLICITADA'
    )

    class Meta:
        verbose_name = 'Requisição'
        verbose_name_plural = 'Requisições'
        ordering = ['-data_requisicao']

    def __str__(self):
        return self.numero


class Item(models.Model):

    codigo = models.CharField(
        max_length=50,
        unique=True
    )

    descricao = models.CharField(
        max_length=255
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT
    )

    unidade_medida = models.CharField(
        max_length=20
    )

    estoque_minimo = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    ativo = models.BooleanField(
        default=True
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'
        ordering = ['descricao']

    def __str__(self):
        return f"{self.codigo} - {self.descricao}"

    def saldo_atual(self):

        entradas = (
            self.movimentacaoestoque_set
            .filter(tipo='E')
            .aggregate(total=Sum('quantidade'))
        )['total'] or 0

        saidas = (
            self.movimentacaoestoque_set
            .filter(tipo='S')
            .aggregate(total=Sum('quantidade'))
        )['total'] or 0

        return entradas - saidas


class Fornecedor(models.Model):

    razao_social = models.CharField(
        max_length=255
    )

    cnpj = models.CharField(
        max_length=18,
        unique=True
    )

    telefone = models.CharField(
        max_length=20,
        blank=True
    )

    email = models.EmailField(
        blank=True
    )

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        ordering = ['razao_social']

    def __str__(self):
        return self.razao_social


class ItemRequisicao(models.Model):

    requisicao = models.ForeignKey(
        Requisicao,
        on_delete=models.CASCADE,
        related_name='itens'
    )

    item = models.ForeignKey(
        Item,
        on_delete=models.PROTECT
    )

    quantidade_solicitada = models.PositiveIntegerField()

    quantidade_atendida = models.PositiveIntegerField(
        default=0
    )

    observacao = models.CharField(
        max_length=255,
        blank=True
    )

    class Meta:
        verbose_name = 'Item da Requisição'
        verbose_name_plural = 'Itens da Requisição'
        ordering = ['id']

    def __str__(self):
        return (
            f'{self.item.descricao} '
            f'({self.quantidade_solicitada})'
        )


class MovimentacaoEstoque(models.Model):

    TIPO_CHOICES = (
        ('E', 'Entrada'),
        ('S', 'Saída'),
    )

    tipo = models.CharField(
        max_length=1,
        choices=TIPO_CHOICES
    )

    destino = models.ForeignKey(
        Destino,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name='Destino'
    )

    item = models.ForeignKey(
        Item,
        on_delete=models.PROTECT
    )

    fornecedor = models.ForeignKey(
        Fornecedor,
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )

    quantidade = models.PositiveIntegerField()

    responsavel = models.CharField(
        max_length=100,
        blank=True
    )

    documento = models.CharField(
        max_length=50,
        blank=True
    )

    data_movimentacao = models.DateTimeField(
        auto_now_add=True
    )

    observacao = models.TextField(
        blank=True
    )

    class Meta:
        verbose_name = 'Movimentação de Estoque'
        verbose_name_plural = 'Movimentações de Estoque'
        ordering = ['-data_movimentacao']

    def __str__(self):
        return (
            f"{self.get_tipo_display()} - "
            f"{self.item.descricao}"
        )