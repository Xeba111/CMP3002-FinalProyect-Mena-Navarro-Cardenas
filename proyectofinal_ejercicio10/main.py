def elements(n, elements_array):
    for i in range(n):
        elements_array.append(i)
    return elements_array

def change_array(elementos, inner_index):
    while True:
        if elementos[inner_index] != inner_index:
            inner_index = elementos[inner_index]
        else:
            break
    return inner_index

def count(edges, elementos, n):
    for i in range(len(edges)):
        index1 = change_array(elementos, edges[i][0])
        index2 = change_array(elementos, edges[i][1])
        if index2 != index1:
            elementos[index2] = index1
            n -= 1
    return n

def respuesta_ejercicio10(edges, n):
    elementos = []
    elements(n, elementos)
    return count(edges, elementos, n)

edges = [[0,1],[1,2],[3,4],[2,0],[1,0],[2,1]]
n = 5
print(respuesta_ejercicio10(edges, n))