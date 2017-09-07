import riemann as rie
def parob (x):
    y = x ** 2
    return y

print rie.riemann (0, 1, 1000, parob)
