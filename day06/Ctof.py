def ctof(c):
    return c * (9/5) + 32

print(ctof(32))

def ftoc(f):
    return (f - 32) * (5/9)

print(ftoc(32))

def operator(func, x):
    return func(x)

c = 0
f = operator(ctof, c)
print('c=%.1f, f=%.1f' % (c, f))

f = 32
c = operator(ftoc, f)
print('c=%.1f, f=%.1f' % (f, c))