"""
  * Author :Ravindra
  * Date   :13-11-2020
  * Time   :15:30
  * Package:BasicCorePrograms
  * Statement:Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N
"""
class HarmonicNumber:
  number = 0

  def __init__(self, number):
    """Constructor Definition """
    self.number = number

  def findHarmonicValue(self):
    """Method Definition
       Operation:Find nth Harmonic Number from given Number
       :return:Does not return any value
      """
    harmonic = 1.00
    # loop to apply the forumula
    for i in range(2, self.number + 1):
      harmonic += 1 / i
    return harmonic

if __name__ == "__main__":
  """Main Method Call """
  while True:
    try:
      numberValue = int(input("Please enter a number: "))
      h1 = HarmonicNumber(numberValue)
      print(h1.findHarmonicValue())
      break
    except ValueError:
      print("Oops!  That was no valid number.  Try again...")


