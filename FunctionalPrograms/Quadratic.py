""" 
  * Author :Ravindra
  * Date   :18-11-2020
  * Time   :16:31
  * Package:Functional Programs
  * Statement:Write a program Quadratic.py to find the roots of the equation a*x*x + b*x + c.
              Since the equation is x*x, hence there are 2 roots.
"""
from math import sqrt

class Quadratic:
  coefficientOfA=0
  coefficientOfB=0
  coefficientOfC=0
  def __init__(self,coefficientOfA,coefficientOfB,coefficientOfC):
    """Constructor to initailize Data Members """

    self.coefficientOfA=coefficientOfA;
    self.coefficientOfB=coefficientOfB
    self.coefficientOfC=coefficientOfC

  def calculateDelta(self):
    """Method definition
       Operation:To Calculate Delta Value
       :return: return The Delta Value
    """
    deltaValue=self.coefficientOfB * self.coefficientOfB - 4 * self.coefficientOfC * self.coefficientOfC
    return abs(deltaValue)

  def calculateRoots(self):
    """Method definition
       operation:To calculate roots of quadratic equation root1 and root2
       :return:does not return any value
    """
    deltataValue=self.calculateDelta()
    rootOneOfX=(- self.coefficientOfB + sqrt(deltataValue)) / (2 * self.coefficientOfA)
    rootTwoOfX=(- self.coefficientOfB - sqrt(deltataValue)) / (2 * self.coefficientOfA)
    print("Roots of Given Quadratic Equation is : ",rootOneOfX,rootTwoOfX)

if __name__ == '__main__':
  """Main method """
  while True:
     try:
       coefficientAValue=int(input("Enter value For Coefficient A"))
       coefficientBValue = int(input("Enter value For Coefficient B"))
       coefficientCValue = int(input("Enter value For Coefficient C"))
       object1 = Quadratic(coefficientAValue, coefficientBValue, coefficientCValue)
       object1.calculateRoots();
       break
     except ValueError:
       print("Opps You Enter Wrong input plz Enter in Digit Only ")



