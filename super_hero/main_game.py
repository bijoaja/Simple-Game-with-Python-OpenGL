import OpenGL.GLUT as glut
from OpenGL import GL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
from heroo import *
from cobakuman import*

w,h= 800,800
x_jalan = 100
speed_jalan = 20
x_kuman = 0
speed_kuman = 40
y_hero = 0


def init():
    glClearColor(0.0,0.0,1.0,0.0)
    gluOrtho2D(-800.0, 800.0, -800.0, 800.0)

def drawText(ch,xpos,ypos):
    glPushMatrix()
    color = (0, 0, 0) # warna
    font_style = glut.GLUT_BITMAP_HELVETICA_18
    glColor3ub(color[0],color[1],color[2])
    line=0
    glRasterPos2f (xpos, ypos)
    for i in ch:
       if  i=='\n':
          line=line+1
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))  
    glPopMatrix()  

def bg_text():
    glColor3ub(255, 0, 0)     
    glBegin(GL_QUADS)
    glVertex2f(295,200)
    glVertex2f(445,200)
    glVertex2f(445,260)
    glVertex2f(295,260)
    glEnd()

#kota
def gedungsatu():
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)
    glVertex2f(70, 460)
    glVertex2f(70, 385)
    glVertex2f(108, 385)
    glVertex2f(152, 410)
    glVertex2f(170, 425)
    glVertex2f(170, 490)
    glEnd()

def gedungsatu_dua():
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)
    glVertex2f(108, 385)
    glVertex2f(108, 352)
    glVertex2f(130, 350)
    glVertex2f(152, 352)
    glVertex2f(152, 410)
    glEnd()

def gedungdua():
    glColor3ub(255, 225, 0)
    glBegin(GL_POLYGON)
    glVertex2f(25, 385)
    glVertex2f(25, 355)
    glVertex2f(75, 355)
    glVertex2f(108, 352)
    glVertex2f(108, 385)
    glEnd()

def gedungduapersegi1():
    glColor3ub(255, 183, 0)
    glBegin(GL_QUADS)
    glVertex2f(35, 375)
    glVertex2f(35, 370)
    glVertex2f(40, 370)
    glVertex2f(40, 375)
    glEnd()

def gedungduapersegi2():
    glColor3ub(255, 183, 0)
    glBegin(GL_QUADS)
    glVertex2f(50, 375)
    glVertex2f(50, 370)
    glVertex2f(55, 370)
    glVertex2f(55, 375)
    glEnd()

def gedungduapersegi3():
    glColor3ub(255, 183, 0)
    glBegin(GL_QUADS)
    glVertex2f(65, 375)
    glVertex2f(65, 370)
    glVertex2f(70, 370)
    glVertex2f(70, 375)
    glEnd()

def gedungduapersegi4():
    glColor3ub(255, 183, 0)
    glBegin(GL_QUADS)
    glVertex2f(80, 375)
    glVertex2f(80, 370)
    glVertex2f(85, 370)
    glVertex2f(85, 375)
    glEnd()

def gedungduapersegi5():
    glColor3ub(255, 183, 0)
    glBegin(GL_QUADS)
    glVertex2f(95, 375)
    glVertex2f(95, 370)
    glVertex2f(100, 370)
    glVertex2f(100, 375)
    glEnd()

def gedungduapersegi6():
    glColor3ub(255, 183, 0)
    glBegin(GL_QUADS)
    glVertex2f(35, 360)
    glVertex2f(35, 355)
    glVertex2f(40, 355)
    glVertex2f(40, 360)
    glEnd()

def gedungduapersegi7():
    glColor3ub(255, 183, 0)
    glBegin(GL_QUADS)
    glVertex2f(50, 360)
    glVertex2f(50, 355)
    glVertex2f(55, 355)
    glVertex2f(55, 360)
    glEnd()

def gedungduapersegi8():
    glColor3ub(255, 183, 0)
    glBegin(GL_QUADS)
    glVertex2f(65, 360)
    glVertex2f(65, 355)
    glVertex2f(70, 355)
    glVertex2f(70, 360)
    glEnd()

def gedungduapersegi9():
    glColor3ub(255, 183, 0)
    glBegin(GL_QUADS)
    glVertex2f(80, 360)
    glVertex2f(80, 355)
    glVertex2f(85, 355)
    glVertex2f(85, 360)
    glEnd()

def gedungduapersegi10():
    glColor3ub(255, 183, 0)
    glBegin(GL_QUADS)
    glVertex2f(95, 360)
    glVertex2f(95, 355)
    glVertex2f(100, 355)
    glVertex2f(100, 360)
    glEnd()

def gedungdua_dua():
    glColor3ub(255, 225, 0)
    glBegin(GL_POLYGON)
    glVertex2f(25, 355)
    glVertex2f(25, 260)
    glVertex2f(80, 260)
    glVertex2f(80, 350)
    glVertex2f(75, 350)
    glVertex2f(75, 355)
    glEnd()

def gedungdua_duapersegi1():
    glColor3ub(255, 183, 0)
    glBegin(GL_QUADS)
    glVertex2f(35, 345)
    glVertex2f(35, 340)
    glVertex2f(40, 340)
    glVertex2f(40, 345)
    glEnd()

def gedungdua_duapersegi2():
    glColor3ub(255, 183, 0)
    glBegin(GL_QUADS)
    glVertex2f(50, 345)
    glVertex2f(50, 340)
    glVertex2f(55, 340)
    glVertex2f(55, 345)
    glEnd()

def gedungdua_duapersegi3():
    glColor3ub(255, 183, 0)
    glBegin(GL_QUADS)
    glVertex2f(65, 345)
    glVertex2f(65, 340)
    glVertex2f(70, 340)
    glVertex2f(70, 345)
    glEnd()

def gedungdua_duapersegi4():
    glColor3ub(255, 183, 0)
    glBegin(GL_QUADS)
    glVertex2f(35, 330)
    glVertex2f(35, 325)
    glVertex2f(40, 325)
    glVertex2f(40, 330)
    glEnd()

def gedungdua_duapersegi5():
    glColor3ub(255, 183, 0)
    glBegin(GL_QUADS)
    glVertex2f(50, 330)
    glVertex2f(50, 325)
    glVertex2f(55, 325)
    glVertex2f(55, 330)
    glEnd()

def gedungdua_duapersegi6():
    glColor3ub(255, 183, 0)
    glBegin(GL_QUADS)
    glVertex2f(65, 330)
    glVertex2f(65, 325)
    glVertex2f(70, 325)
    glVertex2f(70, 330)
    glEnd()

def gedungdua_duapersegi7():
    glColor3ub(255, 183, 0)
    glBegin(GL_QUADS)
    glVertex2f(35, 315)
    glVertex2f(35, 310)
    glVertex2f(40, 315)
    glVertex2f(40, 310)
    glEnd()

def gedungdua_duapersegi8():
    glColor3ub(255, 183, 0)
    glBegin(GL_QUADS)
    glVertex2f(50, 315)
    glVertex2f(50, 310)
    glVertex2f(55, 315)
    glVertex2f(55, 310)
    glEnd()

def gedungdua_duapersegi9():
    glColor3ub(255, 183, 0)
    glBegin(GL_QUADS)
    glVertex2f(65, 315)
    glVertex2f(65, 310)
    glVertex2f(70, 315)
    glVertex2f(70, 310)
    glEnd()

def gedungdua_duapersegi10():
    glColor3ub(255, 183, 0)
    glBegin(GL_QUADS)
    glVertex2f(35, 300)
    glVertex2f(35, 295)
    glVertex2f(40, 295)
    glVertex2f(40, 300)
    glEnd()

def gedungdua_duapersegi11():
    glColor3ub(255, 183, 0)
    glBegin(GL_QUADS)
    glVertex2f(50, 300)
    glVertex2f(50, 295)
    glVertex2f(55, 295)
    glVertex2f(55, 300)
    glEnd()

