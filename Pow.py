from math import floor


def run(x: int, n: int):
    """
    This function return the product of x^n with running time: O(log n)
    :param x: the base (int)
    :param n: the power (int)
    """
    answer = 1
    while n > 0:
        if n % 2 == 1:
            answer *= x
        x *= x
        n = floor(n / 2)
    print('answer: ', answer)
    return answer
