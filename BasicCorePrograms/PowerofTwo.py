"""
  * Author :Ravindra
  * Date   :14-11-2020
  * Time   :15:30
  * Package:BasicCorePrograms
  * Statement:prints a table of the powers of 2 that are less than or equal to 2^N.
"""
class PowerOftwo:

   def calculatePowerOfTwo(number):
    """Method definition
      Operation:Calculate power of two of given Number
    """
    # checking number is between0 to 31
    if (0 <= number < 31 ):
      for num in range (number+1):
        print("___________________________________")
        print("| Power of 2: |", num ," |", 2**num,"|")
    else:
      print("Entered Number Should be 0 to 30 only")
    return

if __name__ == "__main__":
  """Main Mehod """
  numberValue=int (input(" Enter The Number "))
  # Method call
  PowerOftwo.calculatePowerOfTwo(numberValue)




