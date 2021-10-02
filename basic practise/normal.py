from time import time

def func1(a, b):
    return a + b

def func2(a, b):
    num1 = a
    num2 = b

    if(num1 > num2 and num1 !=3):
        pass
    sum([4, 3])
    return a + b

if __name__ == '__main__':
    init = time()
    for i in range(0, 10000):
        func1(3,5)
    print(time() - init)
    
    init = time()
    for i in range(0, 1000):
        func2(3,5)
    print(time() - init)