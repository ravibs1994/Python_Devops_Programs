""" 
  * Author :Ravindra
  * Date   :15-11-2020
  * Time   :16:26
  * Package:Functional Programs
  * Statement:Sum of three Integer adds to ZERO
"""


class SumOfThreeDigit:
  size = 0

  def __init__(self, size):
    """Initalization Of Data Members in Constructor"""

    self.size = size

  def CalculateSumOfThreeDigitisEqulastoZero(self, array):
    """Operation:Calculate Sum of Three Integers equals to zero From Array and Print That elements
          return: No return Value
    """
    length = len(array)
    for i in range(length - 2):
      for j in range(length - 1):
        for k in range(length):
          if array[i] + array[j] + array[k] == 0:
            print(str(array[i]) + " + " + str(array[j]) + " + " + str(array[k]) + " = 0")

  def createArray(self):

    """Operation:Create Array as Per Given size
       :return:Retun the Array
    """
    array = []
    for index in range(self.size):
      while True:
        try:
          number = int(input("Enter Element to add in array"))
          array.append(number)
        except ValueError:
          print("Opps' You Entered Wrong input plz Enter Digit""")
        break
    return array
if __name__ == "__main__":

  """Main Method 
     Operation:Create Class Object , Taking User Inputs And Call Class Methods
  """
  while True:
    """ Exception Handling """
    try:
      size = int(input("Enter The Size Of Array "))
      object1 = SumOfThreeDigit(size)
      elementArray = object1.createArray()
      object1.CalculateSumOfThreeDigitisEqulastoZero(elementArray)
      break
    except ValueError:
      print("Opps You enter  wrong input plz enter digits ")
