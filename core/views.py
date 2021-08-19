from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Cliente, Produto, Pedido
from .forms import ProdutoModelForm

class ClienteView(ListView):
    models = Cliente
    template_name = 'clientes.html'
    queryset = Cliente.objects.all()
    context_object_name = 'clientes'


class ProdutoView(ListView):
    models = Produto
    template_name = 'produtos.html'
    queryset = Produto.objects.all()
    context_object_name = 'produtos'

class PedidosView(ListView):
    models = Pedido
    template_name = 'pedidos.html'
    queryset = Pedido.objects.all()
    context_object_name = 'pedidos'

class AbrirPedidosView(CreateView):
    models = Pedido
    template_name = 'abrir_pedido.html'
    fields = ['nome', 'cliente', 'produto', 'preco', 'quantidade',]
    queryset = Pedido.objects.all()
    success_url = reverse_lazy('abrir_pedido')

class CreateClienteView(CreateView):
    model = Cliente
    template_name = 'cliente_form.html'
    fields = ['nome',]
    success_url = reverse_lazy('clientes_page')

class CreateProdutoView(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'preco', 'multiplo']
    success_url = reverse_lazy('produtos_page')

class UpdateClienteView(UpdateView):
    models = Cliente
    template_name = 'cliente_form.html'
    fields = ['nome',]
    queryset = Cliente.objects.all()
    success_url = reverse_lazy('clientes_page')

class UpdateProdutoView(UpdateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'preco', 'multiplo']
    success_url = reverse_lazy('produtos_page')

class UpdatePedidosView(UpdateView):
    models = Pedido
    template_name = 'abrir_pedido.html'
    fields = ['nome', 'cliente', 'produto', 'preco', 'quantidade',]
    queryset = Pedido.objects.all()
    success_url = reverse_lazy('pedidos_page')

class DeleteClienteView(DeleteView):
    model = Cliente
    template_name = 'cliente_del.html'
    success_url = reverse_lazy('clientes_page')

class DeleteProdutoView(DeleteView):
    model = Produto
    template_name = 'produto_del.html'
    success_url = reverse_lazy('produtos_page')

class DeletePedidoView(DeleteView):
    model = Pedido
    template_name = 'pedido_del.html'
    success_url = reverse_lazy('pedidos_page')