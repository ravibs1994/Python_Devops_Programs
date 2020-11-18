"""
  * Author :Ravindra
  * Date   :12-11-2020
  * Time   :15:30
  * Package:BasicCorePrograms
  * Statement:Computes the prime factorization of N using brute force.
"""
class PrimeFactors:
  number=0

  def __init__(self,number):
    """Constructor Definition """
    self.number=number
  def calculatePrimeFactors(self):
    """Method Definition
       Operation:Calculate Prime Factors of given number, input taken from user
       :return: Does not return any value
    """
    for i in range(2,self.number):
        while self.number%i==0:
          print("Prime Factor Of that Number ",i)
          self.number=self.number/i
  if number>2:
    print(number)
if __name__ == '__main__':
  """Mai mehod call """

  while True:
     try:
       numberValue=int(input("please Enter number Value "))
       p1=PrimeFactors(numberValue)
       p1.calculatePrimeFactors()
       break
     except ValueError:
       print("OOPs"" Plz Enter Valide Number ")