def gedungdua_duapersegi12():
    glColor3ub(255, 183, 0)
    glBegin(GL_QUADS)
    glVertex2f(65, 300)
    glVertex2f(65, 295)
    glVertex2f(70, 295)
    glVertex2f(70, 300)
    glEnd()

def gedungdua_duapersegi13():
    glColor3ub(255, 183, 0)
    glBegin(GL_QUADS)
    glVertex2f(35, 285)
    glVertex2f(35, 280)
    glVertex2f(40, 280)
    glVertex2f(40, 285)
    glEnd()

def gedungdua_duapersegi14():
    glColor3ub(255, 183, 0)
    glBegin(GL_QUADS)
    glVertex2f(50, 285)
    glVertex2f(50, 280)
    glVertex2f(55, 280)
    glVertex2f(55, 285)
    glEnd()

def gedungdua_duapersegi15():
    glColor3ub(255, 183, 0)
    glBegin(GL_QUADS)
    glVertex2f(65, 285)
    glVertex2f(65, 280)
    glVertex2f(70, 280)
    glVertex2f(70, 285)
    glEnd()

def gedungdua_duapersegi16():
    glColor3ub(255, 183, 0)
    glBegin(GL_QUADS)
    glVertex2f(35, 270)
    glVertex2f(35, 265)
    glVertex2f(40, 265)
    glVertex2f(40, 270)
    glEnd()

def gedungdua_duapersegi17():
    glColor3ub(255, 183, 0)
    glBegin(GL_QUADS)
    glVertex2f(50, 270)
    glVertex2f(50, 265)
    glVertex2f(55, 265)
    glVertex2f(55, 270)
    glEnd()

def gedungdua_duapersegi18():
    glColor3ub(255, 183, 0)
    glBegin(GL_QUADS)
    glVertex2f(65, 270)
    glVertex2f(65, 265)
    glVertex2f(70, 265)
    glVertex2f(70, 270)
    glEnd()

def gedungtigaatap():
    glColor3ub(0, 81, 128)
    glBegin(GL_POLYGON)
    glVertex2f(75, 355)
    glVertex2f(75, 350)
    glVertex2f(80, 350)
    glVertex2f(130, 345)
    glVertex2f(180, 350)
    glVertex2f(185, 350)
    glVertex2f(185, 355)
    glVertex2f(130, 350)
    glEnd()

def gedungtiga1():
    glColor3ub(37, 152, 219)
    glBegin(GL_QUADS)
    glVertex2f(80, 350)
    glVertex2f(80, 260)
    glVertex2f(130, 255)
    glVertex2f(130, 345)
    glEnd()

def gedungtiga1persegipanjang1():
    glColor3ub(0, 81, 128)
    glBegin(GL_QUADS)
    glVertex2f(86, 338)
    glVertex2f(86, 336)
    glVertex2f(124, 332)
    glVertex2f(124, 334)
    glEnd()

def gedungtiga1persegipanjang2():
    glColor3ub(0, 81, 128)
    glBegin(GL_QUADS)
    glVertex2f(86, 330)
    glVertex2f(86, 328)
    glVertex2f(124, 324)
    glVertex2f(124, 326)
    glEnd()

def gedungtiga1persegipanjang3():
    glColor3ub(0, 81, 128)
    glBegin(GL_QUADS)
    glVertex2f(86, 322)
    glVertex2f(86, 320)
    glVertex2f(124, 316)
    glVertex2f(124, 318)
    glEnd()

def gedungtiga1persegipanjang4():
    glColor3ub(0, 81, 128)
    glBegin(GL_QUADS)
    glVertex2f(86, 314)
    glVertex2f(86, 312)
    glVertex2f(124, 308)
    glVertex2f(124, 310)
    glEnd()

def gedungtiga1persegipanjang4():
    glColor3ub(0, 81, 128)
    glBegin(GL_QUADS)
    glVertex2f(86, 314)
    glVertex2f(86, 312)
    glVertex2f(124, 308)
    glVertex2f(124, 310)
    glEnd()

def gedungtiga1persegipanjang5():
    glColor3ub(0, 81, 128)
    glBegin(GL_QUADS)
    glVertex2f(86, 306)
    glVertex2f(86, 304)
    glVertex2f(124, 300)
    glVertex2f(124, 302)
    glEnd()

def gedungtiga1persegipanjang6():
    glColor3ub(0, 81, 128)
    glBegin(GL_QUADS)
    glVertex2f(86, 298)
    glVertex2f(86, 296)
    glVertex2f(124, 292)
    glVertex2f(124, 294)
    glEnd()

def gedungtiga1persegipanjang7():
    glColor3ub(0, 81, 128)
    glBegin(GL_QUADS)
    glVertex2f(86, 290)
    glVertex2f(86, 288)
    glVertex2f(124, 286)
    glVertex2f(124, 284)
    glEnd()

def gedungtiga1persegipanjang8():
    glColor3ub(0, 81, 128)
    glBegin(GL_QUADS)
    glVertex2f(86, 282)
    glVertex2f(86, 280)
    glVertex2f(124, 276)
    glVertex2f(124, 278)
    glEnd()

def gedungtiga1persegipanjang9():
    glColor3ub(0, 81, 128)
    glBegin(GL_QUADS)
    glVertex2f(86, 274)
    glVertex2f(86, 272)
    glVertex2f(124, 268)
    glVertex2f(124, 270)
    glEnd()

def gedungtiga1persegipanjang10():
    glColor3ub(0, 81, 128)
    glBegin(GL_QUADS)
    glVertex2f(86, 266)
    glVertex2f(86, 264)
    glVertex2f(124, 260)
    glVertex2f(124, 262)
    glEnd()

def gedungtiga2():
    glColor3ub(37, 152, 219)
    glBegin(GL_QUADS)
    glVertex2f(130, 345)
    glVertex2f(130, 255)
    glVertex2f(180, 260)
    glVertex2f(180, 350)
    glEnd()

def gedungtiga2persegipanjang1():
    glColor3ub(0, 81, 128)
    glBegin(GL_QUADS)
    glVertex2f(136, 334)
    glVertex2f(136, 332)
    glVertex2f(174, 336)
    glVertex2f(174, 338)
    glEnd()

def gedungtiga2persegipanjang2():
    glColor3ub(0, 81, 128)
    glBegin(GL_QUADS)
    glVertex2f(136, 326)
    glVertex2f(136, 324)
    glVertex2f(174, 328)
    glVertex2f(174, 330)
    glEnd()

def gedungtiga2persegipanjang3():
    glColor3ub(0, 81, 128)
    glBegin(GL_QUADS)
    glVertex2f(136, 318)
    glVertex2f(136, 316)
    glVertex2f(174, 320)
    glVertex2f(174, 322)
    glEnd()

def gedungtiga2persegipanjang4():
    glColor3ub(0, 81, 128)
    glBegin(GL_QUADS)
    glVertex2f(136, 310)
    glVertex2f(136, 308)
    glVertex2f(174, 312)
    glVertex2f(174, 314)
    glEnd()

def gedungtiga2persegipanjang5():
    glColor3ub(0, 81, 128)
    glBegin(GL_QUADS)
    glVertex2f(136, 302)
    glVertex2f(136, 300)
    glVertex2f(174, 304)
    glVertex2f(174, 306)
    glEnd()

def gedungtiga2persegipanjang6():
    glColor3ub(0, 81, 128)
    glBegin(GL_QUADS)
    glVertex2f(136, 294)
    glVertex2f(136, 292)
    glVertex2f(174, 296)
    glVertex2f(174, 298)
    glEnd()

