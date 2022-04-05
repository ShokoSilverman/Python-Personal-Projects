from functools import cache, lru_cache

#@cache #remembers the values the function as computed before
@lru_cache(maxsize=5) #does the same as cache but only holds a specified amount of previous values, saving more memory
def fib(n):
    if n <=1:
        return n
    return fib(n-1) + fib(n-1)


def main():
    for i in range(400):
        print(i, fib(i), sep=' || ')
    print('done')



if __name__ == '__main__':
    main()