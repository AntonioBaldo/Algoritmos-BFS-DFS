# Algoritmos BFS y DFS en Topologías de Grafos

Este repositorio contiene la implementación en Python y la evidencia visual de algoritmos de búsqueda (BFS y DFS) aplicados sobre distintos modelos de generación de grafos. El proyecto documenta la expansión topológica y los árboles inducidos resultantes de evaluar 6 modelos matemáticos en 3 escalas de volumen diferentes (30, 100 y 500 nodos).

## 📂 Estructura del Repositorio

*   `main.py`: Código principal que ejecuta la generación de los grafos base, aplica los algoritmos de recorrido y gestiona la exportación de los mismos.
*   `grafos.py`: Módulo que contiene la estructura base de los grafos en formato `.gv` (GraphViz), así como las imagenes renderizadas con Gephi de los grafos y sus árboles inducidos en formato `.png`.
*   `generadores.py`: Módulo con las implementaciones en Python de los 6 modelos de grafos.
*   `grafos/`: Directorio que almacena los 72 archivos `.gv` resultantes y las evidencias visuales renderizadas en imágenes (PNG).

## 🧮 Modelos y Recorridos Implementados

### Modelos de Generación (Grafos Base)
Se incluyen 18 grafos base generados a partir de los siguientes modelos topológicos en escalas de 30, 100 y 500 vértices:
1.  **Malla (Grid):** Estructura en la que los nodos estan interconectados de manera cruzada entre sí, formando una red.
2.  **Erdős-Rényi:** Generación aleatoria uniforme dictada por un número de aristas específico ($m = 3n$).
3.  **Gilbert:** Generación aleatoria uniforme dictada por un valor probabilístico ($p = 6/(n-1)$).
4.  **Geográfico:** Conexión basada en un umbral de distancia $r$.
5.  **Barabási-Albert:** Modelo de conexión preferencial que ilustra la formación de vértices superconectados (hubs).
6.  **Dorogovtsev-Mendes:** Crecimiento fractal pseudo-aleatorio fundamentado en la inserción de triángulos.

### Algoritmos de Búsqueda (Árboles Inducidos)
Para cada uno de los grafos generados, se aplicaron los siguientes métodos partiendo siempre desde el nodo origen `"1"`, resultando en 54 árboles de expansión:
1.  **BFS (Breadth-First Search):** Búsqueda en anchura que revela la expansión por niveles concéntricos y los caminos más cortos de la red.
2.  **DFS Iterativo (Depth-First Search):** Búsqueda en profundidad implementada mediante el control manual de una estructura de pila (*Last In, First Out*).
3.  **DFS Recursivo (Depth-First Search):** Búsqueda en profundidad que delega el seguimiento del recorrido al sistema al implementarse de manera recursiva.

## ⚙️ Entorno y Ejecución

**Requisitos Previos:**
*   Python 3.x
*   **Gephi**: Software de análisis espacial (utilizando preferentemente el algoritmo de repulsión *Yifan Hu proporcional*) para interpretar la topología de los archivos exportados.

**Instrucciones de Uso:**
Para generar los archivos `.gv` de los 6 modelos y sus 3 tamaños de forma automática, ejecutar el script principal desde la terminal:
```bash
python3 main.py
