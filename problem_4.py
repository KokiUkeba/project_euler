#!/usr/bin/python3

import time

def hantei(mn):
    if mn[0]==mn[-1] and mn[1]==mn[-2] and mn[2]==mn[-3]:
        return
    else:
        return 1

start = time.time()

a = list()

for m in range(999, 99, -1):
    for n in range(999, 99, -1):
        mn = str(m*n)
        if hantei(mn)!=1:
            a.append(int(mn))
            print(mn)

end = time.time()

print('test')
print(max(a))
print(end - start)
