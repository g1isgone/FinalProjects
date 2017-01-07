#Ji Won Chung 
#Final: Part III
#A program that creates fireflies and simulates random firefly movement within a box.


from graphics import *
from random import*

class Firefly:
    def __init__(self, x, y, radius, win):
        '''function that constructs a firefly
        '''
        
        self.x = x
        self.y = y
         
        #create body of firefly 
        bodypt1 = Point(x, y)
        self.body = Circle(bodypt1, radius)

        #retrieve coordinates of center of body
        bodycent = self.body.getCenter()
        xbody = bodycent.getX()
        ybody = bodycent.getY()
    
            
    def setFill(self):
        '''function that sets the color of firefly as gray or off
        '''

        self.body.setFill('gray') 
        

    def On(self):
        '''function that turns firefly on or yellow only if randnum  is divisible
        by 5 to ensure that it is more off than on
        '''
        randnum = randint(-21, 21)
        
        #if y is divisible by 5, then yellow or "on"
        if randnum%5 == 0:
            self.body.setFill('yellow')
             


    def move(self):
        '''function that moves firefly so it never escapes the window
        '''
        
        #retrieve x- and y-coordinate of firefly body 
        bodycent = self.body.getCenter()
        xbody = bodycent.getX()
        ybody = bodycent.getY()

        #Original speed/movement of the fireflies 
        dx = randint(-30, 30)
        dy = randint(-30, 30)

        #move firefly randomly back into the invisible box if outside it 
        if xbody < -470:
            diff = xbody + 470
            dx = randint(-diff, -diff + 10)

        if xbody > 470:
            diff = xbody - 470
            dx = randint(-diff -10, -diff)           

        if ybody < -470:
            diff = ybody + 470
            dy = randint(-diff, -diff + 10)
            
        if ybody > 470:
            diff = ybody - 470
            dy = randint(- diff -10, -diff) 
            
        self.body.move(dx, dy)

        return dx, dy

        
    def draw(self, win):
        '''function that draws firefly
        '''
        body = self.body.draw(win)
 

        return body

#-------------------------------------------------------------------------------------

def RandCoords(n):
    '''function that returns random coordinates
    '''
    x = randint(-n, n)
    return x


def main():
    '''function that creates moving fireflies 
    '''

    nfirefly = eval(input("How many fireflies? "))
     
    
    #Create Window
    w = 500
    win = GraphWin('Flying fireflies via list', w, w)
    win.setBackground('black')
    win.setCoords(-w, -w, w, w)
    
 
    #create list of fireflies 
    Lfirefly = []
    for firefly in range(nfirefly):
        x = RandCoords(450)
        y = RandCoords(450)
        radius = 10
        firefly = Firefly( x, y, radius, win)
        firefly.draw(win)
        Lfirefly.append(firefly)
 
  
    #click to animate firefly
    win.getMouse()

    #Print num of fireflies and statement to click mouse to quit
    print("#Fireflies= ", nfirefly)
    print("Click mouse to quit...")


    #continue animating firefly until clicked 
    while True:
        if win.checkMouse():
            break
        
        
        else: 
            for firefly in Lfirefly:
                dx, dy = firefly.move() 
                firefly.setFill()
                firefly.On()
     

    
   
    #close window when clicked 
    win.getMouse()
    win.close()
    
main()

