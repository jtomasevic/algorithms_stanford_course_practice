""" Karatsuba algorithm for multiplication """

def multiply(x,y):
    """ Karatsuba algorithm for multiplication """
    if len(str(x)) == 1 or len(str(y)) == 1:
        # last step in recursion, now go back
        return x * y
    else:
        n = max(len(str(x)),len(str(y)))
        nby2 = n / 2
        a = x / 10**(nby2)
        b = x % 10**(nby2)
        c = y / 10**(nby2)
        d = y % 10**(nby2)
        ac = multiply(a,c)
        bd = multiply(b,d)
        ad_plus_bc = multiply(a+b,c+d) - ac - bd
        # this little trick, writing n as 2*nby2 takes care of both even and odd n
        prod = ac * 10**(2*nby2) + (ad_plus_bc * 10**nby2) + bd
        return prod