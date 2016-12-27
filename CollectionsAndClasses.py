#!/usr/bin/env python

# stub so that the examples below won't throw errors
def DoSomethingWith(*x):
    pass

#
# Containers and Iterators
#

#lists
myList = []
myList.append('arthur')
myList.append('brian')
myList.append('sir robin')
myList.extend(['rabbit', 'shrubbery'])

#sets
mySet = set(myList)

#this does not change mySet ('brian' is already a member):
mySet.add('brian')
#removing from a set
mySet.remove('rabbit')
#this does not change mySet:
mySet.discard('rabbit')
# but mySet.remove('rabbit') would raise an exception


#dictionaries
myDictionary = {}
myDictionary['VA'] = 'Richmond'
myDictionary['NY'] = 'Albany'
myDictionary['CA'] = 'Sacramento'

#raises exception:
try:
    cap = myDictionary['TX']
except:
    pass

#sets cap = None: myDictionary is unchanged
cap = myDictionary.get('TX')

#sets cap = 'Washington' = myDictionary['NJ']
cap = myDictionary.setdefault('NJ', 'Washington')

#tuples
myTuple = ('arthur', 'brian','sir robin')
#no method will change myTuple

#most basic tasks buit-in already; if you want to do something that seems pretty
#generic, check python documentation to see if there is already a function that does it.
#after typing "foo." , IDLE will show list of available methods for type(foo)
myList.sort()
myList.reverse()
myList = myList + ['ThisListHasChanged!']

#importing modules
import math, random, sys, os, importlib, glob

#list comprehension
PowersOfTwo    = [2**i for i in range(16)]
DistinctPairs  =  [ (x,y) for x in range(5) for y in range(5) if x != y]
sublist        = [ x for x in myList if x[0] < x[1] ]
#can do same with sets; use {} instead of []

#this is not only harder to read, it is much less efficient (lots of copying):
PowsOf2 = []
for i in range(16):
    PowsOf2 = PowsOf2 + [2**i]

#dictionary comprehension
#key:value
myFile = open('Files/myFile.txt')
#iterating over a text file returns one line at a time
DfromFile = { line.split()[0]:line.split()[-1] for line in myFile}

X = myList # mySet myTuple myDictionary 'myString' myFile

#non-pythonic looping (direct translation of C into python)
for i in range( len(X) ):
    DoSomethingWith(X[i])

#pythonic looping (using iterators)
for thing in X:
    DoSomethingWith(thing)

#no guarantee of ordering for set or dictionary
# note: iterating through dictionary goes through list of *keys*:
for key in myDictionary:
    DoSomethingWith( myDictionary[key] )
    
# use map/iterators to avoid constructing huge lists
longRange = range(10000000000000000000000000000000000000000)
# typing L = list(longRange) will throw out-of-memory exception
longRangeIter = iter(longRange)
m = map( math.cos, longRangeIter )
#can iterate through m to get cos(0), cos(1), cos(2) ......

#
#function definitions
#

#dynamic typing; works for any object on which '*' operator is defined
def square(x):
    return x*x

#default args, docstrings
#calling fib() is same as fib(-1)
def fib(n=-1):
    """help(fib) will display this string
    compute fibbonacci numbers, ask for input if none given"""
    while n < 1:
        n = int(input("let n = ")) #should catch ValueError exception here!
    a,b = 1,1 #f_0 = 1, f_1 = 1
    for i in range(n):
        a,b = b, a+b #standard python syntax for setting several vars at once
    return a

#variable-length arg lists
#calling maximum(a,b,c,d,e) sets args to the tuple (a,b,c,d,e)
def maximum(*args):
    curmax = args[0]
    for val in args:
        if val > curmax:
            curmax = val
    return curmax

#keyword args
#grav(M1 = 7.2, M2 = 8.33, dist = 2.6) is same as grav(dist = 2.6, M1 = 7.2, M2 = 8.33)
def grav(**kwds):
    """compute gravitational force:
    G* mass1 * mass2 / dist**2"""
    return 6.67e-11* kwds['mass1']*kwds['mass2'] / (kwds['dist']**2)

def noreturn():
    "an example of 'None' returned by void function"
    print('noreturn')

#iteration works the same way on all iterable objects
#builtin functions/operators work on any object for which they make sense
#user-defined classes can behave the same way

class animal:
    "a really simple example of python classes"

    #constructor, called when we crate a new animal: x = animal('fred')
    def __init__(self, name):
        self.name = name

    def doTricks(self):
        print("I don't know any tricks!")

