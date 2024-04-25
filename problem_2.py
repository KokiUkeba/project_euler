#!/usr/bin/python3
import time

start = time.time()

a = 1
b = 2
c = 0
ans = 0

while(c <= 4000000):
    c = a + b
    a = b
    if b%2 == 0:
        ans += b
    b = c

end = time.time()

print(ans)
print(end-start)
