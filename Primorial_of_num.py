from functools import reduce

# Using dict to solve, very efficient, especially using dict keys as hash lookup us fast

def prime_gen(n):
    for i in range(2, n**2):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            yield i

def num_primorial(n):
    raw = {}

    for k in prime_gen(n):
        if len(raw) >= n:
            break
        else:
            raw[k] = None

    return reduce(lambda x, y: x*y, raw.keys())


print(num_primorial(9)) # 223092870
