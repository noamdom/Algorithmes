def search(mat , lis : int, val: int):
    if val < mat[0][0]:  # val is the smallest
        return 0
    elif val > mat[lis - 1][lis - 1]:  # val is the biggest
        return lis
    else:  # Binary Search to locate the val
        left = 0
        right = lis - 1
        while left <= right:
            mid = int((left + right) / 2)
            if left == right:
                return left
            elif val == mat[mid][mid]:
                return mid
            elif val < mat[mid][mid]:
                right = mid
            else:  # val > mat[mid][mid]:
                left = mid + 1


def LIS(arr):
    """
    Dynamic solution for  Longest Incremental subsequent
    Complexity: O(n * (log(n) + n) = O(n*2)
    :param arr: list of numbers
    """
    n = len(arr)
    mat = [[0] * n for i in range(n)]
    lis = 1

    mat[0][0] = arr[0]
    for i in range(1, n):
        val = arr[i]
        idx = search(mat, lis, val)
        mat[idx][idx] = val
        for j in range(0, idx):
            mat[idx][j] = mat[idx - 1][j]

        if idx >= lis:
            lis += 1

    print(lis)
    print(mat[lis - 1])


def run():
    a = [8, 4, 12, 2, 3, 10, 14]
    # a = [1, 2, 3, 4, 5, 6, 1]
    LIS(a)
