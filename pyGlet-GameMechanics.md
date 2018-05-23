# Simple Game Mechanics in Python

In this section, you will explore some simple game mechanics available in Python using [pyGlet](https://bitbucket.org/pyglet/pyglet/wiki/Home), which you will need to install either using MacPorts, Brew, or Anaconda.

There is an excellent & very easy tuturial on basic pyGlet structure which is [available at this link](http://simeonfranklin.com/talk/pyglet/slides.html#slide-1), which you should work your way through. Don't worry about making the game suggested in the final slide of the tutorial. Work through the example below instead.

Here is some code, call it pyGlet-drawCircles.py, that generates randomly placed circles. Note that the makeCircle function actually builds a lists of vertices, which pyGlet then "draws" by sequentially connecting lines between the vertices. The functions in the graphicsWindow class behave as follows:

* \__init__(self) is responsible for initializing the important data structures required during draws & updates

* on_draw() is responsible for executing the drawing instructions
 
* update() is responsible for executing instructions required to update the positions of objects
 
* when pyglet runs, it calles on_draw() and update() at the frequency specified in pyglet.clock.schedule_interval()
 
```
import pyglet
from pyglet.gl import *
from math import *
from random import randint

def makeCircle(numPoints, radius, xcenter, ycenter):
    vertices = []
    for i in range(numPoints):
        angle = radians(float(i)/numPoints * 360.0)
        x = radius*cos(angle) + xcenter
        y = radius*sin(angle) + ycenter
        vertices += [x,y]
    circle = pyglet.graphics.vertex_list(numPoints, ('v2f', vertices))
    return circle

class graphicsWindow(pyglet.window.Window):
    def __init__(self):
        super(graphicsWindow, self).__init__()
        self.ncircles = 2
        self.drawList = [0]*self.ncircles
        self.center1 = [self.width/2,self.height/2]
        self.center2 = [self.width/2,self.height/2]

    def on_draw(self):
        self.drawList[0] = makeCircle(100, 20, self.center1[0], self.center1[1])  # populate the drawList
        self.drawList[1] = makeCircle(100, 50, self.center2[0], self.center2[1])
    
        glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)  # clear the graphics buffer
        glColor3f(1,1,0)                        # specify colors & draw
        self.drawList[0].draw(GL_LINE_LOOP)
        glColor3f(0.5,0,1)                      # specify colors & draw
        self.drawList[1].draw(GL_LINE_LOOP)

    def update(self,dt):
        #print(dt) # time elapsed since last time a draw was called
        print("Updating the centers of the circles")
        self.center1 = [window.width/2 + randint(-200,200), window.height/2 + randint(-200,200)]
        self.center2 = [window.width/2 + randint(-200,200), window.height/2 + randint(-200,200)]
        print("Finished update")

if __name__ == '__main__':
    window = graphicsWindow()                                 # initialize a window class
    pyglet.clock.schedule_interval(window.update, 1/2.0)  # tell pyglet how often it should execute on_draw() & update()
    pyglet.app.run()                                      # run pyglet
```


#Tasks

There's a few things that you should try and do with this code:

* Get it running in PyCharm

* Figure out how to extend the code to draw more than three circles
* 
    here's a hint - think about populating drawList, and then looping over drawList, something like:
```
    for element in drawList:
        glColor3f(1,1,0)
        element.draw(GL_LINE_LOOP)
```
* Rather than randomly generated circles, experiment with different ways of making the circles move. For example, see if you can figure out how to write a function which will make the circles travel in:

    1. Straight lines
    
    2. A circular trajectory
    
    3. Harmonically, based on how far the circle is displaced from the center of the graphics window
    
*  Split out the makeCircle() function so that it lives in a new file called 'simpleShapes.py', and figure out how to construct a module so that can run pyGlet-draw.py by simply including a line which reads "import simpleShapes" 

* Change simpleShapes.py so that rather than calling the makeCircle() function, you have a circle class, which should include data (radius, center positions, and vertex lists), as well as functions (to update position). Now you should be able to modify pyGlet-draw.py to instantiate various circle objects (e.g. circle1 = circle(...)). The position of a circle (e.g., circle1) can then be updated using a command like "circle1.updatePosition()"
 
* If you're really motivated, try and write a new class that draws a new shape (e.g., triangle, square, octagon, ellipse, rectangle, etc.)

