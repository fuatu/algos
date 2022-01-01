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


print("countdown")
countdown(10)
print("factorial {}:".format(5), fact(5))
print("sum n {}:".format(5), sum_n(5))
lll = [1, 2, 100, 4, 7, 14, -1]
print("count list {}:".format(lll), count_list(lll))
print("find max {}:".format(lll), find_max(lll))
