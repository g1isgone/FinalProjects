#Ji Won Chung 
#Final Project: Image Odd-Column Complement
#Program that changes the Odd-Column of a .gif to its complement 

from graphics import *

def Complement(img, win, w,h):
    '''function that changes odd-column of the image to its complement
    '''
    
    for row in range(h):
        win.update() # refresh the window after each inner loop

        for column in range( w ):
            if column%2 == 0:
                r,g,b =  img.getPixel(column, row)
                compr = 255-r
                compg = 255-g
                compb = 255-b
                color = color_rgb( compr, compg, compb )
                img.setPixel( column, row, color)

    
            
    
    
def main():
    '''function that creates a window for an img and transforms it
    '''

    #Ask user for image and import it 
    imageFilename = input( 'Filename: ')
    img = Image( Point(0,0), imageFilename)
    w = img.getWidth( )
    h = img.getHeight( )
    print( 'w, h=', w,h, 'pixels')
    
    
    # Now construct window of size w x h
    win = GraphWin("Image", w, h)
    
    # Move the center to the int center
    img.move( w//2, h//2)
    img.draw( win)

    
    #Click to have odd-column complement of image
    win.getMouse()
    Complement(img, win, w, h)

    #Click to close 
    win.getMouse()
    win.close()

main()
