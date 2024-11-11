class FilaAtendimento:
    def __init__(self):
        self.fila = []

    def adicionar_cliente(self, nome):
        self.fila.append(nome)

    def atender_cliente(self):
        if self.fila:
            cliente_atendido = self.fila.pop(0)
            print(f"Atendendo cliente: {cliente_atendido}")
            return cliente_atendido
        else:
            print("Não há clientes na fila.")
            return None

    def tamanho_fila(self):
        return len(self.fila)
