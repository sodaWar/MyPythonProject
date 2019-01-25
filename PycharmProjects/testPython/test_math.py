import math


class Solver(object):
    def demo(self, a, b, c):
        d = b ** 2 - 4 * a * c
        disc = math.sqrt(d)
        root1 = (-b + disc) / (2 * a)
        root2 = (-b - disc) / (2 * a)
        print (root1, root2)
        return (root1, root2)
