# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot

from PyQt5.QtCore import *
from PyQt5 import uic
import threading
import time


import summer,summer2,sen1,sen2,doncry1,doncry2,chris1,chris2



Main_ui = uic.loadUiType("Main.ui")[0]


cnt = 0
cnt_r = 0
class MyWindow(QMainWindow, Main_ui):
   
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Practice.clicked.connect(self.practice_clicked)
        self.Professional.clicked.connect(self.professional_clicked)
        self.setGeometry(1921,0,664,1176)


    def practice_clicked(self):
        super().__init__()
        self.ui = uic.loadUi("ex_practice.ui")
        self.ui.setGeometry(1921,0,664,1176)

        #self.ui.textBrowser.setPlainText(index)
        
        self.ui.show()
        self.ui.ex_practice.clicked.connect(self.ex_practice_clicked)
        
        #self.ui.textBrowser.clear()

    #def 
    
    def professional_clicked(self):
        super().__init__()
        self.ui = uic.loadUi("ex_professional.ui")
        self.ui.setGeometry(1921,0,664,1176)
        self.ui.show()
        self.ui.ex_professional.clicked.connect(self.ex_professional_clicked)

    def ex_practice_clicked(self):
        self.ui = uic.loadUi("sheet_practice.ui")
        self.ui.setGeometry(1921,0,664,1176)
        self.ui.show()
        self.ui.SUMMER.clicked.connect(self.summer_timer)
        self.ui.CHRISTMAS.clicked.connect(self.christmas_timer)
        self.ui.SEN.clicked.connect(self.sen_timer)
        self.ui.DONTCRY.clicked.connect(self.doncry_timer)

    def ex_professional_clicked(self):
        
        self.ui = uic.loadUi("sheet_professional.ui")
        self.ui.setGeometry(1921,0,664,1176)
        self.ui.show()
        self.ui.RIVER.clicked.connect(self.pro_river_timer)
        self.ui.CHRISTMAS.clicked.connect(self.pro_christmas_timer)
        self.ui.SUMMER.clicked.connect(self.pro_summer_timer)
        self.ui.SEN.clicked.connect(self.pro_sen_timer)
        


    #PROFESSIONAL

    #river
    def pro_river_timer(self):
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.pro_river_timeout)
          

    def pro_river_timeout(self):
        global cnt_r
        self.ui = uic.loadUi("sheet.ui")
        self.ui.setGeometry(1951,150,606,870)
        self.ui.sheet.setStyleSheet("background-image:url(icon/river1.jpg);")
        self.ui.show()


        cnt_r = cnt_r + 1
        
        if cnt_r == 1:
            self.ui.count.setStyleSheet("background-image:url(icon/3.png);background-color:rgba(255,255,255,10);")
            
        elif cnt_r == 2:
            self.ui.count.setStyleSheet("background-image:url(icon/2.png);background-color:rgba(255,255,255,10);")
        elif cnt_r == 3:
            self.ui.count.setStyleSheet("background-image:url(icon/1.png);background-color:rgba(255,255,255,10);")
        elif cnt_r == 4:
            cnt_r = 0
            self.timer.stop()
            self.ui.count.hide()

            self.timer = QTimer(self)
            #넘어가는 초 설정
            self.timer.start(1000*3)
            self.timer.timeout.connect(self.pro_river_page_timeout)
                
    def pro_river_page_timeout(self):
        self.ui = uic.loadUi("sheet.ui")
        self.ui.setGeometry(1951,150,606,870)
        self.ui.sheet.setStyleSheet("background-image:url(icon/river2.jpg);")
        self.ui.checkbox.setStyleSheet("background-color:rgba(255,255,255,10);border : 0px;")
        self.ui.show()
        self.timer.stop()
        
        
    #sen
    def pro_sen_timer(self):
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.pro_sen_timeout)
          

    def pro_sen_timeout(self):
        global cnt_r
        self.ui = uic.loadUi("sheet.ui")
        self.ui.setGeometry(1951,150,606,870)
        self.ui.sheet.setStyleSheet("background-image:url(icon/sen1.png);")
        self.ui.show()
        cnt_r = cnt_r + 1
        
        if cnt_r == 1:
            self.ui.count.setStyleSheet("background-image:url(icon/3.png);background-color:rgba(255,255,255,10);")
        elif cnt_r == 2:
            self.ui.count.setStyleSheet("background-image:url(icon/2.png);background-color:rgba(255,255,255,10);")
        elif cnt_r == 3:
            self.ui.count.setStyleSheet("background-image:url(icon/1.png);background-color:rgba(255,255,255,10);")
        elif cnt_r == 4:
            cnt_r = 0
            self.timer.stop()
            self.ui.count.hide()
            
            self.timer = QTimer(self)
            #넘어가는 초 설정
            self.timer.start(1000*51)
            self.timer.timeout.connect(self.pro_sen_page_timeout)
                
    def pro_sen_page_timeout(self):
        self.ui = uic.loadUi("sheet.ui")
        self.ui.setGeometry(1951,150,606,870)
        self.ui.sheet.setStyleSheet("background-image:url(icon/sen2.png);")
        self.ui.checkbox.setStyleSheet("background-color:rgba(255,255,255,10);border : 0px;")
        self.ui.show()
        self.timer.stop()



    #summer
    def pro_summer_timer(self):
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.pro_summer_timeout)
          

    def pro_summer_timeout(self):
        global cnt_r
        self.ui = uic.loadUi("sheet.ui")
        self.ui.setGeometry(1951,150,606,870)
        self.ui.sheet.setStyleSheet("background-image:url(icon/summer1.png);")
        self.ui.show()
        cnt_r = cnt_r + 1
        
        if cnt_r == 1:
            self.ui.count.setStyleSheet("background-image:url(icon/3.png);background-color:rgba(255,255,255,10);")
        elif cnt_r == 2:
            self.ui.count.setStyleSheet("background-image:url(icon/2.png);background-color:rgba(255,255,255,10);")
        elif cnt_r == 3:
            self.ui.count.setStyleSheet("background-image:url(icon/1.png);background-color:rgba(255,255,255,10);")
        elif cnt_r == 4:
            cnt_r = 0
            self.timer.stop()
            self.ui.count.hide()
            
            self.timer = QTimer(self)
            #넘어가는 초 설정
            self.timer.start(1000*51)
            self.timer.timeout.connect(self.pro_summer_page_timeout)
                
    def pro_summer_page_timeout(self):
        self.ui = uic.loadUi("sheet.ui")
        self.ui.setGeometry(1951,150,606,870)
        self.ui.sheet.setStyleSheet("background-image:url(icon/summer2.png);")
        self.ui.checkbox.setStyleSheet("background-color:rgba(255,255,255,10);border : 0px;")
        self.ui.show()
        self.timer.stop()


    #christmas
    def pro_christmas_timer(self):
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.pro_christmas_timeout)
          

    def pro_christmas_timeout(self):
        global cnt_r
        self.ui = uic.loadUi("sheet.ui")
        self.ui.setGeometry(1951,150,606,870)
        self.ui.sheet.setStyleSheet("background-image:url(icon/christmas1.png);")
        self.ui.show()
        cnt_r = cnt_r + 1
        
        if cnt_r == 1:
            self.ui.count.setStyleSheet("background-image:url(icon/3.png);background-color:rgba(255,255,255,10);")
        elif cnt_r == 2:
            self.ui.count.setStyleSheet("background-image:url(icon/2.png);background-color:rgba(255,255,255,10);")
        elif cnt_r == 3:
            self.ui.count.setStyleSheet("background-image:url(icon/1.png);background-color:rgba(255,255,255,10);")
        elif cnt_r == 4:
            cnt_r = 0
            self.timer.stop()
            self.ui.count.hide()
            
            self.timer = QTimer(self)
            #넘어가는 초 설정
            self.timer.start(1000*51)
            self.timer.timeout.connect(self.pro_christmas_page_timeout)
                
    def pro_christmas_page_timeout(self):
        self.ui = uic.loadUi("sheet.ui")
        self.ui.setGeometry(1951,150,606,870)
        self.ui.sheet.setStyleSheet("background-image:url(icon/christmas2.png);")
        self.ui.checkbox.setStyleSheet("background-color:rgba(255,255,255,10);border : 0px;")
        self.ui.show()
        self.timer.stop()



    #PRACTICE

    #summer
    def summer_timer(self):
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.summer_timeout)
    
    def summer_timeout(self):
        melody_all = summer.melody_all
        
        global cnt
        self.ui = uic.loadUi("sheet.ui")
        self.ui.setGeometry(1951,150,606,870)
        
        self.ui.error.setPlainText("틀렸음 : B3,C5,E2")
        self.ui.error.setStyleSheet("background-color:rgba(150,75,0,50);border:0px;font-size:22pt;color:red;font-weight:bold;")
        self.ui.error.setAlignment(Qt.AlignCenter)
        self.ui.error.setGeometry(10,50,300,41)
        self.ui.sheet.setStyleSheet("background-image:url(icon/summer1.png);")
        self.ui.show()
        cnt = cnt + 1
        
        if cnt == 1:
            self.ui.count.setStyleSheet("background-image:url(icon/3.png);background-color:rgba(255,255,255,10);")
        elif cnt == 2:
            self.ui.count.setStyleSheet("background-image:url(icon/2.png);background-color:rgba(255,255,255,10);")
        elif cnt == 3:
            self.ui.count.setStyleSheet("background-image:url(icon/1.png);background-color:rgba(255,255,255,10);")
        elif cnt == 4:
            cnt = 0
            self.timer.stop()
            self.ui.count.hide()

            '''
            self.timer = QTimer(self)
            #넘어가는 초 설정
            self.timer.start(1000*6)
            self.timer.timeout.connect(self.asdf)
            '''

    def summer_page_timeout(self):
        melody_all = summer2.melody_all

        
        self.ui = uic.loadUi("sheet.ui")
        self.ui.setGeometry(1951,150,606,870)
        self.ui.sheet.setStyleSheet("background-image:url(icon/summer2.png);")
        self.ui.checkbox.setStyleSheet("background-color:rgba(255,255,255,10);border : 0px;")
        self.ui.show()
        self.timer.stop()

        
        '''            
    def asdf(self):
        self.ui = uic.loadUi("sheet.ui")
        self.ui.setGeometry(1951,150,606,870)
        self.ui.sheet.setStyleSheet("background-image:url(icon/summer2.png);")
        self.ui.checkbox1.setStyleSheet("background-color:rgba(255,255,255,10);border : 0px;")
        self.ui.checkbox1.setStyleSheet("background-image:url(icon/red_rectangle.png);background-color:rgba(255,255,255,10);")
        self.ui.show()
        self.timer.stop()
            
    
        self.timer = QTimer(self)
        #넘어가는 초 설정
        self.timer.start(1000)
        self.timer.timeout.connect(self.green_bt)

    def red_bt(self):
        self.ui = uic.loadUi("sheet.ui")
        self.ui.setGeometry(1951,150,606,870)
        self.ui.sheet.setStyleSheet("background-image:url(icon/summer20.png);")
        self.ui.checkbox1.setStyleSheet("background-color:rgba(255,255,255,10);border : 0px;")
        self.ui.checkbox1.setStyleSheet("background-image:url(icon/red_rectangle.png);background-color:rgba(255,255,255,10);")
        self.ui.show()
        self.ui.green.clicked(self.green_bt)
    
    def green_bt(self):
        self.ui = uic.loadUi("sheet.ui")
        self.ui.setGeometry(1951,150,606,870)
        self.ui.sheet.setStyleSheet("background-image:url(icon/summer20.png);")
        self.ui.checkbox1.setStyleSheet("background-color:rgba(255,255,255,10);border : 0px;")
        self.ui.checkbox1.setStyleSheet("background-image:url(icon/greed_rectangle.png);background-color:rgba(255,255,255,10);")
        self.ui.show()
        self.timer.stop()
        '''

    #sen
    #이미지 다시 설정하기
    def sen_timer(self):
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.sen_timeout)
    
    def sen_timeout(self):
        melody_all = sen1.melody_all
        
        global cnt
        self.ui = uic.loadUi("sheet.ui")
        self.ui.setGeometry(1900,150,720,912)
        
        self.ui.error.setPlainText("틀렸음 : B3,C5,E2")
        self.ui.error.setStyleSheet("background-color:rgba(150,75,0,50);border:0px;font-size:22pt;color:red;font-weight:bold;")
        self.ui.error.setAlignment(Qt.AlignCenter)
        
        self.ui.sheet.setGeometry(0,0,720,912)
        self.ui.sheet.setStyleSheet("background-image:url(icon/sen1.png);")
        self.ui.show()
        cnt = cnt + 1
        
        if cnt == 1:
            self.ui.count.setStyleSheet("background-image:url(icon/3.png);background-color:rgba(255,255,255,10);")
        elif cnt == 2:
            self.ui.count.setStyleSheet("background-image:url(icon/2.png);background-color:rgba(255,255,255,10);")
        elif cnt == 3:
            self.ui.count.setStyleSheet("background-image:url(icon/1.png);background-color:rgba(255,255,255,10);")
        elif cnt == 4:
            cnt = 0
            self.timer.stop()
            self.ui.count.hide()


            # 한페이지 끝나면 
            self.timer.timeout.connect(self.sen_page_timeout)
                
    def sen_page_timeout(self):
        self.ui = uic.loadUi("sheet.ui")
        self.ui.setGeometry(1951,150,606,870)
        self.ui.sheet.setStyleSheet("background-image:url(icon/sen2.png);")
        self.ui.checkbox.setStyleSheet("background-color:rgba(255,255,255,10);border : 0px;")
        self.ui.show()
        self.timer.stop()

    

    #CHRISTMAS
    #이미지 다시 설정하기
    def christmas_timer(self):
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.christmas_timeout)
    
    def christmas_timeout(self):
        melody_all = chris1.melody_all
        
        global cnt
        self.ui = uic.loadUi("sheet.ui")
        self.ui.setGeometry(1951,150,606,870)
        
        self.ui.error.setPlainText("틀렸음 : B3,C5,E2")
        self.ui.error.setStyleSheet("background-color:rgba(150,75,0,50);border:0px;font-size:22pt;color:red;font-weight:bold;")
        self.ui.error.setAlignment(Qt.AlignCenter)
        self.ui.error.setGeometry(10,50,300,41)
        
        self.ui.sheet.setStyleSheet("background-image:url(icon/christmas1.png);")
        self.ui.show()
        cnt = cnt + 1
        
        if cnt == 1:
            self.ui.count.setStyleSheet("background-image:url(icon/3.png);background-color:rgba(255,255,255,10);")
        elif cnt == 2:
            self.ui.count.setStyleSheet("background-image:url(icon/2.png);background-color:rgba(255,255,255,10);")
        elif cnt == 3:
            self.ui.count.setStyleSheet("background-image:url(icon/1.png);background-color:rgba(255,255,255,10);")
        elif cnt == 4:
            cnt = 0
            self.timer.stop()
            self.ui.count.hide()


            # 한페이지 끝나면 
            self.timer.timeout.connect(self.christmas_page_timeout)
                
    def christmas_page_timeout(self):
        self.ui = uic.loadUi("sheet.ui")
        self.ui.setGeometry(1951,150,606,870)
        self.ui.error.setPlainText("틀렸음 : B3,C5,E2")
        self.ui.error.setStyleSheet("background-color:rgba(150,75,0,50);border:0px;font-size:22pt;color:red;font-weight:bold;")
        self.ui.error.setAlignment(Qt.AlignCenter)
        
        self.ui.sheet.setStyleSheet("background-image:url(icon/christmas2.png);")
        self.ui.show()
        self.timer.stop()

    

    #DONCRY
    #이미지 다시 설정하기
    def doncry_timer(self):
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.doncry_timeout)
    
    def doncry_timeout(self):
        melody_all = doncry1.melody_all
        
        global cnt
        self.ui = uic.loadUi("sheet.ui")
        self.ui.setGeometry(1930,150,658,937)
        
        self.ui.error.setPlainText("틀렸음 : B3,C5,E2")
        self.ui.error.setStyleSheet("background-color:rgba(150,75,0,50);border:0px;font-size:22pt;color:red;font-weight:bold;")
        self.ui.error.setAlignment(Qt.AlignCenter)
        self.ui.error.setGeometry(10,50,300,41)
        
        self.ui.sheet.setGeometry(0,0,658,937)
        self.ui.sheet.setStyleSheet("background-image:url(icon/doncry1.png);")
        self.ui.show()
        cnt = cnt + 1
        
        if cnt == 1:
            self.ui.count.setStyleSheet("background-image:url(icon/3.png);background-color:rgba(255,255,255,10);")
        elif cnt == 2:
            self.ui.count.setStyleSheet("background-image:url(icon/2.png);background-color:rgba(255,255,255,10);")
        elif cnt == 3:
            self.ui.count.setStyleSheet("background-image:url(icon/1.png);background-color:rgba(255,255,255,10);")
        elif cnt == 4:
            cnt = 0
            self.timer.stop()
            self.ui.count.hide()


            # 한페이지 끝나면 
            self.timer.timeout.connect(self.doncry_page_timeout)
                
    def doncry_page_timeout(self):
        self.ui = uic.loadUi("sheet.ui")
        self.ui.setGeometry(1930,150,606,870)
        self.ui.sheet.setStyleSheet("background-image:url(icon/doncry2.png);")
        self.ui.checkbox.setStyleSheet("background-color:rgba(255,255,255,10);border : 0px;")
        self.ui.show()
        self.timer.stop()
    


    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    
