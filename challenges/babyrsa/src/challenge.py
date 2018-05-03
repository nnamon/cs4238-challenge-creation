#!/usr/bin/python

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

p = 13942525241
q = 18876492527

n = 263185973519245374007
assert n == p*q

flag = file("password").read()
m = int(flag.encode("hex"), 16)

print "m = %d" % m

assert m < n

e = 17
phin = (p - 1) * (q - 1)
d = modinv(e, phin)

c = pow(m, e, n)
print "c = %d" % c

mp = pow(c, d, n)
assert mp == m

print "password = %s" % hex(mp)[2:-1].decode("hex")
