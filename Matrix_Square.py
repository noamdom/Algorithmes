from __future__ import print_function

from pprint import pprint
from random import randint


def generate_random_matrix(n):
    return [[randint(0, 1) for _ in range(0, n)] for _ in range(0, n)]


def run_find_biggest_1_square(mat):
    # init
    n = len(mat)
    m = len(mat[0])
    dynamic = [[0] * m for i in range(n)]
    biggest_square = 0
    row = 0
    col = 0

    # copy the edges
    for i in range(0, n):
        dynamic[i][0] = mat[i][0]
    for j in range(1, m):
        dynamic[0][j] = mat[0][j]

    # dynamic progress
    for i in range(1, n):
        for j in range(1, m):
            if (mat[i][j] == 0):
                mat[i][j] = 0
            else:  # mat[i,j] == 1 -> calc' the size by neighbours
                size = min(mat[i - 1][j - 1], mat[i][j - 1], mat[i - 1][j]) + 1
                dynamic[i][j] = size
                if size > biggest_square:
                    biggest_square = size
                    row = i
                    col = j
    print("############### Dynamic #####################")
    pprint(dynamic)
    print("############### Data #####################")
    print("biggest_square: ", biggest_square)
    print("row idx: ", row - biggest_square + 1)
    print("col idx: ", col - biggest_square + 1)


def max_histogram_area(hist : list(int)) -> int:
    """
    This helper function calculate the rectangle area by histogram bars
    complexity: O(n)
    :param hist: list, represent the sequence of standing ones
    :return: int == max rectangle area which calculated at this iteration
    """
    n = len(hist)
    s = []  # usage of stack
    max_area = 0
    top = 0
    area_with_top = 0
    i = 0
    while i < n:
        if len(s) == 0 or hist[s[ - 1]] <= hist[i]:
            s.append(i)
            i += 1
        else: # found decreasing (zero after non-zero)
            top = s.pop() # is the smallest height idx
            # i is the right most idx, s[-1] == s.peek() left most idx
            width = i if len(s) == 0 else (i - s[ - 1] - 1)
            area_with_top = hist[top] * width
            if max_area < area_with_top:
                max_area = area_with_top

    while len(s) > 0:
        top = s.pop()
        width = i if len(s) == 0 else (i - s[-1] - 1)
        area_with_top = hist[top] * width
        if max_area < area_with_top:
            max_area = area_with_top
    return max_area


def run_find_biggest_1_rectangle(m):
    """
    This function calculate the biggest rectangle area of 1, in 1 and 0 matrix
    :param m: 2D array , of 0 and 1
    :return: print the biggest rectangle area
    """
    rows = len(m)
    cols = len(m[0])
    max_area = 0
    area = 0
    helper = [0] * cols

    for i in range(0, rows):
        # working by rows, calculate the histogram:
        for j in range(0, cols):
            if m[i][j] == 1:
                helper[j] += 1
            else:
                helper[j] = 0
        # then calculate the rectangle area
        area = max_histogram_area(helper)
        if area > max_area:
            max_area = area

    print('Max Area: ', max_area)


def main():
    n = 8
    m = generate_random_matrix(n)
    print("############### Matrix #####################")
    pprint(m)

    # run_find_biggest_1_square(m)
    run_find_biggest_1_rectangle(m)


main()
