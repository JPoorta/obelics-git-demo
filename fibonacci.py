def fib(n):
    '''Calculate the nth fibonacci number'''

    if n == 0 or n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)
