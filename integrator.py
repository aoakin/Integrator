import math

# f(x) = x^2 * e^-x * sin(x)
def f(x):
    return (x**2)*math.exp(-x)*math.sin(x)
class Integrator:
    def __init__(self, xMin, xMax, N):
        self.xMin = xMin
        self.xMax = xMax
        self.N = N

    def integrate(self):       
        dx = (self.xMax-self.xMin)/self.N
        self.S = 0
        for i in range(self.N-1):
            self.S += f(self.xMin + i*dx)*dx
        
    def show(self):
        print(self.S)

examp = Integrator(1,3,200000)
examp.integrate()
examp.show()