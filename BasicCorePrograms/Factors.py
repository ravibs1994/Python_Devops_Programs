class PrimeFactors:
  number=0
  def __init__(self,number):
    self.number=number
  def calculatePrimeFactors(self):
     for i in range(2,self.number):
        while self.number%i==0:
          print("Prime Factor Of that Number ",i)
          self.number=self.number/i
  if number>2:
    print(number)
if __name__ == '__main__':
   while True:
     try:
       numberValue=int(input("please Enter number Value "))
       p1=PrimeFactors(numberValue)
       p1.calculatePrimeFactors()
       break
     except ValueError:
       print("OOPs"" Plz Enter Valide Number ")


