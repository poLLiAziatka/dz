def cached(func):
    dic = {}

    def wrapper(n):
        if n not in dic:
            res = func(n)
            dic[n] = res
            return res

        return dic[n]

    return wrapper


@cached
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
