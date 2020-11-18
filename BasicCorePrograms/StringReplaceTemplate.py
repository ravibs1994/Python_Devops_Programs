"""
  * Author :Ravindra
  * Date   :11-11-2020
  * Time   :12:49
  * Package:BasicCorePrograms
  * Statement:User Input and Replace String Template “Hello <<UserName>>, How are you?
"""
# import regular Expression
import re
# create class StringReplace
class StringReplace:
  # Global Variable Declaration
  userName = ""
  name = ""

  def __init__(self, uname, n):
   """define Constructor
    Operation:To initialize Data Members And Instantiate Object
   """
   self.userName = uname
   self.name = n

  def replacestring(self):
    """Method Definition
       Operation:Replace String one to another
    :return: Does not Retun any Value
    """
    print(" Hello " + self.userName + " How are you?")
    replace = self.userName.replace(self.userName, self.name)
    print(" Hello " + replace + " How are you?")

# Taking inputs from user
while True:
  userName = input("Enter your userName: ")
  name = input(" Enter Name :")

# Validate using regular Expression
  if re.match("^[A-Z]{1}[a-z]{2,}$", userName):
    # object Creation
    str1 = StringReplace(userName, name)
    # method call
    str1.replacestring()
    break
  else:
    print("Enter Valid UserName ")
    continue