def gedungtiga2persegipanjang7():
    glColor3ub(0, 81, 128)
    glBegin(GL_QUADS)
    glVertex2f(136, 286)
    glVertex2f(136, 284)
    glVertex2f(174, 288)
    glVertex2f(174, 290)
    glEnd()

def gedungtiga2persegipanjang8():
    glColor3ub(0, 81, 128)
    glBegin(GL_QUADS)
    glVertex2f(136, 278)
    glVertex2f(136, 276)
    glVertex2f(174, 280)
    glVertex2f(174, 282)
    glEnd()

def gedungtiga2persegipanjang9():
    glColor3ub(0, 81, 128)
    glBegin(GL_QUADS)
    glVertex2f(136, 270)
    glVertex2f(136, 268)
    glVertex2f(174, 272)
    glVertex2f(174, 274)
    glEnd()

def gedungtiga2persegipanjang10():
    glColor3ub(0, 81, 128)
    glBegin(GL_QUADS)
    glVertex2f(136, 262)
    glVertex2f(136, 260)
    glVertex2f(174, 264)
    glVertex2f(174, 266)
    glEnd()

def gedungenambagian1():
    glColor3ub(203, 212, 207)
    glBegin(GL_QUADS)
    glVertex2f(220, 490)
    glVertex2f(220, 464)
    glVertex2f(280, 464)
    glVertex2f(280, 490)
    glEnd()

def gedungenambagian2():
    glColor3ub(203, 212, 207)
    glBegin(GL_QUADS)
    glVertex2f(280, 520)
    glVertex2f(280, 464)
    glVertex2f(380, 464)
    glVertex2f(380, 520)
    glEnd()

def gedungenambagian3():
    glColor3ub(203, 212, 207)
    glBegin(GL_POLYGON)
    glVertex2f(220, 464)
    glVertex2f(220, 430)
    glVertex2f(342, 434)
    glVertex2f(338, 434)
    glVertex2f(338, 438)
    glVertex2f(342, 438)
    glVertex2f(354, 464)
    glEnd()

def gedungenambagian4():
    glColor3ub(203, 212, 207)
    glBegin(GL_POLYGON)
    glVertex2f(220, 430)
    glVertex2f(244, 410)
    glVertex2f(256, 390)
    glVertex2f(342, 390)
    glVertex2f(342, 434)
    glVertex2f(338, 434)
    glEnd()

def gedungenambagian5():
    glColor3ub(203, 212, 207)
    glBegin(GL_POLYGON)
    glVertex2f(244, 410)
    glVertex2f(244, 362)
    glVertex2f(246, 362)
    glVertex2f(260, 362)
    glVertex2f(260, 382)
    glVertex2f(256, 382)
    glVertex2f(256, 390)
    glEnd()

def gedungenambagian6():
    glColor3ub(203, 212, 207)
    glBegin(GL_QUADS)
    glVertex2f(244, 362)
    glVertex2f(246, 352)
    glVertex2f(260, 352)
    glVertex2f(260, 362)
    glEnd()

def gedungenambagian7():
    glColor3ub(203, 212, 207)
    glBegin(GL_QUADS)
    glVertex2f(240, 352)
    glVertex2f(240, 260)
    glVertex2f(260, 260)
    glVertex2f(260, 352)
    glEnd()

def gedungenambagian8():
    glColor3ub(203, 212, 207)
    glBegin(GL_QUADS)
    glVertex2f(304, 390)
    glVertex2f(304, 382)
    glVertex2f(312, 382)
    glVertex2f(312, 390)
    glEnd()

def gedungenambagian9():
    glColor3ub(203, 212, 207)
    glBegin(GL_QUADS)
    glVertex2f(300, 382)
    glVertex2f(300, 260)
    glVertex2f(316, 260)
    glVertex2f(316, 382)
    glEnd()


def atapgedung4():
    glColor3ub(9, 66, 48)
    glBegin(GL_TRIANGLES)
    glVertex2f(198, 448)
    glVertex2f(152, 410)
    glVertex2f(244, 410)
    glEnd()

def gedungempat():
    glColor3ub(1, 143, 46)
    glBegin(GL_POLYGON)
    glVertex2f(152, 410)
    glVertex2f(152, 352)
    glVertex2f(185, 355)
    glVertex2f(188, 362)
    glVertex2f(244, 362)
    glVertex2f(244, 410)
    glEnd()

def gedungempatpersegi1():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(165, 400)
    glVertex2f(165, 395)
    glVertex2f(180, 395)
    glVertex2f(180, 400)
    glEnd()

def gedungempatpersegi2():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(190, 400)
    glVertex2f(190, 395)
    glVertex2f(205, 395)
    glVertex2f(205, 400)
    glEnd()

def gedungempatpersegi3():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(215, 400)
    glVertex2f(215, 395)
    glVertex2f(230, 395)
    glVertex2f(230, 400)
    glEnd()

def gedungempatpersegi4():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(165, 385)
    glVertex2f(165, 380)
    glVertex2f(180, 380)
    glVertex2f(180, 385)
    glEnd()

def gedungempatpersegi5():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(190, 385)
    glVertex2f(190, 380)
    glVertex2f(205, 380)
    glVertex2f(205, 385)
    glEnd()

def gedungempatpersegi6():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(215, 385)
    glVertex2f(215, 380)
    glVertex2f(230, 380)
    glVertex2f(230, 385)
    glEnd()

def gedungempatpersegi7():
    glColor3ub(255, 255,255)
    glBegin(GL_QUADS)
    glVertex2f(165, 370)
    glVertex2f(165, 365)
    glVertex2f(180, 365)
    glVertex2f(180, 370)
    glEnd()

def gedungempatpersegi8():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(190, 370)
    glVertex2f(190, 365)
    glVertex2f(205, 365)
    glVertex2f(205, 370)
    glEnd()

def gedungempatpersegi9():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(215, 370)
    glVertex2f(215, 365)
    glVertex2f(230, 365)
    glVertex2f(230, 370)
    glEnd()

def gedungempatbagian1():
    glColor3ub(1, 143, 46)
    glBegin(GL_QUADS)
    glVertex2f(185, 355)
    glVertex2f(185, 350)
    glVertex2f(188, 352)
    glVertex2f(188, 362)
    glEnd()

def gedungempatbagian2():
    glColor3ub(1, 143, 46)
    glBegin(GL_POLYGON)
    glVertex2f(180, 350)
    glVertex2f(180, 260)
    glVertex2f(194, 260)
    glVertex2f(194, 352)
    glVertex2f(188, 352)
    glVertex2f(185, 350)
    glEnd()

def atapgedunglima():
    glColor3ub(57, 61, 59)
    glBegin(GL_QUADS)
    glVertex2f(188, 362)
    glVertex2f(188, 352)
    glVertex2f(246, 352)
    glVertex2f(246, 362)
    glEnd()

def gedunglima():
    glColor3ub(158, 173, 166)
    glBegin(GL_QUADS)
    glVertex2f(194, 352)
    glVertex2f(194, 260)
    glVertex2f(240, 260)
    glVertex2f(240, 352)
    glEnd()

def gedunglimapersegi1():
    glColor3ub(91, 97, 94)
    glBegin(GL_QUADS)
    glVertex2f(200, 338)
    glVertex2f(200, 328)
    glVertex2f(204, 328)
    glVertex2f(204, 338)
    glEnd()

def gedunglimapersegi2():
    glColor3ub(91, 97, 94)
    glBegin(GL_QUADS)
    glVertex2f(210, 338)
    glVertex2f(210, 328)
    glVertex2f(214, 328)
    glVertex2f(214, 338)
    glEnd()

def gedunglimapersegi3():
    glColor3ub(91, 97, 94)
    glBegin(GL_QUADS)
    glVertex2f(220, 338)
    glVertex2f(220, 328)
    glVertex2f(224, 328)
    glVertex2f(224, 338)
    glEnd()

