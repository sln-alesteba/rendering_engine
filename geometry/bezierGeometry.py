import random
import numpy as np


from geometry.geometry import Geometry
from core.attribute import Attribute

# implement bezier goemetry based on the previous functions;

class BezierGeometry(Geometry):

    @staticmethod
    def fact(number):

        fact = 1

        for i in range(2,number+1):
            
            fact = fact * i

        return fact

    @staticmethod
    def binomial(x, y):
            
            return BezierGeometry.fact(x) // BezierGeometry.fact(y) // BezierGeometry.fact(x - y)

    @staticmethod
    def polynomial(n, i, t):

        return pow((1 - t), (n - i)) * pow (t, i)

    @staticmethod
    def bezier_func(n, t, w):

        sum = 0

        for i in range(0, n+1, 1):

            sum += BezierGeometry.binomial(n, i) * BezierGeometry.polynomial (n, i, t) * w[i] 

        return sum

    def get_point(points, t):

        grade = len(points)-1

        i_comps = list(zip(*points))

        t_point = [ BezierGeometry.bezier_func(grade, t, i_comps[x]) for x in range(len(i_comps)) ]

        return t_point

    # generate n -dimensional control points:

    def __init__(self, points):

        super().__init__()

        positionData = [ BezierGeometry.get_point(points, t) for t in np.linspace(0.0, 1.0, num=100) ]

        self.attributes["vertexPosition"] = Attribute("vec3", positionData)

        self.countVertices()
