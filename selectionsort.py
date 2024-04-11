print('\nThis is an example of selection sort')
print('This algorithm takes n**2 time')
print('Quicksort it\'s more fast, its time is O(n log n)')
print('')

# First we need to write this function
# Search for the smallest number on an array
def FindSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest_index = i
            smallest = arr[i]
    return smallest_index

#Sorts an array
def SelectionSort(arr):
    newArr = []
    #copy the array before mutating
    copiedArr = list(arr)
    
    for i in range(len(copiedArr)):
        smallest = FindSmallest(copiedArr)
        newArr.append(copiedArr.pop(smallest))
    return newArr

#Testing

artist_songs = {'bach':34,
                'mozart':369,
                'mox':8493,
                'pwie':3,
                'henry':54,
                'ki':95
                }

songs_list = list(artist_songs.values())
sorted_songs = SelectionSort(songs_list)

print("unsorted:", songs_list)
print("sorted:", sorted_songs)