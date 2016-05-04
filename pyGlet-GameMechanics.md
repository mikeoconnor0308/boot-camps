# Simple Game Mechanics in Python

In this section, you will explore some simple game mechanics available in Python using [pyGlet](https://bitbucket.org/pyglet/pyglet/wiki/Home), which you will need to install either using MacPorts, Brew, or Anaconda.

There is an excellent & very easy tuturial on basic pyGlet structure which is [available at this link](http://simeonfranklin.com/talk/pyglet/slides.html#slide-1), which you should work your way through.

Here is some code, call it pyGlet-draw.py, that generates randomly placed circles. Note that the makeCircle function actually builds a lists of vertices, which pyGlet then "draws" by sequentially connecting lines between the vertices:

```
import pyglet
from pyglet.gl import *
from math import *
from random import randint
    
window = pyglet.window.Window()
global drawList
    
ncircles = 2
drawList = [0]*ncircles
    
global center1, center2
center1 = [window.width/2, window.height/2]
center2 = [window.width/2, window.height/2]
    
#print window.width, window.height
    
def makeCircle(numPoints, radius, xcenter, ycenter):
    vertices = []
    for i in range(numPoints):
        angle = radians(float(i)/numPoints * 360.0)
        x = radius*cos(angle) + xcenter
        y = radius*sin(angle) + ycenter
        vertices += [x,y]
    circle = pyglet.graphics.vertex_list(numPoints, ('v2f', vertices))
    return circle
    
@window.event
def on_draw():

    drawList[0] = makeCircle(100, 20, center1[0], center1[1])
    drawList[1] = makeCircle(100, 50, center2[0], center2[1])
    
    glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)
    
    glColor3f(1,1,0)
    drawList[0].draw(GL_LINE_LOOP)
    
    glColor3f(0.5,0,1)
    drawList[1].draw(GL_LINE_LOOP)
    
def update(dt):             #note that dt is the time elapsed since last time a draw was called
    #print(dt) 
    print "Execute Some Function here to update the centers of the circles"
    center1[0] = window.width/2 + randint(-200,200)
    center1[1] = window.height/2 + randint(-200,200)
    center2[0] = window.width/2 + randint(-200,200)
    center2[1] = window.height/2 + randint(-200,200)
    
if __name__ == '__main__':
#    pyglet.clock.schedule(update) # this command tells the machine to carry out draws as fast the architecture allows!
    pyglet.clock.schedule_interval(update, 1/2.0) # this command tells the machine to update at 2Hz
    pyglet.app.run()
```

#Tasks

There's a few things that you should try and do with this code:

* Get it running in PyCharm

* Figure out how to extend the code to draw more than three circles
    hint - you can think about populating drawList, and then looping over drawList, something like:
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


