from OpenGL import GL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w,h= 500,500


def rambut():
    glColor3ub(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(23, 244)
    glVertex2f(19, 247)
    glVertex2f(22, 256)
    glVertex2f(31, 254)
    glVertex2f(31, 254)
    glEnd()
    
def wajah():
    glColor3ub(255, 228, 196)
    glBegin(GL_POLYGON)
    glVertex2f(30, 241)
    glVertex2f(23, 244)
    glVertex2f(23, 253)
    glVertex2f(31, 254)
    glVertex2f(40, 252)
    glVertex2f(40, 244)
    glVertex2f(33, 241)    
    glEnd()
    
def bibir():
    glColor3ub(26, 26, 26)
    glBegin(GL_POLYGON)
    glVertex2f(30, 242)
    glVertex2f(29, 243)
    glVertex2f(29, 244)
    glVertex2f(34, 244)
    glVertex2f(34, 243)
    glVertex2f(33, 242)
    glEnd()

def lidah():
    glColor3ub(255, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(30, 242)
    glVertex2f(31, 243)
    glVertex2f(32, 243)
    glVertex2f(33, 242)
    glEnd()
    
def gigi():
    glColor3ub(255, 250, 240)
    glBegin(GL_TRIANGLES)
    glVertex2f(29, 243)
    glVertex2f(29, 244)
    glVertex2f(34, 244)
    glEnd()
    
def hidung():
    glColor3ub(139, 69, 19)
    glBegin(GL_TRIANGLES)
    glVertex2f(31, 245)
    glVertex2f(32, 246)
    glVertex2f(33, 245)
    glEnd()

def bingkaiKiri():
    glColor3ub(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(26, 248)
    glVertex2f(23, 250)
    glVertex2f(23, 251)
    glVertex2f(26, 249)
    glEnd()

def kacaKiri():
    glColor3ub(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex2f(26, 247)
    glVertex2f(26, 250)
    glVertex2f(30, 250)
    glVertex2f(30, 247)
    glEnd()

def mataKiri():
    glColor3ub(255, 228, 196)
    glBegin(GL_QUADS)
    glVertex2f(27, 248)
    glVertex2f(27, 249)
    glVertex2f(29, 249)
    glVertex2f(29, 248)
    glEnd()

def bingkaiTengah():
    glColor3ub(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex2f(30, 248)
    glVertex2f(30, 249)
    glVertex2f(33, 248)
    glVertex2f(33, 249)
    glEnd()
    
def kacaKanan():
    glColor3ub(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex2f(33, 247)
    glVertex2f(33, 250)
    glVertex2f(37, 250)
    glVertex2f(37, 247)
    glEnd()

def bingkaiKanan():
    glColor3ub(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(37, 248)
    glVertex2f(37, 249)
    glVertex2f(40, 251)
    glVertex2f(40, 250)
    glEnd()
    
def mataKanan():
    glColor3ub(255, 228, 196)
    glBegin(GL_QUADS)
    glVertex2f(34, 248)
    glVertex2f(34, 249)
    glVertex2f(36, 249)
    glVertex2f(36, 248)
    glEnd()

def leher():
    glColor3ub(255, 228, 196)
    glBegin(GL_POLYGON)
    glVertex2f(32, 238)
    glVertex2f(29, 240)
    glVertex2f(30, 241)
    glVertex2f(33, 241)
    glVertex2f(34, 240)
    glEnd()

def badan():
    glColor3ub(0, 0, 139)
    glBegin(GL_POLYGON)
    #tangan kanan
    glVertex2f(45, 243)
    glVertex2f(44, 245)
    glVertex2f(39, 239)
    glVertex2f(40, 235)
    glVertex2f(38, 236)
    #badan
    glVertex2f(38, 226)
    glVertex2f(27, 226)
    glVertex2f(26, 237)
    #tangan kiri
    glVertex2f(25, 236)
    glVertex2f(23, 230)
    glVertex2f(26, 226)
    glVertex2f(26, 224)
    glVertex2f(19, 230)
    glVertex2f(23, 239)
    glVertex2f(29, 240)
    glVertex2f(32, 238)
    glVertex2f(34, 240)
    glEnd()
    
def logoLuar():
    glColor3ub(255, 255, 0)
    glBegin(GL_POLYGON)
    glVertex2f(32, 228)
    glVertex2f(29, 230)
    glVertex2f(27, 234)
    glVertex2f(29, 237)
    glVertex2f(35, 237)
    glVertex2f(37, 234)
    glVertex2f(35, 230)
    glEnd()
    
def logoH():
    glColor3ub(255, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(30, 231)
    glVertex2f(30, 236)
    glVertex2f(31, 235)
    glVertex2f(31, 234)
    glVertex2f(33, 234)
    glVertex2f(33, 235)
    glVertex2f(34, 236)
    glVertex2f(34, 231)
    glVertex2f(33, 232)
    glVertex2f(33, 233)
    glVertex2f(31, 233)
    glVertex2f(31, 232)
    glEnd()
    
def segitigaBawah():
    glColor3ub(255, 0, 0)
    glBegin(GL_TRIANGLES)
    glVertex2f(32, 228)
    glVertex2f(31, 230)
    glVertex2f(33, 230)
    glEnd()
    
def segitigaKiri():
    glColor3ub(255, 0, 0)
    glBegin(GL_TRIANGLES)
    glVertex2f(29, 233)
    glVertex2f(28, 234)
    glVertex2f(29, 235)
    glEnd() 

def segitigaKanan():
    glColor3ub(255, 0, 0)
    glBegin(GL_TRIANGLES)
    glVertex2f(35, 233)
    glVertex2f(36, 234)
    glVertex2f(35, 235)
    glEnd() 
    
def sabuk():
    glColor3ub(0,0,0)
    glBegin(GL_QUADS)
    glVertex2f(27, 223)
    glVertex2f(27, 226)
    glVertex2f(38, 226)
    glVertex2f(38, 223)
    glEnd()
    
def kaki():
    glColor3ub(0, 0, 139)
    glBegin(GL_POLYGON)
    #kaki kanan
    glVertex2f(38, 223)
    glVertex2f(40, 216)
    glVertex2f(36, 207)
    glVertex2f(32, 209)
    glVertex2f(35, 215)
    glVertex2f(33, 219)
    #kaki kiri
    glVertex2f(32, 215)
    glVertex2f(29, 209)
    glVertex2f(24, 210)
    glVertex2f(28, 217)
    glVertex2f(27, 223)
    glEnd()
    
def sepatuKiri():
    glColor3ub(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(30, 207)
    glVertex2f(23, 208)
    glVertex2f(24, 210)
    glVertex2f(29, 209)
    glVertex2f(29, 208)
    glEnd()
    
def sepatuKanan():
    glColor3ub(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(35, 205)
    glVertex2f(30, 208)
    glVertex2f(32, 209)
    glVertex2f(36, 207)
    glVertex2f(35, 206)
    glEnd()
 
def sayap():
    glColor3ub(255, 250, 250)
    glBegin(GL_POLYGON)
    glVertex2f(27, 223)
    glVertex2f(25, 220)
    glVertex2f(13, 222)
    glVertex2f(17, 237)
    glVertex2f(21, 242)
    glVertex2f(23, 241)
    glVertex2f(25, 242)
    glVertex2f(29, 240)
    glEnd()
    

    
def heroGabungan():
    glPushMatrix()
    glScalef(2, 2, 0)
    glTranslated(0, -100, 0) 
    rambut()
    wajah()
    bibir()
    lidah()
    gigi()
    hidung()
    bingkaiKiri()
    kacaKiri()
    mataKiri()
    bingkaiTengah()
    kacaKanan()
    bingkaiKanan()
    mataKanan()
    leher()
    badan()
    logoLuar()
    logoH()
    segitigaBawah()
    segitigaKiri()
    segitigaKanan()
    sabuk()
    kaki()
    sepatuKiri()
    sepatuKanan()
    sayap()
    glPopMatrix()
    
