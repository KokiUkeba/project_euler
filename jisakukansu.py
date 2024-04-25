def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def sosumitukeru(N, a=list(), m=2):
    while int(m) <= int(N):
        if is_prime(m, a):
            a.append(m)
        m+=1
    return

