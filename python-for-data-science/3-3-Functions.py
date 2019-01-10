'''Table of Contents
What is a Function?
Using if/else statements in functions
Setting default argument values in your custom functions
Global and local variables
Scope of a Variable
'''
# An example of a function that adds on to the parameter a prints and returns the output as b:
def add(a):
    # documenation
    """
    add 1 to a
    """
    b=a+1 
    print(a, "if you add one" ,b)
    return(b)

# We can obtain help about a function :
help(add)

# call the function
b = add(4)

# The same function can be used for different data types.
def mult(a,b):
    c=a*b
    return(c)

print(mult(2, 3.5)) # --> 7.0
print(mult(2, "Hallo")) # --> HalloHallo

# If there is no return statement, the function returns None. The following two functions are equivalent:
def MJ():
    print('Michael Jackson')
def MJ1():
    print('Michael Jackson')
    return(None)

 # Setting default argument values in your custom functions
def isGoodRating(rating=4): 
    if(rating < 7):
        print("this album sucks it's rating is",rating)
        
    else:
        print("this album is good its rating is",rating)

isGoodRating()
isGoodRating(10)

'''
Pre-defined functions
'''
# The print() function:
album_ratings = [10.0,8.5,9.5,7.0,7.0,9.5,9.0,9.5] 
print(album_ratings)

# The sum() function adds all the elements in a list or tuple:
sum(album_ratings)

# The length function returns the length of a list or tuple:
len(album_ratings)

artist = "Michael Jackson"

# there is a way to create global variables from within a function as follows:
def printer(artist):
    global internal_var 
    internal_var= "Whitney Houston"
    print(artist,"is an artist")

printer(artist) 
printer(internal_var)