def gedunglimapersegi4():
    glColor3ub(91, 97, 94)
    glBegin(GL_QUADS)
    glVertex2f(230, 338)
    glVertex2f(230, 328)
    glVertex2f(234, 328)
    glVertex2f(234, 338)
    glEnd()

def gedunglimapersegi5():
    glColor3ub(91, 97, 94)
    glBegin(GL_QUADS)
    glVertex2f(200, 322)
    glVertex2f(200, 312)
    glVertex2f(204, 312)
    glVertex2f(204, 322)
    glEnd()

def gedunglimapersegi6():
    glColor3ub(91, 97, 94)
    glBegin(GL_QUADS)
    glVertex2f(210, 322)
    glVertex2f(210, 312)
    glVertex2f(214, 312)
    glVertex2f(214, 322)
    glEnd()

def gedunglimapersegi7():
    glColor3ub(91, 97, 94)
    glBegin(GL_QUADS)
    glVertex2f(220, 322)
    glVertex2f(220, 312)
    glVertex2f(224, 312)
    glVertex2f(224, 322)
    glEnd()

def gedunglimapersegi8():
    glColor3ub(91, 97, 94)
    glBegin(GL_QUADS)
    glVertex2f(230, 322)
    glVertex2f(230, 312)
    glVertex2f(234, 312)
    glVertex2f(234, 322)
    glEnd()

def gedunglimapersegi9():
    glColor3ub(91, 97, 94)
    glBegin(GL_QUADS)
    glVertex2f(200, 306)
    glVertex2f(200, 298)
    glVertex2f(204, 298)
    glVertex2f(204, 306)
    glEnd()

def gedunglimapersegi10():
    glColor3ub(91, 97, 94)
    glBegin(GL_QUADS)
    glVertex2f(210, 306)
    glVertex2f(210, 298)
    glVertex2f(214, 298)
    glVertex2f(214, 306)
    glEnd()

def gedunglimapersegi11():
    glColor3ub(91, 97, 94)
    glBegin(GL_QUADS)
    glVertex2f(220, 306)
    glVertex2f(220, 298)
    glVertex2f(224, 298)
    glVertex2f(224, 306)
    glEnd()

def gedunglimapersegi12():
    glColor3ub(91, 97, 94)
    glBegin(GL_QUADS)
    glVertex2f(230, 306)
    glVertex2f(230, 298)
    glVertex2f(234, 298)
    glVertex2f(234, 306)
    glEnd()

def gedunglimapersegi13():
    glColor3ub(91, 97, 94)
    glBegin(GL_QUADS)
    glVertex2f(200, 290)
    glVertex2f(200, 280)
    glVertex2f(204, 280)
    glVertex2f(204, 290)
    glEnd()

def gedunglimapersegi14():
    glColor3ub(91, 97, 94)
    glBegin(GL_QUADS)
    glVertex2f(210, 290)
    glVertex2f(210, 280)
    glVertex2f(214, 280)
    glVertex2f(214, 290)
    glEnd()

def gedunglimapersegi15():
    glColor3ub(91, 97, 94)
    glBegin(GL_QUADS)
    glVertex2f(220, 290)
    glVertex2f(220, 280)
    glVertex2f(224, 280)
    glVertex2f(224, 290)
    glEnd()
    
def gedunglimapersegi16():
    glColor3ub(91, 97, 94)
    glBegin(GL_QUADS)
    glVertex2f(230, 290)
    glVertex2f(230, 280)
    glVertex2f(234, 280)
    glVertex2f(234, 290)
    glEnd()

def gedunglimapersegi17():
    glColor3ub(91, 97, 94)
    glBegin(GL_QUADS)
    glVertex2f(200, 274)
    glVertex2f(200, 264)
    glVertex2f(204, 264)
    glVertex2f(204, 274)
    glEnd()

def gedunglimapersegi18():
    glColor3ub(91, 97, 94)
    glBegin(GL_QUADS)
    glVertex2f(210, 274)
    glVertex2f(210, 264)
    glVertex2f(214, 264)
    glVertex2f(214, 274)
    glEnd()

def gedunglimapersegi19():
    glColor3ub(91, 97, 94)
    glBegin(GL_QUADS)
    glVertex2f(220, 274)
    glVertex2f(220, 264)
    glVertex2f(224, 264)
    glVertex2f(224, 274)
    glEnd()

def gedunglimapersegi20():
    glColor3ub(91, 97, 94)
    glBegin(GL_QUADS)
    glVertex2f(230, 274)
    glVertex2f(230, 264)
    glVertex2f(234, 264)
    glVertex2f(234, 274)
    glEnd()


def atapgedungtujuh():
    glColor3ub(82, 55, 11)
    glBegin(GL_QUADS)
    glVertex2f(256, 390)
    glVertex2f(256, 382)
    glVertex2f(304, 382)
    glVertex2f(304, 390)
    glEnd()

def gedungtujuh():
    glColor3ub(184, 117, 9)
    glBegin(GL_QUADS)
    glVertex2f(260, 382)
    glVertex2f(260, 260)
    glVertex2f(300, 260)
    glVertex2f(300, 382)
    glEnd()

def gedungtujuhpersegi1():
    glColor3ub(163, 117, 42)
    glBegin(GL_QUADS)
    glVertex2f(265, 375)
    glVertex2f(265, 370)
    glVertex2f(290, 370)
    glVertex2f(290, 375)
    glEnd()

def gedungtujuhpersegi2():
    glColor3ub(163, 117, 42)
    glBegin(GL_QUADS)
    glVertex2f(265, 365)
    glVertex2f(265, 360)
    glVertex2f(290, 360)
    glVertex2f(290, 365)
    glEnd()

def gedungtujuhpersegi3():
    glColor3ub(163, 117, 42)
    glBegin(GL_QUADS)
    glVertex2f(265, 355)
    glVertex2f(265, 350)
    glVertex2f(290, 350)
    glVertex2f(290, 355)
    glEnd()

def gedungtujuhpersegi4():
    glColor3ub(163, 117, 42)
    glBegin(GL_QUADS)
    glVertex2f(265, 345)
    glVertex2f(265, 340)
    glVertex2f(290, 340)
    glVertex2f(290, 345)
    glEnd()

def gedungtujuhpersegi5():
    glColor3ub(163, 117, 42)
    glBegin(GL_QUADS)
    glVertex2f(265, 335)
    glVertex2f(265, 330)
    glVertex2f(290, 330)
    glVertex2f(290, 335)
    glEnd()

def gedungtujuhpersegi6():
    glColor3ub(163, 117, 42)
    glBegin(GL_QUADS)
    glVertex2f(265, 325)
    glVertex2f(265, 320)
    glVertex2f(290, 320)
    glVertex2f(290, 325)
    glEnd()

def gedungtujuhpersegi7():
    glColor3ub(163, 117, 42)
    glBegin(GL_QUADS)
    glVertex2f(265, 315)
    glVertex2f(265, 310)
    glVertex2f(290, 310)
    glVertex2f(290, 315)
    glEnd()

def gedungtujuhpersegi8():
    glColor3ub(163, 117, 42)
    glBegin(GL_QUADS)
    glVertex2f(265, 305)
    glVertex2f(265, 300)
    glVertex2f(290, 300)
    glVertex2f(290, 305)
    glEnd()

def gedungtujuhpersegi9():
    glColor3ub(163, 117, 42)
    glBegin(GL_QUADS)
    glVertex2f(265, 295)
    glVertex2f(265, 290)
    glVertex2f(290, 290)
    glVertex2f(290, 295)
    glEnd()
    
def gedungtujuhpersegi10():
    glColor3ub(163, 117, 42)
    glBegin(GL_QUADS)
    glVertex2f(265, 285)
    glVertex2f(265, 280)
    glVertex2f(290, 280)
    glVertex2f(290, 285)
    glEnd()

