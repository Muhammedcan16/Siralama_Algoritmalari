import time
import random

#-----------------------------shell sort--------------------------------------------------------------------------
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
        gap //= 2

    return arr
#-----------------------------shell sort--------------------------------------------------------------------------

#-----------------------------insertion sort--------------------------------------------------------------------------
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
#-----------------------------insertion sort--------------------------------------------------------------------------




#-----------------------------bubble sort--------------------------------------------------------------------------
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
#-----------------------------bubble sort--------------------------------------------------------------------------

#-----------------------------selection sort--------------------------------------------------------------------------
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
#-----------------------------selection sort--------------------------------------------------------------------------

#-----------------------------heap sort--------------------------------------------------------------------------
def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] < arr[left]:
            largest = left
        if right < n and arr[largest] < arr[right]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr
#-----------------------------heap sort--------------------------------------------------------------------------

#-----------------------------quicksort--------------------------------------------------------------------------
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


#-----------------------------quicksort--------------------------------------------------------------------------



#-----------------------------merge sort--------------------------------------------------------------------------
# Merge sort
# Merge Sort,  bir diziyi iki eşit parçaya ayırır, her bir parçayı ayrı ayrı sıralar ve son olarak iki parçayı birleştirerek tamamlar.
# doğru sıralanmış olarak merge sort

def merge_sort(array):
    # Eğer dizinin uzunluğu 1 veya daha azsa, dizi zaten sıralıdır
    if len(array) <= 1:
        return array

    # Diziyi ikiye ayır
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    # Her bir parçayı ayrı ayrı sırala
    left = merge_sort(left)
    right = merge_sort(right)

    # İki parçayı birleştir
    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Bir parçada kalan elemanları sonuca ekle
    result += left[i:]
    result += right[j:]

    return result

#-------------------------------------------merge sort------------------------------------------------------------
random_1 = [random.randint(0, 1000) for i in range(1000)]
random_2 = [random.randint(0, 10000) for i in range(10000)]
random_3 = [random.randint(0, 50000) for i in range(50000)]
random_4 = [random.randint(0, 100000) for i in range(100000)]
random_5 = [random.randint(0, 500000) for i in range(500000)]
random_6 = [random.randint(0, 1000000) for i in range(1000000)]

sorted_1 = sorted(random_1)
sorted_2 = sorted(random_2)
sorted_3 = sorted(random_3)
sorted_4 = sorted(random_4)
sorted_5 = sorted(random_5)
sorted_6 = sorted(random_6)

reverse_1 = sorted(sorted_1, reverse=True)
reverse_2 = sorted(sorted_2, reverse=True)
reverse_3 = sorted(sorted_3, reverse=True)
reverse_4 = sorted(sorted_4, reverse=True)
reverse_5 = sorted(sorted_5, reverse=True)
reverse_6 = sorted(sorted_6, reverse=True)

a = int(input("kaçlık veri dizisinde çalışmak istersiniz sayı ile yazınız: 1000, 10000, 50000, 100000, 500000, 1000000"))
b = input("hangi algoritmayı test etmek istersiniz küçük harfle yazın: merge , quick , heap , selection , bubble , insertion , shell ")

if a == 1000 :
    if b == "merge" :
        start_time = time.time()
        merge_sort(sorted_1)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        merge_sort(reverse_1)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        merge_sort(random_1)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))
    elif b == "quick":
        start_time = time.time()
        quick_sort(sorted_1)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        quick_sort(reverse_1)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        quick_sort(random_1)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))
    elif b == "heap":
        start_time = time.time()
        heap_sort(sorted_1)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        heap_sort(reverse_1)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        heap_sort(random_1)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))
    elif b == "selection":
        start_time = time.time()
        selection_sort(sorted_1)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        selection_sort(reverse_1)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        selection_sort(random_1)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))
    elif b == "bubble":
        start_time = time.time()
        bubble_sort(sorted_1)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        bubble_sort(reverse_1)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        bubble_sort(random_1)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))
    elif b == "insertion":
        start_time = time.time()
        insertion_sort(sorted_1)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a, " elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        insertion_sort(reverse_1)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a, " elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        insertion_sort(random_1)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a, " elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))
    elif b == "shell":
        start_time = time.time()
        shell_sort(sorted_1)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a, " elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        shell_sort(reverse_1)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a, " elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        shell_sort(random_1)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a, " elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))
elif a == 10000 :
    if b == "merge" :
        start_time = time.time()
        merge_sort(sorted_2)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        merge_sort(reverse_2)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        merge_sort(random_2)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))
    elif b == "quick":
        start_time = time.time()
        quick_sort(sorted_2)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        quick_sort(reverse_2)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        quick_sort(random_2)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))
    elif b == "heap":
        start_time = time.time()
        heap_sort(sorted_2)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        heap_sort(reverse_2)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        heap_sort(random_2)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))
    elif b == "selection":
        start_time = time.time()
        selection_sort(sorted_2)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        selection_sort(reverse_2)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        selection_sort(random_2)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))
    elif b == "bubble":
        start_time = time.time()
        bubble_sort(sorted_2)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        bubble_sort(reverse_2)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        bubble_sort(random_2)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))
    elif b == "insertion":
        start_time = time.time()
        insertion_sort(sorted_2)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a, " elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        insertion_sort(reverse_2)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a, " elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        insertion_sort(random_2)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a, " elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))
    elif b == "shell":
        start_time = time.time()
        shell_sort(sorted_2)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a, " elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        shell_sort(reverse_2)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a, " elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        shell_sort(random_2)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a, " elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))
