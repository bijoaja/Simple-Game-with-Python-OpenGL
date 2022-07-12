from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
x = 0
a = 3

def init():
    glClearColor(255.0, 255.0, 255.0, 1.0)
    gluOrtho2D(-50.0, 50.0, -30.0, 30.0)

def background():
    global x,a
    x += a
    if x > 900:
        glRotate(180,0,1,0)
        a *= -1.2
    if x < 0:
        glRotate(180,0,1,0)
        a *= -1.2
    print(x)
    kanvas()
    jalan()
    garis_putus()
    rintangan()
    glFlush()

def kanvas():   
    glBegin(GL_POLYGON)
    glColor3ub(255, 0, 0)
    glVertex2f(-1000.0 + x,-30.0)
    glColor3ub(0, 255, 0)
    glVertex2f(-1000.0 + x, 30.0)
    glColor3ub(0, 0, 255)
    glVertex2f(50.0 + x, 30.0)
    glColor3ub(255, 0, 255)
    glVertex2f(50.0 + x , -30.0)
    glEnd()

def jalan():
    glBegin(GL_POLYGON)
    glColor3ub(0,0,0)
    glVertex2f(50.0, 20.0 )
    glVertex2f(50.0, -20.0 )
    glVertex2f(-1000.0, -20.0 )
    glVertex2f(-1000.0, 20.0 )
    glEnd()

