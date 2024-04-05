from fila import Fila

class RoboDeLimpeza:
    # Construtor do Robo, inicializando as variáveis. Nesse caso apenas a fila é usada como uma variável
    def __init__(self):
        self.fila_tarefas = Fila()

    # Método para adicionar tarefa a fila de uma instância do Robo
    def adicionarTarefa(self, tarefa):
        """
        Objetivo: Adiciona uma tarefa à fila de tarefas.

        :param tarefa: A tarefa a ser adicionada. Representada como uma string.
        :return: None
        """
        self.fila_tarefas.enfileirar(tarefa)

    # Método que executa a proxima tarefa do robo. A fila é checada para ver se está vazia: se não estiver, a tarefa é executada.
    def executarProximaTarefa(self):
        """
        Executa a próxima tarefa na fila. A execução pode consistir na impressão em console.

        :return: O nome da tarefa executada. Representada como string.

        :raises Exception: Se a fila de tarefas estiver vazia.
        """
        if not self.fila_tarefas.vazia():
            print(self.fila_tarefas.items[0])
            return self.fila_tarefas.desenfileirar()
        else:
            raise Exception("Fila de tarefas vazia")

    # Método que executa todas as tarefas pendentes do robo e retorna a lista de todas tarefas executadas.
    def executarTodasTarefas(self):
        """
        Executa todas as tarefas na fila, uma a uma, até a fila estar vazia.

        :return: Lista de tarefas executadas. Lista de strings.
        """
        tarefas_executadas = []
        while not self.fila_tarefas.vazia():
            tarefa_executada = self.executarProximaTarefa()
            tarefas_executadas.append(tarefa_executada)
        return tarefas_executadas


