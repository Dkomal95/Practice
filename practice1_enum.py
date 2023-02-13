# Define a function that take 2 args
# 1) List containing string.
# 2) string that want to find in our list.
# And this function will return the index of the string in our list,
# If string is not present then return -1

fruits=['mango','banana','pineapple','cherry','orange']
def func(pos,find):
     for pos, i in enumerate(fruits):
          if i==find:
              return pos
     
     return -1  
print(func(fruits,'banana'))