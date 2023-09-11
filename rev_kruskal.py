#Algoritmo de Kruskal que remove as arestas de maior peso que não deixam o grafo desconexo.

class Grafo:

    #Define os vértices e arestas
    def __init__(self, vertices):
        self.V = vertices
        self.adj = vertices * [0]
        self.arestas = []

        for i in range(vertices):
            self.adj[i] = []

    # u-->v = caminho / w = distância
    def add_aresta(self, u, v, w):
        #Adiciona a direção de u->v e v->u
        self.adj[u].append(v)
        self.adj[v].append(u)
        self.arestas.append((w, (u,v))) # Adiciona o peso de u->v


    def dfs(self, v, visited):
        #Marca o nó atual 
        visited[v] = True
        
        #Percorre o resto do grafo
        #for i in self.arestas[v]:
        for i in self.adj[v]:
            
            if not visited[i]:
                self.dfs(i, visited)
        #Retorna true se o grafo for conexo

    def connected(self):
        #Marca todos os nós como não visitados
        visited = [False] * self.V
        
        self.dfs(0, visited)

        #Se todos os nós ainda forem alcançados retorna True
        for i in range(1, self.V):
            if not visited[i]:
                return False
            
        return True


    def rev_kruskal(self):
        resultado = []
        entrada = []

        #Trecho p/ imprimir a entrada
        for w in range(len(self.arestas)):
            u = self.arestas[w][1][0]
            v = self.arestas[w][1][1]

            w_ent = self.arestas[w]
            entrada.append([w_ent, u, v])

        #Sort em ordem decresente
        self.arestas = sorted(self.arestas, key=lambda item: item[0], reverse=True)

        #Função de busca nas arestas.
        for w in range(len(self.arestas)):
            u = self.arestas[w][1][0]
            v = self.arestas[w][1][1]
            
            self.adj[u].remove(v)
            self.adj[v].remove(u)


            #Checar se remover a aresta desconeta o grafo
            #Se sim, adiciona a aresta de volta
            if self.connected() == False:
                w = self.arestas[w]
                self.adj[u].append(v)
                self.adj[v].append(u)
                resultado.append([w, u, v])
            

        print("Entrada: ")
        for w, u, v in entrada:
            print(f"{chr(65 + u)} -- {chr(65 + v)} == {w[0]}")

        print("Arestas na Minimum Spanning Tree:")
        #for w in resultado:
        for w, u, v in resultado:
            #print(f"{u} -- {v} == {w[0]}")
            print(f"{chr(65 + u)} -- {chr(65 + v)} == {w[0]}")


grafo = Grafo(15)

#grafo.add_aresta(0, 1, 23)
#grafo.add_aresta(0, 8, 24)
#grafo.add_aresta(1, 2, 30)
#grafo.add_aresta(1, 7, 22)


grafo.add_aresta(0, 1, 23)
grafo.add_aresta(0, 8, 24)
grafo.add_aresta(1, 2, 30)
grafo.add_aresta(1, 7, 22)
grafo.add_aresta(1, 10, 29)
grafo.add_aresta(1, 12, 20)
grafo.add_aresta(2, 3, 5)
grafo.add_aresta(2, 10, 16)
grafo.add_aresta(2, 6, 15)
grafo.add_aresta(2, 14, 12)
grafo.add_aresta(3, 4, 9)
grafo.add_aresta(3, 11, 4)
grafo.add_aresta(4, 5, 10)
grafo.add_aresta(5, 6, 11)
grafo.add_aresta(5, 14, 3)
grafo.add_aresta(6, 7, 31)
grafo.add_aresta(6, 2, 15)
grafo.add_aresta(6, 10, 17)
grafo.add_aresta(6, 13, 8)
grafo.add_aresta(7, 13, 28)
grafo.add_aresta(7, 1, 22)
grafo.add_aresta(7, 0, 26)
grafo.add_aresta(7, 8, 25)
grafo.add_aresta(8, 9, 21)
grafo.add_aresta(9, 10, 1)
grafo.add_aresta(9, 12, 19)
grafo.add_aresta(9, 0, 27)
grafo.add_aresta(10, 1, 29)
grafo.add_aresta(10, 2, 16)
grafo.add_aresta(10, 11, 13)
grafo.add_aresta(10, 13, 18)
grafo.add_aresta(11, 14, 6)
grafo.add_aresta(11, 13, 14)
grafo.add_aresta(13, 12, 2)
grafo.add_aresta(12, 1, 20)


grafo.rev_kruskal()