def gedungtujuhpersegi11():
    glColor3ub(163, 117, 42)
    glBegin(GL_QUADS)
    glVertex2f(265, 275)
    glVertex2f(265, 270)
    glVertex2f(290, 270)
    glVertex2f(290, 275)
    glEnd()

def gedungdelapanbagian1():
    glColor3ub(176, 252, 255)
    glBegin(GL_QUADS)
    glVertex2f(400, 550)
    glVertex2f(400, 464)
    glVertex2f(470, 464)
    glVertex2f(470, 550)
    glEnd()

def gedungdelapanbagian2():
    glColor3ub(176, 252, 255)
    glBegin(GL_POLYGON)
    glVertex2f(406, 464)
    glVertex2f(418, 438)
    glVertex2f(422, 438)
    glVertex2f(438, 438)
    glVertex2f(442, 438)
    glVertex2f(442, 444)
    glVertex2f(470, 444)
    glVertex2f(470, 464)
    glEnd()

def gedungdelapanbagian3():
    glColor3ub(176, 252, 255)
    glBegin(GL_QUADS)
    glVertex2f(422, 438)
    glVertex2f(422, 434)
    glVertex2f(438, 434)
    glVertex2f(438, 438)
    glEnd()

def gedungdelapanbagian4():
    glColor3ub(176, 252, 255)
    glBegin(GL_POLYGON)
    glVertex2f(418, 434)
    glVertex2f(418, 406)
    glVertex2f(438, 406)
    glVertex2f(438, 410)
    glVertex2f(442, 410)
    glVertex2f(442, 434)
    glEnd()

def gedungdelapanbagian5():
    glColor3ub(176, 252, 255)
    glBegin(GL_POLYGON)
    glVertex2f(418, 406)
    glVertex2f(418, 312)
    glVertex2f(420, 312)
    glVertex2f(430, 300)
    glVertex2f(432, 300)
    glVertex2f(432, 296)
    glVertex2f(442, 296)
    glVertex2f(442, 406)
    glEnd()

def gedungdelapanbagian6():
    glColor3ub(176, 252, 255)
    glBegin(GL_QUADS)
    glVertex2f(428, 296)
    glVertex2f(428, 260)
    glVertex2f(442, 260)
    glVertex2f(442, 296)
    glEnd()

def atapgedungsembilan1():
    glColor3ub(101, 31, 112)
    glBegin(GL_QUADS)
    glVertex2f(354, 464)
    glVertex2f(342, 438)
    glVertex2f(418, 438)
    glVertex2f(406, 464)
    glEnd()

def atapgedungsembilan2():
    glColor3ub(111, 50, 120)
    glBegin(GL_QUADS)
    glVertex2f(338, 438)
    glVertex2f(338, 434)
    glVertex2f(422, 434)
    glVertex2f(422, 438)
    glEnd()

def gedungsembilanbagian1():
    glColor3ub(153, 100, 161)
    glBegin(GL_POLYGON)
    glVertex2f(342, 434)
    glVertex2f(342, 390)
    glVertex2f(358, 390)
    glVertex2f(358, 382)
    glVertex2f(418, 382)
    glVertex2f(418, 434)
    glEnd()

def gedungsembilanbagian2():
    glColor3ub(153, 100, 161)
    glBegin(GL_POLYGON)
    glVertex2f(354, 382)
    glVertex2f(354, 300)
    glVertex2f(362, 300)
    glVertex2f(364, 300)
    glVertex2f(374, 312)
    glVertex2f(418, 312)
    glVertex2f(418, 382)
    glEnd()

def gedungsembilanbagian3():
    glColor3ub(153, 100, 161)
    glBegin(GL_POLYGON)
    glVertex2f(354, 300)
    glVertex2f(354, 260)
    glVertex2f(366, 260)
    glVertex2f(366, 296)
    glVertex2f(362, 296)
    glVertex2f(362, 300)
    glEnd()

def gedungsembilanpersegi1():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(350, 426)
    glVertex2f(350, 396)
    glVertex2f(356, 396)
    glVertex2f(356, 426)
    glEnd()

def gedungsembilanpersegi2():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(366, 426)
    glVertex2f(366, 396)
    glVertex2f(372, 396)
    glVertex2f(372, 426)
    glEnd()

def gedungsembilanpersegi3():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(388, 426)
    glVertex2f(388, 396)
    glVertex2f(394, 396)
    glVertex2f(394, 426)
    glEnd()

def gedungsembilanpersegi4():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(404, 426)
    glVertex2f(404, 396)
    glVertex2f(410, 396)
    glVertex2f(410, 426)
    glEnd()

def gedungsembilanpersegi5():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(366, 390)
    glVertex2f(366, 360)
    glVertex2f(372, 360)
    glVertex2f(372, 390)
    glEnd()

def gedungsembilanpersegi6():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(388, 390)
    glVertex2f(388, 360)
    glVertex2f(394, 360)
    glVertex2f(394, 390)
    glEnd()

def gedungsembilanpersegi7():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(404, 390)
    glVertex2f(404, 360)
    glVertex2f(410, 360)
    glVertex2f(410, 390)
    glEnd()

def gedungsembilanpersegi8():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(366, 354)
    glVertex2f(366, 324)
    glVertex2f(372, 324)
    glVertex2f(372, 354)
    glEnd()

def gedungsembilanpersegi9():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(388, 354)
    glVertex2f(388, 324)
    glVertex2f(394, 324)
    glVertex2f(394, 354)
    glEnd()

def gedungsembilanpersegi10():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(404, 354)
    glVertex2f(404, 324)
    glVertex2f(410, 324)
    glVertex2f(410, 354)
    glEnd()

def atapgedungsepuluh():
    glColor3ub(82, 55, 11)
    glBegin(GL_QUADS)
    glVertex2f(312, 390)
    glVertex2f(312, 382)
    glVertex2f(358, 382)
    glVertex2f(358, 390)
    glEnd()

def gedungsepuluh():
    glColor3ub(184, 117, 9)
    glBegin(GL_QUADS)
    glVertex2f(316, 382)
    glVertex2f(316, 260)
    glVertex2f(354, 260)
    glVertex2f(354, 382)
    glEnd()

def gedungsepuluhpersegi1():
    glColor3ub(163, 117, 42)
    glBegin(GL_QUADS)
    glVertex2f(320, 375)
    glVertex2f(320, 370)
    glVertex2f(350, 370)
    glVertex2f(350, 375)
    glEnd()

def gedungsepuluhpersegi2():
    glColor3ub(163, 117, 42)
    glBegin(GL_QUADS)
    glVertex2f(320, 365)
    glVertex2f(320, 360)
    glVertex2f(350, 360)
    glVertex2f(350, 365)
    glEnd()

def gedungsepuluhpersegi3():
    glColor3ub(163, 117, 42)
    glBegin(GL_QUADS)
    glVertex2f(320, 355)
    glVertex2f(320, 350)
    glVertex2f(350, 350)
    glVertex2f(350, 355)
    glEnd()

def gedungsepuluhpersegi4():
    glColor3ub(163, 117, 42)
    glBegin(GL_QUADS)
    glVertex2f(320, 345)
    glVertex2f(320, 340)
    glVertex2f(350, 340)
    glVertex2f(350, 345)
    glEnd()

def gedungsepuluhpersegi5():
    glColor3ub(163, 117, 42)
    glBegin(GL_QUADS)
    glVertex2f(320, 335)
    glVertex2f(320, 330)
    glVertex2f(350, 330)
    glVertex2f(350, 335)
    glEnd()

def gedungsepuluhpersegi6():
    glColor3ub(163, 117, 42)
    glBegin(GL_QUADS)
    glVertex2f(320, 325)
    glVertex2f(320, 320)
    glVertex2f(350, 320)
    glVertex2f(350, 325)
    glEnd()