def garis_putus():
    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(35.0+x, -10.0)
    glVertex2f(35.0+x, -5.0)
    glVertex2f(42.5+x, -5.0)
    glVertex2f(42.5+x, -10.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(20.0+x, 5.0)
    glVertex2f(20.0+x, 10.0)
    glVertex2f(35.0+x, 10.0)
    glVertex2f(35.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(5.0+x, -10.0)
    glVertex2f(5.0+x, -5.0)
    glVertex2f(20.0+x, -5.0)
    glVertex2f(20.0+x, -10.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-10.0+x, 5.0)
    glVertex2f(-10.0+x, 10.0)
    glVertex2f(5.0+x, 10.0)
    glVertex2f(5.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-25.0+x, -10.0)
    glVertex2f(-25.0+x, -5.0)
    glVertex2f(-10.0+x, -5.0)
    glVertex2f(-10.0+x, -10.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-40.0+x, 5.0)
    glVertex2f(-40.0+x, 10.0)
    glVertex2f(-25.0+x, 10.0)
    glVertex2f(-25.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-55.0+x, -10.0)
    glVertex2f(-55.0+x, -5.0)
    glVertex2f(-40.0+x, -5.0)
    glVertex2f(-40.0+x, -10.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-70.0+x, 5.0)
    glVertex2f(-70.0+x, 10.0)
    glVertex2f(-55.0+x, 10.0)
    glVertex2f(-55.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-85.0+x, -10.0)
    glVertex2f(-85.0+x, -5.0)
    glVertex2f(-70.0+x, -5.0)
    glVertex2f(-70.0+x, -10.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-100.0+x, 5.0)
    glVertex2f(-100.0+x, 10.0)
    glVertex2f(-85.0+x, 10.0)
    glVertex2f(-85.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-115.0+x, -10.0)
    glVertex2f(-115.0+x, -5.0)
    glVertex2f(-100.0+x, -5.0)
    glVertex2f(-100.0+x, -10.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-130.0+x, 5.0)
    glVertex2f(-130.0+x, 10.0)
    glVertex2f(-115.0+x, 10.0)
    glVertex2f(-115.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-145.0+x, -10.0)
    glVertex2f(-145.0+x, -5.0)
    glVertex2f(-130.0+x, -5.0)
    glVertex2f(-130.0+x, -10.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-160.0+x, 5.0)
    glVertex2f(-160.0+x, 10.0)
    glVertex2f(-145.0+x, 10.0)
    glVertex2f(-145.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-175.0+x, -10.0)
    glVertex2f(-175.0+x, -5.0)
    glVertex2f(-160.0+x, -5.0)
    glVertex2f(-160.0+x, -10.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-190.0+x, 5.0)
    glVertex2f(-190.0+x, 10.0)
    glVertex2f(-175.0+x, 10.0)
    glVertex2f(-175.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-205.0+x, -10.0)
    glVertex2f(-205.0+x, -5.0)
    glVertex2f(-190.0+x, -5.0)
    glVertex2f(-190.0+x, -10.0)
    glEnd()    

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-220.0+x, 5.0)
    glVertex2f(-220.0+x, 10.0)
    glVertex2f(-205.0+x, 10.0)
    glVertex2f(-205.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-235.0+x, -10.0)
    glVertex2f(-235.0+x, -5.0)
    glVertex2f(-220.0+x, -5.0)
    glVertex2f(-220.0+x, -10.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-250.0+x, 5.0)
    glVertex2f(-250.0+x, 10.0)
    glVertex2f(-235.0+x, 10.0)
    glVertex2f(-235.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-265.0+x, -10.0)
    glVertex2f(-265.0+x, -5.0)
    glVertex2f(-250.0+x, -5.0)
    glVertex2f(-250.0+x, -10.0)
    glEnd()    

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-280.0+x, 5.0)
    glVertex2f(-280.0+x, 10.0)
    glVertex2f(-265.0+x, 10.0)
    glVertex2f(-265.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-295.0+x, -10.0)
    glVertex2f(-295.0+x, -5.0)
    glVertex2f(-280.0+x, -5.0)
    glVertex2f(-280.0+x, -10.0)
    glEnd()    

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-310.0+x, 5.0)
    glVertex2f(-310.0+x, 10.0)
    glVertex2f(-295.0+x, 10.0)
    glVertex2f(-295.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-325.0+x, -10.0)
    glVertex2f(-325.0+x, -5.0)
    glVertex2f(-310.0+x, -5.0)
    glVertex2f(-310.0+x, -10.0)
    glEnd()    

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-340.0+x, 5.0)
    glVertex2f(-340.0+x, 10.0)
    glVertex2f(-325.0+x, 10.0)
    glVertex2f(-325.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-355.0+x, -10.0)
    glVertex2f(-355.0+x, -5.0)
    glVertex2f(-340.0+x, -5.0)
    glVertex2f(-340.0+x, -10.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-370.0+x, 5.0)
    glVertex2f(-370.0+x, 10.0)
    glVertex2f(-355.0+x, 10.0)
    glVertex2f(-355.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-385.0+x, -10.0)
    glVertex2f(-385.0+x, -5.0)
    glVertex2f(-370.0+x, -5.0)
    glVertex2f(-370.0+x, -10.0)
    glEnd()    

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-400.0+x, 5.0)
    glVertex2f(-400.0+x, 10.0)
    glVertex2f(-385.0+x, 10.0)
    glVertex2f(-385.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-415.0+x, -10.0)
    glVertex2f(-415.0+x, -5.0)
    glVertex2f(-400.0+x, -5.0)
    glVertex2f(-400.0+x, -10.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-430.0+x, 5.0)
    glVertex2f(-430.0+x, 10.0)
    glVertex2f(-415.0+x, 10.0)
    glVertex2f(-415.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-445.0+x, -10.0)
    glVertex2f(-445.0+x, -5.0)
    glVertex2f(-430.0+x, -5.0)
    glVertex2f(-430.0+x, -10.0)
    glEnd()    

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-460.0+x, 5.0)
    glVertex2f(-460.0+x, 10.0)
    glVertex2f(-445.0+x, 10.0)
    glVertex2f(-445.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-475.0+x, -10.0)
    glVertex2f(-475.0+x, -5.0)
    glVertex2f(-460.0+x, -5.0)
    glVertex2f(-460.0+x, -10.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-490.0+x, 5.0)
    glVertex2f(-490.0+x, 10.0)
    glVertex2f(-475.0+x, 10.0)
    glVertex2f(-475.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-505.0+x, -10.0)
    glVertex2f(-505.0+x, -5.0)
    glVertex2f(-490.0+x, -5.0)
    glVertex2f(-490.0+x, -10.0)
    glEnd()    

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-520.0+x, 5.0)
    glVertex2f(-520.0+x, 10.0)
    glVertex2f(-505.0+x, 10.0)
    glVertex2f(-505.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-535.0+x, -10.0)
    glVertex2f(-535.0+x, -5.0)
    glVertex2f(-520.0+x, -5.0)
    glVertex2f(-520.0+x, -10.0)
    glEnd()     

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-550.0+x, 5.0)
    glVertex2f(-550.0+x, 10.0)
    glVertex2f(-535.0+x, 10.0)
    glVertex2f(-535.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-565.0+x, -10.0)
    glVertex2f(-565.0+x, -5.0)
    glVertex2f(-550.0+x, -5.0)
    glVertex2f(-550.0+x, -10.0)
    glEnd()    

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-580.0+x, 5.0)
    glVertex2f(-580.0+x, 10.0)
    glVertex2f(-565.0+x, 10.0)
    glVertex2f(-565.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-595.0+x, -10.0)
    glVertex2f(-595.0+x, -5.0)
    glVertex2f(-580.0+x, -5.0)
    glVertex2f(-580.0+x, -10.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-610.0+x, 5.0)
    glVertex2f(-610.0+x, 10.0)
    glVertex2f(-595.0+x, 10.0)
    glVertex2f(-595.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-625.0+x, -10.0)
    glVertex2f(-625.0+x, -5.0)
    glVertex2f(-610.0+x, -5.0)
    glVertex2f(-610.0+x, -10.0)
    glEnd()    

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-640.0+x, 5.0)
    glVertex2f(-640.0+x, 10.0)
    glVertex2f(-625.0+x, 10.0)
    glVertex2f(-625.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-655.0+x, -10.0)
    glVertex2f(-655.0+x, -5.0)
    glVertex2f(-640.0+x, -5.0)
    glVertex2f(-640.0+x, -10.0)
    glEnd()  

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-670.0+x, 5.0)
    glVertex2f(-670.0+x, 10.0)
    glVertex2f(-655.0+x, 10.0)
    glVertex2f(-655.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-685.0+x, -10.0)
    glVertex2f(-685.0+x, -5.0)
    glVertex2f(-670.0+x, -5.0)
    glVertex2f(-670.0+x, -10.0)
    glEnd()    

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-700.0+x, 5.0)
    glVertex2f(-700.0+x, 10.0)
    glVertex2f(-685.0+x, 10.0)
    glVertex2f(-685.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-715.0+x, -10.0)
    glVertex2f(-715.0+x, -5.0)
    glVertex2f(-700.0+x, -5.0)
    glVertex2f(-700.0+x, -10.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-730.0+x, 5.0)
    glVertex2f(-730.0+x, 10.0)
    glVertex2f(-715.0+x, 10.0)
    glVertex2f(-715.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-745.0+x, -10.0)
    glVertex2f(-745.0+x, -5.0)
    glVertex2f(-730.0+x, -5.0)
    glVertex2f(-730.0+x, -10.0)
    glEnd()    

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-760.0+x, 5.0)
    glVertex2f(-760.0+x, 10.0)
    glVertex2f(-745.0+x, 10.0)
    glVertex2f(-745.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-775.0+x, -10.0)
    glVertex2f(-775.0+x, -5.0)
    glVertex2f(-760.0+x, -5.0)
    glVertex2f(-760.0+x, -10.0)
    glEnd()  

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-790.0+x, 5.0)
    glVertex2f(-790.0+x, 10.0)
    glVertex2f(-775.0+x, 10.0)
    glVertex2f(-775.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-805.0+x, -10.0)
    glVertex2f(-805.0+x, -5.0)
    glVertex2f(-790.0+x, -5.0)
    glVertex2f(-790.0+x, -10.0)
    glEnd()    

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-820.0+x, 5.0)
    glVertex2f(-820.0+x, 10.0)
    glVertex2f(-805.0+x, 10.0)
    glVertex2f(-805.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-835.0+x, -10.0)
    glVertex2f(-835.0+x, -5.0)
    glVertex2f(-820.0+x, -5.0)
    glVertex2f(-820.0+x, -10.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-850.0+x, 5.0)
    glVertex2f(-850.0+x, 10.0)
    glVertex2f(-835.0+x, 10.0)
    glVertex2f(-835.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-865.0+x, -10.0)
    glVertex2f(-865.0+x, -5.0)
    glVertex2f(-850.0+x, -5.0)
    glVertex2f(-850.0+x, -10.0)
    glEnd()    

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-880.0+x, 5.0)
    glVertex2f(-880.0+x, 10.0)
    glVertex2f(-865.0+x, 10.0)
    glVertex2f(-865.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-895.0+x, -10.0)
    glVertex2f(-895.0+x, -5.0)
    glVertex2f(-880.0+x, -5.0)
    glVertex2f(-880.0+x, -10.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-910.0+x, 5.0)
    glVertex2f(-910.0+x, 10.0)
    glVertex2f(-895.0+x, 10.0)
    glVertex2f(-895.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-925.0+x, -10.0)
    glVertex2f(-925.0+x, -5.0)
    glVertex2f(-910.0+x, -5.0)
    glVertex2f(-910.0+x, -10.0)
    glEnd()    

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-940.0+x, 5.0)
    glVertex2f(-940.0+x, 10.0)
    glVertex2f(-925.0+x, 10.0)
    glVertex2f(-925.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-955.0+x, -10.0)
    glVertex2f(-955.0+x, -5.0)
    glVertex2f(-940.0+x, -5.0)
    glVertex2f(-940.0+x, -10.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-970.0+x, 5.0)
    glVertex2f(-970.0+x, 10.0)
    glVertex2f(-955.0+x, 10.0)
    glVertex2f(-955.0+x, 5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-985.0+x, -10.0)
    glVertex2f(-985.0+x, -5.0)
    glVertex2f(-970.0+x, -5.0)
    glVertex2f(-970.0+x, -10.0)
    glEnd()    

    glBegin(GL_POLYGON)
    glColor3ub(255,255,255)
    glVertex2f(-1000.0+x, 5.0)
    glVertex2f(-9100.0+x, 10.0)
    glVertex2f(-985.0+x, 10.0)
    glVertex2f(-985.0+x, 5.0)
    glEnd()
    glFlush()

