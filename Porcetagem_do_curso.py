# Informações do curso
TOTAL_DISCIPLINAS = 45
CARGA_TOTAL = 3200
DISCIPLINAS_OBRIGATORIAS = 38
DISCIPLINAS_OPTATIVAS = 7

# Quantidade de disciplinas obrigatórias por semestre
DISCIPLINAS_POR_SEMESTRE = {
    1: 5, 2: 6, 3: 5, 4: 6,
    5: 4, 6: 4, 7: 4, 8: 3, 9: 1
}

# Inicializando os dados
disciplinas_feitas = {s: {"obrigatorias": []} for s in range(1, 10)}
optativas_feitas = []

# Função para salvar os relatórios em arquivo
def salvar_em_arquivo(caminho, conteudo):
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(conteudo)

# Função para adicionar disciplinas (obrigatórias ou optativas)
def adicionar_disciplina():
    print("\n=== Adicionar Disciplinas ===")
    semestre = int(input("Digite o semestre (1-9 para obrigatórias, 10 para optativas): "))
    
    if 1 <= semestre <= 9:
        while True:
            nome = input(f"Nome da disciplina do semestre {semestre} (ENTER para sair): ")
            if nome == "":
                break
            carga = int(input(f"Carga horária da disciplina {nome}: "))
            disciplinas_feitas[semestre]["obrigatorias"].append({"nome": nome, "carga": carga})
    elif semestre >= 10:
        while True:
            nome = input("Nome da optativa (ENTER para sair): ")
            if nome == "":
                break
            carga = int(input(f"Carga horária da optativa {nome}: "))
            optativas_feitas.append({"nome": nome, "carga": carga})
    else:
        print("Semestre inválido!\n")

# Ver disciplinas por semestre ou optativas
def ver_disciplinas():
    print("\n=== Ver Disciplinas ===")
    entrada = input("Digite o semestre (1-9) ou 'optativas': ")
    conteudo = ""

    if entrada == "optativas":
        if optativas_feitas:
            conteudo += "Optativas feitas:\n"
            for d in optativas_feitas:
                conteudo += f" - {d['nome']} ({d['carga']} hrs)\n"
            total_carga = sum(d["carga"] for d in optativas_feitas)
            conteudo += f"Total de carga horária das optativas: {total_carga} hrs\n"
        else:
            conteudo = "Nenhuma optativa cadastrada.\n"
        salvar_em_arquivo("disciplinas_por_semestre/disciplinas.txt", conteudo)
    else:
        try:
            semestre = int(entrada)
            if semestre in disciplinas_feitas:
                lista = disciplinas_feitas[semestre]["obrigatorias"]
                if lista:
                    conteudo += f"Disciplinas do semestre {semestre}:\n"
                    for d in lista:
                        conteudo += f" - {d['nome']} ({d['carga']} hrs)\n"
                    total = sum(d["carga"] for d in lista)
                    conteudo += f"Total de carga horária do semestre {semestre}: {total} hrs\n"
                else:
                    conteudo = f"Semestre {semestre} ainda não tem disciplinas registradas.\n"
                salvar_em_arquivo("disciplinas_por_semestre/disciplinas.txt", conteudo)
            else:
                print("Semestre inválido!\n")
        except ValueError:
            print("Entrada inválida!\n")

# Ver status geral do curso
def ver_status():
    print("\n=== Status do Curso ===")
    total_obrigatorias = sum(len(disciplinas_feitas[s]["obrigatorias"]) for s in disciplinas_feitas)
    carga_obrigatoria = sum(d["carga"] for s in disciplinas_feitas for d in disciplinas_feitas[s]["obrigatorias"])
    total_optativas = len(optativas_feitas)
    carga_optativas = sum(d["carga"] for d in optativas_feitas)
    carga_total = carga_obrigatoria + carga_optativas
    disciplinas_restantes = DISCIPLINAS_OBRIGATORIAS - total_obrigatorias
    optativas_restantes = DISCIPLINAS_OPTATIVAS - total_optativas
    porcentagem = (carga_total / CARGA_TOTAL) * 100

    conteudo = "--- STATUS DO CURSO ---\n"
    conteudo += f"Disciplinas obrigatórias feitas: {total_obrigatorias}\n"
    conteudo += f"Disciplinas obrigatórias restantes: {disciplinas_restantes}\n"
    conteudo += f"Optativas feitas: {total_optativas}/{DISCIPLINAS_OPTATIVAS}\n"
    conteudo += f"Optativas restantes: {optativas_restantes}\n"
    conteudo += f"Carga horária cumprida: {carga_total} hrs\n"
    conteudo += f"Porcentagem do curso concluída: {porcentagem:.2f}%\n"
    print(conteudo)
    salvar_em_arquivo("status_do_curso/status.txt", conteudo)

# Progresso por semestre
def tabela_progresso():
    print("\n=== Progresso por Semestre ===")
    conteudo = "--- TABELA DE PROGRESSO POR SEMESTRE ---\n"
    for semestre in range(1, 10):
        feitas = len(disciplinas_feitas[semestre]["obrigatorias"])
        previstas = DISCIPLINAS_POR_SEMESTRE[semestre]
        if feitas < previstas:
            status = "Atrasado"
        elif feitas > previstas:
            status = "Adiantado"
        else:
            status = "Correto"
        conteudo += f"Semestre {semestre}: {feitas}/{previstas} disciplinas obrigatórias ({status})\n"
    conteudo += f"\nOptativas feitas: {len(optativas_feitas)}/{DISCIPLINAS_OPTATIVAS} feitas\n"
    print(conteudo)
    salvar_em_arquivo("progresso_por_semestre/progresso.txt", conteudo)

# Menu principal
def menu():
    import os
    os.makedirs("disciplinas_por_semestre", exist_ok=True)
    os.makedirs("status_do_curso", exist_ok=True)
    os.makedirs("progresso_por_semestre", exist_ok=True)

    while True:
        print("\n" + "="*40)
        print("      CONTROLE DE CURSO - MENU")
        print("="*40)
        print("1. Adicionar disciplinas")
        print("2. Ver disciplinas por semestre ou optativas")
        print("3. Ver status geral do curso")
        print("4. Ver progresso por semestre")
        print("5. Sair")
        print("="*40)
        escolha = input("Escolha uma opção (1-5): ")
        print()

        if escolha == "1":
            adicionar_disciplina()
        elif escolha == "2":
            ver_disciplinas()
        elif escolha == "3":
            ver_status()
        elif escolha == "4":
            tabela_progresso()
        elif escolha == "5":
            print("Saindo... até a próxima!")
            break
        else:
            print("Opção inválida! Tente novamente.\n")

if __name__ == "__main__":
    menu()
