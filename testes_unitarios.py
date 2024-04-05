from fila import Fila
from robo import RoboDeLimpeza

class TestFila:
    # Metodo para testar a funcionalidade de desinfileirar
    def test_desenfileirar(self):
        fila = Fila()
        
        # Enfileirando items (1, 2)
        fila.enfileirar(1)
        fila.enfileirar(2)
        
        # Verificar se os items que foram enfileirados antes, são desinfileirados na mesma ordem
        assert fila.desenfileirar() == 1
        assert fila.desenfileirar() == 2

        # Metodo para testar a funcionalidade de enfileirar e desinfileirar
    def test_enfileirar(self):
        fila = Fila()
        
        # Enfileirando items (1, 2)
        fila.enfileirar(1)
        
        assert fila.items[0] == 1
    
    # Funcao que irá testar a funcao 'vazia' da classe Fila que checa se a fila está vazia
    def test_vazia(self):
        fila = Fila()
        
        # Verificar se a fila está vazia
        assert fila.vazia() == True
        
        # Enfileirar um item e verificar se a fila está vazia [FALSE]
        fila.enfileirar(1)
        assert fila.vazia() == False
        
        # Desenfileirar o item e verificar se a fila está vazia novamente
        fila.desenfileirar()
        assert fila.vazia() == True

# Classe para testar os metodos do RoboDeLimpeza
class TestRobo:
    # Método para testar a adição de uma tarefa 
    def test_adicionar_tarefa(self):
        robo = RoboDeLimpeza()
        
        robo.adicionarTarefa("a")
        assert robo.fila_tarefas.items[0] == "a"
    
    # Método para testar a execução de próxima tarefa 
    def test_executar_proxima_tarefa(self):
        robo = RoboDeLimpeza()

        robo.adicionarTarefa("a")
        
        assert robo.executarProximaTarefa() == "a"
    
    # Método para testar executar todas tarefas 
    def test_executar_todas_tarefas(self):
        robo = RoboDeLimpeza()
        
        robo.adicionarTarefa("a")
        robo.adicionarTarefa("b")

        assert robo.executarTodasTarefas() == ["a", "b"]
    

# Executando os testes da Fila
test_fila = TestFila()
test_fila.test_desenfileirar()
test_fila.test_enfileirar()
test_fila.test_vazia()
        
# Executando os testes do Robo
test_robo = TestRobo()
test_robo.test_adicionar_tarefa()
test_robo.test_executar_proxima_tarefa()
test_robo.test_executar_todas_tarefas()

