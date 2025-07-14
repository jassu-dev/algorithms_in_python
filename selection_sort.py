def selection_sort(list):
    for i in range(len(list)-1):
        min_index = i
        for m in range(i+1, len(list)):
            if(list[min_index]>list[m]):
                min_index = m
        temp = list[i]
        list[i]=list[min_index]
        list[min_index] = temp
a = [5, 4, 3, 2, 1]
selection_sort(a)
print(a)

#the classical selection sorting algorithm
