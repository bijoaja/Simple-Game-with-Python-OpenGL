from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


x_time = 0
angle_time =0

x = 0


# def garis():
#     glColor3ub(0, 204, 0)
#     glBegin(GL_LINES)
#     glVertex2f(199.6, 83.7)
#     glVertex2f(250.2, 83.3)
#     glVertex2f(199.9, 74.2)
#     glVertex2f(250.2, 73.4)
#     glVertex2f(349.7, 100.6)
#     glVertex2f(400, 100)
#     glVertex2f(349.3, 113.7)
#     glVertex2f(400.2, 113.7)
#     glVertex2f(499.5, 179.6)
#     glVertex2f(549.7, 180.1)
#     glVertex2f(500, 200)
#     glVertex2f(550, 200)
#     glVertex2f(650, 150)
#     glVertex2f(700, 150)
#     glVertex2f(650, 170)
#     glVertex2f(700, 170)
#     glVertex2f(650, 650)
#     glVertex2f(700, 650)
#     glVertex2f(650, 632)
#     glVertex2f(700, 632)
#     glVertex2f(800, 150)
#     glVertex2f(850, 150)
#     glVertex2f(800, 180)
#     glVertex2f(850, 180)
#     glVertex2f(800, 628)
#     glVertex2f(850, 628)
#     glVertex2f(800, 608.5)
#     glVertex2f(850, 608.4)
#     glVertex2f(950, 250)
#     glVertex2f(1000, 250)
#     glVertex2f(950, 270)
#     glVertex2f(1000, 270)
#     glVertex2f(1100, 300)
#     glVertex2f(1150, 300)
#     glVertex2f(1100, 330)
#     glVertex2f(1150, 330)
#     glVertex2f(1250, 650)
#     glVertex2f(1300, 650)
#     glVertex2f(1250, 620)
#     glVertex2f(1300, 620)
#     glVertex2f(1400, 200)
#     glVertex2f(1450, 200)
#     glVertex2f(1400, 200)
#     glVertex2f(1450, 220)
#     glVertex2f(1400, 550)
#     glVertex2f(1450, 550)
#     glVertex2f(1400, 520)
#     glVertex2f(1450, 520)
#     glEnd()

