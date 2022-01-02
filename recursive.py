def countdown(i: int):
    print(i, end=" ")
    if i <= 1:
        print("")
        return
    else:
        countdown(i-1)


def fact(i: int):
    if i == 1:
        return 1
    else:
        return i * fact(i-1)


def sum_n(n):
    if n <= 1:
        return n
    return n + sum_n(n - 1)


def count_list(ll: []):
    if not ll:
        return 0
    return 1 + count_list(ll[1:])


def find_max(ll: []):
    if not ll:
        return None
    temp = find_max(ll[1:])
    if temp is None:
        return ll[0]
    elif ll[0] > temp:
        return ll[0]
    else:
        return temp


def binary_search(arr: [], low: int, high: int, x: int):
    if not arr or x is None or high is None or low is None:
        return None

    mid = (high + low) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] > x:
        return binary_search(arr, low, mid, x)
    else:
        return binary_search(arr, mid+1, high, x)

def quicksort(arr: []):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    smaller = [i for i in arr[1:] if i <= pivot ]
    bigger = [i for i in arr[1:] if i > pivot ]
    return quicksort(smaller) + [pivot] + quicksort(bigger)

print("countdown")
countdown(10)
print("factorial {}:".format(5), fact(5))
print("sum n {}:".format(5), sum_n(5))
lll = [5, 2, 100, 4, 7, 14, -1]
print("count list {}:".format(lll), count_list(lll))
print("find max {}:".format(lll), find_max(lll))

llx = quicksort(lll)
print("quicksort {}:".format(lll), llx)

print("binary search {} in {}:".format(7, llx), binary_search(llx, 0, len(llx)-1, 7))


