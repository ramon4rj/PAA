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
        #self.arestas.append([u, v, w])   ## Ordem original ##
        #self.arestas.append([w, u, v])

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
            #print(ls)
            if not visited[i]:
                #print("dfs: ")
                #print(visited)
                self.dfs(i, visited)
        #Retorna true se o grafo for conexo

    def connected(self):
        #Marca todos os nós como não visitados
        visited = [False] * self.V
        
        self.dfs(0, visited)

        #Se todos os nós ainda forem alcançados retorna True
        for i in range(1, self.V):
            if not visited[i]:
                #print(visited)
                #print("FALSO ")
                return False
            
        return True

    def rev_kruskal(self):
        resultado = []
        a = self.arestas = sorted(self.arestas, key=lambda item: item[0], reverse=True)
        #print("Sorted: ")
        #print(a)
        #print(ls)
        #pai = list(range(self.V))

        #Função de busca na lista que guarda as arestas.  Union-find
        for w in range(len(self.arestas)):
        #for u, v, w in self.arestas:       ## Ordem original ##
            u = self.arestas[w][1][0]
            v = self.arestas[w][1][1]
            
            self.adj[u].remove(v)    #[x,y,z] --> [w,z]
            self.adj[v].remove(u)

            #print(self.arestas)

            #Checar se remover a aresta desconeta o grafo
            #Se sim, adiciona a aresta de volta
            if self.connected() == False:
                self.adj[u].append(v)
                self.adj[v].append(u)
                resultado.append([u, v])
            
                print("( %d, %d )" % (u, v))
        
        #print("raiz u: ")
        #print(resultado)

        print("Arestas na Minimum Spanning Tree:")
        for u, v in resultado:
            print(f"{u} -- {v}")
            #print((f"{chr(65 + u)} -- {chr(65 + v)}"))
            #print(f"{chr(65 + u)} -- {chr(65 + v)} == {w}")

# Exemplo de uso
grafo = Grafo(9)

#grafo.add_aresta(0, 1, 10)
#grafo.add_aresta(0, 2, 6)
#grafo.add_aresta(0, 3, 5)
#grafo.add_aresta(1, 3, 15)
#grafo.add_aresta(2, 3, 4)

grafo.add_aresta(0, 1, 4)
grafo.add_aresta(0, 7, 8)
grafo.add_aresta(1, 2, 8)
grafo.add_aresta(1, 7, 11)
grafo.add_aresta(2, 3, 7)
grafo.add_aresta(2, 8, 2)
grafo.add_aresta(2, 5, 4)
grafo.add_aresta(3, 4, 9)
grafo.add_aresta(3, 5, 14)
grafo.add_aresta(4, 5, 10)
grafo.add_aresta(5, 6, 2)
grafo.add_aresta(6, 7, 1)
grafo.add_aresta(6, 8, 6)
grafo.add_aresta(7, 8, 7)


#print(grafo.arestas)

grafo.rev_kruskal()

