'''Table of Contents
For Loops
While Loops
'''
print(type(range(3)))
print(range(3)) # --> range(0, 3)

# for loop
dates = [1982,1980,1973]
N=len(dates)
for i in range(N):
    print(dates[i]) 

# prints 0,1,....7
for i in range(0,8):
    print(i)

dates = [1982,1980,1973]
for year in dates:  
    print(year) 

squares=['red','yellow','green','purple','blue ']
for i in range(0,5):
    print("Before square ",i, 'is',  squares[i])
    squares[i]='wight'
    print("After square ",i, 'is',  squares[i])

squares=['red','yellow','green','purple','blue ']
for i,square in enumerate(squares):
    print(i,square)

'''
While Loops
'''

dates = [1982,1980,1973,2000]

i=0
year=0
while(year!=1973):
    year=dates[i]
    i=i+1
    print(year)
print("it took ", i ,"repetitions to get out of loop")