#!/usr/bin/python3

#2520 は 1 から 10 の数字の全ての整数で割り切れる数字であり, そのような数字の中では最小の値である.
#では, 1 から 20 までの整数全てで割り切れる数字の中で最小の正の数はいくらになるか.

import time

def main():
    n=20
    Ans=hitawari(n, n+1)
    print(Ans)

def hitawari(n, N=1):
    for i in range(n, 0, -1):
        if N%i == 0:
            print(i, N)
        if N%i!=0:
            N+=1
            hitawari(n, N)
            return
    return N
        
        

start = time.time()

if __name__ == '__main__':
    main()

end = time.time()

print(end - start)