#dog is subclass of animal
class dog(animal):
    #a class variable, common to all instances
    #i.e. any variable defined in the class is 'static'
    count = 0
    def __init__(self, name, master):
        super().__init__(name) #call animal.__init__, just like Java 'super'
        dog.count = dog.count+1
        self.master = master
        self.tricks = set()

    #if D is a dog, then D.learnTrick('fetch') calls learnTrick with D as first argument
    def learnTrick(self,t):
        self.tricks.add(t)

    #overrides animal.doTricks:
    def doTricks(self):
        for t in self.tricks: ##different from Java: must say 'self.tricks', not just 'tricks'
            print(t+'!!!!!!')

    #called 'behind the scenes' when we print a dog object
    def __repr__(self):
        return self.master + "'s dog " + self.name


    #called when we compare two dogs: 'fido < rex' is True if fido.name
    #comes alphabetically before rex.name, compare masters' names if
    #dog's names are the same
    def __lt__(self, other):
        #print('comparing', self, '<', other)
        if self.name == other.name:
            return self.master < other.master
        return self.name < other.name
    
    def __gt__(self, other):
        #print('comparing', self, '>', other)
        return not ( (self < other) or (self == other) )
    
    def __eq__(self, other):
        #print('comparing', self, '==', other)
        return self.name == other.name and self.master == other.master

    #called when last reference to object is removed: del fido
    def __del__(self):
        self.__class__.count = self.__class__.count - 1
        #super().__del__()
        
       
DogList = [ dog(s, 'Guido') for s in ['Fido', 'Spot', 'Rex', 'Spot' ] ]
DogList[-1].master = 'Larry'

# since we have defined ordering on dogs, we can use the built-in 'sort' function on a
# list of dogs
DogList.sort()

class polynomial:
    "a really simple one-variable polynomial class"
    #takes list or tuple of coefficients as argument
    def __init__(self, coeffs):
        i = len(coeffs)
        #remove leading zeros
        while coeffs[i-1] == 0 and i > 1:
            i = i-1
        self.coeffs = tuple(coeffs[0:i]) #Polys are immutable

    def __repr__(self):
        "this could be much improved!!"
        return ' + '.join( [ str(c)+'x^'+str(n) for n,c in enumerate(self.coeffs) if c != 0] )
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
        #need __radd__ to do 1+p as well as p+1 etc
    def __add__(self, other):
        #better : if isinstance( other , numbers.Number)
        if isinstance( other, (int, float, complex) ):
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
        return self*q

    def __eq__(self, other):
        return self.coeffs == other.coeffs

#
# user-defined iterators
#
class Fib:                                        
    def __init__(self, max):                      
        self.max = max

    def __iter__(self):                           
        self.a = 0
        self.b = 1
        return self

    def __next__(self):                           
        fib = self.a
        if fib > self.max:
            raise StopIteration                   
        self.a, self.b = self.b, self.a + self.b
        return fib

##print('first few fibonacci numbers:')
##for i in Fib(10):
##    print(i)

#builtin 'in' operator uses iteration also:
#>>> 7 in Fib(10)
# False

    
#
# multiple inheritance
#
class one:
    def __init__(self):
        print('init one')
    def both(self):
        print('both one')

class two:
    def __init__(self):
        print('init two')
    def onlyTwo(self):
        print('only two')
    def both(self):
        print('both two')

#method search goes left to right
class multip(one, two):
    pass

#-------------------------------
class A:
    def m(self):
        print("called m of A")

class B(A):
    def m(self):
        print("entering m of B")
        super().m()
        print("\texiting m of B")
    
class C(A):
    def m(self):
        print("entering m of C")
        super().m()
        print("\texiting m of C")

class D(B,C):
    def m(self):
        print("entering m of D")
        super().m()
        print("\texiting m of D")

obj = D()
# calling obj.m() calls  D.m, B.m, C.m, A.m   - method resolution order


#
#decorators/properties
#
class P:

    def __init__(self,x):
        self.x = x

    #x is not an ordinary instance member
    @property
    def x(self):
        return self.__x

    #don't allow x to be negative or greater than 1000:
    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

#so code like 'p.x = 1001' actually calls a setter function, resulting in p.x == 1000

#
# Exceptions
#

class myEx(BaseException):
    pass

def ExThrower():
    raise myEx

def ExCatcher():
    try:
        throw()
    except myEx:
        print('caught it!')

