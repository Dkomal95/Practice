class check:
   def func(n):
      if n<15 and n>5:
          print("The entered number lies between 5 and 15")
      elif n>15:
        print("The entered number is more than 15")
      else:
        print("The entered number is less than 5")
        
obj=check.func(int(input("Enter a no. ")))