import matplotlib.pyplot as plt

'''
Creating a Class
'''

class Circle(object):
    
    # constructor
    def __init__(self,radius=3,color='blue'):
        
        self.radius=radius
        self.color=color 
    
    # methods
    def add_radius(self,r):
        
        self.radius=self.radius+r
        return(self.radius)
    def drawCircle(self):
        
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show() 

# new instance 
RedCircle=Circle(10,'red') 

# We can use the dir command to get a list of the object's methods. Many of them are default Python methods.
print(dir(RedCircle))

# We can look at the data attributes of the object:
print(RedCircle.radius)

# We can change the object's data attributes:
RedCircle.radius=1

# We can draw the object by using the method drawCircle():
RedCircle.drawCircle()

# We can increase the radius of the circle by applying the method add_radius(). Let increases the radius by 2 and then by 5:
print('Radius of object:',RedCircle.radius)
RedCircle.add_radius(2)
print('Radius of object of after applying the method add_radius(2):',RedCircle.radius)
RedCircle.add_radius(5)
print('Radius of object of after applying the method add_radius(5):',RedCircle.radius)
print('Radius of object:',RedCircle.radius)
RedCircle.add_radius(2)
print('Radius of object of after applying the method add_radius(2):',RedCircle.radius)
RedCircle.add_radius(5)
print('Radius of object of after applying the method add_radius(5):',RedCircle.radius)

# Let’s create a blue circle. As the default colour is blue, all we have to do is specify what the radius is:
BlueCircle=Circle(radius=100)
BlueCircle.drawCircle()


class Rectangle(object):
    
    def __init__(self,width=2,height =3,color='r'):
        self.height=height 
        self.width=width
        self.color=color
    
    def drawRectangle(self):
        import matplotlib.pyplot as plt
        plt.gca().add_patch(plt.Rectangle((0, 0),self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()

SkinnyBlueRectangle= Rectangle(2,10,'blue')
SkinnyBlueRectangle.drawRectangle()