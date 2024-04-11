print('QUICKSORT\nIt is a fast algorithm and is \
frequently used in real life.\nThis algorithm uses a \
Divide&Conquer approach, which means you want to break down\n\
the array until you reach de base case.')
print('Empty arrays and arrays with just one element are the base case.')
print('Quicksort is basically:\n1.Picking a random pivot \n2.\
Calling quicksort() on each side of the partition\n')



def quicksort(array):
    if len(array) < 2:
        return array
    
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i<= pivot]
        greater = [i for i in array[1:] if i > pivot]
        
        return quicksort(less) + [pivot] + quicksort(greater)
    
lista=[545,1,32,53455,43,3,32,542,6]
print(lista)

lista2 = quicksort(lista)
print(lista2)
