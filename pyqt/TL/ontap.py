#def adder(x,y):
 #   return x + y
#print(adder(1,2))
#print(adder("abc","xyz"))
#print(adder(['longa','longb'],['ac','ad']))
#from dictionary import *
def copyDict(dict1):
    new = {}
    for key in dict1.keys():
        new[key] = dict1[key]
    return new
d = {'a':1,'b':2}
e = copyDict(d)
d['?'] = 2
print(d)
print(e)

def addDict(dict1,dict2):
    new = {}
    for key1 in dict1.keys():
        new[key1] = dict1[key1]
    for key2 in dict2.keys():
        new[key2] = dict2[key2]
    return new
x = {'a' : 1, 'b' : 2}
y = {'c' : 3, 'd' : 4}
z = addDict(x,y)
print(z)

def countLines(name):
    f = open(name,'r')
    return len(f.readlines())
def countChars(name):
    return len(open(name,'r').read())
def test(name):
    return countLines(name),countChars(name)
s = input()
print(test(s))
