class HarmonicNumber:
  number = 0

  def __init__(self, number):
    self.number = number

  def findHarmonicValue(self):
    harmonic = 1.00
    # loop to apply the forumula
    for i in range(2, self.number + 1):
      harmonic += 1 / i
    return harmonic
if __name__ == "__main__":
  while True:
    try:
      numberValue = int(input("Please enter a number: "))
      h1 = HarmonicNumber(numberValue)
      print(h1.findHarmonicValue())
      break
    except ValueError:
      print("Oops!  That was no valid number.  Try again...")


