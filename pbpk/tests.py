import numpy as np

def printinfo(arg1, *params):
    print 'Output is: '
    print arg1
    for p in params:
        print p


printinfo(10)
printinfo(70, 60, 50)


A = np.array([[1,2,3], [4,5,6]])
print A
A = np.append(A, [[7,8,9]], axis=0)
print A
