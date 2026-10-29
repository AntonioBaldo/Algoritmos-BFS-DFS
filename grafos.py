import random   # Libreria para introducir numeros aleatorios

class Nodo:
    # Un nodo necesita una etiqueta para identificarlo, un ID
    def __init__(self,id):
        self.id = id
    # Se define el método para comparar 2 nodos, son iguales si sus ID son iguales
    def __eq__(self,other):
        if not isinstance(other, Nodo):
            return NotImplemented
        return self.id == other.id

class Arista:
    # Una arista necesita un nodo inicial, un nodo final, y saber si es dirigida o no
    def __init__(self,nodo1,nodo2,dirigido=False):
        self.nodo_inicial = nodo1
        self.nodo_final = nodo2
        self.dirigido = dirigido
    # Se define el método para comparar 2 aristas, son iguales si ambos nodos iniciales son identicos, y ambos 
    # finales tambien, y si es no dirigido, tambien si son iguales el nodo inicial de la arista 1 y el nodo final 
    # de la arista 2, y el nodo final de la arista 1 junto con el nodo inicial de la arista 2.
    def __eq__(self,other):
        if not isinstance(other, Arista):
            return NotImplemented
        mismo_sentido = (self.nodo_inicial == other.nodo_inicial and self.nodo_final == other.nodo_final)
        sentido_inverso = (self.nodo_inicial == other.nodo_final and self.nodo_final == other.nodo_inicial)
        if self.dirigido==False:
            return mismo_sentido or sentido_inverso
        else:
            return mismo_sentido

class Grafo:
    # Un grafo necesita saber sus nodos, sus aristas, su lista de adyacencia y si es dirigido o no.
    # Estrictamente, con la lista de adyacencia basta pero las listas de nodos y aristas nos ayudan a
    # escribir diferentes métodos necesarios de una forma más sencilla que revisar la lista.
    def __init__(self, dirigido=False):
        self.lista_adyacencia = {}
        self.dirigido = dirigido
        self.nodos = []
        self.aristas = []

    def agregar_nodo(self, id):
        # Crear el nodo
        nuevo_nodo = Nodo(id)
        # Si el nodo no esta, lo agrega
        if nuevo_nodo.id not in self.lista_adyacencia:
            self.lista_adyacencia[nuevo_nodo.id] = set()
        if nuevo_nodo not in self.nodos:
            self.nodos.append(nuevo_nodo)

    def agregar_arista(self, nodo1, nodo2):
        # No permitir aristas entre el mismo nodo (lazos)
        if nodo1 == nodo2:
            return
        # No perimitir aristas repetidas
        if nodo1 in self.lista_adyacencia and nodo2 in self.lista_adyacencia[nodo1]:
            return
        # Crear y agregar la nueva arista
        nueva_arista = Arista(nodo1, nodo2, self.dirigido)
        self.aristas.append(nueva_arista)
        # Crear los nodos si es que no existen
        if nueva_arista.nodo_inicial not in self.lista_adyacencia:
            self.agregar_nodo(nueva_arista.nodo_inicial)
        if nueva_arista.nodo_final not in self.lista_adyacencia:
            self.agregar_nodo(nueva_arista.nodo_final)
        # Añadir la arista a la lista de adyacencia
        self.lista_adyacencia[nueva_arista.nodo_inicial].add(nueva_arista.nodo_final)
        # Si el grafo no es dirigido, añadir el sentido inverso tambien
        if self.dirigido == False:
            self.lista_adyacencia[nueva_arista.nodo_final].add(nueva_arista.nodo_inicial)

    def exportar_a_GraphViz(self, nombre_archivo):
        if self.dirigido == True:
            declaracion = "digraph"
            conector = "->"
        else:
            declaracion = "graph"
            conector = "--"
        with open(nombre_archivo, "w") as archivo:
            archivo.write(f"{declaracion} G {{\n")
            for arista in self.aristas:
                archivo.write(f"{arista.nodo_inicial} {conector} {arista.nodo_final};\n")
            # Si hay un nodo que no tenga aristas, faltará en el archivo .gv, si se desease
            # agregar todos los nodos aunque no esten conectados, se podría añadir cada nodo individualmente
            #for nodo in self.nodos:
            #    archivo.write(f"{nodo.id};\n")
            archivo.write("}\n")
        return self
    
    def BFS(self, s):
        grafo = Grafo()
        grafo.agregar_nodo(s)
        visitados = set()
        visitados.add(s)
        i = 0
        lista_capas = {}
        lista_capas[i] = [s]
        while lista_capas[i]:
            lista_capas[i+1] = []
            for nodo in lista_capas[i]:
                for nodo_incidente in self.lista_adyacencia[nodo]:
                    if nodo_incidente not in visitados:
                        visitados.add(nodo_incidente)
                        lista_capas[i+1].append(nodo_incidente)
                        grafo.agregar_arista(nodo, nodo_incidente)
            i += 1
        return grafo

    def DFS_R(self, s):
        grafo = Grafo()
        grafo.agregar_nodo(s)
        visitados = set()
        visitados.add(s)
        def explorar(nodo_actual):
            for nodo_incidente in self.lista_adyacencia[nodo_actual]:
                if nodo_incidente not in visitados:
                    grafo.agregar_arista(nodo_actual, nodo_incidente)
                    visitados.add(nodo_incidente)
                    explorar(nodo_incidente)
        explorar(s)
        return grafo

    def DFS_I(self, s):
        grafo = Grafo()
        grafo.agregar_nodo(s)
        visitados = set()
        lista_aristas = []
        lista_aristas.append((None, s))
        while lista_aristas:
            (nodo_padre, nodo_actual) = lista_aristas.pop()
            if nodo_actual not in visitados:
                visitados.add(nodo_actual)
                grafo.agregar_nodo(nodo_actual)
                if nodo_padre is not None:
                    grafo.agregar_arista(nodo_padre, nodo_actual)
                for nodo_incidente in self.lista_adyacencia[nodo_actual]:
                    lista_aristas.append((nodo_actual, nodo_incidente))
        return grafo
