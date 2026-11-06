def criar_grafo():
    """
    Cria e retorna uma matriz de adjacência vazia e uma lista de vértices.

    Passos:
    1. Criar uma lista vazia chamada matriz (para armazenar as conexões).
    2. Criar uma lista vazia chamada vertices (para armazenar os nomes dos vértices).
    3. Retornar (matriz, vertices).
    """
    matriz = []
    vertices = []
    return matriz, vertices


def inserir_vertice(matriz, vertices, vertice):
    """
    Adiciona um novo vértice ao grafo.

    Passos:
    1. Verificar se o vértice já existe em 'vertices'.
    2. Caso não exista:
        - Adicionar o vértice à lista 'vertices'.
        - Aumentar o tamanho da matriz:
            a) Para cada linha existente, adicionar um valor 0 no final (nova coluna).
            b) Adicionar uma nova linha com zeros do tamanho atualizado.
    """
    if vertice not in vertices:
        vertices.append(vertice)
        # Para cada linha existente, adicionar um 0 no final
        for linha in matriz:
            linha.append(0)
        # Adicionar uma nova linha com zeros do tamanho atualizado
        nova_linha = [0] * len(vertices)
        matriz.append(nova_linha)


def inserir_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
    """
    Adiciona uma aresta entre dois vértices.

    Passos:
    1. Garantir que 'origem' e 'destino' existam em 'vertices':
        - Se não existirem, chamar 'inserir_vertice' para adicioná-los.
    2. Localizar o índice da origem (i) e do destino (j).
    3. Marcar a conexão na matriz: matriz[i][j] = 1.
    4. Se nao_direcionado=True, também marcar a conexão inversa matriz[j][i] = 1.
    """
    if origem not in vertices:
        inserir_vertice(matriz, vertices, origem)
    if destino not in vertices:
        inserir_vertice(matriz, vertices, destino)
    
    i = vertices.index(origem)
    j = vertices.index(destino)
    matriz[i][j] = 1
    if nao_direcionado:
        matriz[j][i] = 1


def remover_vertice(matriz, vertices, vertice):
    """
    Remove um vértice e todas as arestas associadas.

    Passos:
    1. Verificar se o vértice existe em 'vertices'.
    2. Caso exista:
        - Descobrir o índice correspondente (usando vertices.index(vertice)).
        - Remover a linha da matriz na posição desse índice.
        - Remover a coluna (mesmo índice) de todas as outras linhas.
        - Remover o vértice da lista 'vertices'.
    """
    if vertice in vertices:
        i = vertices.index(vertice)
        # Remover a linha correspondente
        matriz.pop(i)
        # Remover a coluna i de todas as outras linhas
        for linha in matriz:
            linha.pop(i)
        # Remover o vértice da lista
        vertices.pop(i)
        print(f"Vértice '{vertice}' removido com sucesso.")
    else:
        print(f"Vértice '{vertice}' não encontrado.")


def remover_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
    """
    Remove uma aresta entre dois vértices.

    Passos:
    1. Verificar se ambos os vértices existem.
    2. Localizar os índices (i e j).
    3. Remover a aresta: matriz[i][j] = 0.
    4. Se nao_direcionado=True, também remover a inversa: matriz[j][i] = 0.
    """
    if origem in vertices and destino in vertices:
        i = vertices.index(origem)
        j = vertices.index(destino)
        matriz[i][j] = 0
        if nao_direcionado:
            matriz[j][i] = 0
        print(f"Aresta entre '{origem}' e '{destino}' removida com sucesso.")
    else:
        print("Um ou ambos os vértices não foram encontrados.")


def existe_aresta(matriz, vertices, origem, destino):
    """
    Verifica se existe uma aresta direta entre dois vértices.

    Passos:
    1. Verificar se ambos os vértices existem em 'vertices'.
    2. Obter os índices (i, j).
    3. Retornar True se matriz[i][j] == 1, caso contrário False.
    """
    if origem in vertices and destino in vertices:
        i = vertices.index(origem)
        j = vertices.index(destino)
        return matriz[i][j] == 1
    return False


def vizinhos(matriz, vertices, vertice):
    """
    Retorna a lista de vizinhos (vértices alcançáveis a partir de 'vertice').

    Passos:
    1. Verificar se 'vertice' existe em 'vertices'.
    2. Obter o índice 'i' correspondente.
    3. Criar uma lista de vizinhos vazia
    4. Para cada item da linha matriz[i], verificar se == 1
        - Adicionar o vértice correspondente na lista de vizinhos
    5. Retornar essa lista.
    """
    if vertice not in vertices:
        return []
    i = vertices.index(vertice)
    lista_vizinhos = []
    for j, val in enumerate(matriz[i]):
        if val == 1:
            lista_vizinhos.append(vertices[j])
    return lista_vizinhos


def grau_vertices(matriz, vertices):
    """
    Calcula o grau de entrada, saída e total de cada vértice.

    Passos:
    1. Criar um dicionário vazio 'graus'.
    2. Para cada vértice i:
        - Se o grafo for direcionado:
            - Grau de saída: somar os valores da linha i.
            - Grau de entrada: somar os valores da coluna i.
            - Grau total = entrada + saída.
        - Se não:
            - calcular apenas o grau de saida ou entrada
    3. Armazenar no dicionário no formato:
        graus[vértice] = {"saida": x, "entrada": y, "total": z} ou graus[vértice] = x.
    4. Retornar 'graus'.
    """
    graus = {}
    for idx, v in enumerate(vertices):
        saida = sum(matriz[idx])
        entrada = sum(matriz[i][idx] for i in range(len(vertices)))
        total = entrada + saida
        graus[v] = {"saida": saida, "entrada": entrada, "total": total}
    return graus


