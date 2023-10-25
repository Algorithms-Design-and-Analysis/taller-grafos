def floyd_warshall(tiempos):

    celdas_cantidad = len(tiempos)

    for celda_intermedia in range(celdas_cantidad):
        for celda_inicial in range(celdas_cantidad):
            for celda_final in range(celdas_cantidad):
                tiempos[celda_inicial][celda_final] = min(tiempos[celda_inicial][celda_final], tiempos[celda_inicial][celda_intermedia] + tiempos[celda_intermedia][celda_final])
    
    return tiempos

def obtener_respuesta(tiempos, celda_salida, cronometro):

    salieron = 1
    for celda in tiempos:
        salieron = salieron+1 if  0 < celda[celda_salida-1] <= cronometro else salieron
    
    return salieron

def main():

    casos_numero = int(input())
    input()
    for caso in range(casos_numero):
        infinito = 0
        celdas_cantidad = int(input())
        matriz_adyacencia = [[-1 for _ in range(celdas_cantidad)] for _ in range(celdas_cantidad)]
        celda_salida = int(input())
        cronometro = float(input())
        arcos_numero = int(input())
        for _ in range(arcos_numero):
            arco = input().split(" ")
            celda_inicial, celda_final, tiempo = int(arco[0]), int(arco[1]), float(arco[2])
            matriz_adyacencia[celda_inicial-1][celda_final-1] = tiempo
        infinito = float('inf')
        for fila in range(len(matriz_adyacencia)):
            for columna in range(len(matriz_adyacencia[0])):
                matriz_adyacencia[fila][columna] = 0 if fila == columna else (infinito if matriz_adyacencia[fila][columna] == -1 else matriz_adyacencia[fila][columna])
        if caso != casos_numero-1:
            input()
        print(obtener_respuesta(floyd_warshall(matriz_adyacencia), celda_salida, cronometro))
        print()
        

if __name__=='__main__':
    main()