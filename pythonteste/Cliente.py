class Cliente:
    def __init__(self):
        self.nome = None:
        self.email = None:
        self.telefone = None:
        self._cupom_desconto = 0
    def get_cupom_desconto(self):
        return self._cupom_desconto
    def realizar_compras(self, lista_itens):
        pass
class ClienteVipPF(Cliente):
    def __init__(self):
        super().__init__()
        self._cupom_desconto = 0.2
