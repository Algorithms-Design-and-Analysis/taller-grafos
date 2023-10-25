import sys
import heapq

def jail(g):

    _min = float('inf')
    final_node = len(g) - 1
    distances = [float('inf') for _ in range(len(g))]
    distances[0] = 0
    node_to_arrive = [None for _ in range(len(g))]
    pq = [(0, 0)]
    while pq:
        dist, node = heapq.heappop(pq)
        if dist > distances[node]:
            continue
        for neighbor, weight in g[node]:
            if dist + weight < distances[neighbor]:
                distances[neighbor] = dist + weight
                node_to_arrive[neighbor] = node
                heapq.heappush(pq, (dist + weight, neighbor))
                if neighbor == final_node:
                    temp_g = [row[:] for row in g]
                    w1, w2 = float('inf'), float('inf')
                    current_start_node = node_to_arrive[final_node]
                    current_end_node = final_node
                    while True:
                        temp_g[current_start_node] = list(filter(lambda x: x[0] != current_end_node, temp_g[current_start_node]))
                        temp_g[current_end_node] = list(filter(lambda x: x[0] != current_start_node, temp_g[current_end_node]))
                        for edge in g[current_start_node]:
                            if edge[0] == current_end_node:
                                w1 = edge[1] if w1 == float('inf') else w1 + edge[1]
                                break
                        if current_start_node == 0:
                            break
                        current_end_node = current_start_node
                        current_start_node = node_to_arrive[current_start_node]
                    w2 = Dijkstra(temp_g, 0, final_node)
                    _min = w1 + w2 if w1 + w2 < _min else _min
    if _min >= 2**32:
        return "Back to jail"
    return f"{_min}"

def Dijkstra(g, start, end):
    distances = [float('inf') for _ in range(len(g))]
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        dist, node = heapq.heappop(pq)
        if dist > distances[node]:
            continue
        for neighbor, weight in g[node]:
            if dist + weight < distances[neighbor]:
                distances[neighbor] = dist + weight
                heapq.heappush(pq, (dist + weight, neighbor))
    return distances[end]

def main():
    n = int(sys.stdin.readline().strip())
    while n != 0:
        m = int(sys.stdin.readline().strip())
        g = [[] for _ in range(n)]
        for _ in range(m):
            u, v, w = map(int, sys.stdin.readline().strip().split())
            u -= 1
            v -= 1
            g[u].append((v, w))
            g[v].append((u, w))
        print(jail(g))
        n = int(sys.stdin.readline().strip())

if __name__ == "__main__":
    main()