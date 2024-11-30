tarefas = []

# Função para adicionar uma nova tarefa
def adicionar_tarefa(titulo):
    tarefa = {
        'titulo': titulo,
        'status': 'pendente'
    }
    tarefas.append(tarefa)
    print(f"Tarefa '{titulo}' adicionada com sucesso!")

# Função para listar as tarefas
def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa disponível.")
        return

    print("Lista de tarefas:")
    for index, tarefa in enumerate(tarefas):
        print(f"{index + 1}. {tarefa['titulo']} - Status: {tarefa['status']}")

# Função para atualizar o status de uma tarefa
def atualizar_status(indice, novo_status):
    if indice < 1 or indice > len(tarefas):
        print("Índice inválido.")
        return

    tarefas[indice - 1]['status'] = novo_status
    print(f"Tarefa '{tarefas[indice - 1]['titulo']}' atualizada para '{novo_status}'.")

# Função para remover uma tarefa
def remover_tarefa(indice):
    if indice < 1 or indice > len(tarefas):
        print("Índice inválido.")
        return

    tarefa_removida = tarefas.pop(indice - 1)
    print(f"Tarefa '{tarefa_removida['titulo']}' removida com sucesso!")

# Função para listar tarefas por status
def listar_por_status(status):
    tarefas_filtradas = [t for t in tarefas if t['status'] == status]

    if not tarefas_filtradas:
        print(f"Nenhuma tarefa com status '{status}'.")
        return

    print(f"Tarefas com status '{status}':")
    for index, tarefa in enumerate(tarefas_filtradas):
        print(f"{index + 1}. {tarefa['titulo']}")

# Menu interativo para o usuário
def exibir_menu():
    while True:
        print("\n--- Gerenciador de Tarefas ---")
        print("1. Adicionar tarefa")
        print("2. Listar todas as tarefas")
        print("3. Atualizar status de uma tarefa")
        print("4. Remover tarefa")
        print("5. Listar tarefas por status")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")

        match opcao:
            case '1':
                titulo = input("Digite o título da tarefa: ")
                adicionar_tarefa(titulo)
            case '2':
                listar_tarefas()
            case '3':
                listar_tarefas()
                indice = int(input("Digite o número da tarefa que deseja atualizar: "))
                novo_status = input("Digite o novo status: ").lower()
                atualizar_status(indice, novo_status)
            case '4':
                listar_tarefas()
                indice = int(input("Digite o número da tarefa que deseja remover: "))
                remover_tarefa(indice)
            case '5':
                status = input("Digite o status para filtrar: ").lower()
                listar_por_status(status)
            case '6':
                print("Saindo...")
                break
            case _:
                print("Opção inválida! Tente novamente.")


exibir_menu()
