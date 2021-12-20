# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def subarrays_odd(arr):
    suma_odd = 0

    for i in range(len(arr)):
        val = 0

        for j in range(len(arr) - i):
            val = val + arr[j + i]
            "print(val)"
            if val % 2 != 0:
                suma_odd += 1
            j += 1
        "print(""salio j"")"
        i += 1

    return suma_odd

