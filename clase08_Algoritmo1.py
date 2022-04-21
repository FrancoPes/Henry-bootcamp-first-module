

#ALGORITMOS DE ORDENAMIENTO


# quick algoritm
def quick_sort(sequence):
    length = len(sequence)   
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)
print(quick_sort([4,3,-1,4,4,3434,34,2,1]))


#insertion sort
def insertion_sort(list_a):
    indexing_length = range(1, len(list_a) )
    for i in indexing_length:
        value_to_sort = list_a[i]

        while list_a[i-1] > value_to_sort and i>0:           #corregir
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
            i = i -1
        return list_a
#Selection sort
print(insertion_sort([7,8,9,-1,7,6,5,6,7,8,9]))

def selection_sort(list_a):
    indexing_length = range(0, len(list_a)-1)

    for i in indexing_length:
        min_value = i

        for j in range(i+1, len(list_a)):
            if list_a[j] < list_a[min_value]:
                min_value = j


        if min_value != i:
            list_a[min_value], list_a[i] = list_a[i], list_a[min_value]

    return list_a

print(selection_sort([7,8,9,8,7,6,5,6,7,8,9,0]))


#bubble
def bubble(list_a):
    indexing_lenght = len(list_a) - 1
    sorted = False
    
    while not sorted:
        sorted = True
        for i in range(i, indexing_lenght):
            if list_a[i] > list_a[i + 1]:
                sorted = False
                list_a[i], list_a[i+1] = list_a[i + 1], list_a[i]
    return list_a
print(bubble([7,8,9,8,7,6,5,6,7,8,9,0]))
             




