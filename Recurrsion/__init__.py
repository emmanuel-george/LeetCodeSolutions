def recursion_factorial(n):
    if n == 1:
        return 1

    return n * recursion_factorial(n - 1)


if __name__ == '__main__':
    print(recursion_factorial(5))
