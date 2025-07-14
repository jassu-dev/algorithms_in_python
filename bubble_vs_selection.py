import time
a = [
    471, 886, 74, 642, 192, 735, 106, 386, 508, 268,
    583, 120, 452, 996, 598, 343, 723, 286, 484, 313,
    572, 699, 937, 33, 946, 456, 792, 214, 872, 181,
    361, 814, 658, 432, 67, 847, 893, 978, 118, 915,
    35, 426, 774, 616, 154, 260, 777, 904, 806, 515,
    873, 321, 483, 38, 766, 184, 549, 921, 697, 220,
    225, 899, 28, 91, 680, 544, 688, 140, 281, 619,
    581, 177, 70, 532, 903, 966, 744, 742, 267, 839,
    695, 835, 783, 599, 606, 634, 996, 395, 90, 156,
    890, 595, 697, 653, 299, 879, 404, 45, 669, 337
]
b = a[:]
start = time.time()

def selection_sort(list):
    for i in range(len(list)-1):
        min_index = i
        for m in range(i+1, len(list)):
            if(list[min_index]>list[m]):
                min_index = m
        temp = list[i]
        list[i]=list[min_index]
        list[min_index] = temp
selection_sort(a)

end = time.time()

def bubble_sort(list):
    for m in range(len(list)):
        for i in range(len(list)-1):
            if(list[i] > list[i+1]):
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
bubble_sort(b)
end2 = time.time()


print(f"time taken by selection sort is {end-start}")
print(f"time taken by bubble sort is {end2-end}")

print(f"time diff {(end2-end) - (end-start)}")