def percurso_valido(matriz, vertices, caminho):
    """
    Verifica se um percurso (sequência de vértices) é possível no grafo.

    Passos:
    1. Percorrer a lista 'caminho' de forma sequencial (de 0 até len-2).
    2. Para cada par consecutivo (u, v):
        - Verificar se existe_aresta(matriz, vertices, u, v) é True.
        - Se alguma não existir, retornar False.
    3. Se todas existirem, retornar True.
    """
    if not caminho:
        return False
    for k in range(len(caminho) - 1):
        u = caminho[k]
        v = caminho[k+1]
        if not existe_aresta(matriz, vertices, u, v):
            return False
    return True


def listar_vizinhos(matriz, vertices, vertice):
    """
    Exibe (ou retorna) os vizinhos de um vértice.

    Passos:
    1. Verificar se o vértice existe.
    2. Chamar a função vizinhos() para obter a lista.
    3. Exibir a lista formatada (ex: print(f"Vizinhos de {v}: {lista}")).
    """
    if vertice in vertices:
        lista = vizinhos(matriz, vertices, vertice)
        print(f"-> Vizinhos de '{vertice}': {lista}")
    else:
        print(f"Vértice '{vertice}' não encontrado.")


def exibir_grafo(matriz, vertices):
    """
    Exibe o grafo em formato de matriz de adjacência.

    Passos:
    1. Exibir cabeçalho com o nome dos vértices.
    2. Para cada linha i:
        - Mostrar o nome do vértice.
        - Mostrar os valores da linha (0 ou 1) separados por espaço.
    """
    if not vertices:
        print("\nO grafo está vazio.")
        return
    
    print("\n--- Matriz de Adjacência ---")
    cabecalho = "     " + " ".join(f"{v:>3}" for v in vertices)
    print(cabecalho)
    for i, v in enumerate(vertices):
        linha_str = " ".join(f"{matriz[i][j]:3}" for j in range(len(vertices)))
        print(f"{v:>3}: {linha_str}")
    print("-" * 30)


def main():
    matriz, vertices = criar_grafo()
    
    while True:
        print("\n================ MENU (MATRIZ DE ADJACÊNCIA) ================")
        print("1. Exibir o Grafo")
        print("2. Inserir Vértice")
        print("3. Inserir Aresta")
        print("4. Remover Vértice")
        print("5. Remover Aresta")
        print("6. Listar Vizinhos de um Vértice")
        print("7. Verificar se Existe Aresta")
        print("8. Exibir Grau dos Vértices")
        print("9. Verificar se Percurso é Válido")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            exibir_grafo(matriz, vertices)
        elif opcao == '2':
            v = input("Digite o nome do vértice: ").strip()
            inserir_vertice(matriz, vertices, v)
            print(f"Vértice '{v}' inserido (ou já existia).")
        elif opcao == '3':
            origem = input("Vértice de origem: ").strip()
            destino = input("Vértice de destino: ").strip()
            nd_input = input("O grafo é não-direcionado? (s/n): ").strip().lower()
            nd = True if nd_input == 's' else False
            inserir_aresta(matriz, vertices, origem, destino, nao_direcionado=nd)
            print("Aresta processada com sucesso.")
        elif opcao == '4':
            v = input("Digite o vértice que deseja remover: ").strip()
            remover_vertice(matriz, vertices, v)
        elif opcao == '5':
            origem = input("Vértice de origem: ").strip()
            destino = input("Vértice de destino: ").strip()
            nd_input = input("Era não-direcionado? (s/n): ").strip().lower()
            nd = True if nd_input == 's' else False
            remover_aresta(matriz, vertices, origem, destino, nao_direcionado=nd)
        elif opcao == '6':
            v = input("Digite o vértice: ").strip()
            listar_vizinhos(matriz, vertices, v)
        elif opcao == '7':
            origem = input("Origem: ").strip()
            destino = input("Destino: ").strip()
            if existe_aresta(matriz, vertices, origem, destino):
                print(f"-> SIM, existe aresta direta de '{origem}' para '{destino}'.")
            else:
                print(f"-> NÃO existe aresta direta de '{origem}' para '{destino}'.")
        elif opcao == '8':
            graus = grau_vertices(matriz, vertices)
            print("\n--- Grau dos Vértices ---")
            for v, info in graus.items():
                print(f"Vértice '{v}': Saída = {info['saida']}, Entrada = {info['entrada']}, Total = {info['total']}")
            print("-------------------------")
        elif opcao == '9':
            caminho_str = input("Digite o percurso separado por espaços (ex: A B C): ").strip()
            if caminho_str:
                caminho = caminho_str.split()
                if percurso_valido(matriz, vertices, caminho):
                    print(f"-> O percurso {' -> '.join(caminho)} é VÁLIDO!")
                else:
                    print(f"-> O percurso {' -> '.join(caminho)} NÃO é válido.")
            else:
                print("Caminho vazio.")
        elif opcao == '0':
            print("Encerrando o programa. Bom trabalho!")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()