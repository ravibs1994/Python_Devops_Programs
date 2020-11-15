class PowerOftwo:
  #method definition

   def calculatePowerOfTwo(number):
    # checking number is between0 to 31
    if (0 <= number < 31 ):
      for num in range (number+1):
        print("___________________________________")
        print("| Power of 2: |", num ," |", 2**num,"|")
    else:
      print("Entered Number Should be 0 to 30 only")
    return
#Main method call

if __name__ == "__main__":
  numberValue=int (input(" Enter The Number "))
  # Method call
  PowerOftwo.calculatePowerOfTwo(numberValue)




