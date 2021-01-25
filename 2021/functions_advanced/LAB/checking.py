arr = ['a', 'b', 'c', 'd', 'e', 'f']


def check_rqcurse(arr):
    if len(arr) == 1:
        house = arr[0]
        print("Left {}".format(house))

    else:
        mid = len(arr) // 2
        f = arr[:mid]
        l = arr[mid:]
        check_rqcurse(f)
        check_rqcurse(l)


check_rqcurse(arr)
