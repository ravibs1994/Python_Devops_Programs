"""
   * author - Ravindra Suryawanshi
   * date - 11/11/2020
   * time - 15.30
   * package - Basic core programs
   * Title -User Input and Replace String Template “Hello <<UserName>>, How are you?
"""
# import regular Expression
import re
# create class StringReplace
class StringReplace:
  # Global Variable Declaration
  userName = ""
  name = ""
  # constructor
  def __init__(self, uname, n):
   self.userName = uname
   self.name = n
# method definition
  def replacestring(self):
   print(" Hello " + self.userName + " How are you?")
   replace = self.userName.replace(self.userName, self.name)
   print(" Hello " + replace + " How are you?")
# Taking inputs from user
userName = input("Enter your userName: ")
name = input(" Enter Name :")
# Validate using regular Expression
if re.match("^[A-Z]{1}[a-z]{2,}$", userName):
  # object Creation
  str1 = StringReplace(userName, name)
  # method call
  str1.replacestring()
else:
  print("Enter Valid UserName ")