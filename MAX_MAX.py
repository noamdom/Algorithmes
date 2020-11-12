def max_max_ind(arr):
    # init
    n = len(arr)
    first = arr[0]
    second = arr[1]

    if first < second:
        max1 = second
        max2 = first

    else:
        max1 = first
        max2 = second

    # ind
    for i in range(2, n, 2):
        # todo case of odd len
        first = arr[i]
        second = arr[i + 1]

        if first > second:
            if first > max1:
                if second > max1:
                    max2 = second
                else:
                    max2 = max1
                max1 = first
            else : # f < m1
                if first > max2:
                    max2 = first
        else: # second < first
            if second > max1:
                if first > max1:
                    max2 = first
                else:
                    max2 = max1
                max1 = first
            else:
                if second > max1:
                    max2 = second

    print("max1:", max1)
    print("max2:", max2)



def run():
    a = [8, 4, 12, 22, 3, 8.5]

    max_max_ind(a)
