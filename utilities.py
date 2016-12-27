#from x import y; import x as z
# in operator on iterators
# chr/ord, unicode


#
# String Formatting
#
from CollectionsAndClasses import *
ss=[]

ss.append(   '{0} and {1} and {2} are the inputs'.format('string', 37, dog('Doug', 'Dave')  ) )

ss.append( 'the usual: {0:.2f} and {0:+.4f} and {0:.3e} etc'.format(13.2713905) )

ss.append( 'bases: {0:d} == 0X{0:x} == b{0:b}'.format(115) )

ss.append( 'Name: {name}, IDnum: {ID}'.format(name='Bob', ID=13) )

for line in ss:
    print(line)
    
#bound methods
HexFormatter = '0x{:0>2X}'.format
print('-----------------------------------------------')
print(    [ HexFormatter(n) for n in range(10,20) ]   )


#
# Regular Expressions
#
import re
strng=True
print('type a string to see regex demo')
print('hit return with no input to go on to next demo')
while strng:
    strng=input('find all words in all caps ')
    print( re.findall(r'\b[A-Z]+\b', strng) ) #note raw string
    #returns list of matched strings
    
strng=True
while strng:
    strng=input('find first occurence of pattern word:number : ')
    m = re.search(r'([a-z,A-Z]+):(\d+)', strng) #re.match looks only at beginning
    if m:
        print('word:', m.group(1))
        print('number:', m.group(2))
        #m.groups() returns list of groups; m.group(0) is entire mach
    else:
        print('no match')

#backrefs
strng=True
while strng:
    strng=input('find first matching tag in simplified html:  ')
    m = re.search(r"<([a-z]+)>(.*)</\1>",strng)
    if m:
        print('tag:', m.group(1))
        print('content:', m.group(2))
        #can also have named groups (?P<name>pattern) , backref (?P=name)
    else:
        print('no match')

#substitution
strng=True
while strng:
    strng=input('get rid of annoying ALL CAPS: ')
    newstrng = re.sub(r"\b[A-Z]{2,}\b","....", strng) #backrefs in replacement
    #sub returns string, not match object
    print(newstrng)
    print('but this is even better:')
    newstrng   = re.sub(r"\b[A-Z]{2,}\b", lambda mo : mo.group(0).lower(), strng) #replace with function
    print(newstrng)

#also re.split, m.span

#
# Extended regular expressions: include comments, ignore whitespace
#
mo = re.search(r"""
 [+\-]?                # optional sign
 (
     0o[0-7]+         # Octal form
   | [1-9][0-9]*          # Decimal form without leading zeros
   | x[0-9a-fA-F]+   # Hexadecimal form
 )
 \s                  # Trailing space
""",
    '-x3f ;', re.VERBOSE)

#compiling
compiledRegex  = re.compile(r"<([a-z]+)>(.*)</\1>")
# then compiledRegex.search(...), compiledRegex.sub(...) etc

#for handling date/time strings, use datetime module
#for handling CSV files, use csv module
#several options for HTML/XML

#
# Sorting on attributes
#
from operator import attrgetter
DogList.sort(key=attrgetter('master'))



#key is actually a function called on each list element
#sort by number of tricks
DogList.sort(key= lambda d : len(d.tricks))


#
# Pickling
#
import pickle
archive = open('archive.pkl', 'wb') #write, binary
pickle.dump(DogList, archive)
pickle.dump(HexFormatter, archive)
archive.close()

archive = open('archive.pkl', 'rb') 
aList = pickle.load( archive ) #==DogList
aHF =  pickle.load( archive )  #==HexFormatter
archive.close()


# reading binary files:
binfile=open('Files/unicode.txt','rb')
utextfile = open('Files/unicode.txt','r',encoding="UTF-8")
