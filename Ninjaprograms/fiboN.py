def calc_fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return calc_fib(n - 1) + calc_fib(n - 2)

n = int(input())
if n >= 1:
    print(calc_fib(n))

