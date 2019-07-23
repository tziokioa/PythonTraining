def exp(z,e=2):
    """Counts Exponent"""
    x=z
    while e>1:
        x=x*z
        e=e-1
    return x

print(exp(2,3))
print(exp(2))