#Create a polygon function that accepts a turtle, sides, and distance.
#function file

def polygon(t, sides, distance):
    angle = 360/sides#angle variable is inside the function
    t.begin_fill()
    for times in range(sides):
        t.forward(distance)
        t.right(angle)
    t.end_fill()
    
def polygonUnfill(t, sides, distance):
    angle = 360/sides#angle variable is inside the function
    
    for times in range(sides):
        t.forward(distance)
        t.right(angle)
   

def cool(t,d,c1,c2):
    t.color(c1)
    polygon(t,4,d)
    t.color(c2)
    polygon(t,3,d)


def coolSquared(t,d,c1,c2):
    for times in range(4):
        cool(t,d,c1,c2)
        t.right(90)

def coolSquared2(t,d,c1,c2):
    for times in range(4):
        coolSquared(t,d,c1,c2)
        t.forward(d*2)
        t.right(90)

def jump(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()


    
def rightcurve(t):
    
    for n in range(20):
        t.begin_fill()
    
        t.circle(n)
        t.forward(n)
        t.left(n)
        t.end_fill()

def leftcurve(t):
    
    for n in range(20):
        t.begin_fill()
    
        t.circle(n)
        t.forward(n)
        t.right(n)
        t.end_fill()
    
    
def cloud(t,r):
    for c in ['light blue','blue','light blue','blue']:
        t.begin_fill()
        t.color(c)
        t.circle(r)
        t.right(90)
        t.end_fill()

def star(t,d,c):
    t.begin_fill()
    t.color(c)
    for times in range(8):
        t.forward(d)
        t.left(135)
    t.end_fill()

def stars(t,c):
    for times in range(11):
        star(t,times *10 + 8,c)
        t.penup()
        t.right(30)
        t.forward(50)
        t.pendown()


def funky(t,d,c1,c2):
    t.color(c1)
    polygon(t,3,d)
    t.color(c2)
    polygon(t,3,d/2)
        



       
def holiday(t,x,n,a):

    for times in range (x):
        for c in ['yellow','light yellow','gold']:
   
            t.pencolor(c)
            t.forward(times*n)
            t.right(a)
    t.right(90)
    for times in range (x):
        for c in ['yellow','light yellow','gold']:
            t.pencolor(c)
            t.forward(times*n)
            
            t.right(a)
            
    t.right(90)
    for times in range (x):
        for c in ['yellow','light yellow','gold']:
       
            t.pencolor(c)
            t.forward(times*n)
            t.right(a)
           
       
    t.right(90)
    for times in range (x):
        for c in ['yellow','light yellow','gold']:
            t.pencolor(c)
            t.forward(times*n)
            t.right(a)
            

def flower(t,c1,c2,x,y):
    t.color(c1)
    t.pensize(20)
    for times in range(6):
        t.forward(60)
        t.right(60)
        jump(t,x,y)
 

    jump(t,x,x-15)
    t.pensize(1)
    t.begin_fill()
    t.color(c2)
    t.circle(20)
    t.end_fill()

def margolin(t):      

    for times in range(25):
        t.color(times*10,0,0)
            
        polygon(t,3,times+10)
        t.left(1)
        t.forward(10)

    t.left(90)
























        
