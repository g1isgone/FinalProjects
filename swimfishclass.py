#Ji Won Chung A9
#160411
#Create a program that creates moving fish and anchors

from graphics import *
from random import*

class Fish:
    def __init__(self, x, y, speed, radius, win):
        '''function that construct a fish
        '''
     
        self.x = x
        self.y = y
        self.speed = speed

        #create body of fish 
        bodypt1 = Point(x, y)
        bodypt2 = Point(x + 120, y + 35)
        
        self.body = Oval(bodypt1, bodypt2)

        #retrieve coordinates of center of body
        bodycent = self.body.getCenter()
        xbody = bodycent.getX()
        ybody = bodycent.getY()

        #find x-coordinates of tail and iris depending on speed 
        if self.speed < 0:
            x1tail = xbody + 50
            x2tail = x1tail + 30
            xiris = xbody - 40

        else:
            x1tail = xbody - 50
            x2tail = x1tail - 30
            xiris = xbody + 40
        
        #create tail of fish 
        y1tail = ybody - 40
        y2tail = ybody + 40
        
        tailpt1 = Point(x1tail, y1tail)
        tailpt2 = Point(x2tail, y2tail)

        self.tail = Oval(tailpt1, tailpt2)

        #create iris of fish 
        yiris = ybody
        irisradius = radius
        irispoint = Point(xiris, yiris)
        
        self.iris = Circle(irispoint, irisradius)

        #create pupil of fish 
        pupilradius = radius//4
        self.pupil = Circle(irispoint, pupilradius)

            
    def setFill(self, bodycolor, iriscolor):
        '''function that sets the color of fish
        '''
        
        self.body.setFill(bodycolor)
        self.tail.setFill(bodycolor)
        self.iris.setFill(iriscolor)
        self.pupil.setFill('black')


    def getSpeed(self):
        '''function that gets the speed of fish and return it
        '''
        
        return self.speed


    def move(self):
        '''function that moves fish and wrap around if necessary
        '''
        
        #retrieve center and x-coordinate of fish body 
        bodycent = self.body.getCenter()
        xbody = bodycent.getX()
        
        dy = 0
        dx = self.speed

        #move fish depending on location of the x-coord of body
        if xbody < -500:
            dx = 1000

        elif xbody > 500:
            dx = -1000            
            
        self.body.move(dx, dy)
        self.iris.move(dx, dy)
        self.tail.move(dx, dy)
        self.pupil.move(dx, dy)
        
    def draw(self, win):
        '''function that draws fish
        '''
        
        tail = self.tail.draw(win)
        body = self.body.draw(win)
        iris = self.iris.draw(win)
        pupil = self.pupil.draw(win)

        return tail, body, iris, pupil 

    
#----------------------------------------------------------------------------------------------

