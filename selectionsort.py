def selectionSort(array, size):
    
    for ind in range(size):
        min_index = ind
 
        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        (array[ind], array[min_index]) = (array[min_index], array[ind])

n=int(input("Enter the number of elements: "))
print("Enter the the elements in the array: ")
a = [int(input())for i in range(n)]
selectionSort(a,n)
print('The array after sorting in Ascending Order by selection sort is:')
print(a)