def gedungsepuluhpersegi7():
    glColor3ub(163, 117, 42)
    glBegin(GL_QUADS)
    glVertex2f(320, 315)
    glVertex2f(320, 310)
    glVertex2f(350, 310)
    glVertex2f(350, 315)
    glEnd()

def gedungsepuluhpersegi8():
    glColor3ub(163, 117, 42)
    glBegin(GL_QUADS)
    glVertex2f(320, 305)
    glVertex2f(320, 300)
    glVertex2f(350, 300)
    glVertex2f(350, 305)
    glEnd()

def gedungsepuluhpersegi9():
    glColor3ub(163, 117, 42)
    glBegin(GL_QUADS)
    glVertex2f(320, 295)
    glVertex2f(320, 290)
    glVertex2f(350, 290)
    glVertex2f(350, 295)
    glEnd()

def gedungsepuluhpersegi10():
    glColor3ub(163, 117, 42)
    glBegin(GL_QUADS)
    glVertex2f(320, 285)
    glVertex2f(320, 280)
    glVertex2f(350, 280)
    glVertex2f(350, 285)
    glEnd()

def gedungsepuluhpersegi11():
    glColor3ub(163, 117, 42)
    glBegin(GL_QUADS)
    glVertex2f(320, 275)
    glVertex2f(320, 270)
    glVertex2f(350, 270)
    glVertex2f(350, 275)
    glEnd()

def atapgedungsebelas1():
    glColor3ub(143, 38, 6)
    glBegin(GL_QUADS)
    glVertex2f(374, 312)
    glVertex2f(364, 300)
    glVertex2f(430, 300)
    glVertex2f(420, 312)
    glEnd()

def atapgedungsebelas2():
    glColor3ub(201, 59, 16)
    glBegin(GL_QUADS)
    glVertex2f(362, 300)
    glVertex2f(362, 296)
    glVertex2f(432, 296)
    glVertex2f(432, 300)
    glEnd()

def gedungsebelas():
    glColor3ub(237, 128, 19)
    glBegin(GL_QUADS)
    glVertex2f(366, 296)
    glVertex2f(366, 260)
    glVertex2f(428, 260)
    glVertex2f(428, 296)
    glEnd()

def gedungsebelaspersegi1():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(378, 286)
    glVertex2f(378, 270)
    glVertex2f(402, 270)
    glVertex2f(402, 286)
    glEnd()

def gedungsebelaspersegi2():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(410, 286)
    glVertex2f(410, 270)
    glVertex2f(414, 270)
    glVertex2f(414, 286)
    glEnd()

def gedungsebelaspersegi3():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(418, 286)
    glVertex2f(418, 270)
    glVertex2f(422, 270)
    glVertex2f(422, 286)
    glEnd()  

def atapgedungduabelas():
    glColor3ub(92, 55, 18)
    glBegin(GL_QUADS)
    glVertex2f(442, 444)
    glVertex2f(442, 438)
    glVertex2f(484, 438)
    glVertex2f(484, 444)
    glEnd()

def atapgedunduabelaspersegi1():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(446, 442)
    glVertex2f(446, 438)
    glVertex2f(448, 438)
    glVertex2f(448, 442)
    glEnd()

def atapgedunduabelaspersegi2():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(450, 442)
    glVertex2f(450, 438)
    glVertex2f(452, 438)
    glVertex2f(452, 442)
    glEnd()

def atapgedunduabelaspersegi3():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(454, 442)
    glVertex2f(454, 438)
    glVertex2f(456, 438)
    glVertex2f(456, 442)
    glEnd()

def atapgedunduabelaspersegi4():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(458, 442)
    glVertex2f(458, 438)
    glVertex2f(460, 438)
    glVertex2f(460, 442)
    glEnd()

def atapgedunduabelaspersegi5():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(462, 442)
    glVertex2f(462, 438)
    glVertex2f(464, 438)
    glVertex2f(464, 442)
    glEnd()

def atapgedunduabelaspersegi6():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(466, 442)
    glVertex2f(466, 438)
    glVertex2f(468, 438)
    glVertex2f(468, 442)
    glEnd()

def atapgedunduabelaspersegi7():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(470, 442)
    glVertex2f(470, 438)
    glVertex2f(472, 438)
    glVertex2f(472, 442)
    glEnd()

def atapgedunduabelaspersegi8():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(474, 442)
    glVertex2f(474, 438)
    glVertex2f(476, 438)
    glVertex2f(476, 442)
    glEnd()

def atapgedunduabelaspersegi9():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(478, 442)
    glVertex2f(478, 438)
    glVertex2f(480, 438)
    glVertex2f(480, 442)
    glEnd()

def atapgedungduabelas2():
    glColor3ub(255, 140, 0)
    glBegin(GL_QUADS)
    glVertex2f(438, 438)
    glVertex2f(438, 434)
    glVertex2f(488, 434)
    glVertex2f(488, 438)
    glEnd()

def gedungduabelas1():
    glColor3ub(255, 255, 0)
    glBegin(GL_QUADS)
    glVertex2f(442, 434)
    glVertex2f(442, 410)
    glVertex2f(484, 410)
    glVertex2f(484, 434)
    glEnd()

def gedungduabelas1persegi1():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(448, 430)
    glVertex2f(448, 412)
    glVertex2f(456, 412)
    glVertex2f(456, 430)
    glEnd()

def gedungduabelas1persegi2():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(470, 430)
    glVertex2f(470, 412)
    glVertex2f(478, 412)
    glVertex2f(478, 430)
    glEnd()

def atapgedungduabelas3():
    glColor3ub(255, 140, 0)
    glBegin(GL_QUADS)
    glVertex2f(438, 410)
    glVertex2f(438, 406)
    glVertex2f(488, 406)
    glVertex2f(488, 410)
    glEnd()

def gedungduabelas2():
    glColor3ub(255, 255, 0)
    glBegin(GL_QUADS)
    glVertex2f(442, 406)
    glVertex2f(442, 260)
    glVertex2f(484, 260)
    glVertex2f(484, 406)
    glEnd()

def gedungduabelas2persegi1():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(448, 404)
    glVertex2f(448, 270)
    glVertex2f(456, 270)
    glVertex2f(456, 404)
    glEnd()

def gedungduabelas2persegi2():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(470, 404)
    glVertex2f(470, 270)
    glVertex2f(478, 270)
    glVertex2f(478, 404)
    glEnd()

def gedungtigabelas():
    glColor3ub(111, 255, 0)
    glBegin(GL_POLYGON)
    glVertex2f(720, 560)
    glVertex2f(720, 500)
    glVertex2f(740, 500)
    glVertex2f(740, 260)
    glVertex2f(820, 260)
    glVertex2f(820, 560)
    glEnd()

def gedungtigabelaspersegi1():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(760, 540)
    glVertex2f(760, 460)
    glVertex2f(780, 460)
    glVertex2f(780, 540)
    glEnd()

def gedungtigabelaspersegi2():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(760, 420)
    glVertex2f(760, 340)
    glVertex2f(780, 340)
    glVertex2f(780, 420)
    glEnd()

def gedungempatbelas():
    glColor3ub(255, 140, 0)
    glBegin(GL_POLYGON)
    glVertex2f(580, 600)
    glVertex2f(580, 540)
    glVertex2f(640, 540)
    glVertex2f(640, 500)
    glVertex2f(690, 500)
    glVertex2f(690, 600)
    glEnd()

def gedungempatbelaspersegi1():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(590, 590)
    glVertex2f(590, 560)
    glVertex2f(600, 560)
    glVertex2f(600, 590)
    glEnd()

def gedungempatbelaspersegi2():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(610, 590)
    glVertex2f(610, 560)
    glVertex2f(620, 560)
    glVertex2f(620, 590)
    glEnd()