# logika rintangan
def rintangan():
    global x
    x_r = -35
    glPushMatrix()
    glTranslate(x,0,0)
    rintangan1(x_r)
    rintangan2(x_r-15)
    rintangan3(x_r-30)
    rintangan4(x_r-45)
    rintangan5(x_r-60)
    rintangan6(x_r-75)
    rintangan7(x_r-90)
    rintangan8(x_r-155)
    rintangan9(x_r-195)
    rintangan10(x_r-305)
    rintangan11(x_r-320)
    rintangan12(x_r-335)
    rintangan13(x_r-350)
    rintangan14(x_r-365)
    rintangan15(x_r-380)
    rintangan16(x_r-395)
    rintangan17(x_r-410)
    rintangan18(x_r-475)
    rintangan19(x_r-515)
    rintangan20(x_r-625)
    rintangan21(x_r-640)
    rintangan22(x_r-655)
    rintangan23(x_r-670)
    rintangan24(x_r-685)
    rintangan25(x_r-700)
    rintangan26(x_r-715)
    rintangan27(x_r-730)
    rintangan28(x_r-795)
    rintangan29(x_r-835)
    rintangan30(x_r-945)
    glPopMatrix()

def rintangan1(x_r):
    glBegin(GL_POLYGON)
    glColor3ub(170,169,173)
    glVertex2f(x_r, -10)
    glVertex2f(x_r+1, -8)
    glVertex2f(x_r+2, -9)
    glVertex2f(x_r+3, -6)
    glVertex2f(x_r+3, -9)
    glVertex2f(x_r+4, -8)
    glVertex2f(x_r+5, -10)
    glVertex2f(x_r, -10)
    glEnd()

