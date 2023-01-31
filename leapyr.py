'''def is_leap(year):
    leap = False
#  If a number is evenly divided by 400 is a leap year.
    if year%400 == 0:
        leap=True
#  If a number is evenly divided by 4 but not with 100 is a leap year
    elif year%100 !=0 and year%4 == 0: 
        leap=True
    return leap

year = int(input())
print(is_leap(year))




#     (OR)

def is_leap(year):
    leap = False
    if (year%400 == 0) or (year%100 !=0 and year%4 == 0):
        leap=True
    return leap

year = int(input())
print(is_leap(year))





#      (OR)

def is_leap(year):
    
    if (year%400 == 0) or (year%100 !=0 and year%4 == 0):
        return True
    else:
        return False

year = int(input())
print(is_leap(year))'''


n = int(input("n = "))
s=""
for i in range(1,n+1):
    s =s+str(i) 
print(s)