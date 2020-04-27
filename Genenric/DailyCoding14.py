#Estimate pi to 3 dicimal point using Monte Carlo method
#Solution:
#We draw 1 square with side of 1. At the center of the square we draw a circle with radius 0.5
#Area of square: 1
#Area of circle: pi*(radius**2)= pi/4
#We generate randomly points between x: [-0.5,0.5] and: [-0.5,0.5]
# Area of circle / Area of square = point inside circle / total point

from random import uniform

class Solution:
    def estimatePi(self, points=1000):
        pointInside = 0
        for i in range(points):
            x = uniform(-0.5, 0.5)
            y = uniform(-0.5, 0.5)
            if x**2 + y**2 <= 1/4:
                pointInside += 1
        print("Pi estimation: {:.3f}".format(4*(pointInside/points)))

if __name__ == "__main__":
    A = Solution()
    A.estimatePi(10**6)