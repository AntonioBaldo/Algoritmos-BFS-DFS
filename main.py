from grafos import Grafo
import math
import generadores as gen
import os

nodos = [30, 100, 500]
nodo_fuente = '1'
diccionario_grafos = {}

for n in nodos:
    #Método Malla
    match n:
        case 30:
            grafo_malla = gen.grafoMalla(5,6)
        case 100:
            grafo_malla = gen.grafoMalla(10,10)
        case 500:
            grafo_malla = gen.grafoMalla(20,25)
    key_malla = f"malla_{n}"
    diccionario_grafos[key_malla] = grafo_malla
    
    diccionario_grafos[f"{key_malla}_BFS"] = grafo_malla.BFS(nodo_fuente)
    diccionario_grafos[f"{key_malla}_DFS_R"] = grafo_malla.DFS_R(nodo_fuente)
    diccionario_grafos[f"{key_malla}_DFS_I"] = grafo_malla.DFS_I(nodo_fuente)

    #Método Erdos Renyi
    grafo_erdos = gen.grafoErdosRenyi(n, 3*n)
    key_erdos = f"erdos_{n}"
    diccionario_grafos[key_erdos] = grafo_erdos

    diccionario_grafos[f"{key_erdos}_BFS"] = grafo_erdos.BFS(nodo_fuente)
    diccionario_grafos[f"{key_erdos}_DFS_R"] = grafo_erdos.DFS_R(nodo_fuente)
    diccionario_grafos[f"{key_erdos}_DFS_I"] = grafo_erdos.DFS_I(nodo_fuente)

    #Método Gilbert
    p = 6/(n-1)
    grafo_gilbert = gen.grafoGilbert(n, p)
    key_gilbert = f"gilbert_{n}"
    diccionario_grafos[key_gilbert] = grafo_gilbert

    diccionario_grafos[f"{key_gilbert}_BFS"] = grafo_gilbert.BFS(nodo_fuente)
    diccionario_grafos[f"{key_gilbert}_DFS_R"] = grafo_gilbert.DFS_R(nodo_fuente)
    diccionario_grafos[f"{key_gilbert}_DFS_I"] = grafo_gilbert.DFS_I(nodo_fuente)

    #Método Geografico
    r = (6/(math.pi*(n-1))) ** 0.5
    grafo_geo = gen.grafoGeografico(n, r)
    key_geo = f"geo_{n}"
    diccionario_grafos[key_geo] = grafo_geo

    diccionario_grafos[f"{key_geo}_BFS"] = grafo_geo.BFS(nodo_fuente)
    diccionario_grafos[f"{key_geo}_DFS_R"] = grafo_geo.DFS_R(nodo_fuente)
    diccionario_grafos[f"{key_geo}_DFS_I"] = grafo_geo.DFS_I(nodo_fuente)

    #Método Barabasi-Albert
    grafo_barabasi = gen.grafoBarabasiAlbert(n, 3)
    key_barabasi = f"barabasi_{n}"
    diccionario_grafos[key_barabasi] = grafo_barabasi

    diccionario_grafos[f"{key_barabasi}_BFS"] = grafo_barabasi.BFS(nodo_fuente)
    diccionario_grafos[f"{key_barabasi}_DFS_R"] = grafo_barabasi.DFS_R(nodo_fuente)
    diccionario_grafos[f"{key_barabasi}_DFS_I"] = grafo_barabasi.DFS_I(nodo_fuente)

    #Método Dorogovstev-Mendes
    grafo_dorogovstev = gen.grafoDorogovstevMendes(n)
    key_dorogovstev = f"dorogovstev_{n}"
    diccionario_grafos[key_dorogovstev] = grafo_dorogovstev

    diccionario_grafos[f"{key_dorogovstev}_BFS"] = grafo_dorogovstev.BFS(nodo_fuente)
    diccionario_grafos[f"{key_dorogovstev}_DFS_R"] = grafo_dorogovstev.DFS_R(nodo_fuente)
    diccionario_grafos[f"{key_dorogovstev}_DFS_I"] = grafo_dorogovstev.DFS_I(nodo_fuente)

for key, grafo in diccionario_grafos.items():
    partes = key.split('_')
    metodo = partes[0]
    tamano = partes[1]

    ruta_carpeta = os.path.join("grafos", metodo, f"{tamano}_nodos")
    os.makedirs(ruta_carpeta, exist_ok=True)

    ruta_archivo = os.path.join(ruta_carpeta, f"{key}.gv")

    grafo.exportar_a_GraphViz(ruta_archivo)
