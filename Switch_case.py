def add(x,y):
    s = x+y
    return s
def mul(x,y):
    m=x*y
    return m
def div(x,y):
    d=x//y
    return d
def mod(x,y):
    r=x%y
    return r
def sub(x,y):
    sb=x-y
    return sb

myswitch={ 1: add(),       
           2: mul(),
           3: div(),
           4: div(),
           5: div(),
          }
def main():
     print('Hello!')
     print('1. Addition')
     print('2. Multiplication')
     print('3. Division')
     print('4. Modulus')
     print('5. Subtraction')
     print()
     print('Enter the suitable option you want:')
     textInput = int(input())
     print("Enter two numbers to perform the operation: ")
     x=int(input())
     y=int(input())
     myswitch.get(textInput)(x,y)
ch=''
print("Do you want to continue?Press 'Y' to continue and 'N' for Exit: {}".format(ch))
while ch=='y' or ch=='Y':
     continue
     main()
     
