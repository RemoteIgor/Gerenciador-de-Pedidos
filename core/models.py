from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    '''
    class Meta:
        verbose_name = 'Cliente'
        Verbose_name_plural = 'Clientes'
    '''
    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField('Preço Unitário', max_digits=8, decimal_places=2, null='True', validators=[MinValueValidator(0.01)])
    multiplo = models.IntegerField('multiplo',validators=[MinValueValidator(1)])

    '''
    class Meta:
        verbose_name = 'Produto'
        Verbose_name_plural = 'Produtos'
    '''
    def __str__(self):
        return f'{self.nome} {self.preco} {self.multiplo}'

variavel_global=0
def retorna_produto(value):
    global variavel_global
    variavel_global=value
    return value

def validate_even(value):
    multiplo = Produto.objects.get(id=variavel_global)
    multiplo=multiplo.multiplo
    if value % multiplo != 0:
        raise ValidationError(
            _('%(value)s não é um múltiplo válido do produto'),
            params={'value': value},
        )

class Pedido(models.Model):
    nome = models.CharField(max_length=100)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE,  validators=[retorna_produto])
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2, null='True', validators=[MinValueValidator(0.01)])
    quantidade = models.IntegerField('Quantidade', validators=[MinValueValidator(1), validate_even])


    '''
    class Meta:
        verbose_name = 'Pedido'
        Verbose_name_plural = 'Pedidos'
    '''
    def __str__(self):
        return f'{self.nome} {self.cliente} {self.produto} {self.preco} {self.quantidade}'
        #return  self.nome

