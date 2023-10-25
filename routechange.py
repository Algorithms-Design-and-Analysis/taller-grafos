import heapq

def lina(n, c, k, grafo, ruta):
    distancias = [float('inf')] * n
    distancias[k] = 0
    nodos_anteriores = [-1] * n
    cola_prioridad = [(0, k)]

    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

        if distancia_actual > distancias[nodo_actual]:
            continue

        for vecino, peso in enumerate(grafo[nodo_actual]):
            if peso == float('inf'):
                continue
            if nodo_actual in ruta and nodo_actual != c:
                indice_ruta_servicio = ruta.index(nodo_actual)
                distancia_potencial = distancia_actual

                while indice_ruta_servicio < len(ruta) - 1:
                    siguiente_nodo_servicio = ruta[indice_ruta_servicio + 1]
                    distancia_potencial += grafo[nodo_actual][siguiente_nodo_servicio]

                    if distancia_potencial < distancias[siguiente_nodo_servicio]:
                        distancias[siguiente_nodo_servicio] = distancia_potencial
                        nodos_anteriores[siguiente_nodo_servicio] = nodo_actual
                        heapq.heappush(cola_prioridad, (distancia_potencial, siguiente_nodo_servicio))
                    
                    nodo_actual = siguiente_nodo_servicio
                    indice_ruta_servicio += 1
                continue
            
            nueva_distancia = distancia_actual + peso

            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                nodos_anteriores[vecino] = nodo_actual
                heapq.heappush(cola_prioridad, (nueva_distancia, vecino))

    return distancias

def main():
    while True:
        n, m, c, k = map(int, input().split())
        if n == m == c == k == 0:
            break
        
        grafo = [[float('inf')] * n for _ in range(n)]
        for _ in range(m):
            u, v, p = map(int, input().split())
            grafo[u][v] = grafo[v][u] = p
        
        ruta = list(range(c))
        distancias = lina(n, c-1, k, grafo, ruta)
        print(distancias[c-1])

if __name__ == '__main__':
    main()
