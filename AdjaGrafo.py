def criar_grafo():
    """Cria e retorna um dicionário vazio para representar o grafo."""
    return {}

def inserir_vertice(grafo, v):
    """Insere um vértice no grafo se ele ainda não existir."""
    if v not in grafo:
        grafo[v] = []

def inserir_aresta(grafo, origem, destino, nao_direcionado=True):
    """Insere uma aresta entre a origem e o destino."""
    inserir_vertice(grafo, origem)
    inserir_vertice(grafo, destino)
    
    if destino not in grafo[origem]:
        grafo[origem].append(destino)
        
    if nao_direcionado and origem not in grafo[destino]:
        grafo[destino].append(origem)

def remover_vertice(grafo, v):
    """Remove um vértice e todas as arestas associadas a ele."""
    if v in grafo:
        # Remove o vértice do dicionário principal
        del grafo[v]
        # Remove todas as referências a ele nos vizinhos dos outros vértices
        for vertice in grafo:
            if v in grafo[vertice]:
                grafo[vertice].remove(v)
        print(f"Vértice '{v}' removido com sucesso.")
    else:
        print(f"Vértice '{v}' não encontrado no grafo.")

def remover_aresta(grafo, origem, destino, nao_direcionado=True):
    """Remove uma aresta entre a origem e o destino."""
    removido = False
    if origem in grafo and destino in grafo[origem]:
        grafo[origem].remove(destino)
        removido = True
        
    if nao_direcionado and destino in grafo and origem in grafo[destino]:
        grafo[destino].remove(origem)
        removido = True
        
    if removido:
        print(f"Aresta entre '{origem}' e '{destino}' removida com sucesso.")
    else:
        print("Aresta não encontrada.")

def exibir_grafo(grafo):
    """Exibe a lista de adjacências do grafo."""
    if not grafo:
        print("\nO grafo está vazio.")
        return
    
    print("\n--- Estrutura do Grafo (Lista de Adjacência) ---")
    for v in sorted(grafo.keys()):
        print(f"Vértice {v} -> Vizinhos: {grafo[v]}")
    print("-----------------------------------------------")

def listar_vizinhos(grafo, v):
    """Lista todos os vizinhos de um determinado vértice."""
    if v in grafo:
        print(f"-> Vizinhos do vértice '{v}': {grafo[v]}")
    else:
        print(f"Vértice '{v}' não encontrado.")

def existe_aresta(grafo, origem, destino):
    """Retorna True se existe uma aresta direta entre origem e destino."""
    if origem in grafo and destino in grafo[origem]:
        return True
    return False

def grau_vertices(grafo):
    """Exibe o grau de cada vértice do grafo."""
    if not grafo:
        print("\nO grafo está vazio.")
        return
    
    print("\n--- Grau dos Vértices ---")
    for v in sorted(grafo.keys()):
        grau = len(grafo[v])
        print(f"Vértice '{v}': grau {grau}")
    print("-------------------------")

def percurso_valido(grafo, caminho):
    """Verifica se um dado caminho (lista de vértices) é válido no grafo."""
    if not caminho:
        return False
    
    for i in range(len(caminho) - 1):
        origem = caminho[i]
        destino = caminho[i+1]
        if not existe_aresta(grafo, origem, destino):
            return False
    return True

def main():
    """Menu interativo para gerenciar o grafo."""
    grafo = criar_grafo()
    
    while True:
        print("\n================ MENU GRAFO ================")
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
            exibir_grafo(grafo)
        elif opcao == '2':
            v = input("Digite o nome do vértice: ").strip()
            inserir_vertice(grafo, v)
            print(f"Vértice '{v}' inserido (ou já existia).")
        elif opcao == '3':
            origem = input("Vértice de origem: ").strip()
            destino = input("Vértice de destino: ").strip()
            nd_input = input("O grafo é não-direcionado? (s/n): ").strip().lower()
            nd = True if nd_input == 's' else False
            inserir_aresta(grafo, origem, destino, nao_direcionado=nd)
            print("Aresta processada com sucesso.")
        elif opcao == '4':
            v = input("Digite o vértice que deseja remover: ").strip()
            remover_vertice(grafo, v)
        elif opcao == '5':
            origem = input("Vértice de origem: ").strip()
            destino = input("Vértice de destino: ").strip()
            nd_input = input("Era não-direcionado? (s/n): ").strip().lower()
            nd = True if nd_input == 's' else False
            remover_aresta(grafo, origem, destino, nao_direcionado=nd)
        elif opcao == '6':
            v = input("Digite o vértice: ").strip()
            listar_vizinhos(grafo, v)
        elif opcao == '7':
            origem = input("Origem: ").strip()
            destino = input("Destino: ").strip()
            if existe_aresta(grafo, origem, destino):
                print(f"-> SIM, existe aresta direta de '{origem}' para '{destino}'.")
            else:
                print(f"-> NÃO existe aresta direta de '{origem}' para '{destino}'.")
        elif opcao == '8':
            grau_vertices(grafo)
        elif opcao == '9':
            caminho_str = input("Digite o percurso separado por espaços (ex: A B C): ").strip()
            if caminho_str:
                caminho = caminho_str.split()
                if percurso_valido(grafo, caminho):
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