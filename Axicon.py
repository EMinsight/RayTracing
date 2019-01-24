import ABCD as rt
import matplotlib.pyplot as plt

"""
Axicon: An advanced module that describes an axicon lens, not part of the basic formalism.

"""

class Axicon(rt.Matrix):
	def __init__(self, alpha, n, diameter=float('+Inf')):	
		self.n = n
		self.alpha = alpha

		super(Axicon, self).__init__(A=1, B=0, C=0,D=1, physicalLength=0, apertureDiameter=diameter)

	def mul_ray(self, rightSideRay):
		outputRay = rt.Ray()
		outputRay.y = self.A * rightSideRay.y + self.B * rightSideRay.theta
		if rightSideRay.y > 0:
			outputRay.theta = self.C * rightSideRay.y + self.D * rightSideRay.theta + -(self.n-1)*self.alpha
		else:
			outputRay.theta = self.C * rightSideRay.y + self.D * rightSideRay.theta + (self.n-1)*self.alpha

		outputRay.z = self.L + rightSideRay.z

		if abs(rightSideRay.y) > self.apertureDiameter/2:			
			outputRay.isBlocked = True
		else:
			outputRay.isBlocked = rightSideRay.isBlocked		

		return outputRay

	def drawAt(self, z, axes):
		halfHeight = 4
		if self.apertureDiameter != float('Inf'):
			halfHeight = self.apertureDiameter/2

		plt.arrow(z, 0, 0, halfHeight, width=0.1, fc='k', ec='k',head_length=0.25, head_width=0.25,length_includes_head=True)
		plt.arrow(z, 0, 0, -halfHeight, width=0.1, fc='k', ec='k',head_length=0.25, head_width=0.25, length_includes_head=True)


if __name__ == "__main__":
	path = rt.OpticalPath()
	path.name = "Demo Axicon"
	path.fanAngle = 0
	path.rayNumber = 10
	path.objectHeight = 2.0

	path.append(rt.Space(d=10))
	path.append(Axicon(n=1.55, alpha=0.25))
	path.append(rt.Space(d=20))
	path.display()