class Anchor:
    def __init__(self, x, y, speed, radius, win, w):
        '''function that constructs anchor
        '''
        
        self.x = x
        self.y = y
        self.speed = speed
        self.radius = radius

        #creating top knob of anchor
        center = Point(x,y)

        self.tophole = Circle(center, self.radius//2)        
        self.topcircle = Circle(center, self.radius)

        #creating line that links anchor to the top 
        linept2 = Point(x, w*3)
        
        self.line = Line(center, linept2)

        #creating vertical oval
        bottomx = x
        bottomy = y - 50 - 2*self.radius
        bottompt = Point(bottomx, bottomy)
        
        self.vertoval = Oval(center, bottompt)

        #retrieving center of vertoval 
        vertcent = self.vertoval.getCenter()
        vertx = vertcent.getX()
        verty = vertcent.getY()
        
        #creating horizontal oval of anchor
        horzx1 = vertx - 3*self.radius
        horzy1 = verty + self.radius
        horzp1 = Point(horzx1, horzy1)

        horzx2 = vertx + 3*self.radius
        horzy2 = verty + self.radius
        horzp2 = Point(horzx2, horzy2)
        
        self.horzoval = Oval(horzp1, horzp2)


        #creating ocean-colored overlap of black anchor 
        centx = x
        centy = y -50
        circlecent = Point(centx, centy + self.radius)
        
        self.overlap= Circle(circlecent, self.radius*3)

        #creating the actual black part of the anchor
        self.blackanch  = Circle(circlecent, self.radius * 4)

        #creating invisible rectangle (in_rect)
        llxrect = centx - self.radius * 5
        urxrect = centx + self.radius * 5
        llpoint = Point(llxrect, centy)
        urpoint = Point(urxrect, centy + self.radius *6)
        
        self.in_rect = Rectangle(llpoint, urpoint)

        #Information needed to create triangles
        rightx = centx + self.radius * 4 + 5
        righty = centy
        pt1 = Point(rightx, righty)

        leftx = centx + self.radius*3 - 5  
        lefty = centy
        pt2 = Point(leftx, lefty)

        midx = (leftx + rightx)//2
        midy = centy + int(self.radius * 1.5)
        pt3 = Point(midx, midy)

        #Create Right Triangle
        self.rtri = Polygon(pt1, pt2, pt3)
        self.rtri.move(0, -self.radius*.5)
        
        #Create Left Triangle 
        self.ltri = self.rtri.clone()
        self.ltri.move(-self.radius *7, 0)

    def move(self):
        '''function that moves anchor
        '''
        
        anchcent = self.blackanch.getCenter()
        yanch = anchcent.getY()
        
        dx = 0
        dy = self.speed
    
        if yanch < -500:
            dy = 1000
            dx = randint(-50, 50)

        elif yanch > 500:
            dy = -1000
            dx = randint(-50, 50)

        #move entire anchor
        self.line.move(dx, dy)
        self.in_rect.move(dx, dy)
        self.blackanch.move(dx, dy)
        self.overlap.move(dx, dy)
        self.horzoval.move(dx, dy)
        self.vertoval.move(dx, dy)
        self.topcircle.move(dx,dy)
        self.tophole.move(dx,dy)
        self.rtri.move(dx, dy)
        self.ltri.move(dx, dy)
                

    def draw(self, win):
        '''function that draws anchor and line
        '''
        
        blackanch = self.blackanch.draw(win)
        overlap = self.overlap.draw(win)
        in_rect = self.in_rect.draw(win)
        topcircle = self.topcircle.draw(win)
        vertoval = self.vertoval.draw(win)
        horzoval = self.horzoval.draw(win)
        line = self.line.draw(win)
        tophole = self.tophole.draw(win)
        rtri = self.rtri.draw(win)
        ltri = self.ltri.draw(win)
    
        return blackanch, overlap, in_rect, topcircle, vertoval, horzoval, line, tophole, rtri, ltri

    def setFill(self, oceancolor):
        '''function that sets the color of anchor and line
        '''
        
        self.topcircle.setFill('black')
        self.tophole.setFill(oceancolor)
        self.line.setFill('gray')
        self.vertoval.setFill('black')
        self.overlap.setFill(oceancolor)
        self.blackanch.setFill('black')
        self.in_rect.setFill(oceancolor)
        self.rtri.setFill('black')
        self.ltri.setFill('black')

    def setOutline(self, oceancolor):
        '''function that sets color of rectangle and overlap outline
        '''
        self.overlap.setOutline(oceancolor)
        self.in_rect.setOutline(oceancolor)

    def setWidth(self):
        '''function that sets width of line, ovals, blackanch, triangles
        '''
        self.line.setWidth(self.radius//3)
        self.vertoval.setWidth(self.radius)
        self.horzoval.setWidth(self.radius//2)
        self.blackanch.setWidth(self.radius)
        self.rtri.setWidth(self.radius//2)
        self.ltri.setWidth(self.radius//2)

    def getSpeed(self):
        '''function that returns speed of anchor
        '''
        
        return self.speed
#--------------------------------------------------------------------------------------------------------
def RanSpeed( ):
    '''function that returns a random speed
    '''
    ranspeed = randint(-50, 50)
    while ranspeed == 0:
        ranspeed = randint(-50,50)

    return ranspeed


def RanColor():
    '''function that generates and returns a random color
    '''
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    rancolor = color_rgb(r, g, b)

    return rancolor

    
def RandCoords(n):
    '''function that returns random coordinates
    '''
    x = randint(-n, n)
    return x


def main():
    '''function that creates moving fish and moving anchors
    '''

    nfish = eval(input("How many fish? "))
    nanch = eval(input("How many anchors? "))

    
    #Create Window
    w = 500
    win = GraphWin('Swimming Fish via list', w, w, autoflush = False)
    oceancolor = 'steel blue'
    win.setBackground(oceancolor)
    win.setCoords(-w, -w, w, w)
    
    
    

    #create list of anchors and list of speeds of anchors
    Lanchor = []
    Lanchspeeds = []

    for anchor in range(nanch):
        y = RandCoords(400)
        x = RandCoords(400)
        ranspeed = RanSpeed()
        tradius = 7
        anch = Anchor(x, y, ranspeed, tradius, win, w)
        anch.setFill(oceancolor)
        anch.setWidth()
        anch.setOutline(oceancolor)
        anch.draw(win)
        Lanchor.append(anch)
        Lanchspeeds.append(ranspeed)

    
    

    #create list of fish and list of speeds of fish
    Lfish = []
    Lspeeds = []
    for fish in range(nfish):
        x = RandCoords(400)
        y = RandCoords(400)
        rancolor = RanColor()
        iriscolor = RanColor()
        ranspeed = RanSpeed()
        radius = 6
        fish = Fish( x, y, ranspeed, radius, win) 
        fish.setFill(rancolor , iriscolor)
        fish.draw(win)
        Lfish.append(fish)
        Lspeeds.append(ranspeed)

    
    #click to animate Fish
    win.getMouse()

    #Print num of fish and anchors and speed of fish and anchors
    print("#Fish= ", nfish)
    print("Fish speeds= ", Lspeeds)
    print("Anchor speeds= ", Lanchspeeds)
    print("Click mouse to quit...")


    #continue animating anchor and fish until clicked 
    while True:
        if win.checkMouse():
            break
        
        else: 
            for fish in Lfish:
                fish.move()

            for anch in Lanchor:
                anch.move()
             
    #close window when clicked 
    win.getMouse()
    win.close()
    
main()

