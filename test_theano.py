'''
Created on Nov 10, 2014

@author: ASALLAB
'''
'''
import theano
from theano import tensor

# declare two symbolic floating-point scalars
a = tensor.dscalar()
b = tensor.dscalar()

# create a simple expression
c = a + b

# convert the expression into a callable object that takes (a,b)
# values as input and computes a value for c
f = theano.function([a,b], c)

# bind 1.5 to 'a', 2.5 to 'b', and evaluate 'c'
assert 4.0 == f(1.5, 2.5)
print(f(1.5, 2.5))
#Theano is a python library that makes writing deep learning models easy, and gives the option of training them on a GPU
'''


import theano.tensor as T
from theano import function
x = T.dscalar('x')
y = T.dscalar('y')
z = x + y

#print(z)
f = function([x,y], z)
print(f(1,2))
