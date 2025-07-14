# the bubble sort algorithm written in python
def bubble_sort(list):
    for m in range(len(list)):
        for i in range(len(list)-1):
            if(list[i] > list[i+1]):
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
b = [5, 4, 3, 2, 1]
bubble_sort(b)
print(b)
