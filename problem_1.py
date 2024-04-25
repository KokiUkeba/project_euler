#!/usr/bin/python3
import time

start = time.time()

N = 1000
m = 0
i = 0

for i in range(N):
    if i%3 == 0:
        m += i
    if i%5 == 0 and i%15 != 0:
        m += i

end = time.time()

print(m)
print(end - start)
