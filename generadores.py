from grafos import Grafo
import random

def grafoMalla(m, n, dirigido=False): # m=numero de columnas; n=numero de filas; n*m nodos
    grafo = Grafo(dirigido)
    for i in range(m):
        for j in range(n):
            id_actual = (i*n) + j + 1
            grafo.agregar_nodo(f"{id_actual}")
            if i+1 < m:
                grafo.agregar_arista(f"{id_actual}",f"{id_actual + n}")
            if j+1 < n:
                grafo.agregar_arista(f"{id_actual}",f"{id_actual + 1}")
    return grafo

def grafoErdosRenyi(n, m, dirigido=False):  #n=numero de nodos; m=numero de aristas
    grafo = Grafo(dirigido)
    if dirigido == False:
        max_aristas = (n*(n-1))/2
    else:
        max_aristas = n*(n-1)
    if m > max_aristas:
        m = max_aristas

    for i in range(n):
        grafo.agregar_nodo(f"{i+1}")

    while (len(grafo.aristas) < m):
        aleatorio_1 = random.randint(1, n)
        aleatorio_2 = random.randint(1, n)
        grafo.agregar_arista(f"{aleatorio_1}", f"{aleatorio_2}")

    return grafo

def grafoGilbert(n, p, dirigido=False): #n=numero de nodos; p=probabilidad de crear una arista
    grafo = Grafo(dirigido)
    
    for i in range(n):
        grafo.agregar_nodo(f"{i+1}")

    for i in range(n):
        if dirigido:
            inicio_j = 0
        else:
            inicio_j = i+1

        for j in range(inicio_j, n):
            if j==i:
                continue
            aleatorio = random.random()
            if aleatorio <= p:
                grafo.agregar_arista(f"{i+1}",f"{j+1}")
    return grafo

def grafoGeografico(n, r, dirigido=False):  #n=numero de nodos; r=distancia para crear aristas entre nodos
    grafo = Grafo(dirigido)
    lista_x = list()
    lista_y = list()

    for i in range(n):
        coordenada_x = random.random()
        coordenada_y = random.random()
        grafo.agregar_nodo(f"{i+1}")
        lista_x.append(coordenada_x)
        lista_y.append(coordenada_y)
    
    for i in range(n):
        for j in range(i+1, n):
            delta_x = lista_x[i] - lista_x[j]
            delta_y = lista_y[i] - lista_y[j]
            distancia = (delta_x**2)+(delta_y**2)
            if distancia <= r**2:
                grafo.agregar_arista(f"{i+1}", f"{j+1}")
                if dirigido == True:
                    grafo.agregar_arista(f"{j+1}", f"{i+1}")
    return grafo
    
def grafoBarabasiAlbert(n, d, dirigido=False):  #n=numero de nodos; d=grado maximo esperado por cada nodo
    grafo = Grafo(dirigido)
    lista_grados = list()
    
    for i in range(d):
        grafo.agregar_nodo(f"{i+1}")
    
    for i in range(d):
        if dirigido:
            inicio_j = 0
        else:
            inicio_j = i + 1
        for j in range(inicio_j, d):
            grafo.agregar_arista(f"{i+1}",f"{j+1}")
        lista_grados.append(d-1)
    
    for i in range(d, n):
        grafo.agregar_nodo(f"{i+1}")
        muestras = set()
        while len(muestras) < d:
            nodo_seleccionado = random.choices(grafo.nodos[:-1], lista_grados)
            nodo_sel_id = nodo_seleccionado[0].id
            if nodo_sel_id not in muestras:
                grafo.agregar_arista(f"{i+1}",nodo_sel_id)
                muestras.add(nodo_sel_id)
                lista_grados[int(nodo_sel_id) - 1] += 1
        lista_grados.append(d)
    return grafo

def grafoDorogovstevMendes(n, dirigido=False):  #n=numero de nodos
    grafo = Grafo(dirigido)

    for i in range(3):
        grafo.agregar_nodo(f"{i+1}")

    for i in range(3):
        for j in range(i+1, 3):
            grafo.agregar_arista(f"{i+1}",f"{j+1}")

    for i in range(3, n):
        aleatorio = random.randint(0, len(grafo.aristas) - 1)
        arista_seleccionada = grafo.aristas[aleatorio]
        grafo.agregar_nodo(f"{i+1}")
        grafo.agregar_arista(f"{i+1}", arista_seleccionada.nodo_inicial)
        grafo.agregar_arista(f"{i+1}", arista_seleccionada.nodo_final)
    
    return grafo