def gedungempatbelaspersegi3():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(630, 590)
    glVertex2f(630, 560)
    glVertex2f(640, 560)
    glVertex2f(640, 590)
    glEnd()

def gedungempatbelaspersegi4():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(650, 590)
    glVertex2f(650, 560)
    glVertex2f(660, 560)
    glVertex2f(660, 590)
    glEnd()

def gedungempatbelaspersegi5():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(670, 590)
    glVertex2f(670, 560)
    glVertex2f(680, 560)
    glVertex2f(680, 590)
    glEnd()

def gedunglimabelas():
    glColor3ub(255, 94, 188)
    glBegin(GL_POLYGON)
    glVertex2f(540, 540)
    glVertex2f(540, 470)
    glVertex2f(580, 470)
    glVertex2f(580, 260)
    glVertex2f(640, 260)
    glVertex2f(640, 540)
    glEnd()

def gedunglimabelaspersegi1():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(550, 530)
    glVertex2f(550, 480)
    glVertex2f(570, 480)
    glVertex2f(570, 530)
    glEnd()

def gedunglimabelaspersegi2():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(580, 530)
    glVertex2f(580, 480)
    glVertex2f(600, 480)
    glVertex2f(600, 530)
    glEnd()

def gedunglimabelaspersegi3():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(610, 530)
    glVertex2f(610, 480)
    glVertex2f(630, 480)
    glVertex2f(630, 530)
    glEnd()

def gedungenambelas():
    glColor3ub(146, 3, 255)
    glBegin(GL_QUADS)
    glVertex2f(640, 500)
    glVertex2f(640, 260)
    glVertex2f(740, 260)
    glVertex2f(740, 500)
    glEnd()

def gedungenambelaspersegi1():
    glColor3ub(59, 0, 105)
    glBegin(GL_QUADS)
    glVertex2f(650, 480)
    glVertex2f(650, 450)
    glVertex2f(730, 450)
    glVertex2f(730, 480)
    glEnd()

def gedungenambelaspersegi2():
    glColor3ub(59, 0, 105)
    glBegin(GL_QUADS)
    glVertex2f(650, 430)
    glVertex2f(650, 400)
    glVertex2f(730, 400)
    glVertex2f(730, 430)
    glEnd()

def gedungenambelaspersegi3():
    glColor3ub(59, 0, 105)
    glBegin(GL_QUADS)
    glVertex2f(650, 380)
    glVertex2f(650, 350)
    glVertex2f(730, 350)
    glVertex2f(730, 380)
    glEnd()

def gedungenambelaspersegi4():
    glColor3ub(59, 0, 105)
    glBegin(GL_QUADS)
    glVertex2f(650, 330)
    glVertex2f(650, 300)
    glVertex2f(730, 300)
    glVertex2f(730, 330)
    glEnd()

def gedungtujuhbelas():
    glColor3ub(0, 196, 190)
    glBegin(GL_QUADS)
    glVertex2f(500, 470)
    glVertex2f(500, 260)
    glVertex2f(580, 260)
    glVertex2f(580, 470)
    glEnd()

def gedungtujuhbelas():
    glColor3ub(0, 196, 190)
    glBegin(GL_QUADS)
    glVertex2f(500, 470)
    glVertex2f(500, 260)
    glVertex2f(580, 260)
    glVertex2f(580, 470)
    glEnd()

def gedungtujuhbelaspersegi1():
    glColor3ub(0, 102, 99)
    glBegin(GL_QUADS)
    glVertex2f(510, 450)
    glVertex2f(510, 435)
    glVertex2f(570, 435)
    glVertex2f(570, 450)
    glEnd()

def gedungtujuhbelaspersegi2():
    glColor3ub(0, 102, 99)
    glBegin(GL_QUADS)
    glVertex2f(510, 425)
    glVertex2f(510, 410)
    glVertex2f(570, 410)
    glVertex2f(570, 425)
    glEnd()

def gedungtujuhbelaspersegi3():
    glColor3ub(0, 102, 99)
    glBegin(GL_QUADS)
    glVertex2f(510, 400)
    glVertex2f(510, 385)
    glVertex2f(570, 385)
    glVertex2f(570, 400)
    glEnd()

#Jalan

def jalan():
    glColor3ub(88, 92, 82)
    glBegin(GL_QUADS)
    glVertex2f(0, 260)
    glVertex2f(0, 200)
    glVertex2f(820, 200)
    glVertex2f(820, 260)
    glEnd()

def garisputihjalan1():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(55, 235)
    glVertex2f(55, 225)
    glVertex2f(105, 225)
    glVertex2f(105, 235)
    glEnd()

def garisputihjalan2():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(135, 235)
    glVertex2f(135, 225)
    glVertex2f(185, 225)
    glVertex2f(185, 235)
    glEnd()

def garisputihjalan3():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(215, 235)
    glVertex2f(215, 225)
    glVertex2f(265, 225)
    glVertex2f(265, 235)
    glEnd()

def garisputihjalan4():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(300, 260)
    glVertex2f(300, 200)
    glVertex2f(310, 200)
    glVertex2f(310, 260)
    glEnd()

def garisputihjalan5():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(340, 260)
    glVertex2f(340, 200)
    glVertex2f(350, 200)
    glVertex2f(350, 260)
    glEnd()

def garisputihjalan6():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(380, 260)
    glVertex2f(380, 200)
    glVertex2f(390, 200)
    glVertex2f(390, 260)
    glEnd()

def garisputihjalan7():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(430, 235)
    glVertex2f(430, 225)
    glVertex2f(480, 225)
    glVertex2f(480, 235)
    glEnd()

def garisputihjalan8():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(510, 235)
    glVertex2f(510, 225)
    glVertex2f(560, 225)
    glVertex2f(560, 235)
    glEnd()

def garisputihjalan9():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(590, 235)
    glVertex2f(590, 225)
    glVertex2f(640, 225)
    glVertex2f(640, 235)
    glEnd()

def garisputihjalan10():
    glBegin(GL_QUADS)
    glVertex2f(670, 235)
    glVertex2f(670, 225)
    glVertex2f(720, 225)
    glVertex2f(720, 235)
    glEnd()

def hero():
    glPushMatrix()
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
    glPopMatrix()
    
