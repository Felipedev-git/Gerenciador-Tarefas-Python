tarefa = []


while True:
    
    print('\n1. Adicionar Tarefa \n2. Listar Tarefas \n3. Marcar como Concluída \n4. Remover Tarefa \n5. Sair')
    opcao = input('Como gostaria de prosseguir? ')
     
    if opcao == '1':
        usta = input('Qual tarefa gostaria de adicionar? ').upper()
        tarefa.append(f'{usta}')
        print(f'Tarefa adicionada {usta}. ')
    elif opcao == '2':
        for i in range(len(tarefa)):
            print(f'{i + 1}. {tarefa[i]}')
    elif opcao == '3':
        for i in range(len(tarefa)):
            print(f'{i + 1}. {tarefa[i]}')
        try:    
            confirm = int(input('Qual tarefa gostaria de concluir? '))
        except (ValueError):
            print('Erro: USE AS OPÇÕES DO MENU! ')
            continue
        indice = confirm - 1
        if 0 <= indice < len(tarefa):
            tarefa[indice] = '[x]' + tarefa[indice]
        else:
            print('Tarefa não encontrada! ')
            continue
    elif opcao == '4':
        for i in range(len(tarefa)):
            print(f'{i + 1}. {tarefa[i]}')
        try:
            remove = int(input('Qual tarefa gostaria de remover? '))
        except(ValueError):
            print('ERRO: USE AS OPÇÕES DO MENU!')
            continue
        indice2 = remove - 1
        if 0 <= indice2 < len(tarefa):
            tarefa.pop(indice2)
        else:
            print('Tarefa não encontrada! ')
    elif opcao == '5':
        print('Obrigado por utilizar! ')
        break
    else:
        print('Escolha uma opção do menu! ')
        continue 
        
        

            
    
        

        
