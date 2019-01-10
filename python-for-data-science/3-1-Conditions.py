'''Table of Contents
Comparison Operators
Branching
Logic Operation
'''

'''
COMPARISON OPERATORS
'''
a=5
print(a==6) # False

i=6
print(i>5) # True

i=2
print(i!=6) # True

print("ACDC"=="Michael Jackson") # False

print('B'>'A') # True
print('BA'>'AB') # True

'''
Branching
'''
age=19
#expression that can be true or false
if age>18:
    #within an indent, we have the expression that is run if the condition is true
    print("you can enter" )
elif age==18:
    print("go see Pink Floyd")
else:
    print("go see Meat Loaf" )   
#The statements after the if statement will run regardless if the condition is true or false 
print("move on")

'''
Logical operators
'''
album_year = 1980

if(album_year > 1979) and (album_year < 1990):
    print ("Album year was in between 1980 and 1989")

if(album_year > 1979) or (album_year < 1990):
    print ("Album year was bigger 1979 or lower 1990")
    
if not (album_year == '1984'):
    print ("Album year is not 1984")

if (album_year!= '1984'):
    print ("Album year is not 1984")