def pipa1():
    global x
    x -= 0.2
    if x < -600 :
        x = 0
    glTranslated(x,0,0)
    glColor3ub(0, 204, 0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(200, 0)
    glVertex2f(250, 0)
    glVertex2f(250.2, 73.4)
    glVertex2f(250.2, 83.3)
    glVertex2f(226.3, 103.9)
    glVertex2f(199.6, 83.7)
    glVertex2f(199.9, 74.2)
    glVertex2f(200, 0)
    glEnd()

def pipa2():
    glColor3ub(0, 204, 0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(350, 0)
    glVertex2f(400, 0)
    glVertex2f(400,100)
    glVertex2f(400.2, 113.7)
    glVertex2f(376.4, 133)
    glVertex2f(349.3, 113.7)
    glVertex2f(349.7, 100.6)
    glVertex2f(350, 0)
    glEnd()

def pipa3():
    glColor3ub(0, 204, 0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(500, 0)
    glVertex2f(550, 0)
    glVertex2f(549.7, 180.1)
    glVertex2f(550, 200)
    glVertex2f(527, 223.2)
    glVertex2f(500, 200)
    glVertex2f(499.5, 179.6)
    glVertex2f(500, 0)
    glEnd()

def pipa4():
    glColor3ub(0, 204, 0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(500, 700)
    glVertex2f(550, 700)
    glVertex2f(526.2, 674.9)
    glEnd()

def pipa5():
    glColor3ub(0, 204, 0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(650, 0)
    glVertex2f(700, 0)
    glVertex2f(700, 150)
    glVertex2f(700, 170)
    glVertex2f(676, 190)
    glVertex2f(650, 170)
    glVertex2f(650, 150)
    glVertex2f(650, 0)
    glEnd()

def pipa6():
    glColor3ub(0, 204, 0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(650, 700)
    glVertex2f(700, 700)
    glVertex2f(700, 650)
    glVertex2f(700, 632)
    glVertex2f(674.2, 607.9)
    glVertex2f(650, 632)
    glVertex2f(650, 650)
    glVertex2f(650, 700)
    glEnd()

def pipa7():
    glColor3ub(0, 204, 0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(800, 0)
    glVertex2f(850, 0)
    glVertex2f(850, 150)
    glVertex2f(850, 180)
    glVertex2f(825, 200)
    glVertex2f(800, 180)
    glVertex2f(800, 150)
    glVertex2f(800, 0)
    glEnd()

def pipa8():
    glColor3ub(0, 204, 0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(800, 700)
    glVertex2f(850, 700)
    glVertex2f(850, 628)
    glVertex2f(850, 608.5)
    glVertex2f(824, 580)
    glVertex2f(800, 608.5)
    glVertex2f(800, 628)
    glVertex2f(800, 700)
    glEnd()

def pipa9():
    glColor3ub(0, 204, 0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(950, 0)
    glVertex2f(1000, 0)
    glVertex2f(1000, 250)
    glVertex2f(1000, 270)
    glVertex2f(975, 290)
    glVertex2f(950, 270)
    glVertex2f(950, 250)
    glVertex2f(950, 0)
    glEnd()

def pipa10():
    glColor3ub(0, 204, 0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(950, 700)
    glVertex2f(1000, 700)
    glVertex2f(975, 665)
    glEnd()

def pipa11():
    glColor3ub(0, 204, 0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(1100, 0)
    glVertex2f(1150, 0)
    glVertex2f(1150, 300)
    glVertex2f(1150, 330)
    glVertex2f(1125, 360)
    glVertex2f(1100, 330)
    glVertex2f(1100, 300)
    glVertex2f(1100, 0)
    glEnd()

def pipa12():
    glColor3ub(0, 204, 0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(1100, 700)
    glVertex2f(1150, 700)
    glVertex2f(1125, 650)
    glEnd()

def pipa13():
    glColor3ub(0, 204, 0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(1250, 0)
    glVertex2f(1300, 0)
    glVertex2f(1300, 100)
    glVertex2f(1275, 150)
    glVertex2f(1250, 100)
    glVertex2f(1250, 0)
    glEnd()

def pipa14():
    glColor3ub(0, 204, 0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(1250, 700)
    glVertex2f(1300, 700)
    glVertex2f(1300, 650)
    glVertex2f(1300, 620)
    glVertex2f(1275, 590)
    glVertex2f(1250, 620)
    glVertex2f(1250, 650)
    glVertex2f(1250, 700)
    glEnd()

def pipa15():
    glColor3ub(0, 204, 0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(1400, 0)
    glVertex2f(1450, 0)
    glVertex2f(1450, 200)
    glVertex2f(1450, 220)
    glVertex2f(1425, 245)
    glVertex2f(1400, 220)
    glVertex2f(1400, 200)
    glVertex2f(1400, 0)
    glEnd()

def pipa16():
    glColor3ub(0, 204, 0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(1400, 700)
    glVertex2f(1450, 700)
    glVertex2f(1450, 550)
    glVertex2f(1450, 520)
    glVertex2f(1426, 480)
    glVertex2f(1400, 520)
    glVertex2f(1400, 550)
    glVertex2f(1400, 700)
    glEnd()

def balon1() :
    glColor3ub(0, 0, 0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(43.4, 44.4)
    glVertex2f(53.2, 47.5)
    glVertex2f(61.3, 55.9)
    glVertex2f(66.3, 64.2)
    glVertex2f(69.9, 74.2)
    glVertex2f(71.8, 87.3)
    glVertex2f(71, 99.6)
    glVertex2f(65.4, 109.9)
    glVertex2f(56.9, 118.5)
    glVertex2f(43.5, 122.4)
    glVertex2f(31.6, 119.6)
    glVertex2f(22, 112.4)
    glVertex2f(15.9, 102.4)
    glVertex2f(13.7, 89.5)
    glVertex2f(15.6, 77.3)
    glVertex2f(19.8, 65.6)
    glVertex2f(26, 55)
    glVertex2f(33.3, 48)
    glEnd()

def warnaBalon1() :
    glBegin(GL_POLYGON) #utk membuat objek yang titik koordinatnya banyak
    glColor3ub(139, 5, 0)
    glVertex2f(43.4, 44.4)
    glVertex2f(53.2, 47.5)
    glVertex2f(61.3, 55.9)
    glVertex2f(66.3, 64.2)
    glVertex2f(69.9, 74.2)
    glVertex2f(71.8, 87.3)
    glVertex2f(71, 99.6)
    glVertex2f(65.4, 109.9)
    glVertex2f(56.9, 118.5)
    glVertex2f(43.5, 122.4)
    glVertex2f(31.6, 119.6)
    glVertex2f(22, 112.4)
    glVertex2f(15.9, 102.4)
    glVertex2f(13.7, 89.5)
    glVertex2f(15.6, 77.3)
    glVertex2f(19.8, 65.6)
    glVertex2f(26, 55)
    glVertex2f(33.3, 48)
    glEnd()

def balon2():
    glColor3ub(0,0,0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(40.3, 38.4)
    glVertex2f(46.8, 38.3)
    glVertex2f(43.4, 44.4)
    glEnd()

def warnaBalon2():
    glBegin(GL_POLYGON) #utk membuat objek yang titik koordinatnya banyak
    glColor3ub(139, 5, 0)
    glVertex2f(40.3, 38.4)
    glVertex2f(46.8, 38.3)
    glVertex2f(43.4, 44.4)
    glEnd()

def hiasanBalon():
    glBegin(GL_LINE_LOOP) #utk membuat objek yang titik koordinatnya banyak
    glColor3ub(0,0,0)
    glVertex2f(26.4, 92.5)
    glVertex2f(28.2, 93.7)
    glVertex2f(29.4, 95.5)
    glVertex2f(30.5, 97.9)
    glVertex2f(31.3, 100.2)
    glVertex2f(32, 102.5)
    glVertex2f(32.3, 104.8)
    glVertex2f(31.8, 106.6)
    glVertex2f(30.1, 105.7)
    glVertex2f(28.9, 104.2)
    glVertex2f(27.7, 101.8)
    glVertex2f(26.6, 99.1)
    glVertex2f(26, 96.5)
    glVertex2f(25.8, 94.4)
    glEnd()

def hiasanBalon2():
    glColor3ub(0,0,0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(25.5, 87.5)
    glVertex2f(25.6, 83.8)
    glVertex2f(26.5, 80.6)
    glEnd()

def taliBalon():
    glColor3ub(0,0,0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(43.4, 44.4)
    glVertex2f(49.4, 43.1)
    glVertex2f(55.4, 41.1)
    glVertex2f(60.4, 37.5)
    glVertex2f(63.4, 32.4)
    glVertex2f(65.5, 27)
    glVertex2f(66.3, 19.9)
    glVertex2f(67.9, 14.6)
    glVertex2f(70.7, 9.6)
    glVertex2f(74.6, 5.5)
    glVertex2f(79.9, 3.8)
    glVertex2f(81.6, 4.1)
    glVertex2f(80.9, 2.4)
    glEnd()

def balon_utama():
    glPushMatrix()
    balon1()
    warnaBalon1()
    warnaBalon2()
    balon2()
    hiasanBalon()
    hiasanBalon2()
    taliBalon()
    glPopMatrix()

def pipa_bawah():
    pipa1()
    pipa2()
    pipa3()
    pipa5()
    pipa7()
    pipa9()
    pipa11()
    pipa13()
    pipa15()
    
def pipa_atas():
    pipa4()
    pipa6()
    pipa8()
    pipa10()
    pipa12()
    pipa14()
    pipa16()

def pipa_utama():
    global x
    x -= 0.1
    if x < -500 :
        x = 0
    glTranslated(x,0,0)
    glPushMatrix()
    pipa_bawah()
    pipa_atas()
    glPopMatrix()


def timer(value):
    global angle_time
    angle_time += 20
    glutTimerFunc(100,timer,0)


def iterate():
    glViewport(0, 0, 1200, 700) #utk mengatur area pandang
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1200, 0.0, 700, 0.0, 1.0) #utk mengatur berapa blok yang digunakan (skala) nilai x, y, z
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClearColor(184.0/255.0, 213.0/255.0, 238.0/255.0, 1.0)#kalo dihilangkan hitam
    glClear(GL_COLOR_BUFFER_BIT)
    iterate()
    glLineWidth(3)
    glTranslated(5, x_time, 0) #memindahkan sebanyak 5x dan 5y atau kekanan(memindahkan objek)
    # garis()
    balon_utama()
    pipa_utama()
    glutSwapBuffers() #utk membersihkan layar, double buffering

glutInit() #inisialisasi glut
glutInitDisplayMode(GLUT_RGBA) #utk mengatur display supaya berwarna
glutInitWindowSize(1200, 700) #utk mengatur ukuran window
glutInitWindowPosition(0, 0) #utk mengatur letak window
timer(0)
wind = glutCreateWindow("flappy balon") #utk memberi nama pada window
glutDisplayFunc(showScreen) #utk fungsi callback
glutIdleFunc(showScreen) #utk fungsi callback
glutMainLoop() #fungsi yang akan memulai keseluruhan program
