# Simple Game Mechanics in Python

In this section, you will explore some simple game mechanics available in Python using [pyGlet](https://bitbucket.org/pyglet/pyglet/wiki/Home), which you will need to install either using MacPorts, Brew, or Anaconda.

There is an excellent tuturial on basic pyGlet structure which is [available at this link](http://simeonfranklin.com/talk/pyglet/slides.html#slide-1), which you should work your way through.

Here is some code that generates randomly placed circles:

    $ import pyglet
    $ from pyglet.gl import *
    $ from math import *
    $ from random import randint
    $
    $ window = pyglet.window.Window()
    $ global drawList
    $
    $ ncircles = 2
    $ drawList = [0]*ncircles
    $
    $ global center1, center2
    $ center1 = [window.width/2, window.height/2]
    $ center2 = [window.width/2, window.height/2]
    $
    $ #print window.width, window.height
    $
    $def makeCircle(numPoints, radius, xcenter, ycenter):
    $    vertices = []
    $    for i in range(numPoints):
    $        angle = radians(float(i)/numPoints * 360.0)
    $        x = radius*cos(angle) + xcenter
    $        y = radius*sin(angle) + ycenter
    $        vertices += [x,y]
    $    circle = pyglet.graphics.vertex_list(numPoints, ('v2f', vertices))
    $    return circle
    $
    $@window.event
    $def on_draw():
    $
    $    drawList[0] = makeCircle(100, 20, center1[0], center1[1])
    $    drawList[1] = makeCircle(100, 50, center2[0], center2[1])
    $
    $    glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)
    $
    $    glColor3f(1,1,0)
    $    drawList[0].draw(GL_LINE_LOOP)
    $
    $    glColor3f(0.5,0,1)
    $    drawList[1].draw(GL_LINE_LOOP)
    $
    $#    for element in drawList:
    $#        glColor3f(1,1,0)
    $#        element.draw(GL_LINE_LOOP)
    $
    $def update(dt):
    $    #print(dt) # time elapsed since last time a draw was called
    $    print "Execute Some Function here to update the centers of the circles"
    $    center1[0] = window.width/2 + randint(-200,200)
    $    center1[1] = window.height/2 + randint(-200,200)
    $    center2[0] = window.width/2 + randint(-200,200)
    $    center2[1] = window.height/2 + randint(-200,200)
    $
    $if __name__ == '__main__':
    $
    $    #    pyglet.clock.schedule(update) # cause a timed event as fast the architecture allows!
    $    pyglet.clock.schedule_interval(update, 1/2.0) # update at 2Hz
    $    pyglet.app.run()