#kumano
def badanKuman():
    glPushMatrix()
    glColor3ub(255, 250, 250)
    glTranslated(100, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(70, 235)
    glVertex2f(77, 233)
    glVertex2f(80, 225)
    glVertex2f(79, 221)
    glVertex2f(76, 217)
    glVertex2f(70, 215)
    glVertex2f(61, 220)
    glVertex2f(60, 225)
    glVertex2f(65, 233)
    glEnd()
    glPopMatrix()

def gedung():
    glPushMatrix()
    gedungsatu()
    gedungsatu_dua()
    gedungdua()
    gedungduapersegi1()
    gedungduapersegi2()
    gedungduapersegi3()
    gedungduapersegi4()
    gedungduapersegi5()
    gedungduapersegi6()
    gedungduapersegi7()
    gedungduapersegi8()
    gedungduapersegi9()
    gedungduapersegi10()
    gedungdua_dua()
    gedungdua_duapersegi1()
    gedungdua_duapersegi2()
    gedungdua_duapersegi3()
    gedungdua_duapersegi4()
    gedungdua_duapersegi5()
    gedungdua_duapersegi6()
    gedungdua_duapersegi7()
    gedungdua_duapersegi8()
    gedungdua_duapersegi9()
    gedungdua_duapersegi10()
    gedungdua_duapersegi11()
    gedungdua_duapersegi12()
    gedungdua_duapersegi13()
    gedungdua_duapersegi14()
    gedungdua_duapersegi15()
    gedungdua_duapersegi16()
    gedungdua_duapersegi17()
    gedungdua_duapersegi18()
    gedungtigaatap()
    gedungtiga1()
    gedungtiga1persegipanjang1()
    gedungtiga1persegipanjang2()
    gedungtiga1persegipanjang3()
    gedungtiga1persegipanjang4()
    gedungtiga1persegipanjang5()
    gedungtiga1persegipanjang6()
    gedungtiga1persegipanjang7()
    gedungtiga1persegipanjang8()
    gedungtiga1persegipanjang9()
    gedungtiga1persegipanjang10()
    gedungtiga2()
    gedungtiga2persegipanjang1()
    gedungtiga2persegipanjang2()
    gedungtiga2persegipanjang3()
    gedungtiga2persegipanjang4()
    gedungtiga2persegipanjang5()
    gedungtiga2persegipanjang6()
    gedungtiga2persegipanjang7()
    gedungtiga2persegipanjang8()
    gedungtiga2persegipanjang9()
    gedungtiga2persegipanjang10()
    gedungenambagian1()
    gedungenambagian2()
    gedungenambagian3()
    gedungenambagian4()
    gedungenambagian5()
    gedungenambagian6()
    gedungenambagian7()
    gedungenambagian8()
    gedungenambagian9()
    atapgedung4()
    gedungempat()
    gedungempatpersegi1()
    gedungempatpersegi2()
    gedungempatpersegi3()
    gedungempatpersegi4()
    gedungempatpersegi5()
    gedungempatpersegi6()
    gedungempatpersegi7()
    gedungempatpersegi8()
    gedungempatpersegi9()
    gedungempatbagian1()
    gedungempatbagian2()
    atapgedunglima()
    gedunglima()
    gedunglimapersegi1()
    gedunglimapersegi2()
    gedunglimapersegi3()
    gedunglimapersegi4()
    gedunglimapersegi5()
    gedunglimapersegi6()
    gedunglimapersegi7()
    gedunglimapersegi8()
    gedunglimapersegi9()
    gedunglimapersegi10()
    gedunglimapersegi11()
    gedunglimapersegi12()
    gedunglimapersegi13()
    gedunglimapersegi14()
    gedunglimapersegi15()
    gedunglimapersegi16()
    gedunglimapersegi17()
    gedunglimapersegi18()
    gedunglimapersegi19()
    gedunglimapersegi20()
    atapgedungtujuh()
    gedungtujuh()
    gedungtujuhpersegi1()
    gedungtujuhpersegi2()
    gedungtujuhpersegi3()
    gedungtujuhpersegi4()
    gedungtujuhpersegi5()
    gedungtujuhpersegi6()
    gedungtujuhpersegi7()
    gedungtujuhpersegi8()
    gedungtujuhpersegi9()
    gedungtujuhpersegi10()
    gedungtujuhpersegi11()
    gedungdelapanbagian1()
    gedungdelapanbagian2()
    gedungdelapanbagian3()
    gedungdelapanbagian4()
    gedungdelapanbagian5()
    gedungdelapanbagian6()
    atapgedungsembilan1()
    atapgedungsembilan2()
    gedungsembilanbagian1()
    gedungsembilanbagian2()
    gedungsembilanbagian3()
    gedungsembilanpersegi1()
    gedungsembilanpersegi2()
    gedungsembilanpersegi3()
    gedungsembilanpersegi4()
    gedungsembilanpersegi5()
    gedungsembilanpersegi6()
    gedungsembilanpersegi7()
    gedungsembilanpersegi8()
    gedungsembilanpersegi9()
    gedungsembilanpersegi10()
    atapgedungsepuluh()
    gedungsepuluh()
    gedungsepuluhpersegi1()
    gedungsepuluhpersegi2()
    gedungsepuluhpersegi3()
    gedungsepuluhpersegi4()
    gedungsepuluhpersegi5()
    gedungsepuluhpersegi6()
    gedungsepuluhpersegi7()
    gedungsepuluhpersegi8()
    gedungsepuluhpersegi9()
    gedungsepuluhpersegi10()
    gedungsepuluhpersegi11()
    atapgedungsebelas1()
    atapgedungsebelas2()
    gedungsebelas()
    gedungsebelaspersegi1()
    gedungsebelaspersegi2()
    gedungsebelaspersegi3()
    atapgedungduabelas()
    atapgedunduabelaspersegi1()
    atapgedunduabelaspersegi2()
    atapgedunduabelaspersegi3()
    atapgedunduabelaspersegi4()
    atapgedunduabelaspersegi5()
    atapgedunduabelaspersegi6()
    atapgedunduabelaspersegi7()
    atapgedunduabelaspersegi8()
    atapgedunduabelaspersegi9()
    atapgedungduabelas2()
    gedungduabelas1()
    gedungduabelas1persegi1()
    gedungduabelas1persegi2()
    atapgedungduabelas3()
    gedungduabelas2()
    gedungduabelas2persegi1()
    gedungduabelas2persegi2()
    gedungtigabelas()
    gedungtigabelaspersegi1()
    gedungtigabelaspersegi2()
    gedungempatbelas()
    gedungempatbelaspersegi1()
    gedungempatbelaspersegi2()
    gedungempatbelaspersegi3()
    gedungempatbelaspersegi4()
    gedungempatbelaspersegi5()
    gedunglimabelas()
    gedunglimabelaspersegi1()
    gedunglimabelaspersegi2()
    gedunglimabelaspersegi3()
    gedungenambelas()
    gedungenambelaspersegi1()
    gedungenambelaspersegi2()
    gedungenambelaspersegi3()
    gedungenambelaspersegi4()
    gedungtujuhbelas()
    gedungtujuhbelaspersegi1()
    gedungtujuhbelaspersegi2()
    gedungtujuhbelaspersegi3()
    glPopMatrix()

def Jalan():
    jalan()
    glPushMatrix()
    glTranslate(x_jalan,0,0)
    garisputihjalan1()
    garisputihjalan2()
    garisputihjalan3()
    garisputihjalan4()
    garisputihjalan5()
    garisputihjalan6()
    garisputihjalan7()
    garisputihjalan8()
    garisputihjalan9()
    garisputihjalan10()
    glPopMatrix()

def hero():
    glPushMatrix()
    glTranslate(0,y_hero,0)
    heroGabungan()
    glPopMatrix()

def Kuman():
    glPushMatrix()
    glTranslate(x_kuman,0,0)
    kuman()
    glPopMatrix()

def iterate():
    glViewport(0, 0, 800, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 800, 0.0, 800, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    global speed_jalan, speed_kuman
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    gedung()
    Jalan()
    if y_hero ==0 and x_kuman < -340:
        speed_jalan,speed_kuman = 0,0
        bg_text()
        drawText("G A M E O V E R",300,225,0,0,0)
    else:
        hero()
        # heroGabungan()
        Kuman()
    glutSwapBuffers()

def timer_jalan(value):
    global x_jalan, x_kuman,y_hero, speed_jalan, speed_kuman
    x_jalan -= speed_jalan
    x_kuman -= speed_kuman
    if x_jalan < -120:
        x_jalan = 80
    if x_kuman < -460:
        x_kuman = 380
        
    glutTimerFunc(300,timer_jalan,0)

def timer_hero(value):
    global y_hero
    y_hero =0
    glutTimerFunc(2000,timer_hero,0)


def input_keyboard(key,x,y):
    global y_hero,x_kuman,x_jalan
    if key == GLUT_KEY_UP:
        if y_hero == 180:
            y_hero += 0
        else:
            y_hero += 90

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(800, 800)
    glutInitWindowPosition(100, 100)
    wind = glutCreateWindow("OpenGL Coding Practice")
    glutDisplayFunc(showScreen)
    glutIdleFunc(showScreen)
    glutSpecialFunc(input_keyboard)
    timer_jalan(0)
    timer_hero(0)
    init()
    glutMainLoop()
main()