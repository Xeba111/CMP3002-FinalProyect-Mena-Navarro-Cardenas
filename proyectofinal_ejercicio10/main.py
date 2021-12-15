def connected_parts(n, edges):
    count = 0
    visited = [False for i in range(n)]
    for i in range(n):
        if visited[i] is not True:
            check(i, visited, edges)
            count += 1
    return count


def check(i, visited, edges):
    if visited[i] is False:
        visited[i] = True
        for vertex in edges:
            if i in vertex:
                if i == vertex[0]:
                    check(vertex[1], visited, edges)
                else:
                    check(vertex[0], visited, edges)
    else:
        return


def respuesta_ejercicio10(edges, n):
    return connected_parts(n, edges)
