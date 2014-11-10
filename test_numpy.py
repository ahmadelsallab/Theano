'''
Created on Nov 10, 2014

@author: ASALLAB
'''
import numpy

'''
print(numpy.asarray([[1., 2], [3, 4], [5, 6]]))
print(numpy.asarray([[1., 2], [3, 4], [5, 6]]).shape)
print(numpy.asarray([[1., 2], [3, 4], [5, 6]])[2, 0])
'''

'''
a = numpy.asarray([[1, 2], [3, 4], [5, 6]])
b = numpy.asarray([[2, 4], [6, 8], [10, 12]])
c = numpy.asarray([[2, 4], [6, 8]])

# Not matrix multiplication, but broadcasting--> Element  by element multiplication
print(numpy.multiply(a,b))
print(a*b)
#print(c*b)
'''

a = numpy.array([[1, 2], [3, 4], [5, 6]])
c = numpy.array([[1, 2], [3, 4]])
b = numpy.array([[2, 4], [6, 8], [10, 12]])
print(a*b)
#print(numpy.dot(a,b))
print(numpy.dot(a,c))