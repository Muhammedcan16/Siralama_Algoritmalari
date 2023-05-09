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
print("------------------------------MERGE SORT------------------------------------------")


array_random_1 = [random.randint(0, 1000) for i in range(1000)]
# 1 ile 1000 arasındaki sayıları kullanarak rastgele 1000 elemanlı bir dizi oluştur


# Diziyi sırala
array_sorted = sorted(array_random_1)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
merge_sort(array_sorted)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("1000 elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))



# Diziyi sırala
array_reverse = sorted(array_sorted, reverse=True)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
merge_sort(array_reverse)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("1000 elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))


start_time = time.time()
# başlangıç zamanını kaydet
merge_sort(array_random_1)
# İşlem bitiş zamanını kaydet
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000

# İşlem süresini yazdır
print("1000 elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))

print("------------------------------------------------------------------------")

array_random_2 = [random.randint(0, 10000) for i in range(10000)]
# 1 ile 1000 arasındaki sayıları kullanarak rastgele 1000 elemanlı bir dizi oluştur


# Diziyi sırala
array_sorted = sorted(array_random_2)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
merge_sort(array_sorted)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("10000 elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))



# Diziyi sırala
array_reverse = sorted(array_sorted, reverse=True)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
merge_sort(array_reverse)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("10000 elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))


start_time = time.time()
# başlangıç zamanını kaydet
merge_sort(array_random_2)
# İşlem bitiş zamanını kaydet
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000

# İşlem süresini yazdır
print("10000 elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))

print("------------------------------------------------------------------------")

array_random_3 = [random.randint(0, 50000) for i in range(50000)]
# 1 ile 1000 arasındaki sayıları kullanarak rastgele 1000 elemanlı bir dizi oluştur


# Diziyi sırala
array_sorted = sorted(array_random_3)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
merge_sort(array_sorted)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("50000 elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))



# Diziyi sırala
array_reverse = sorted(array_sorted, reverse=True)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
merge_sort(array_reverse)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("50000 elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))


start_time = time.time()
# başlangıç zamanını kaydet
merge_sort(array_random_3)
# İşlem bitiş zamanını kaydet
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000

# İşlem süresini yazdır
print("50000 elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))

print("------------------------------------------------------------------------")

array_random_4 = [random.randint(0, 100000) for i in range(100000)]
# 1 ile 1000 arasındaki sayıları kullanarak rastgele 1000 elemanlı bir dizi oluştur


# Diziyi sırala
array_sorted = sorted(array_random_4)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
merge_sort(array_sorted)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("100000 elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))



# Diziyi sırala
array_reverse = sorted(array_sorted, reverse=True)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
merge_sort(array_reverse)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("100000 elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))


start_time = time.time()
# başlangıç zamanını kaydet
merge_sort(array_random_4)
# İşlem bitiş zamanını kaydet
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000

# İşlem süresini yazdır
print("100000 elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))

print("------------------------------------------------------------------------")


array_random_5 = [random.randint(0, 500000) for i in range(500000)]
# 1 ile 1000 arasındaki sayıları kullanarak rastgele 1000 elemanlı bir dizi oluştur


# Diziyi sırala
array_sorted = sorted(array_random_5)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
merge_sort(array_sorted)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("500000 elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))



# Diziyi sırala
array_reverse = sorted(array_sorted, reverse=True)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
merge_sort(array_reverse)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("500000 elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))


start_time = time.time()
# başlangıç zamanını kaydet
merge_sort(array_random_5)
# İşlem bitiş zamanını kaydet
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000

# İşlem süresini yazdır
print("500000 elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))

print("------------------------------------------------------------------------")


array_random_6 = [random.randint(0, 1000000) for i in range(1000000)]
# 1 ile 1000 arasındaki sayıları kullanarak rastgele 1000 elemanlı bir dizi oluştur


# Diziyi sırala
array_sorted = sorted(array_random_6)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
merge_sort(array_sorted)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("1000000 elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))



# Diziyi sırala
array_reverse = sorted(array_sorted, reverse=True)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
merge_sort(array_reverse)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("1000000 elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))


start_time = time.time()
# başlangıç zamanını kaydet
merge_sort(array_random_6)
# İşlem bitiş zamanını kaydet
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000

# İşlem süresini yazdır
print("1000000 elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))

print("------------------------------------------------------------------------")
print("------------------------------------------------------------------------")
print("------------------------------QUICK SORT------------------------------------------")


# Diziyi sırala
array_sorted = sorted(array_random_1)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
quick_sort(array_sorted)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("1000 elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))



# Diziyi sırala
array_reverse = sorted(array_sorted, reverse=True)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
quick_sort(array_reverse)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("1000 elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))


start_time = time.time()
# başlangıç zamanını kaydet
quick_sort(array_random_1)
# İşlem bitiş zamanını kaydet
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000

# İşlem süresini yazdır
print("1000 elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))

print("------------------------------------------------------------------------")

# Diziyi sırala
array_sorted = sorted(array_random_2)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
quick_sort(array_sorted)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("10000 elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))



# Diziyi sırala
array_reverse = sorted(array_sorted, reverse=True)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
quick_sort(array_reverse)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("10000 elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))


start_time = time.time()
# başlangıç zamanını kaydet
quick_sort(array_random_2)
# İşlem bitiş zamanını kaydet
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000

# İşlem süresini yazdır
print("10000 elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))

print("------------------------------------------------------------------------")

# Diziyi sırala
array_sorted = sorted(array_random_3)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
quick_sort(array_sorted)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("50000 elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))



# Diziyi sırala
array_reverse = sorted(array_sorted, reverse=True)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
quick_sort(array_reverse)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("50000 elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))


start_time = time.time()
# başlangıç zamanını kaydet
quick_sort(array_random_3)
# İşlem bitiş zamanını kaydet
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000

# İşlem süresini yazdır
print("50000 elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))

print("------------------------------------------------------------------------")

# Diziyi sırala
array_sorted = sorted(array_random_4)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
quick_sort(array_sorted)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("100000 elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))



# Diziyi sırala
array_reverse = sorted(array_sorted, reverse=True)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
quick_sort(array_reverse)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("100000 elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))


start_time = time.time()
# başlangıç zamanını kaydet
quick_sort(array_random_4)
# İşlem bitiş zamanını kaydet
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000

# İşlem süresini yazdır
print("100000 elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))

print("------------------------------------------------------------------------")

# Diziyi sırala
array_sorted = sorted(array_random_5)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
quick_sort(array_sorted)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("500000 elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))



# Diziyi sırala
array_reverse = sorted(array_sorted, reverse=True)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
quick_sort(array_reverse)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("500000 elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))


start_time = time.time()
# başlangıç zamanını kaydet
quick_sort(array_random_5)
# İşlem bitiş zamanını kaydet
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000

# İşlem süresini yazdır
print("500000 elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))

print("------------------------------------------------------------------------")

# Diziyi sırala
array_sorted = sorted(array_random_6)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
quick_sort(array_sorted)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("1000000 elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))



# Diziyi sırala
array_reverse = sorted(array_sorted, reverse=True)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
quick_sort(array_reverse)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("1000000 elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))


start_time = time.time()
# başlangıç zamanını kaydet
quick_sort(array_random_6)
# İşlem bitiş zamanını kaydet
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000

# İşlem süresini yazdır
print("1000000 elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))


print("------------------------------------------------------------------------")
print("------------------------------------------------------------------------")
print("------------------------------HEAP SORT------------------------------------------")


# Diziyi sırala
array_sorted = sorted(array_random_1)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
heap_sort(array_sorted)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("1000 elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))



# Diziyi sırala
array_reverse = sorted(array_sorted, reverse=True)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
heap_sort(array_reverse)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("1000 elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))


start_time = time.time()
# başlangıç zamanını kaydet
heap_sort(array_random_1)
# İşlem bitiş zamanını kaydet
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000

# İşlem süresini yazdır
print("1000 elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))

print("------------------------------------------------------------------------")

# Diziyi sırala
array_sorted = sorted(array_random_2)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
heap_sort(array_sorted)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("10000 elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))



# Diziyi sırala
array_reverse = sorted(array_sorted, reverse=True)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
heap_sort(array_reverse)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("10000 elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))


start_time = time.time()
# başlangıç zamanını kaydet
heap_sort(array_random_2)
# İşlem bitiş zamanını kaydet
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000

# İşlem süresini yazdır
print("10000 elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))

print("------------------------------------------------------------------------")

# Diziyi sırala
array_sorted = sorted(array_random_3)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
heap_sort(array_sorted)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("50000 elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))



# Diziyi sırala
array_reverse = sorted(array_sorted, reverse=True)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
heap_sort(array_reverse)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("50000 elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))


start_time = time.time()
# başlangıç zamanını kaydet
heap_sort(array_random_3)
# İşlem bitiş zamanını kaydet
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000

# İşlem süresini yazdır
print("50000 elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))

print("------------------------------------------------------------------------")

# Diziyi sırala
array_sorted = sorted(array_random_4)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
heap_sort(array_sorted)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("100000 elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))



# Diziyi sırala
array_reverse = sorted(array_sorted, reverse=True)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
heap_sort(array_reverse)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("100000 elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))


start_time = time.time()
# başlangıç zamanını kaydet
heap_sort(array_random_4)
# İşlem bitiş zamanını kaydet
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000

# İşlem süresini yazdır
print("100000 elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))

print("------------------------------------------------------------------------")

# Diziyi sırala
array_sorted = sorted(array_random_5)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
heap_sort(array_sorted)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("500000 elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))



# Diziyi sırala
array_reverse = sorted(array_sorted, reverse=True)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
heap_sort(array_reverse)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("500000 elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))


start_time = time.time()
# başlangıç zamanını kaydet
heap_sort(array_random_5)
# İşlem bitiş zamanını kaydet
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000

# İşlem süresini yazdır
print("500000 elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))

print("------------------------------------------------------------------------")

# Diziyi sırala
array_sorted = sorted(array_random_6)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
heap_sort(array_sorted)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("1000000 elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))



# Diziyi sırala
array_reverse = sorted(array_sorted, reverse=True)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
heap_sort(array_reverse)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("1000000 elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))


start_time = time.time()
# başlangıç zamanını kaydet
heap_sort(array_random_6)
# İşlem bitiş zamanını kaydet
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000

# İşlem süresini yazdır
print("1000000 elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))

print("------------------------------------------------------------------------")
print("------------------------------------------------------------------------")
print("------------------------------SELECTION SORT------------------------------------------")


# Diziyi sırala
array_sorted = sorted(array_random_1)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
selection_sort(array_sorted)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("1000 elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))



# Diziyi sırala
array_reverse = sorted(array_sorted, reverse=True)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
selection_sort(array_reverse)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("1000 elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))


start_time = time.time()
# başlangıç zamanını kaydet
selection_sort(array_random_1)
# İşlem bitiş zamanını kaydet
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000

# İşlem süresini yazdır
print("1000 elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))

print("------------------------------------------------------------------------")

# Diziyi sırala
array_sorted = sorted(array_random_2)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
selection_sort(array_sorted)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("10000 elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))



# Diziyi sırala
array_reverse = sorted(array_sorted, reverse=True)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
selection_sort(array_reverse)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("10000 elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))


start_time = time.time()
# başlangıç zamanını kaydet
selection_sort(array_random_2)
# İşlem bitiş zamanını kaydet
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000

# İşlem süresini yazdır
print("10000 elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))

print("------------------------------------------------------------------------")

# Diziyi sırala
array_sorted = sorted(array_random_3)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
selection_sort(array_sorted)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("50000 elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))



# Diziyi sırala
array_reverse = sorted(array_sorted, reverse=True)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
selection_sort(array_reverse)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("50000 elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))


start_time = time.time()
# başlangıç zamanını kaydet
selection_sort(array_random_3)
# İşlem bitiş zamanını kaydet
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000

# İşlem süresini yazdır
print("50000 elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))

print("------------------------------------------------------------------------")

# Diziyi sırala
array_sorted = sorted(array_random_4)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
selection_sort(array_sorted)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("100000 elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))



# Diziyi sırala
array_reverse = sorted(array_sorted, reverse=True)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
selection_sort(array_reverse)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("100000 elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))


start_time = time.time()
# başlangıç zamanını kaydet
selection_sort(array_random_4)
# İşlem bitiş zamanını kaydet
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000

# İşlem süresini yazdır
print("100000 elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))

print("------------------------------------------------------------------------")

# Diziyi sırala
array_sorted = sorted(array_random_5)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
selection_sort(array_sorted)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("500000 elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))



# Diziyi sırala
array_reverse = sorted(array_sorted, reverse=True)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
selection_sort(array_reverse)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("500000 elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))


start_time = time.time()
# başlangıç zamanını kaydet
selection_sort(array_random_5)
# İşlem bitiş zamanını kaydet
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000

# İşlem süresini yazdır
print("500000 elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))

print("------------------------------------------------------------------------")

# Diziyi sırala
array_sorted = sorted(array_random_6)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
selection_sort(array_sorted)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("1000000 elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))



# Diziyi sırala
array_reverse = sorted(array_sorted, reverse=True)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
selection_sort(array_reverse)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("1000000 elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))


start_time = time.time()
# başlangıç zamanını kaydet
selection_sort(array_random_6)
# İşlem bitiş zamanını kaydet
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000

# İşlem süresini yazdır
print("1000000 elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))

print("------------------------------------------------------------------------")
print("------------------------------------------------------------------------")
print("------------------------------BUBBLE SORT------------------------------------------")


# Diziyi sırala
array_sorted = sorted(array_random_1)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
bubble_sort(array_sorted)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("1000 elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))



# Diziyi sırala
array_reverse = sorted(array_sorted, reverse=True)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
bubble_sort(array_reverse)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("1000 elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))


start_time = time.time()
# başlangıç zamanını kaydet
bubble_sort(array_random_1)
# İşlem bitiş zamanını kaydet
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000

# İşlem süresini yazdır
print("1000 elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))

print("------------------------------------------------------------------------")

# Diziyi sırala
array_sorted = sorted(array_random_2)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
bubble_sort(array_sorted)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("10000 elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))



# Diziyi sırala
array_reverse = sorted(array_sorted, reverse=True)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
bubble_sort(array_reverse)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("10000 elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))


start_time = time.time()
# başlangıç zamanını kaydet
bubble_sort(array_random_2)
# İşlem bitiş zamanını kaydet
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000

# İşlem süresini yazdır
print("10000 elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))

print("------------------------------------------------------------------------")

# Diziyi sırala
array_sorted = sorted(array_random_3)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
bubble_sort(array_sorted)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("50000 elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))



# Diziyi sırala
array_reverse = sorted(array_sorted, reverse=True)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
bubble_sort(array_reverse)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("50000 elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))


start_time = time.time()
# başlangıç zamanını kaydet
bubble_sort(array_random_3)
# İşlem bitiş zamanını kaydet
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000

# İşlem süresini yazdır
print("50000 elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))

print("------------------------------------------------------------------------")

# Diziyi sırala
array_sorted = sorted(array_random_4)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
bubble_sort(array_sorted)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("100000 elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))



# Diziyi sırala
array_reverse = sorted(array_sorted, reverse=True)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
bubble_sort(array_reverse)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("100000 elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))


start_time = time.time()
# başlangıç zamanını kaydet
bubble_sort(array_random_4)
# İşlem bitiş zamanını kaydet
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000

# İşlem süresini yazdır
print("100000 elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))

print("------------------------------------------------------------------------")

# Diziyi sırala
array_sorted = sorted(array_random_5)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
bubble_sort(array_sorted)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("500000 elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))



# Diziyi sırala
array_reverse = sorted(array_sorted, reverse=True)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
bubble_sort(array_reverse)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("500000 elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))


start_time = time.time()
# başlangıç zamanını kaydet
bubble_sort(array_random_5)
# İşlem bitiş zamanını kaydet
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000

# İşlem süresini yazdır
print("500000 elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))

print("------------------------------------------------------------------------")

# Diziyi sırala
array_sorted = sorted(array_random_6)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
bubble_sort(array_sorted)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("1000000 elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))



# Diziyi sırala
array_reverse = sorted(array_sorted, reverse=True)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
selection_sort(array_reverse)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("1000000 elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))


start_time = time.time()
# başlangıç zamanını kaydet
selection_sort(array_random_6)
# İşlem bitiş zamanını kaydet
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000

# İşlem süresini yazdır
print("1000000 elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))

print("------------------------------------------------------------------------")
print("------------------------------------------------------------------------")
print("------------------------------INSERTION SORT------------------------------------------")


# Diziyi sırala
array_sorted = sorted(array_random_1)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
insertion_sort(array_sorted)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("1000 elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))



# Diziyi sırala
array_reverse = sorted(array_sorted, reverse=True)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
insertion_sort(array_reverse)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("1000 elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))


start_time = time.time()
# başlangıç zamanını kaydet
insertion_sort(array_random_1)
# İşlem bitiş zamanını kaydet
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000

# İşlem süresini yazdır
print("1000 elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))

print("------------------------------------------------------------------------")

# Diziyi sırala
array_sorted = sorted(array_random_2)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
insertion_sort(array_sorted)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("10000 elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))



# Diziyi sırala
array_reverse = sorted(array_sorted, reverse=True)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
insertion_sort(array_reverse)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("10000 elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))


start_time = time.time()
# başlangıç zamanını kaydet
insertion_sort(array_random_2)
# İşlem bitiş zamanını kaydet
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000

# İşlem süresini yazdır
print("10000 elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))

print("------------------------------------------------------------------------")

# Diziyi sırala
array_sorted = sorted(array_random_3)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
insertion_sort(array_sorted)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("50000 elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))



# Diziyi sırala
array_reverse = sorted(array_sorted, reverse=True)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
insertion_sort(array_reverse)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("50000 elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))


start_time = time.time()
# başlangıç zamanını kaydet
insertion_sort(array_random_3)
# İşlem bitiş zamanını kaydet
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000

# İşlem süresini yazdır
print("50000 elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))

print("------------------------------------------------------------------------")

# Diziyi sırala
array_sorted = sorted(array_random_4)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
insertion_sort(array_sorted)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("100000 elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))



# Diziyi sırala
array_reverse = sorted(array_sorted, reverse=True)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
insertion_sort(array_reverse)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("100000 elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))


start_time = time.time()
# başlangıç zamanını kaydet
insertion_sort(array_random_4)
# İşlem bitiş zamanını kaydet
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000

# İşlem süresini yazdır
print("100000 elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))

print("------------------------------------------------------------------------")

# Diziyi sırala
array_sorted = sorted(array_random_5)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
insertion_sort(array_sorted)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("500000 elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))



# Diziyi sırala
array_reverse = sorted(array_sorted, reverse=True)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
insertion_sort(array_reverse)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("500000 elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))


start_time = time.time()
# başlangıç zamanını kaydet
insertion_sort(array_random_5)
# İşlem bitiş zamanını kaydet
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000

# İşlem süresini yazdır
print("500000 elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))

print("------------------------------------------------------------------------")

# Diziyi sırala
array_sorted = sorted(array_random_6)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
insertion_sort(array_sorted)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("1000000 elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))



# Diziyi sırala
array_reverse = sorted(array_sorted, reverse=True)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
insertion_sort(array_reverse)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("1000000 elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))


start_time = time.time()
# başlangıç zamanını kaydet
insertion_sort(array_random_6)
# İşlem bitiş zamanını kaydet
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000

# İşlem süresini yazdır
print("1000000 elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))

print("------------------------------------------------------------------------")
print("------------------------------------------------------------------------")
print("------------------------------SHELL SORT------------------------------------------")


# Diziyi sırala
array_sorted = sorted(array_random_1)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
shell_sort(array_sorted)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("1000 elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))



# Diziyi sırala
array_reverse = sorted(array_sorted, reverse=True)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
shell_sort(array_reverse)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("1000 elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))


start_time = time.time()
# başlangıç zamanını kaydet
shell_sort(array_random_1)
# İşlem bitiş zamanını kaydet
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000

# İşlem süresini yazdır
print("1000 elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))

print("------------------------------------------------------------------------")

# Diziyi sırala
array_sorted = sorted(array_random_2)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
shell_sort(array_sorted)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("10000 elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))



# Diziyi sırala
array_reverse = sorted(array_sorted, reverse=True)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
shell_sort(array_reverse)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("10000 elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))


start_time = time.time()
# başlangıç zamanını kaydet
shell_sort(array_random_2)
# İşlem bitiş zamanını kaydet
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000

# İşlem süresini yazdır
print("10000 elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))

print("------------------------------------------------------------------------")

# Diziyi sırala
array_sorted = sorted(array_random_3)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
shell_sort(array_sorted)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("50000 elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))



# Diziyi sırala
array_reverse = sorted(array_sorted, reverse=True)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
shell_sort(array_reverse)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("50000 elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))


start_time = time.time()
# başlangıç zamanını kaydet
shell_sort(array_random_3)
# İşlem bitiş zamanını kaydet
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000

# İşlem süresini yazdır
print("50000 elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))

print("------------------------------------------------------------------------")

# Diziyi sırala
array_sorted = sorted(array_random_4)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
shell_sort(array_sorted)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("100000 elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))



# Diziyi sırala
array_reverse = sorted(array_sorted, reverse=True)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
shell_sort(array_reverse)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("100000 elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))


start_time = time.time()
# başlangıç zamanını kaydet
shell_sort(array_random_4)
# İşlem bitiş zamanını kaydet
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000

# İşlem süresini yazdır
print("100000 elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))

print("------------------------------------------------------------------------")

# Diziyi sırala
array_sorted = sorted(array_random_5)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
shell_sort(array_sorted)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("500000 elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))



# Diziyi sırala
array_reverse = sorted(array_sorted, reverse=True)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
shell_sort(array_reverse)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("500000 elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))


start_time = time.time()
# başlangıç zamanını kaydet
shell_sort(array_random_5)
# İşlem bitiş zamanını kaydet
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000

# İşlem süresini yazdır
print("500000 elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))

print("------------------------------------------------------------------------")

# Diziyi sırala
array_sorted = sorted(array_random_6)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
shell_sort(array_sorted)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("1000000 elemanlı sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))



# Diziyi sırala
array_reverse = sorted(array_sorted, reverse=True)
# Sıralama süresini hesaplamak için başlangıç zamanını kaydet
start_time = time.time()
# İşlem bitiş zamanını kaydet
shell_sort(array_reverse)
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000
# İşlem süresini yazdır
print("1000000 elemanlı tersten sıralanmış dizinin sıralaması:{:.2f} ms".format(process_time_ms))


start_time = time.time()
# başlangıç zamanını kaydet
shell_sort(array_random_6)
# İşlem bitiş zamanını kaydet
end_time = time.time()
# Sıralama süresini hesapla
process_time_ms = (end_time - start_time) * 1000

# İşlem süresini yazdır
print("1000000 elemanlı random dizinin sıralaması:{:.2f} ms".format(process_time_ms))

print("------------------------------------------------------------------------")
