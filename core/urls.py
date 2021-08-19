from django.urls import path

from .views import ClienteView, CreateClienteView, ProdutoView, CreateProdutoView, PedidosView, AbrirPedidosView,\
    UpdateClienteView, UpdateProdutoView, UpdatePedidosView, DeleteClienteView, DeleteProdutoView, DeletePedidoView

urlpatterns = [
    path('clientespage', ClienteView.as_view(), name='clientes_page'),
    path('addcliente', CreateClienteView.as_view(), name='add_cliente'),
    path('produtospage', ProdutoView.as_view(), name='produtos_page'),
    path('addproduto', CreateProdutoView.as_view(), name='add_produto'),
    path('pedidospage', PedidosView.as_view(), name='pedidos_page'),
    path('abrirpedido',  AbrirPedidosView.as_view(), name='abrir_pedido'),
    path('<int:pk>/updatecliente/',  UpdateClienteView.as_view(), name='update_cliente'),
    path('<int:pk>/updateproduto/',  UpdateProdutoView.as_view(), name='update_produto'),
    path('<int:pk>/updatepedido/',  UpdatePedidosView.as_view(), name='update_pedido'),
    path('<int:pk>/deletecliente/',  DeleteClienteView.as_view(), name='delete_cliente'),
    path('<int:pk>/deleteproduto/',  DeleteProdutoView.as_view(), name='delete_produto'),
    path('<int:pk>/deletepedido/',  DeletePedidoView.as_view(), name='delete_pedido'),
]