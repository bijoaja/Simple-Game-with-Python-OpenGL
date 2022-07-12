from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


w,h = 800,800 


def badan():
    glBegin(GL_POLYGON)
    glColor3ub(124, 252, 0)
    glVertex2f(60, 224)
    glVertex2f(61, 230)
    glVertex2f(65, 233)
    glVertex2f(70, 234)
    glVertex2f(75, 233)
    glVertex2f(79, 230)
    glVertex2f(80, 224)
    glEnd()
    
def badan2():
    glBegin(GL_POLYGON)
    glColor3ub(124, 252, 0)
    glVertex2f(60, 224)
    glVertex2f(61, 220)
    glVertex2f(65, 216)
    glVertex2f(70, 214)
    glVertex2f(76, 216)
    glVertex2f(79, 221)
    glVertex2f(80, 224)
    glEnd()


def mataKanan():
    glBegin(GL_QUADS)
    glColor3ub(255,250,250)
    glVertex2f(64, 230)
    glVertex2f(68, 230)
    glVertex2f(68, 226)
    glVertex2f(64, 226)
    glEnd()
    
def hitamKanan():
    glBegin(GL_QUADS)
    glColor3ub(0,0,0)
    glVertex2f(65, 227)
    glVertex2f(65, 229)
    glVertex2f(67, 229)
    glVertex2f(67, 227)
    glEnd()


def mataKiri():
    glBegin(GL_QUADS)
    glColor3ub(255,250,250)
    glVertex2f(72, 230)
    glVertex2f(72, 226)
    glVertex2f(76, 226)
    glVertex2f(76, 230)
    glEnd()


def hitamKiri():
    glBegin(GL_QUADS)
    glColor3ub(0,0,0)
    glVertex2f(73, 229)
    glVertex2f(73, 227)
    glVertex2f(75, 227)
    glVertex2f(75, 229)
    glEnd()

def mulut2():
    glBegin(GL_POLYGON)
    glColor3ub(0,0,0)
    glVertex2f(66, 222)
    glVertex2f(66, 224)
    glVertex2f(74, 224)
    glVertex2f(74, 222)
    glVertex2f(72, 220)
    glVertex2f(69, 220)
    glEnd()

def gigi1():    
    glBegin(GL_TRIANGLES)
    glColor3ub(255,250,250)
    glVertex2f(66, 224)
    glVertex2f(67, 223)
    glVertex2f(68, 224)
    glEnd()
    
def gigi2():    
    glBegin(GL_TRIANGLES)
    glColor3ub(255,250,250)
    glVertex2f(70, 224)
    glVertex2f(69, 223)
    glVertex2f(68, 224)
    glEnd()

def gigi3():    
    glBegin(GL_TRIANGLES)
    glColor3ub(255,250,250)
    glVertex2f(70, 224)
    glVertex2f(71, 223)
    glVertex2f(72, 224)
    glEnd()

def gigi4():    
    glBegin(GL_TRIANGLES)
    glColor3ub(255,250,250)
    glVertex2f(72, 224)
    glVertex2f(73, 223)
    glVertex2f(74, 224)
    glEnd()
    
def gigi():
    gigi1()
    gigi2()
    gigi3()
    gigi4()
    
def lidah():
    glBegin(GL_POLYGON)
    glColor3ub(255,0,0)
    glVertex2f(68, 220)
    glVertex2f(69, 221)
    glVertex2f(71, 221)
    glVertex2f(72, 220)
    glEnd()
    
def duri1():
    glBegin(GL_TRIANGLES)
    glColor3ub(0, 0, 0)
    glVertex2f(65, 233)
    glVertex2f(66, 237)
    glVertex2f(70, 234)
    glEnd()

def duri2():
    glBegin(GL_TRIANGLES)
    glColor3ub(0, 0, 0)
    glVertex2f(70, 234)
    glVertex2f(74, 237)
    glVertex2f(75, 233)
    glEnd()

def duri3():
    glBegin(GL_TRIANGLES)
    glColor3ub(0, 0, 0)
    glVertex2f(75, 233)
    glVertex2f(79, 234)
    glVertex2f(79, 230)
    glEnd()

def duri4():
    glBegin(GL_TRIANGLES)
    glColor3ub(0, 0, 0)
    glVertex2f(79, 230)
    glVertex2f(82, 229)
    glVertex2f(80, 224)
    glEnd()

def duri5():
    glBegin(GL_TRIANGLES)
    glColor3ub(0, 0, 0)
    glVertex2f(80, 224)
    glVertex2f(85, 221)
    glVertex2f(79, 221)
    glEnd()

def duri6():
    glBegin(GL_TRIANGLES)
    glColor3ub(0, 0, 0)
    glVertex2f(79, 221)
    glVertex2f(82, 216)
    glVertex2f(76, 216)
    glEnd()
        

def duri7():
    glBegin(GL_TRIANGLES)
    glColor3ub(0, 0, 0)
    glVertex2f(76, 216)
    glVertex2f(74, 212)
    glVertex2f(70, 214)
    glEnd()

def duri8():
    glBegin(GL_TRIANGLES)
    glColor3ub(0, 0, 0)
    glVertex2f(70, 214)
    glVertex2f(66, 211)
    glVertex2f(65, 216)
    glEnd()

def duri9():
    glBegin(GL_TRIANGLES)
    glColor3ub(0, 0, 0)
    glVertex2f(65, 216)
    glVertex2f(60, 215)
    glVertex2f(61, 220)
    glEnd()

def duri10():
    glBegin(GL_TRIANGLES)
    glColor3ub(0, 0, 0)
    glVertex2f(61, 220)
    glVertex2f(56, 222)
    glVertex2f(60, 224)
    glEnd()

def duri11():
    glBegin(GL_TRIANGLES)
    glColor3ub(0, 0, 0)
    glVertex2f(60, 224)
    glVertex2f(56, 228)
    glVertex2f(61, 230)
    glEnd()

def duri12():
    glBegin(GL_TRIANGLES)
    glColor3ub(0, 0, 0)
    glVertex2f(61, 230)
    glVertex2f(60, 235)
    glVertex2f(65, 233)
    glEnd()
    
def duri():
    duri1()
    duri2()
    duri3()
    duri4()    
    duri5()
    duri6()
    duri7()
    duri8()
    duri9()
    duri10()
    duri11()
    duri12()
    
def kuman():
    glPushMatrix()
    glScalef(2, 2, 0)
    glTranslated(150, -109, 0) 
    badan()
    badan2()
    mataKanan()
    hitamKanan()
    mataKiri()
    hitamKiri()
    mulut2()
    gigi()
    lidah()
    duri()
    glPopMatrix()
