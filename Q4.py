lst = [77, 5, 5, 22, 13, 55, 97, 4, 796, 1, 0 , 9]

def quicksort(lst, left, right):
    if left >= right:
        return 
    
    pivot = lst[left]
    i, j = left, right

    while i != j:
        while pivot < lst[j] and i < j:
            j -= 1
        while pivot >= lst[i] and i < j:
            i += 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]

    lst[left], lst[i] = lst[i], pivot
    quicksort(lst, left, i-1)
    quicksort(lst, i+1, right)

quicksort(lst, 0, len(lst)-1)
print(lst)