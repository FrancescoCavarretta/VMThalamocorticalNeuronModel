import numpy

def vector_to_ndarray(vector):
  return numpy.array([vector.x[i] for i in range(vector.size())])
