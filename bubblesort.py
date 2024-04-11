def bubble_sort(arr):
    n = len(arr)
    
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

lista=[45354,343,4,2335,7,2323,653,52,1]

print(lista)
bubble_sort(lista)

print(lista)