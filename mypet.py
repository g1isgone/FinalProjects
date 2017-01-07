#160422 A10 Tamagochi
#Ji Won Chung
#Program creates a Platypus Tamagochi. Pet can be fed and the feed meter changes correspondingly.
#The program also involves an user-interactive game that affects the emotion of the Platypus.

from graphics import *
from random import *

#---------------------------------------------------------------------------------------
class Platypus:
    def __init__(self, w, x, y):
        '''Constructs a Platypus and its clothes
        ''' 

        self.x = x
        self.y = y

        #default happiness level is 0, or neutral
        self.happiness = 0
            
        #create body of platypus
        b = w//3
        a = w//7

        bodypt1 = Point(-b, a)
        bodypt2 = Point(b, -a)
        
        self.body = Rectangle( bodypt1, bodypt2 )

        #create tail of platypus
        tailpt1 = Point(b, -a//3)
        tailpt2 = Point(2*b, -a//3)
        tailpt3 = Point(2*b, -a)
        tailpt4 = Point(b, -a)

        self.tail = Polygon( tailpt1, tailpt2, tailpt3, tailpt4)


        #create happytail of platypus
        htailpt1 = Point(b, -a//3 )
        htailpt2 = Point(2*b, -a//3 + 20)
        htailpt3 = Point(2*b, -a + 20)
        htailpt4 = Point(b, -a)

        self.htail = Polygon( htailpt1, htailpt2, htailpt3, htailpt4 )

        #create sadtail of platypus
        stailpt1 = Point(b, -a//3 )
        stailpt2 = Point(2*b, -a//3 -20)
        stailpt3 = Point(2*b, -a -20)
        stailpt4 = Point(b,-a )

        self.stail = Polygon( stailpt1, stailpt2, stailpt3, stailpt4 )
        
        #create eye of platypus
        irispt = Point(-b//2, -a + a)

        self.iris = Circle(irispt, b//10)

        #create pupil of platypus
        pupilpt = irispt
        
        self.pupil = Circle(pupilpt, b//20)

        #create bottom mouth of platypus
        bmpt1 = Point(-3*b//2, -3*a//4)
        bmpt2 = Point(-b, -a)

        self.bmouth = Rectangle( bmpt1, bmpt2 )


        #create top mouth of platypus
        tmpt1 = Point(-3*b//2, -2*a//6)
        tmpt2 = Point(-b, -2*a//4)
   
        self.tmouth = Rectangle( tmpt1, tmpt2 )

        #create top mouth of platypus when happy
        self.ntmouth = self.tmouth.clone()
        self.ntmouth.move(0, 20)

        #create top mouth of platypus when sad
        self.stmouth = self.tmouth.clone()
        self.stmouth.move(0, -20) 

        #create one foot of platypus
        foot1pt1 = Point(-2*b//3, -a -20 )
        foot1pt2 = Point(-2*b//3 + 40, -a - 20 )
        foot1pt3 = Point(-2*b//3 +20, -a + 20)

        self.foot = Polygon(foot1pt1, foot1pt2, foot1pt3)

        #create second foot of platypus
        self.foot2 = self.foot.clone()
        self.foot2.move(200, 0)

        #create agent hat
        toppt1 = Point(x, y-20)
        toppt2 = Point(x + 90,y +30)
        self.top = Rectangle(toppt1, toppt2)

        fringept1 = Point(x-20, y)
        fringept2 = Point(x + 110, y - 40)
        self.fringe = Oval(fringept1, fringept2 )

        bandpt1 = Point(x , y -10)
        bandpt2 = Point(x +90, y - 20)
        self.band = Rectangle(bandpt1, bandpt2)

        #create tutuband 
        tutupt1 = Point(2*b//3, a + 20)
        tutupt2 = Point(2*b//3, -a - 20)
        tutupt3 = Point(20, -a)
        tutupt4 = Point(20, a)
        
        self.tutu = Polygon( tutupt1, tutupt2, tutupt3, tutupt4)
        
                        
    def draw(self):
        '''Draw the Platypus
        '''
        
        foot = self.foot.draw(win)
        foot2 = self.foot2.draw(win)
        body = self.body.draw(win)
        tail = self.tail.draw(win)
        iris = self.iris.draw(win)
        pupil  = self.pupil.draw(win)
        bmouth = self.bmouth.draw(win)
        tmouth = self.tmouth.draw(win)
       
        return body, tail, iris, pupil, bmouth, tmouth, foot, foot2 


    def drawMood(self, mood):
        '''Draw the Mood of the Platypus
        '''

        #undraw components that affect the mood
        self.tail.undraw()
        self.htail.undraw()
        self.stail.undraw()
        self.tmouth.undraw()
        self.ntmouth.undraw()
        self.stmouth.undraw()
        self.band.undraw()
        self.top.undraw()
        self.fringe.undraw()
        self.tutu.undraw()
        
        #if happiness level is -1 or sad 
        if mood == -1:
            tail = self.stail.draw(win)
            mouth = self.stmouth.draw(win)
            tutu = self.tutu.draw(win)
            
            return tail, mouth, tutu
        
        #if happiness level is 1 or happy
        elif mood == 1:
            tail = self.htail.draw(win)
            mouth = self.ntmouth.draw(win)
            fringe = self.fringe.draw(win)
            top = self.top.draw(win)
            band = self.band.draw(win)
            
            return tail, mouth, top, fringe, band

        #if mood level is 0 or neutral
        elif mood == 0:
            tail = self.tail.draw(win)
            mouth = self.tmouth.draw(win)
            
            return tail, mouth
        
    def setMood(self, mood):
        '''set the nood and change the Platypus accordingly
        '''
        
        self.mood = mood
        self.drawMood(mood)

    def getMood(self):
        '''Retrieve level of mood
        '''
        
        return self.mood
        
    def setFill(self):
        '''Set the color of the platypus and its clothes
        '''
         
        self.body.setFill('dark turquoise')
        self.tail.setFill('orange')
        self.iris.setFill('white')
        self.pupil.setFill('black')
        self.bmouth.setFill('orange')
        self.ntmouth.setFill('orange')
        self.stmouth.setFill('orange')
        self.tmouth.setFill('orange')
        self.htail.setFill('orange')
        self.stail.setFill('orange')
        self.foot.setFill('orange')
        self.foot2.setFill('orange')
        self.top.setFill('saddle brown')
        self.band.setFill('black')
        self.fringe.setFill('saddle brown')
        self.tutu.setFill('pink')
    
#-----------------------------------------------------------------
class Button:

    def __init__( self, pcent, width, height, strlabel ):
        ''' Creates Buttons
        '''
        
        w,h = width/2, height/2
        x,y = pcent.getX( ), pcent.getY( )
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point( self.xmin, self.ymin )
        p2 = Point( self.xmax, self.ymax )
        self.rect = Rectangle( p1, p2 )
        self.rect.setFill( 'LightGray' )
        self.rect.draw( win )
        self.textlabel = Text( pcent, strlabel )
        self.textlabel.setSize( 18 )
        self.strlabel = strlabel
        self.textlabel.draw( win )
        self.active = False
        self.deactivate( )

    def clicked( self, p ):
        ''' Returns T if p is inside active button
        '''

        x,y = p.getX( ), p.getY( )
        bool_clicked = (self.active
                and
                self.xmin <= x <= self.xmax
                and
                self.ymin <= y <= self.ymax
                )
                         
        return bool_clicked
    
    def getLabel( self ):
        ''' Return the button label
        '''
        return self.strlabel

    def activate( self ):
        ''' Activate the button visually and with a boolean flag
        '''
        
        self.textlabel.setFill( 'Black' )
        self.rect.setWidth( 3 )
        self.rect.setOutline( 'Red' )
        self.active = True

    def deactivate( self ):
        ''' Deativate the button visually and set flag to F
        '''

        self.textlabel.setFill( 'darkgray' )
        self.rect.setWidth( 1 )
        self.rect.setOutline( 'Black' )
        self.active = False


#-------------------------------------------------------------------------------------
class Game:
    def __init__(self, cent, radius):
        '''Creates game
        '''
        
        self.bubble = Circle(cent, radius)
        self.rect = Rectangle(Point(-400, -100), Point(400, -450))
        self.smallrect = Rectangle(Point(-350, - 150), Point(350, -400))
        self.radius = radius

    
    def boardDraw(self):
        '''Draw board of the game
        '''
        return self.rect.draw(win), self.smallrect.draw(win)

    def bubbleDraw(self):
        '''Draw bubble of the game
        '''
        return self.bubble.draw(win)

    def bubbleUndraw(self):
        '''Undraw bubble of the game
        '''
        return self.bubble.undraw()

    def bubbleMove(self, dx, dy):
        '''Move bubble by dx, dy
        '''
        self.bubbleMove(dx, dy)
        
    def setFill(self):
        '''Set the color for the board and the bubble
        '''
        self.bubble.setFill('darkturquoise')
        self.rect.setFill('darkgoldenrod')
        self.smallrect.setFill('khaki')

   
    def clicked(self):
        '''Determine if bubble is clicked, return mood
        '''

        #Retrieve center of the bubble
        self.circent = self.bubble.getCenter()
        self.circentx, self.circenty = self.circent.getX(), self.circent.getY()

        #Set the click range limits
        self.xmin = self.circentx - self.radius
        self.xmax = self.circentx + self.radius
        self.ymin = self.circenty - self.radius
        self.ymax = self.circenty + self.radius

        #click mouse and its center
        self.cent = win.getMouse()
        self.centX = self.cent.getX()
        self.centY = self.cent.getY()

        #generate random numbers
        a = randint(-50, 50)
        b = randint(-50, 50)


        #define bool_clicked or click range
        bool_clicked = (self.xmin <= self.centX <= self.xmax and
            self.ymin <= self.centY <= self.ymax)

        #if bubble is clicked 
        if bool_clicked == True:

            #move the bubble
            self.bubble.move(a, b)

            #retrieve the newcenter of teh bubble
            newcent = self.bubble.getCenter()
            newcentX = newcent.getX()
            newcentY = newcent.getY() 

            #if bubble escaped the box return 1, or happy and move bubble back into box 
            if 350 <= newcentX:
                self.bubble.move(-50, 0)
                self.bubble.undraw()
                return 1

            if newcentX <= -350:
                self.bubble.move(50, 0)
                self.bubble.undraw()
                return 1

            if -150 <= newcentY:
                self.bubble.move(0, -50)
                self.bubble.undraw()
                return 1

            if newcentY <= -400:
                self.bubble.move(0, 50)
                self.bubble.undraw()
                return 1

            #if bubble is still inside the box return 0, or neutral
            elif -350 <= newcentX <= 350 and -400 <= newcentY <= -150:
                return 0

            #otherwise return neutral 
            else:
                return 0
            
        if bool_clicked == False:
            return 0 
               
    def undraw(self):
        '''undraw the board
        '''
        self.rect.undraw()
        self.smallrect.undraw()

    def move(self, dx, dy):
        '''move the bubble
        '''
        self.bubble.move(dx, dy)

    def getCenter(self):
        '''retrieve the center of the bubble
        '''
        return self.bubble.getCenter()

#-------------------------------------------------------------------------------------

class HungerMeter:
    def __init__(self, x, y):
        '''Create a Hunger meter that indicates levels of hunger
        '''
        
        self.x = x
        self.y = y
        self.hunger = 0

        #Create the Gray part of the meter
        rectpt = Point(x, y)
        rectpt2 = Point(x + 70, y + 205 )
        self.rect = Rectangle(rectpt, rectpt2)
        
        #Create the bar of the meter
        barpt = Point(x , y)
        barpt2 = Point(x + 70, y + 5)
        self.bar = Rectangle(barpt, barpt2)

        #Hunger Level 1 
        onept1 = Point(x, y+40)
        onept2 = Point(x+70, y+40)
  
        #hunger Level 2
        twopt1 = Point(x, y+80)
        twopt2 = Point(x+70, y+80)
  
        #hunger Level 3
        threept1 = Point(x, y+120)
        threept2 = Point(x+70, y+120)
       
        
        #hunger Level 4
        fourpt1 = Point(x, y+160)
        fourpt2 = Point(x+70, y+160)
      
        #construct hunger indication lines
        self.line1 = Line(onept1, onept2)
        self.line2 = Line(twopt1, twopt2)
        self.line3 = Line(threept1, threept2)
        self.line4 = Line(fourpt1, fourpt2)

        #create a hunger text
        self.hungertext = Text(Point(430, 150), "Hunger \n Meter")
        self.hungertext.setTextColor('white')
        self.hungertext.setSize(15)
        
    def draw(self):
        '''Draw the Hunger Meter
        '''

        #draws the gray part first
        rect = self.rect.draw(win)

        #draws the lines on the meter to indicate energy levels
        line1 = self.line1.draw(win)
        line2 = self.line2.draw(win)
        line3 = self.line3.draw(win)
        line4 = self.line4.draw(win)

        #draws text that describes meter
        text = self.hungertext.draw(win)
       
        return rect, line1, line2, line3, line4, text

    def drawBar(self):
        '''Draw the bars or levels of energy in the meter
        '''

        #draw bar when self.hunger is negative
        if self.hunger <= 0:
            pt1 = Point(self.x, self.y + 20)
            pt2 = Point(self.x + 70, self.y)
            self.bar = Rectangle(pt1, pt2)
            return self.bar.draw(win)

        #draw bar when self.hunger is 1 ~ 5 
        if 1 <= self.hunger <= 5:
            pt1 = Point(self.x, self.y + 40 * self.hunger)
            pt2 = Point(self.x + 70, self.y)
            self.bar = Rectangle(pt1, pt2)
            return self.bar.draw(win)

        #draw bar when self.hunger is greater than 5
        if 5 < self.hunger:
            pt1 = Point(self.x, self.y + 40 * 5)
            pt2 = Point(self.x + 70, self.y)
            self.bar = Rectangle(pt1, pt2)
            return self.bar.draw(win)

    def undrawBar(self):
        '''Undraw the bar or energy level
        '''
        self.bar.undraw()

    def setFill(self):
        '''Fill the color of the gray part of the meter
        '''
        self.rect.setFill('gray')
    
        
    def barFill(self):
        '''Fill the bar energy level color to red
        '''
        self.bar.setFill('red')

    def setHunger(self, hunger):
        '''Sets the Hunger of the meter, and changes the meter accordingly
        '''

        #defines self.hunger 
        self.hunger = self.hunger + hunger

        #if energy is below meter, say it has 0 energy, instaead of negative
        if self.hunger < 0:
            self.hunger = 0

        #if energy is above meter, say it has full energy levels to prevent overload 
        if 5 < self.hunger:
            self.hunger = 5

        #modify the bar 
        self.undrawBar()
        self.drawBar()
        self.barFill()

    def getHunger(self):
        return self.hunger 
#----------------------------------------------------------------------------

def main():
    '''function that creates platypuses
    '''
    global win

    #Create Window
    w = 500
    win = GraphWin('Platypus Tamagochi', w, w, autoflush = False)
    oceancolor = 'steel blue'
    win.setBackground(oceancolor)
    win.setCoords(-w, -w, w, w)

    #Construct and change platypus
    platypus = Platypus(w, -100, 90)
    platypus.setFill()

    #construct the opening text
    text = Text(Point(0,0), "Click screen to start.")
    text.draw(win)
    text.setSize(30)
    text.setTextColor('white')

    #get rid of text after click and draw platypus
    win.getMouse()
    text.undraw()
    platypus.draw()
 

    #create a play button
    playbtnlocation = Point(-430, 450)
    playbtn = Button( playbtnlocation, 100, 50, 'Play')

    #create a quit button
    quitbtnlocation = Point(-430, 370)
    quitbtn = Button( quitbtnlocation, 100, 50, 'Quit')

    #create a feed button
    feedbtnlocation = Point(430, 450)
    feedbtn = Button( feedbtnlocation, 100, 50, 'Feed')

    #create a hunger meter
    hungermeter = HungerMeter(400, 200)
    hungermeter.setFill()
    hungermeter.draw()
    hungermeter.setHunger(5)
        
    #creae a bubble
    radius = 30
    game = Game(Point(0, -200), radius)
    game.setFill()
       

    #text for description of game 
    description = Text(Point(0, -470), "Click the blue Perry bubble to help Perry the Platypus escape.")
    description.setSize(15)
    description.setTextColor('white')
    
    #text for state of platypus 
    state = Text(Point( 0, - 150), "You're Trapped!")

    #Game 
    playing = True
    while playing:
        playbtn.activate()
        quitbtn.activate()
        feedbtn.activate()

        p = win.getMouse()

        #deactivate play button if platypus is low on energy
        hungerlvl = hungermeter.getHunger()
        if hungerlvl == 0:
            playbtn.deactivate()
        
        #If you click Play button, start game
        elif playbtn.clicked( p ):

            #Set neutral or initial settings 
            description.draw(win)
            state.undraw()
            game.boardDraw()
            game.bubbleDraw()
            platypus.setMood(0)
            hungermeter.setHunger(-1)
            playbtn.deactivate()
     
            #Game that requires 10 clicks 
            for i in range(10):
                mood = game.clicked()
                platypus.setMood(mood)

                #if platypus is out the box, indicate victory
                if mood == 1:
                    playbtn.activate() 
                    hungermeter.setHunger(1)
                    state = Text(Point( 0, - 170), "You've Escaped!")
                    state.setSize(36)
                    state.setTextColor('white')
                    break
                
            #If platypus is in the box, indciate loss
            if platypus.mood == 0:
                playbtn.activate()
                platypus.setMood(-1)
                hungermeter.setHunger(-1)
                state = Text(Point( 0, - 170), "You're Trapped!")
                state.setSize(36)
                state.setTextColor('white')                

            #Get rid of game, draw the state of win/loss
            game.undraw()
            game.bubbleUndraw()
            description.undraw()
            state.draw(win)
     
        #If you click feed button, change hunger meter                
        if feedbtn.clicked(p):
            feedbtn.deactivate()
            hungermeter.setHunger(1)
            state.undraw()
            
        #If you click quit button, return false and break the loop
        if quitbtn.clicked(p):
            playing = False
            break

    #close entire game and window 
    if playing == False:
        win.close()
            
 
main()
         
