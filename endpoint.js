// Imports
const express = require('express');
const app = express();

// Definir o método GET com a rota /executar_todas_tarefas com o 
app.get('/executar_todas_tarefas', (req, res) => {
    // Constante que irá guardar todas as tarefas a serem executadas pelo robo
    const tarefas = filaDeTarefas.executarTodasTarefas();

    if (tarefas.length > 0) {
        // Se as tarefas foram executadas, retornar status 200 OK com as lista de tarefas executadas
        res.status(200).json({
            mensagem: "Todas as tarefas foram executadas com sucesso.",
            tarefasExecutadas: tarefas
        });
    } else {
        // Se não tiverem tarefas para serem executadas, retornar status 204 No Content
        res.status(204).json({
            mensagem: "Não há tarefas pendentes a serem executadas",
            tarefasExecutadas: []
        });
    }
});

// Iniciar o servidor na porta 3000
const PORT = 3000;
app.listen(PORT, () => {
});
