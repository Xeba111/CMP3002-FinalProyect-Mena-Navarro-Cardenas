import math

def quadratic_function(array, a, b, c):
    for i in range(0, len(array)):
        num1 = a * array[i]**2
        num2 = b * array[i]
        num3 = c
        new_number = num1 + num2 + num3
        # print("Número 1 es " + str(num1))
        # print("Número 2 es " + str(num2))
        # print("Número 3 es " + str(num3))
        # print("El número con índice " + str(i) + " es " + str(new_number))
        array[i] = new_number
    return array

def partir(inicio, final, array):
    pivote_original = inicio
    pivote = array[inicio]

    while inicio < final:
        while inicio < len(array) and array[inicio] <= pivote:
            inicio += 1

        while array[final] > pivote:
            final -= 1

        if inicio < final:
            array[inicio], array[final] = array[final], array[inicio]

    array[final], array[pivote_original] = array[pivote_original], array[final]

    return final


def quick_sort(inicio, final, array):
    if inicio < final:
        particion = partir(inicio, final, array)

        quick_sort(inicio, particion - 1, array)
        quick_sort(particion + 1, final, array)

def respuesta_ejercicio1(array, a, b, c):
    quadratic_function(array, a, b, c)
    quick_sort(0, len(array)-1, array)
    return array

nums = [-10, -6, -2, -1, 0]
a = 4
b = 5
c = 7
print(nums)
respuesta_ejercicio1(nums, a, b, c)
print(nums)
