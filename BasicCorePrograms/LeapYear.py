"""
   * Author :Ravindra
   * Date - 13/11/2020
   * Time - 00.24
   * Package - BasicCoreprograms
   * Statement -Find Leap Year
"""
class LeapYear:

  def findLeapYear(year):
    """Method definition
       Operation: Find leap year from given input year
       :return:Does not return any value
     """

  # check Year Value Is Equal to 4 digit or not
    if len(str(year)) == 4:
    # Find Leap Year that is divisible by 4 and 400 not by 100

      if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(str(year) + " is Leap Year")
      else:
        print(str(year) + " is not Leap year")
    else:
      print("You Entered Invalid Year ")

if __name__ == "__main__":
  """ main method call"""
  yearValue = int(input("Enter Year: "))
  # method call
  LeapYear.findLeapYear(yearValue)