def rintangan2(x_r):
    glBegin(GL_POLYGON)
    glColor3ub(170,169,173)
    glVertex2f(x_r, 5)
    glVertex2f(x_r+1, 7)
    glVertex2f(x_r+2, -6)
    glVertex2f(x_r+3, -9)
    glVertex2f(x_r+3, 6)
    glVertex2f(x_r+4, 7)
    glVertex2f(x_r+5, 5)
    glVertex2f(x_r, 5)
    glEnd()

def rintangan3(x_r):
    glBegin(GL_POLYGON)
    glColor3ub(170,169,173)
    glVertex2f(x_r, -10)
    glVertex2f(x_r+1, -8)
    glVertex2f(x_r+2, -9)
    glVertex2f(x_r+3, -6)
    glVertex2f(x_r+3, -9)
    glVertex2f(x_r+4, -8)
    glVertex2f(x_r+5, -10)
    glVertex2f(x_r, -10)
    glEnd()

def rintangan4(x_r):
    glBegin(GL_POLYGON)
    glColor3ub(170,169,173)
    glVertex2f(x_r, 5)
    glVertex2f(x_r+1, 7)
    glVertex2f(x_r+2, 6)
    glVertex2f(x_r+3, 9)
    glVertex2f(x_r+4, 6)
    glVertex2f(x_r+4, 7)
    glVertex2f(x_r+5, 5)
    glVertex2f(x_r, 5)
    glEnd()

