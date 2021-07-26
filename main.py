
import random
from gl import Renderer
from obj import Object

windoWidth = 1920*1
windowHeight = 1080*1
scale= 1
viewportWidth= windoWidth*scale
viewportHeight= windowHeight *scale
viewportX=0
viewportY=0



myRenderer = Renderer(windoWidth, windowHeight)
myRenderer.glViewPort(viewportX,viewportY,viewportWidth,viewportHeight)

myObject = Object("model.obj")




#myRenderer.show()
myRenderer.glFinish("output.bmp")