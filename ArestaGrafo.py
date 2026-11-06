def criar_grafo():
    """
    Cria e retorna uma estrutura de grafo com lista de arestas e lista de vértices.

    Passos:
    1. Criar uma lista vazia chamada 'vertices'.
    2. Criar uma lista vazia chamada 'arestas', onde cada elemento será uma lista de tamanho 2 (origem, destino)
    3. Retornar vertices e arestas
    """
    vertices = []
    arestas = []
    return vertices, arestas


def inserir_vertice(vertices, vertice):
    """
    Adiciona um novo vértice no grafo.

    Passos:
    1. Verificar se o vértice já existe em 'vertices'.
    2. Se não existir, adicionar à lista 'vertices'.
    """
    if vertice not in vertices:
        vertices.append(vertice)


def inserir_aresta(vertices, arestas, origem, destino, nao_direcionado=False):
    """
    Adiciona uma aresta entre dois vértices.

    Passos:
    1. Garantir que 'origem' e 'destino' existam em 'vertices'.
       - Se não existirem, chamar 'inserir_vertice' para adicioná-los.
    2. Adicionar uma lista [origem, destino] na lista 'arestas'.
    3. Se nao_direcionado=True, adicionar também [destino, origem].
    """
    if origem not in vertices:
        inserir_vertice(vertices, origem)
    if destino not in vertices:
        inserir_vertice(vertices, destino)
    
    if [origem, destino] not in arestas:
        arestas.append([origem, destino])
    
    if nao_direcionado:
        if [destino, origem] not in arestas:
            arestas.append([destino, origem])


def remover_aresta(arestas, origem, destino, nao_direcionado=False):
    """
    Remove uma aresta entre dois vértices.

    Passos:
    1. Percorrer a lista de Arestas procurando [origem, destino]
    2. Se encontrar, remover
    3. Se nao_direcionado=True, também procurar por [destino, origem]
    """
    removida = False
    if [origem, destino] in arestas:
        arestas.remove([origem, destino])
        removida = True
        
    if nao_direcionado:
        if [destino, origem] in arestas:
            arestas.remove([destino, origem])
            removida = True
            
    if removida:
        print(f"Aresta entre '{origem}' e '{destino}' removida com sucesso.")
    else:
        print("Aresta não encontrada.")


def remover_vertice(vertices, arestas, vertice):
    """
    Remove um vértice e todas as arestas conectadas a ele.

    Passos:
    1. Verificar se o vértice existe na lista de vertices.
    2. Caso encontrado, remover o vértice da lista 'vertices'.
    3. Percorrer a lista de 'arestas' e remover todas onde o vértice aparece
       como origem ou destino.
    """
    if vertice in vertices:
        vertices.remove(vertice)
        arestas_para_remover = [a for a in arestas if a[0] == vertice or a[1] == vertice]
        for a in arestas_para_remover:
            arestas.remove(a)
        print(f"Vértice '{vertice}' e respetivas arestas removidos com sucesso.")
    else:
        print(f"Vértice '{vertice}' não encontrado.")


def existe_aresta(arestas, origem, destino):
    """
    Verifica se existe uma aresta entre origem e destino.

    Passos:
    1. Percorrer a lista de aresta procurando [origem, destino]
    2. Retornar True se encontrar
    3. Caso não encontre na lista, retornar False no final.
    """
    for aresta in arestas:
        if aresta == [origem, destino]:
            return True
    return False


def vizinhos(vertices, arestas, vertice):
    """
    Retorna a lista de vizinhos (vértices alcançáveis a partir de 'vertice').

    Passos:
    1. Criar uma lista vazia chamada 'vizinhos'.
    2. Percorrer todas as arestas [origem, destino].
    3. Se origem == vertice, adicionar destino na lista de vizinhos.
    4. Retornar a lista final.
    """
    lista_vizinhos = []
    for origem, destino in arestas:
        if origem == vertice:
            if destino not in lista_vizinhos:
                lista_vizinhos.append(destino)
    return lista_vizinhos