def rintangan5(x_r):
    glBegin(GL_POLYGON)
    glColor3ub(170,169,173)
    glVertex2f(x_r, -10)
    glVertex2f(x_r+1, -8)
    glVertex2f(x_r+2, -9)
    glVertex2f(x_r+3, -6)
    glVertex2f(x_r+3, -9)
    glVertex2f(x_r+4, -8)
    glVertex2f(x_r+5, -10)
    glVertex2f(x_r, -10)
    glEnd()

def rintangan6(x_r):
    glBegin(GL_POLYGON)
    glColor3ub(170,169,173)
    glVertex2f(x_r, 5)
    glVertex2f(x_r+1, 7)
    glVertex2f(x_r+2, 6)
    glVertex2f(x_r+3, 9)
    glVertex2f(x_r+3, 6)
    glVertex2f(x_r+4, 7)
    glVertex2f(x_r+5, 5)
    glVertex2f(x_r, 5)
    glEnd()

def rintangan7(x_r):
    glBegin(GL_POLYGON)
    glColor3ub(170,169,173)
    glVertex2f(x_r, -10)
    glVertex2f(x_r+1, -8)
    glVertex2f(x_r+2, -9)
    glVertex2f(x_r+3, -6)
    glVertex2f(x_r+3, -9)
    glVertex2f(x_r+4, -9)
    glVertex2f(x_r+5, -10)
    glVertex2f(x_r, -10)
    glEnd()

def rintangan8(x_r):
    glBegin(GL_POLYGON)
    glColor3ub(170,169,173)
    glVertex2f(x_r, -10)
    glVertex2f(x_r+2, -4)
    glVertex2f(x_r+4, -8)
    glVertex2f(x_r+6, 0)
    glVertex2f(x_r+8, -8)
    glVertex2f(x_r+10, -4)
    glVertex2f(x_r+12, -10)
    glVertex2f(x_r, -10)
    glEnd()

def rintangan9(x_r):
    glBegin(GL_POLYGON)
    glColor3ub(170,169,173)
    glVertex2f(x_r, 0)
    glVertex2f(x_r+5, 10)
    glVertex2f(x_r+10, 5)
    glVertex2f(x_r+12, 16)
    glVertex2f(x_r+14, 5)
    glVertex2f(x_r+19, 10)
    glVertex2f(x_r+25, 0)
    glVertex2f(x_r, 0)
    glEnd()

def rintangan10(x_r):
    glBegin(GL_POLYGON)
    glColor3ub(170,169,173)
    glVertex2f(x_r, -10)
    glVertex2f(x_r+10, 10)
    glVertex2f(x_r+20, 0)
    glVertex2f(x_r+30, 10)
    glVertex2f(x_r+40, -10)
    glVertex2f(x_r, -10)
    glEnd()

def rintangan11(x_r):
    glBegin(GL_POLYGON)
    glColor3ub(170,169,173)
    glVertex2f(x_r, 5)
    glVertex2f(x_r+1, 7)
    glVertex2f(x_r+2, 6)
    glVertex2f(x_r+3, 9)
    glVertex2f(x_r+4, 6)
    glVertex2f(x_r+4, 7)
    glVertex2f(x_r+5, 5)
    glVertex2f(x_r, 5)
    glEnd()

def rintangan12(x_r):
    glBegin(GL_POLYGON)
    glColor3ub(170,169,173)
    glVertex2f(x_r, -10)
    glVertex2f(x_r+1, -8)
    glVertex2f(x_r+2, -9)
    glVertex2f(x_r+3, -6)
    glVertex2f(x_r+3, -9)
    glVertex2f(x_r+4, -8)
    glVertex2f(x_r+5, -10)
    glVertex2f(x_r, -10)
    glEnd()

