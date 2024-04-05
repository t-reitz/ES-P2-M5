class Fila:
    # Construtor para inicializar os atributos de fila, nesse caso os itens
    def __init__(self):
        self.items = []

    # Método para enfileirar os items (postos no final da lista)
    def enfileirar(self, item):
        self.items.append(item)

    # Método para retirar o primeiro item da lista e retorna-lo
    def desenfileirar(self):
        if self.vazia():
            raise Exception("A fila está vazia")
        return self.items.pop(0)

    # Método que verifica se a lista está vazia de itens e retorna True se sim, e False se não
    def vazia(self):
        if len(self.items) == 0:
            return True
        else: 
            return False