def grau_vertices(vertices, arestas):
    """
    Calcula o grau de entrada, saída e total de cada vértice.

    Passos:
    1. Criar um dicionário vazio 'graus'.
    2. Percorrer todas as arestas [origem, destino]:
        I. Se o grafo for não direcionado:
            - incrementar grau analisando apenas se origem ou destino equivale ao vértice analisado
        II. Se o grafo for direcionado
            - Se o vértice for origem Incrementar grau de saída do vértice origem
            - Se o vértice for destino incrementar grau de entrada do vértice destino.
            - Calcular o grau total (entrada + saída).
    4. Retornar o dicionário 'graus' para cada vértice.
    """
    graus = {}
    for v in vertices:
        graus[v] = {"saida": 0, "entrada": 0, "total": 0}
        
    for origem, destino in arestas:
        if origem in graus:
            graus[origem]["saida"] += 1
        if destino in graus:
            graus[destino]["entrada"] += 1
            
    for v in vertices:
        total = graus[v]["saida"] + graus[v]["entrada"]
        graus[v]["total"] = total
        
    return graus


def percurso_valido(arestas, caminho):
    """
    Verifica se um percurso é possível (seguindo as arestas na ordem dada).

    Passos:
    1. Percorrer o caminho de 0 até len(caminho) - 2.
    2. Para cada par consecutivo (u, v):
        - Verificar se (u, v) existe na lista de 'arestas' (funcao existe_aresta).
        - Se alguma não existir, retornar False.
    3. Se todas existirem, retornar True.
    """
    if not caminho or len(caminho) < 2:
        return False
        
    for k in range(len(caminho) - 1):
        u = caminho[k]
        v = caminho[k+1]
        if not existe_aresta(arestas, u, v):
            return False
    return True


def listar_vizinhos(vertices, arestas, vertice):
    """
    Exibe os vizinhos de um vértice.

    Passos:
    1. Chamar a função vizinhos() para obter a lista.
    2. Exibir a lista formatada.
    """
    if vertice in vertices:
        lista = vizinhos(vertices, arestas, vertice)
        print(f"-> Vizinhos de '{vertice}': {lista}")
    else:
        print(f"Vértice '{vertice}' não encontrado.")


def exibir_grafo(vertices, arestas):
    """
    Exibe todas as arestas do grafo.

    Passos:
    1. Exibir a lista de vértices.
    2. Exibir todas as arestas no formato (origem -> destino).
    """
    print("\n--- Estrutura do Grafo (Lista de Arestas) ---")
    print(f"Vértices: {sorted(vertices)}")
    print("Arestas:")
    if not arestas:
        print("  (Nenhuma aresta registada)")
    else:
        for origem, destino in arestas:
            print(f"  {origem} -> {destino}")
    print("---------------------------------------------")


def main():
    vertices, arestas = criar_grafo()
    
    while True:
        print("\n================ MENU (LISTA DE ARESTAS) ================")
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
            exibir_grafo(vertices, arestas)
        elif opcao == '2':
            v = input("Digite o nome do vértice: ").strip()
            inserir_vertice(vertices, v)
            print(f"Vértice '{v}' inserido (ou já existia).")
        elif opcao == '3':
            origem = input("Vértice de origem: ").strip()
            destino = input("Vértice de destino: ").strip()
            nd_input = input("O grafo é não-direcionado? (s/n): ").strip().lower()
            nd = True if nd_input == 's' else False
            inserir_aresta(vertices, arestas, origem, destino, nao_direcionado=nd)
            print("Aresta processada com sucesso.")
        elif opcao == '4':
            v = input("Digite o vértice que deseja remover: ").strip()
            remover_vertice(vertices, arestas, v)
        elif opcao == '5':
            origem = input("Vértice de origem: ").strip()
            destino = input("Vértice de destino: ").strip()
            nd_input = input("Era não-direcionado? (s/n): ").strip().lower()
            nd = True if nd_input == 's' else False
            remover_aresta(arestas, origem, destino, nao_direcionado=nd)
        elif opcao == '6':
            v = input("Digite o vértice: ").strip()
            listar_vizinhos(vertices, arestas, v)
        elif opcao == '7':
            origem = input("Origem: ").strip()
            destino = input("Destino: ").strip()
            if existe_aresta(arestas, origem, destino):
                print(f"-> SIM, existe aresta de '{origem}' para '{destino}'.")
            else:
                print(f"-> NÃO existe aresta de '{origem}' para '{destino}'.")
        elif opcao == '8':
            graus = grau_vertices(vertices, arestas)
            print("\n--- Grau dos Vértices ---")
            for v, info in graus.items():
                print(f"Vértice '{v}': Saída = {info['saida']}, Entrada = {info['entrada']}, Total = {info['total']}")
            print("-------------------------")
        elif opcao == '9':
            caminho_str = input("Digite o percurso separado por espaços (ex: A B C): ").strip()
            if caminho_str:
                caminho = caminho_str.split()
                if percurso_valido(arestas, caminho):
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