def rintangan13(x_r):
    glBegin(GL_POLYGON)
    glColor3ub(170,169,173)
    glVertex2f(x_r, -10)
    glVertex2f(x_r+2, -4)
    glVertex2f(x_r+4, -8)
    glVertex2f(x_r+6, 0)
    glVertex2f(x_r+8, -8)
    glVertex2f(x_r+10, -4)
    glVertex2f(x_r+12, -10)
    glVertex2f(x_r, -10)
    glEnd()

def rintangan14(x_r):
    glBegin(GL_POLYGON)
    glColor3ub(170,169,173)
    glVertex2f(x_r, 0)
    glVertex2f(x_r+5, 10)
    glVertex2f(x_r+10, 5)
    glVertex2f(x_r+12, 16)
    glVertex2f(x_r+14, 5)
    glVertex2f(x_r+19, 10)
    glVertex2f(x_r+25, 0)
    glVertex2f(x_r, 0)
    glEnd()

def rintangan15(x_r):
    glBegin(GL_POLYGON)
    glColor3ub(170,169,173)
    glVertex2f(x_r, 5)
    glVertex2f(x_r+1, 7)
    glVertex2f(x_r+2, 6)
    glVertex2f(x_r+3, 9)
    glVertex2f(x_r+3, 6)
    glVertex2f(x_r+4, 7)
    glVertex2f(x_r+5, 5)
    glVertex2f(x_r, 5)
    glEnd()

def rintangan16(x_r):
    glBegin(GL_POLYGON)
    glColor3ub(170,169,173)
    glVertex2f(x_r, -10)
    glVertex2f(x_r+1, -8)
    glVertex2f(x_r+2, -9)
    glVertex2f(x_r+3, -6)
    glVertex2f(x_r+3, -9)
    glVertex2f(x_r+4, -9)
    glVertex2f(x_r+5, -10)
    glVertex2f(x_r, -10)
    glEnd()

def rintangan17(x_r):
    glBegin(GL_POLYGON)
    glColor3ub(170,169,173)
    glVertex2f(x_r, 0)
    glVertex2f(x_r+5, 10)
    glVertex2f(x_r+10, 5)
    glVertex2f(x_r+12, 16)
    glVertex2f(x_r+14, 5)
    glVertex2f(x_r+19, 10)
    glVertex2f(x_r+25, 0)
    glVertex2f(x_r, 0)
    glEnd()

def rintangan18(x_r):
    glBegin(GL_POLYGON)
    glColor3ub(170,169,173)
    glVertex2f(x_r, -10)
    glVertex2f(x_r+10, 10)
    glVertex2f(x_r+20, 0)
    glVertex2f(x_r+30, 10)
    glVertex2f(x_r+40, -10)
    glVertex2f(x_r, -10)
    glEnd()

def rintangan19(x_r):
    glBegin(GL_POLYGON)
    glColor3ub(170,169,173)
    glVertex2f(x_r, -10)
    glVertex2f(x_r+1, -8)
    glVertex2f(x_r+2, -9)
    glVertex2f(x_r+3, -6)
    glVertex2f(x_r+3, -9)
    glVertex2f(x_r+4, -8)
    glVertex2f(x_r+5, -10)
    glVertex2f(x_r, -10)
    glEnd()

def rintangan20(x_r):
    glBegin(GL_POLYGON)
    glColor3ub(170,169,173)
    glVertex2f(x_r, 5)
    glVertex2f(x_r+1, 7)
    glVertex2f(x_r+2, -6)
    glVertex2f(x_r+3, -9)
    glVertex2f(x_r+3, 6)
    glVertex2f(x_r+4, 7)
    glVertex2f(x_r+5, 5)
    glVertex2f(x_r, 5)
    glEnd()

def rintangan21(x_r):
    glBegin(GL_POLYGON)
    glColor3ub(170,169,173)
    glVertex2f(x_r, 0)
    glVertex2f(x_r+5, 10)
    glVertex2f(x_r+10, 5)
    glVertex2f(x_r+12, 16)
    glVertex2f(x_r+14, 5)
    glVertex2f(x_r+19, 10)
    glVertex2f(x_r+25, 0)
    glVertex2f(x_r, 0)
    glEnd()

def rintangan22(x_r):
    glBegin(GL_POLYGON)
    glColor3ub(170,169,173)
    glVertex2f(x_r, -10)
    glVertex2f(x_r+10, 10)
    glVertex2f(x_r+20, 0)
    glVertex2f(x_r+30, 10)
    glVertex2f(x_r+40, -10)
    glVertex2f(x_r, -10)
    glEnd()

