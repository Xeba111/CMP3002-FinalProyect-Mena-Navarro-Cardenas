contador = 0

def array_subsequences(array, max_index, subarray):
    if max_index is len(array):
        if len(subarray) > 2:
            if check_subsequence(subarray):
                global contador
                contador += 1
    else:
        array_subsequences(array, max_index+1, subarray)
        #En este caso se aumenta el caracter que está en el índice length
        array_subsequences(array, max_index+1, subarray+[array[max_index]])

def check_subsequence(array):
    #La diferencia entre elementos puede ser 0 pero siempre será positiva por eso el [+1] - [+0]
    difference = array[1] - array[0]
    for i in range(len(array)-1):
        if not array[i+1] - array[i] == difference:
            return False
    return True

def respuesta_ejercicio7(array):
    array_subsequences(array, 0, [])
    return contador
