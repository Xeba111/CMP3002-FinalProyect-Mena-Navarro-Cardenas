def observations(rolls, n):
    return len(rolls)+n

def array_sum(rolls):
    suma = 0
    for i in rolls:
        suma += i
    return suma

def total_number(rolls, mean, n):
    return observations(rolls, n) * mean

def remainder(rolls, mean, n):
    return total_number(rolls, mean, n) - array_sum(rolls)

def partitions(number, n, answer):
    if number <= 0:
        return answer
    modulo = number%n
    if modulo > 0:
        answer.append(modulo)
        new_number = number - modulo
        partitions(new_number, n-1, answer)
        return answer
    else:
        for i in range(n):
            answer.append(number/n)
        return answer

def respuesta_ejercicio4(rolls, mean, n):
    answer = []
    remainder_var = remainder(rolls, mean, n)
    partitions(remainder_var, n, answer)
    int_answer = [int(i) for i in answer]
    return int_answer

rolls = [1,5,6]
mean = 3
n = 4
respuesta_ejercicio4(rolls, mean, n)