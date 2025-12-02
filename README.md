# ✅ Gerenciador de Tarefas (To-Do List) - Python

Um sistema de gerenciamento de tarefas via terminal aplicando o conceito de **CRUD** (Create, Read, Update, Delete). O projeto permite controle total sobre uma lista de atividades em tempo de execução.

## 🛠️ Funcionalidades (CRUD)

- [x] **Create (Adicionar):** Insere novas tarefas na lista dinâmica.
- [x] **Read (Listar):** Exibe todas as tarefas cadastradas com numeração humanizada (iniciando em 1).
- [x] **Update (Concluir):** Permite marcar uma tarefa como realizada `[x]`, alterando a string original sem perder a informação.
- [x] **Delete (Remover):** Utiliza o método `.pop()` para excluir tarefas definitivamente e reorganizar os índices da lista.

## ⚙️ Lógica Implementada

* **Conversão de Índices:** Algoritmo que traduz a entrada do usuário (ex: tarefa 1) para o índice real da lista (índice 0).
* **Validação de Intervalo:** Proteção lógica que impede o usuário de tentar acessar ou remover tarefas que não existem, evitando erros de `IndexError`.
* **Menu Cíclico:** Loop infinito que mantém o programa rodando até o comando de saída.

## 💻 Como rodar

```bash
git clone [https://github.com/Felipedev-git/Gerenciador-Tarefas-Python.git](https://github.com/Felipedev-git/Gerenciador-Tarefas-Python.git)
cd Gerenciador-Tarefas-Python
python todo_list.py
Desenvolvido por Felipe de Campos 🦁
