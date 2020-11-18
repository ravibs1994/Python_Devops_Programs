""" 
  * Author :Ravindra
  * Date   :18-11-2020
  * Time   :20:12
  * Package:LogicalPrograms
  * Statement:Simulates a gambler who start with $stake and place fair $1 bets until he/she goes broke (i.e. has no money) or reach $goal.
"""
import random

class Gambler:

    def gamePlay(self):
      """Method Definition
         Operation:Find Average of win and loss in Gambler game
         :return:does not return any value
      """
      winCount = 0
      lossCount = 0
      playCount = 0
      startMoney = self.stake
      while 0 < startMoney < self.goal and playCount < self.numberOfTimes:
       rand= random.randint(0,1)
       playCount += 1
       if rand == 0:
        startMoney = startMoney - 1
        lossCount = lossCount + 1
       else:
        winCount = winCount + 1
        startMoney = startMoney + 1

      winPercentage = (winCount / playCount) * 100
      lossPercentage = (lossCount / playCount) * 100
      print("Win Percentage: ", winPercentage)
      print("Loss Percentage: ", lossPercentage)

    def setCondition(self):
      """Method Definition
         Operation:Taking inputs from user
         :return:does not return any value
      """
      try:
        self.stake = int(input("Enter amount to start gambling: "))
        self.goal = int(input("Enter amount for win: "))
        self.numberOfTimes = int(input("How many times you want to play: "))
      except ValueError:
        print("Opps you Enter Wrong Value  ")

if __name__ == "__main__":
  """Main method """
  gambler = Gambler()
  gambler.setCondition()
  gambler.gamePlay()
