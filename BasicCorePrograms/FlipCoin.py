"""
   * author - Ravindra Suryawanshi
   * date - 12/11/2020
   * time - 13.30
   * package - Basic core programs
   * Title -Flip Coin and print percentage of Heads and Tails
"""
import random
class FlipCoin:

  def flipPercentage(self):
   headCount = 0
   tailCount = 0
   # Taking user input how may times flip the coin
   numberOfTimesFlips = int(input("How many times you wants to flip coin: "))
   if numberOfTimesFlips > 0:
    for flip in range(numberOfTimesFlips):
      randomValue = random.random()
    # count Haid And Tail

      if float(randomValue) > 0.5:
        headCount += 1
      else:
        tailCount += 1
  # Calculate Coin Percentage

    headPercentage = (headCount / numberOfTimesFlips) * 100
    tailPercentage = (tailCount / numberOfTimesFlips) * 100
    print("Head Percentage is: ", headPercentage)
    print("Tail Percentage is: ", tailPercentage)
   else:
    print("number should be positive")
   return

if __name__ == "__main__":
  # method call
   FlipCoin.flipPercentage(self=0)
