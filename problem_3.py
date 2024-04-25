#!/usr/bin/python3
import time 

start = time.time()

N = 600851475143
a = list()

def bunkaikun(n, a):
    i = 2
    while n != 1:
        if n%i == 0:
            n //= i
            a.append(i)
            bunkaikun(n, a)
            return
        i += 1
    return 

bunkaikun(N, a)

end = time.time()

print(a[-1])
print(end-start)
