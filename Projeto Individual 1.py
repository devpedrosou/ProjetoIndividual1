# Lista de resultados
lista_resultados = [
    "e8_t9_p7_s5",
    "e6_t6_p6_s6",
    "e4_t5_p3_s8",
    "e9_t7_p8_s9",
    "e2_t4_p1_s3"
]

# Função para buscar candidatos de acordo com os critérios
def buscar_candidatos(lista, criterios):
    return [f'Candidato {i + 1}' for i, resultado in enumerate(lista)
            if all(int(nota[1:]) >= criterios[chave] for nota, chave in zip(resultado.split('_'), ['e', 't', 'p', 's']))]

# Função para adicionar um novo resultado à lista
def adicionar_resultado(lista, resultado):
    lista.append(resultado)

# Perguntar ao usuário se deseja adicionar um novo candidato
adicionar_novo = input("Deseja adicionar um novo candidato? (s/n): ")

if adicionar_novo.lower() == 's':
    try:
        # Solicitar as notas do novo usuário
        entrevista = int(input("Nota da entrevista: "))
        teste_teórico = int(input("Nota do teste teórico: "))
        teste_prático = int(input("Nota do teste prático: "))
        soft_skills = int(input("Nota das soft skills: "))
    except ValueError:
        print("Por favor, insira apenas números inteiros para as notas.")
        exit()

    # Construir o resultado para o novo usuário e adicioná-lo à lista de resultados
    novo_resultado = f"e{entrevista}_t{teste_teórico}_p{teste_prático}_s{soft_skills}"
    adicionar_resultado(lista_resultados, novo_resultado)

    # Exibir mensagem indicando que o novo usuário foi adicionado
    print("Novo candidato adicionado com sucesso!")

# Solicitar critérios ao usuário e converter para inteiros
criterios = {}
try:
    for chave, pergunta in [('e', 'entrevista'), ('t', 'teste teórico'), ('p', 'teste prático'), ('s', 'soft skills')]:
        criterios[chave] = int(input(f"Nota mínima para {pergunta}: "))
except ValueError:
    print("Por favor, insira apenas números inteiros.")
    exit()

# Buscar candidatos compatíveis
candidatos_encontrados = buscar_candidatos(lista_resultados, criterios)

# Exibir candidatos compatíveis encontrados
if candidatos_encontrados:
    print("\nCandidatos compatíveis encontrados:")
    print(*candidatos_encontrados, sep="\n")
else:
    print("\nNenhum candidato compatível encontrado.")
