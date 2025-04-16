import json

# Função para ver disciplinas por semestre ou optativas
def ver_disciplinas():
    print("\n=== Ver Disciplinas ===")
    entrada = input("Digite o semestre (1-9) ou 'optativas' para ver as optativas: ")
    conteudo = ""

    if entrada == "optativas":
        # Verificando se existem optativas registradas
        if optativas_feitas:
            conteudo += "Optativas feitas:\n"
            for d in optativas_feitas:
                conteudo += f" - {d['nome']} ({d['carga']} hrs)\n"
            total_carga = sum(d["carga"] for d in optativas_feitas)
            conteudo += f"Total de carga horária das optativas: {total_carga} hrs\n"
        else:
            conteudo = "Nenhuma optativa cadastrada.\n"
        print(conteudo)
    
    else:
        try:
            semestre = int(entrada)  # Tentando converter a entrada para inteiro (semestre)
            if 1 <= semestre <= 9:  # Semestre válido (1-9)
                lista = disciplinas_feitas[semestre]["obrigatorias"]
                if lista:  # Se houver disciplinas registradas
                    conteudo += f"Disciplinas do semestre {semestre}:\n"
                    for d in lista:
                        conteudo += f" - {d['nome']} ({d['carga']} hrs)\n"
                    total = sum(d["carga"] for d in lista)
                    conteudo += f"Total de carga horária do semestre {semestre}: {total} hrs\n"
                else:
                    conteudo = f"Semestre {semestre} ainda não tem disciplinas registradas.\n"
                print(conteudo)
            else:
                print("Semestre inválido! Tente entre 1 e 9.\n")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número válido.\n")

# Função para adicionar disciplinas
def adicionar_disciplinas():
    print("\n=== Adicionar Disciplinas ===")
    semestre = int(input("Digite o semestre (1-9): "))
    nome = input("Nome da disciplina: ")
    carga = int(input("Carga horária da disciplina: "))
    tipo = input("Tipo (obrigatoria/optativa): ").lower()
    
    if tipo == "obrigatoria":
        disciplinas_feitas[semestre]["obrigatorias"].append({"nome": nome, "carga": carga})
    elif tipo == "optativa":
        optativas_feitas.append({"nome": nome, "carga": carga})
    else:
        print("Tipo de disciplina inválido. Use 'obrigatoria' ou 'optativa'.")
        return
    
    print(f"Disciplina {nome} adicionada com sucesso!")

# Função para mostrar o progresso do curso
def progresso_do_curso():
    print("\n=== Progresso do Curso ===")
    total_disciplinas = sum(DISCIPLINAS_POR_SEMESTRE.values())  # Total de disciplinas obrigatórias no curso
    disciplinas_feitas_count = sum(len(disciplinas_feitas[semestre]["obrigatorias"]) for semestre in range(1, 10))
    total_optativas = len(optativas_feitas)
    carga_obrigatoria = sum(d["carga"] for semestre in range(1, 10) for d in disciplinas_feitas[semestre]["obrigatorias"])
    carga_optativas = sum(d["carga"] for d in optativas_feitas)
    
    total_carga = carga_obrigatoria + carga_optativas
    porcentagem_concluida = (total_carga / 3200) * 100
    
    print(f"Disciplinas obrigatórias feitas: {disciplinas_feitas_count}/{total_disciplinas}")
    print(f"Optativas feitas: {total_optativas}/7")
    print(f"Carga horária total cumprida: {total_carga} hrs")
    print(f"Porcentagem concluída: {porcentagem_concluida:.2f}%")

# Função para mostrar o progresso por semestre
def tabela_progresso():
    print("\n=== Tabela de Progresso por Semestre ===")
    
    for semestre in range(1, 10):
        feitas = len(disciplinas_feitas[semestre]["obrigatorias"])
        previstas = DISCIPLINAS_POR_SEMESTRE[semestre]
        
        if feitas < previstas:
            status = "Atrasado"
        elif feitas > previstas:
            status = "Adiantado"
        else:
            status = "Correto"
        
        print(f"Semestre {semestre}: {feitas}/{previstas} disciplinas obrigatórias ({status})")
    
    print(f"\nOptativas: {len(optativas_feitas)}/7 optativas feitas.")

# Menu principal
def menu():
    while True:
        print("\n=== Menu ===")
        print("1. Adicionar Disciplinas")
        print("2. Ver Disciplinas por Semestre ou Optativas")
        print("3. Ver Progresso do Curso")
        print("4. Ver Tabela de Progresso por Semestre")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_disciplinas()
        elif opcao == "2":
            ver_disciplinas()
        elif opcao == "3":
            progresso_do_curso()
        elif opcao == "4":
            tabela_progresso()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

# Inicializando as variáveis
DISCIPLINAS_POR_SEMESTRE = {
    1: 5, 2: 6, 3: 5, 4: 6, 5: 4, 6: 4, 7: 4, 8: 3, 9: 1
}

# Carregando dados dos arquivos 
dados = {"disciplinas_feitas": {semestre: {"obrigatorias": []} for semestre in range(1, 10)}, "optativas_feitas": []}
disciplinas_feitas = dados["disciplinas_feitas"]
optativas_feitas = dados["optativas_feitas"]

# Rodando o menu
menu()
