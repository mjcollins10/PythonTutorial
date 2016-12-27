#memoization
def memo(f):
    mem = {}
    def memo_f(x):
        if mem.get(x):
            return mem[x]
        mem[x] = f(x)
        return mem[x]
    return memo_f
    #returns closure

#inefficient recursive implementation
def f(n):
    if n < 2:
        return 1
    return f(n-1) + f(n-2)

#linear-time implemenation
f = memo(f)


#
#iterators with yield
#
def FibIter(m):
    """iterator to generate first m fibonacci numbers"""
    a,b = 0,1
    counter = 0
    while counter < m:
        yield b
        a,b = b, a+b
        counter = counter+1
    #return raises StopIteration
        
        
#        
#class/statc methods
#
import numbers

class polynomial:
    "a really simple one-variable polynomial class"
    #takes list or tuple of coefficients as argument
    def __init__(self, coeffs):
        i = len(coeffs)
        if i == 0:
            self.coeffs = (0,)
            return
        #remove leading zeros
        while coeffs[i-1] == 0 and i > 1:
            i = i-1
        self.coeffs = tuple(coeffs[0:i]) #Polys are immutable
        
    @classmethod #or @classmethod monomialRep(cls,n,c)
    def monomialRep(cls,n,c):
        if n == 0:
            return str(c)
        else:
            return   (((c != 1) and '{:+}'.format(c)) or '+') + 'x' + (((n>1) and '^'+str(n)) or '')

        
    def __repr__(self):
        return ' '.join( [ self.monomialRep(n,c) for n,c in enumerate(self.coeffs) if c != 0] )
    # builtin 'ennumerate' returns tuples: (0, coeffs[o]), (1, coeffs[1]), ...

    def deg(self):
        return len(self.coeffs)-1

    #__getitem__ is called when we index an object like a list/tuple/string:
    # obj[n] = obj.__getitem__(n)
    def __getitem__(self, i):
        "return zero for indices higher than degree"
        if i <= self.deg():
            return self.coeffs[i]
        else:
            return 0

    #add two polys (p+q) or add number to poly
    def __add__(self, other):
        if isinstance( other, numbers.Number):
            return polynomial(  ( self.coeffs[0] + other,) + self.coeffs[1:] )
        sumC = [ self[i]+other[i] for i in range(max(self.deg(), other.deg())+1) ]
        return polynomial(sumC)

    def __radd__(self, other):
        return self + other

    #can call a polynomial just like a function:
    #p(t) == p.__call__(t)
    def __call__(self, x):
        "uses horner's method"
        y = self[self.deg()]
        for i in range(self.deg(), 0, -1):
            y = y*x + self[i-1]
        return y

    def __mul__(self, q):
        if isinstance(q, numbers.Number):
            return polynomial( [self[i]*q for i in range(self.deg()+1) ] )
        return polynomial(  [sum( [ self[k-j]*q[j] for j in range(k+1) ] )   for k in range(self.deg()+q.deg()+1) ] )

    def __rmul__(self, q):
        if self.deg() == 0:
            return polynomial([0])
        return self*q

    def deriv(self):
        return polynomial( [ i*self[i] for i in range(1,self.deg()+1) ] )

    def __eq__(self, other):
        return self.coeffs == other.coeffs


#os module
import os
#os.getcwd
#os.chdir
#os.walk
#os.listdir
#os.path.join/split
#os.path.dirname/basename
#os.pardir
#os.system to run command line args 



#copy module
import copy
#works with user-defined classes
#python handles circular structures
class MyClass():
    def __init__(self, L):
        self.L = L

#subclassing builtins
class newDict(dict):
    """D[key] returns None if key not in D"""
    def __getitem__(self, key):
        return self.get(key)

D = {}
D['VA'] = 'Richmond'
D['NY'] = 'Albany'
D['CA'] = 'Sacramento'

               
#HW: list that extends itself when we index out of bounds
  

      
#broadcasting
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
xx, yy = np.meshgrid(x, y, sparse=True) #sparse = false
z = np.sin(xx**2 + yy**2) / (xx**2 + yy**2)
h = plt.contour(x,y,z)
#be careful with matrix addition!
#similarly can plot polynomial curves
curve = xx**3 - xx*(yy**2) + 8*xx*yy


##more on indexing
t = (17,33)
#z[t]
#Out[62]: 0.067989193042101603
#
#z[17,33]
#Out[63]: 0.067989193042101603
#
#z[(17,33)]
#Out[64]: 0.067989193042101603
#
#z[ slice(0,4) , slice(96,100) ]
#Out[65]: 
#array([[ 0.01779498,  0.00071954, -0.01651205, -0.01939806],
#       [ 0.02053382,  0.01852793,  0.00156902, -0.01626204],
#       [ 0.00488659,  0.02020437,  0.01875796,  0.00156902],
#       [-0.01545849,  0.00444585,  0.02020437,  0.01852793]])
#
#z[ [1,5] , [17,66] ]
#Out[66]: array([-0.00962249, -0.03201937])
#
#z[5,66]
#Out[67]: -0.032019367177355158
#
#z[ [1,5] , 66 ]
#Out[68]: array([ 0.03730136, -0.03201937])


#
# miscellaneous numpy functions
#


#np.random.normal(mu, sig, size=...)
#np.random.shuffle(a) # this modifies the array a!

#vals, vects = np.linalg.eig(a) #np.cross, np.outer
#np.polyfit(x,y,deg) ; np.polyval(coeffs, x) ; np.polyint/der