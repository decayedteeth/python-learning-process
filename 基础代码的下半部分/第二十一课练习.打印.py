def make_repeat(n):
    return lambda s:s*n #s=s*n
double=make_repeat(2)#此时的s=2
print(double(8))#n=2*8
print(double('CC'))#CC*2
