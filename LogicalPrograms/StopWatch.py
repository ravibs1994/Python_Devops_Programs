""" 
  * Author :Ravindra
  * Date   :18-11-2020
  * Time   :22:59
  * Package:Logical Programs
  * Statement:Write a Stopwatch Program for measuring the time that elapses between the start and end clicks
"""

from time import time

class StopWatch:
  startTime=0
  stopTime=0
  elapsTime=0
  def inputStartTime(self):
    """Method Definition
      Operation:Input start time in millisecond
      :return:
    """
    self.startTime = int(time() * 1000)
    print(self.startTime)

  def inputStopTime(self):
    """ Method Definition
        Operation:Input Stop Time in millisecond
        :return
    """
    self.stopTime = int(time() * 1000)
    print(self.stopTime)

  def elapsedTime(self):
    """Method Definition
       Operation:Calculate Ellapsed Time and Display
       :return
    """
    self.elapsTime = self.stopTime - self.startTime
    print(int(self.elapsTime)/1000)#print Ellapsed Time In Second

if __name__ == '__main__':
  """Main Method """
  object1= StopWatch()
  while True:
    try:
      startTimeInput=int(input(" Enter Value As A 1 Only like Press 1 "))
      if startTimeInput!=1:
        print("Opps You did not Enter 1 ")
        continue
      object1.inputStartTime()#method call
      stopTimeInput = int(input(" Enter Value As A 2 Only like Press 2 "))
      if stopTimeInput!=2:
        print("Opps You did not Enter 2 ")
        continue
      object1.inputStopTime()#method Call
      object1.elapsedTime()#Method call
      break
    except ValueError:
      print("Opps You Enter Wrong  Choice/Value Enter 1 For start 2 for stop ")
