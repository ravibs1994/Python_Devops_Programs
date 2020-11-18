""" 
  * Author :Ravindra
  * Date   :15-11-2020
  * Time   :16:26
  * Package:Functional Programs
  * Statement:Sum of three Integer adds to ZERO
"""
class SumOfThreeDigit:
  size=0

  """Initalization Of Data Members in Constructor"""
  def __init__(self,size):
    self.size=size

    """Operation:Calculate Sum of Three Integers equals to zero From Array and Print That elements
      return: No return Value 
    """
  def CalculateSumOfThreeDigitisEqulastoZero(self,array):
      length = len(array)
      for i in range(length - 2):
        for j in range(length - 1):
          for k in range(length):
            if array[i] + array[j] + array[k] == 0:
              print(str(array[i]) + " + " + str(array[j]) + " + " + str(array[k]) + " = 0")

  """Operation:Create Array as Per Given size
     :return:Retun the Array 
  """
  def createArray(self):
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

"""Main Method 
   Operation:Create Class Object , Taking User Inputs And Call Class Methods
"""
if __name__ == "__main__":
  while True:
    try:
      size=int(input("Enter The Size Of Array "))
      object1=SumOfThreeDigit(size)
      elementArray = object1.createArray()
      object1.CalculateSumOfThreeDigitisEqulastoZero(elementArray)
      break
    except ValueError:
      print("Opps You enter  wrong input plz enter digits ")

