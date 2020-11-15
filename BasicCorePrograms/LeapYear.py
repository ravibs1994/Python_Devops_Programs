"""
   * author - Ravindra Suryawanshi
   * date - 13/11/2020
   * time - 00.24
   * package - Basic core programs
   * Title -Find Leap Year
"""
class LeapYear:

  # method definition

  def findLeapYear(year):
  # check Year Value Is Equal to 4 digit or not

    if len(str(year)) == 4:
    # Find Leap Year that is divisible by 4 and 400 not by 100

      if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(str(year) + " is Leap Year")
      else:
        print(str(year) + " is not Leap year")
    else:
      print("You Entered Invalid Year ")
# main method call

if __name__ == "__main__":
  yearValue = int(input("Enter Year: "))
  # method call
  LeapYear.findLeapYear(yearValue)
