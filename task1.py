def caching_fibonacci ():
    cache = {}

    def fibonacci (n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]
        
    return fibonacci

fi = caching_fibonacci()
print (fi(11))
print (fi(121))
