""" 
  * Author :Ravindra
  * Date   :18-11-2020
  * Time   :19:10
  * Package:Functional Programs
  * Statement:A library for reading in 2D arrays of integers, doubles, or booleans from standard input and printing them out to standard output.
"""
class TwoDArray:

  def inputArrayParameters(self):
    """ Method Definition
    Operation:Taking input for 2d array from user for number of rows and columns and all elements in array
    :return:does not return any value
    """
    while True:
      try:
        numberOfColumns = int(input("Enter number of columns: "))
        numberOfRows = int(input("Enter number of rows: "))
        if (numberOfColumns or numberOfRows) <= 0:
          print("number of columns and rows should be one or above ")
          continue
        break
      except ValueError:
        print("Opps You enter wrong input plz enter in digit and not zero")

    self.array = []
    for column in range(numberOfColumns):
      rowElements = []
      for row in range(numberOfRows):
         while True:
           try:
             element = int(input("Enter element in array: "))
             rowElements.append(element)
             break
           except ValueError:
            print("Opps you enter wrong input plz enter in digit only ")
      self.array.append(rowElements)

  def printArray(self):
    """ Method definition
        Operation:printing array
        :return:does not return any value
    """
    print(self.array)

if __name__ == "__main__":
  """Main method"""
  twoDArray =TwoDArray()
  twoDArray.inputArrayParameters()
  twoDArray.printArray()