def rintangan23(x_r):
    glBegin(GL_POLYGON)
    glColor3ub(170,169,173)
    glVertex2f(x_r, 5)
    glVertex2f(x_r+1, 7)
    glVertex2f(x_r+2, 6)
    glVertex2f(x_r+3, 9)
    glVertex2f(x_r+4, 6)
    glVertex2f(x_r+4, 7)
    glVertex2f(x_r+5, 5)
    glVertex2f(x_r, 5)
    glEnd()

def rintangan24(x_r):
    glBegin(GL_POLYGON)
    glColor3ub(170,169,173)
    glVertex2f(x_r, -10)
    glVertex2f(x_r+1, -8)
    glVertex2f(x_r+2, -9)
    glVertex2f(x_r+3, -6)
    glVertex2f(x_r+3, -9)
    glVertex2f(x_r+4, -8)
    glVertex2f(x_r+5, -10)
    glVertex2f(x_r, -10)
    glEnd()

def rintangan25(x_r):
    glBegin(GL_POLYGON)
    glColor3ub(170,169,173)
    glVertex2f(x_r, -10)
    glVertex2f(x_r+2, -4)
    glVertex2f(x_r+4, -8)
    glVertex2f(x_r+6, 0)
    glVertex2f(x_r+8, -8)
    glVertex2f(x_r+10, -4)
    glVertex2f(x_r+12, -10)
    glVertex2f(x_r, -10)
    glEnd()

def rintangan26(x_r):
    glBegin(GL_POLYGON)
    glColor3ub(170,169,173)
    glVertex2f(x_r, 0)
    glVertex2f(x_r+5, 10)
    glVertex2f(x_r+10, 5)
    glVertex2f(x_r+12, 16)
    glVertex2f(x_r+14, 5)
    glVertex2f(x_r+19, 10)
    glVertex2f(x_r+25, 0)
    glVertex2f(x_r, 0)
    glEnd()

def rintangan27(x_r):
    glBegin(GL_POLYGON)
    glColor3ub(170,169,173)
    glVertex2f(x_r, 5)
    glVertex2f(x_r+1, 7)
    glVertex2f(x_r+2, 6)
    glVertex2f(x_r+3, 9)
    glVertex2f(x_r+3, 6)
    glVertex2f(x_r+4, 7)
    glVertex2f(x_r+5, 5)
    glVertex2f(x_r, 5)
    glEnd()

def rintangan28(x_r):
    glBegin(GL_POLYGON)
    glColor3ub(170,169,173)
    glVertex2f(x_r, 5)
    glVertex2f(x_r+1, 7)
    glVertex2f(x_r+2, 6)
    glVertex2f(x_r+3, 9)
    glVertex2f(x_r+3, 6)
    glVertex2f(x_r+4, 7)
    glVertex2f(x_r+5, 5)
    glVertex2f(x_r, 5)
    glEnd()

def rintangan29(x_r):
    glBegin(GL_POLYGON)
    glColor3ub(170,169,173)
    glVertex2f(x_r, -10)
    glVertex2f(x_r+1, -8)
    glVertex2f(x_r+2, -9)
    glVertex2f(x_r+3, -6)
    glVertex2f(x_r+3, -9)
    glVertex2f(x_r+4, -9)
    glVertex2f(x_r+5, -10)
    glVertex2f(x_r, -10)
    glEnd()

def rintangan30(x_r):
    glBegin(GL_POLYGON)
    glColor3ub(170,169,173)
    glVertex2f(x_r, -10)
    glVertex2f(x_r+2, -4)
    glVertex2f(x_r+4, -8)
    glVertex2f(x_r+6, 0)
    glVertex2f(x_r+8, -8)
    glVertex2f(x_r+10, -4)
    glVertex2f(x_r+12, -10)
    glVertex2f(x_r, -10)
    glEnd()

# def timer(value):
    
#     glutTimerFunc(1000,timer,0)
    

def update(value):
    global x 
    glutPostRedisplay()
    glutTimerFunc(100,update,0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(1000,600)
    glutInitWindowPosition(100,100)
    glutCreateWindow("bekgron")
    glutDisplayFunc(background)
    

    # timer(0)
    glutTimerFunc(50, update, 0)
    init()
    glutMainLoop()

main()