elif a == 50000 :
    if b == "merge" :
        start_time = time.time()
        merge_sort(sorted_3)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        merge_sort(reverse_3)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        merge_sort(random_3)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))
    elif b == "quick":
        start_time = time.time()
        quick_sort(sorted_3)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        quick_sort(reverse_3)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        quick_sort(random_3)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))
    elif b == "heap":
        start_time = time.time()
        heap_sort(sorted_3)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        heap_sort(reverse_3)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        heap_sort(random_3)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))
    elif b == "selection":
        start_time = time.time()
        selection_sort(sorted_3)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        selection_sort(reverse_3)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        selection_sort(random_3)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))
    elif b == "bubble":
        start_time = time.time()
        bubble_sort(sorted_3)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        bubble_sort(reverse_3)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        bubble_sort(random_3)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))
    elif b == "insertion":
        start_time = time.time()
        insertion_sort(sorted_3)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a, " elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        insertion_sort(reverse_3)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a, " elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        insertion_sort(random_3)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a, " elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))
    elif b == "shell":
        start_time = time.time()
        shell_sort(sorted_3)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a, " elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        shell_sort(reverse_3)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a, " elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        shell_sort(random_3)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a, " elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))
elif a == 100000 :
    if b == "merge" :
        start_time = time.time()
        merge_sort(sorted_4)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        merge_sort(reverse_4)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        merge_sort(random_4)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))
    elif b == "quick":
        start_time = time.time()
        quick_sort(sorted_4)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        quick_sort(reverse_4)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        quick_sort(random_4)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))
    elif b == "heap":
        start_time = time.time()
        heap_sort(sorted_4)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        heap_sort(reverse_4)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        heap_sort(random_4)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))
    elif b == "selection":
        start_time = time.time()
        selection_sort(sorted_4)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        selection_sort(reverse_4)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        selection_sort(random_4)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))
    elif b == "bubble":
        start_time = time.time()
        bubble_sort(sorted_4)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        bubble_sort(reverse_4)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        bubble_sort(random_4)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))
    elif b == "insertion":
        start_time = time.time()
        insertion_sort(sorted_4)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a, " elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        insertion_sort(reverse_4)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a, " elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        insertion_sort(random_4)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a, " elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))
    elif b == "shell":
        start_time = time.time()
        shell_sort(sorted_4)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a, " elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        shell_sort(reverse_4)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a, " elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        shell_sort(random_4)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a, " elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))
elif a == 500000 :
    if b == "merge" :
        start_time = time.time()
        merge_sort(sorted_5)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        merge_sort(reverse_5)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        merge_sort(random_5)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))
    elif b == "quick":
        start_time = time.time()
        quick_sort(sorted_5)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        quick_sort(reverse_5)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        quick_sort(random_5)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))
    elif b == "heap":
        start_time = time.time()
        heap_sort(sorted_5)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        heap_sort(reverse_5)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        heap_sort(random_5)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))
    elif b == "selection":
        start_time = time.time()
        selection_sort(sorted_5)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        selection_sort(reverse_5)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        selection_sort(random_5)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))
    elif b == "bubble":
        start_time = time.time()
        bubble_sort(sorted_5)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        bubble_sort(reverse_5)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        bubble_sort(random_5)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))
    elif b == "insertion":
        start_time = time.time()
        insertion_sort(sorted_5)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a, " elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        insertion_sort(reverse_5)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a, " elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        insertion_sort(random_5)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a, " elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))
    elif b == "shell":
        start_time = time.time()
        shell_sort(sorted_5)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a, " elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        shell_sort(reverse_5)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a, " elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        shell_sort(random_5)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a, " elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))
elif a == 1000000 :
    if b == "merge" :
        start_time = time.time()
        merge_sort(sorted_6)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        merge_sort(reverse_6)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        merge_sort(random_6)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))
    elif b == "quick":
        start_time = time.time()
        quick_sort(sorted_6)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        quick_sort(reverse_6)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        quick_sort(random_6)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))
    elif b == "heap":
        start_time = time.time()
        heap_sort(sorted_6)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        heap_sort(reverse_6)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        heap_sort(random_6)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))
    elif b == "selection":
        start_time = time.time()
        selection_sort(sorted_6)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        selection_sort(reverse_6)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        selection_sort(random_6)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))
    elif b == "bubble":
        start_time = time.time()
        bubble_sort(sorted_6)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        bubble_sort(reverse_6)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        bubble_sort(random_6)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a," elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))
    elif b == "insertion":
        start_time = time.time()
        insertion_sort(sorted_6)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a, " elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        insertion_sort(reverse_6)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a, " elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        insertion_sort(random_6)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a, " elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))
    elif b == "shell":
        start_time = time.time()
        shell_sort(sorted_6)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a, " elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        shell_sort(reverse_6)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a, " elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))

        start_time = time.time()
        shell_sort(random_6)
        end_time = time.time()
        process_time_ms = (end_time - start_time) * 1000
        print(a, " elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))