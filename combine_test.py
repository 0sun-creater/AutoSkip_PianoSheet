# -*- coding: utf-8 -*-

import copy
import pyaudio
import numpy as np
from scipy.signal import find_peaks
from scipy.fftpack import fft
import threading
import matplotlib.pyplot as plt
# import main1 as gui
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic, QtWidgets
import time

import summer, summer2, sen1, sen2, doncry1, doncry2, chris1, chris2

Main_ui = uic.loadUiType("Main.ui")[0]

melody_all = []
melody_sheet = []
start_flag = 0

cnt = 0
cnt_r = 0


class MyWindow(QMainWindow, Main_ui):
    global melody_sheet
    global melody_all
    global start_flag

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Practice.clicked.connect(self.practice_clicked)
        self.Professional.clicked.connect(self.professional_clicked)
        #1921, 0, 664, 1176
        self.setGeometry(1990, 40, 664, 1176)

    def practice_clicked(self):
        super().__init__()
        self.ui = uic.loadUi("ex_practice.ui")
        self.ui.setGeometry(1990, 40, 664, 1176)

        # self.ui.textBrowser.setPlainText(index)

        self.ui.show()
        self.ui.ex_practice.clicked.connect(self.ex_practice_clicked)

        # self.ui.textBrowser.clear()

    def professional_clicked(self):
        super().__init__()
        self.ui = uic.loadUi("ex_professional.ui")
        self.ui.setGeometry(1990, 40, 664, 1176)
        self.ui.show()
        self.ui.ex_professional.clicked.connect(self.ex_professional_clicked)

    def ex_practice_clicked(self):
        self.ui = uic.loadUi("sheet_practice.ui")
        self.ui.setGeometry(1990, 40, 664, 1176)
        self.ui.show()
        self.ui.SUMMER.clicked.connect(self.summer_click)
        self.ui.CHRISTMAS.clicked.connect(self.christmas_timer)
        self.ui.SEN.clicked.connect(self.sen_timer)
        self.ui.DONTCRY.clicked.connect(self.doncry_timer)

        self.dialogs = list()

    def summer_click(self):
        dialog = SHEETCLASS
        self.dialogs.append(dialog)
        dialog.show()

    def ex_professional_clicked(self):

        self.ui = uic.loadUi("sheet_professional.ui")
        self.ui.setGeometry(1990, 40, 664, 1176)
        self.ui.show()
        self.ui.RIVER.clicked.connect(self.pro_river_timer)
        self.ui.CHRISTMAS.clicked.connect(self.pro_christmas_timer)
        self.ui.SUMMER.clicked.connect(self.pro_summer_timer)
        self.ui.SEN.clicked.connect(self.pro_sen_timer)

    # PROFESSIONAL

    # river
    def pro_river_timer(self):
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.pro_river_timeout)

    def pro_river_timeout(self):
        global cnt_r
        self.ui = uic.loadUi("sheet.ui")
        self.ui.setGeometry(1990, 150, 606, 870)
        self.ui.sheet.setStyleSheet("background-image:url(icon/river1.jpg);")
        self.ui.error.setStyleSheet("background-color:rgba(255,255,255,10);border:0px;")
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
            # 넘어가는 초 설정
            self.timer.start(1000 * 52)
            self.timer.timeout.connect(self.pro_river_page_timeout)

    def pro_river_page_timeout(self):
        self.ui = uic.loadUi("sheet.ui")
        self.ui.setGeometry(1990, 150, 606, 870)
        self.ui.sheet.setStyleSheet("background-image:url(icon/river2.jpg);")
        self.ui.error.setStyleSheet("background-color:rgba(255,255,255,10);border:0px;")
        self.ui.show()
        self.timer.stop()

    # sen
    def pro_sen_timer(self):
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.pro_sen_timeout)

    def pro_sen_timeout(self):
        global cnt_r
        self.ui = uic.loadUi("sheet.ui")
        self.ui.setGeometry(1990, 150, 722, 912)
        self.ui.error.setStyleSheet("background-color:rgba(255,255,255,10);border:0px;")
        self.ui.sheet.setStyleSheet("background-image:url(icon/sen1.png);")
        self.ui.sheet.setGeometry(0,0,722,912)
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
            # 넘어가는 초 설정
            self.timer.start(1000 * 43)
            self.timer.timeout.connect(self.pro_sen_page_timeout)

    def pro_sen_page_timeout(self):
        self.ui = uic.loadUi("sheet.ui")
        self.ui.setGeometry(1990, 150, 720, 902)
        self.ui.sheet.setStyleSheet("background-image:url(icon/sen2.png);")
        self.ui.sheet.setGeometry(0, 0, 722, 902)
        self.ui.error.setStyleSheet("background-color:rgba(255,255,255,10);border:0px;")
        self.ui.show()
        self.timer.stop()

    # summer
    def pro_summer_timer(self):
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.pro_summer_timeout)

    def pro_summer_timeout(self):
        global cnt_r
        self.ui = uic.loadUi("sheet.ui")
        self.ui.setGeometry(1990, 150, 606, 870)
        self.ui.error.setStyleSheet("background-color:rgba(255,255,255,10);border:0px;")
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
            # 넘어가는 초 설정
            self.timer.start(1000 * 33)
            self.timer.timeout.connect(self.pro_summer_page_timeout)

    def pro_summer_page_timeout(self):
        self.ui = uic.loadUi("sheet.ui")
        self.ui.setGeometry(1990, 150, 606, 870)
        self.ui.sheet.setStyleSheet("background-image:url(icon/summer2.png);")
        self.ui.error.setStyleSheet("background-color:rgba(255,255,255,10);border:0px;")
        self.ui.show()
        self.timer.stop()

    # christmas
    def pro_christmas_timer(self):
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.pro_christmas_timeout)

    def pro_christmas_timeout(self):
        global cnt_r
        self.ui = uic.loadUi("sheet.ui")
        self.ui.setGeometry(1990, 150, 606, 870)
        self.ui.error.setStyleSheet("background-color:rgba(255,255,255,10);border:0px;")
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
            # 넘어가는 초 설정
            self.timer.start(1000 * 24)
            self.timer.timeout.connect(self.pro_christmas_page_timeout)

    def pro_christmas_page_timeout(self):
        self.ui = uic.loadUi("sheet.ui")
        self.ui.setGeometry(1990, 150, 614, 803)
        self.ui.error.setStyleSheet("background-color:rgba(255,255,255,10);border:0px;")
        self.ui.sheet.setStyleSheet("background-image:url(icon/christmas2.png);")
        self.ui.show()
        self.timer.stop()

    # PRACTICE

    # summer


    # def hello(self):
    #     self.timer = QTimer(self)
    #     self.timer.start(50)
    #     self.timer.timeout.connect(self.error_present)
    #     print("여긴 왔다감?")

    # def error_present(self, error_index, condition_flag):
    #     apple = QApplication(sys.argv)
    #     print("여긴 들어옴?")
    #     # self.timer.stop()
    #     self.ui = uic.loadUi("error.ui")
    #     self.ui.setGeometry(1951, 170, 300, 41)
    #     self.ui.error.setPlainText(''.join(melody_sheet[error_index]))
    #     # self.ui.error.setStyleSheet("background-image:url(icon/doncry2.png);")
    #     self.ui.error.setStyleSheet("background-color:rgba(150,75,0,50);border:0px;font-size:22pt;color:red;font-weight:bold;")
    #     self.ui.error.setAlignment(Qt.AlignCenter)
    #
    #     # self.ui.show()
    #     if condition_flag == -999:
    #         print("flag == -999")
    #         self.ui.show()
    #     elif condition_flag == 323:
    #         self.ui.close()
    #     # apple.exec_()
    #     sys.exit(apple.exec())
    #     print("aaaaaaaaaaaaaaaaaaaaaaaaa")

    '''
    def error_present(self, error_index):
        self.ui = uic.loadUi("error.ui")
        self.ui.error.setPlainText(sheet[error_index])
        self.ui.error.setStyleSheet("background-color:rgba(150,75,0,50);border:0px;font-size:22pt;color:red;font-weight:bold;")
        self.ui.error.setAlignment(Qt.AlignCenter)
        self.ui.show()
    '''

# error_ui = uic.loadUiType("error.ui")[0]

class SHEETCLASS(MyWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.summer_timer()

    def summer_timer(self):
        self.timer = QTimer(self)
        self.timer.start(500)
        self.timer.timeout.connect(self.summer_timeout)

    def summer_timeout(self):
        global melody_sheet
        melody_sheet = summer.melody_all
        print(melody_sheet)

        global cnt
        global start_flag
        self.ui = uic.loadUi("sheet.ui")
        self.ui.setGeometry(1990, 150, 606, 870)

        self.ui.sheet.setStyleSheet("background-image:url(icon/summer1.png);")
        self.ui.error.setStyleSheet("background-color:rgba(255,255,255,10);border:0px;")
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

            start_flag = 1

            '''
            self.timer = QTimer(self)
            #넘어가는 초 설정
            self.timer.start(1000*6)
            self.timer.timeout.connect(self.asdf)
            '''

    def summer_page_timeout(self):
        melody_all = summer2.melody_all

        self.ui = uic.loadUi("sheet.ui")
        self.ui.setGeometry(1990, 150, 606, 870)
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

    # sen
    # 이미지 다시 설정하기
    def sen_timer(self):
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.sen_timeout)

    def sen_timeout(self):
        global melody_sheet
        melody_sheet = sen1.melody_all

        global cnt
        global start_flag
        self.ui = uic.loadUi("sheet.ui")
        self.ui.setGeometry(1900, 150, 720, 912)

        self.ui.error.setStyleSheet("background-color:rgba(255,255,255,10);border:0px;")

        self.ui.sheet.setGeometry(0, 0, 720, 912)
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

            start_flag = 1

            # 한페이지 끝나면
            self.timer.timeout.connect(self.sen_page_timeout)

    def sen_page_timeout(self):
        self.ui = uic.loadUi("sheet.ui")
        self.ui.setGeometry(1990, 150, 606, 870)
        self.ui.sheet.setStyleSheet("background-image:url(icon/sen2.png);")
        self.ui.checkbox.setStyleSheet("background-color:rgba(255,255,255,10);border : 0px;")
        self.ui.show()
        self.timer.stop()

    # CHRISTMAS
    # 이미지 다시 설정하기
    def christmas_timer(self):
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.christmas_timeout)

    def christmas_timeout(self):
        global melody_sheet
        melody_all = chris1.melody_all

        global cnt
        global start_flag
        self.ui = uic.loadUi("sheet.ui")
        self.ui.setGeometry(1990, 150, 606, 870)

        self.ui.error.setStyleSheet("background-color:rgba(255,255,255,10);border:0px;")

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
            start_flag = 1
            # 한페이지 끝나면
            self.timer.timeout.connect(self.christmas_page_timeout)

    def christmas_page_timeout(self):
        self.ui = uic.loadUi("sheet.ui")
        self.ui.setGeometry(1990, 150, 606, 870)
        self.ui.error.setPlainText("틀렸음 : B3,C5,E2")
        self.ui.error.setStyleSheet(
            "background-color:rgba(150,75,0,50);border:0px;font-size:22pt;color:red;font-weight:bold;")
        self.ui.error.setAlignment(Qt.AlignCenter)

        self.ui.sheet.setStyleSheet("background-image:url(icon/christmas2.png);")
        self.ui.show()
        self.timer.stop()

    # DONCRY
    # 이미지 다시 설정하기
    def doncry_timer(self):
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.doncry_timeout)

    def doncry_timeout(self):
        global melody_sheet
        melody_sheet = doncry1.melody_all

        global cnt
        global start_flag
        self.ui = uic.loadUi("sheet.ui")
        self.ui.setGeometry(1990, 150, 658, 937)

        self.ui.error.setStyleSheet("background-color:rgba(255,255,255,10);border:0px;")

        self.ui.sheet.setGeometry(0, 0, 658, 937)
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

            start_flag = 1
            # 한페이지 끝나면
            self.timer.timeout.connect(self.doncry_page_timeout)

    def doncry_page_timeout(self):
        self.ui = uic.loadUi("sheet.ui")
        self.ui.setGeometry(1990, 150, 606, 870)
        self.ui.sheet.setStyleSheet("background-image:url(icon/doncry2.png);")
        self.ui.checkbox.setStyleSheet("background-color:rgba(255,255,255,10);border : 0px;")
        self.ui.show()
        self.timer.stop()

class ERRORCLASS(MyWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def error_present(self, error_index, condition_flag):
        apple = QApplication(sys.argv)
        self.ui = uic.loadUi("error.ui")
        self.ui.setGeometry(1990, 170, 300, 41)
        self.ui.error.setPlainText(''.join(melody_sheet[error_index]))
        self.ui.error.setStyleSheet("background-color:rgba(150,75,0,50);border:0px;font-size:22pt;color:red;font-weight:bold;")
        self.ui.error.setAlignment(Qt.AlignCenter)
        if condition_flag == -999:
            print("flag == -999")
            self.ui.show()
        elif condition_flag == 323:
            self.ui.error.clear()

        sys.exit(apple.exec())
        print("aaaaaaaaaaaaaaaaaaaaaaaaa")


real_note = []
wait_matching_gyename = []
matching_gyename = []
sheet_match_point = 0
note_match_point = 0
match_matrix = []
matching_result = -1

_class1 = 0

lock = threading.Lock()

# array내에 value값과 가장 가까운 값을 찾아주는 함수
def find_nearest(array, value):
    idx = (np.abs(array - value)).argmin()  # array 내의 값에서 value를 뺀 후 0에 가장 가까운 값을 value와 가장 가깝다고 판단
    return array[idx]


def find_nearest_idx(array, value):
    idx = (np.abs(array - value)).argmin()  # array 내의 값에서 value를 뺀 후 0에 가장 가까운 값을 value와 가장 가깝다고 판단
    return idx


# fre_key(인자)가 해당하는 계이름을 찾아주는 함수
def find_interval(fre_key):
    interval_Dict = {32.7032: 'C1', 34.6478: 'C#1', 36.7081: 'D1', 38.8909: 'D#1', 41.2034: 'E1', 43.6535: 'F1',
                     46.2493: 'F#1', 48.9994: 'G1', 51.9130: 'G#1', 55.0000: 'A1', 58.2705: 'A#1', 61.7354: 'B1',
                     65.4064: 'C2', 69.2957: 'C#2', 73.4162: 'D2', 77.7817: 'D#2', 82.4069: 'E2', 87.3071: 'F2',
                     92.4986: 'F#2', 97.9989: 'G2', 103.8262: 'G#2', 110.0000: 'A2', 116.5409: 'A#2', 123.4708: 'B2',
                     130.8128: 'C3', 138.5913: 'C#3', 146.8324: 'D3', 155.5635: 'D#3', 164.8138: 'E3', 174.6141: 'F3',
                     184.9972: 'F#3', 195.9977: 'G3', 207.6523: 'G#3', 220.0000: 'A3', 226.0819: 'A#3', 246.9417: 'B3',
                     261.6256: 'C4', 277.1826: 'C#4', 293.6648: 'D4', 311.1270: 'D#4', 329.6276: 'E4', 349.2282: 'F4',
                     369.9944: 'F#4', 391.9954: 'G4', 415.3047: 'G#4', 440.0000: 'A4', 466.1638: 'A#4', 493.8833: 'B4',
                     523.2511: 'C5', 554.3653: 'C#5', 587.3295: 'D5', 622.2540: 'D#5', 659.2551: 'E5', 698.4565: 'F5',
                     739.9888: 'F#5', 783.9909: 'G5', 830.6094: 'G#5', 880.0000: 'A5', 932.3275: 'A#5', 987.7666: 'B5',
                     1108.502: 'C6', 1108.731: 'C#6', 1174.659: 'D6', 1244.508: 'D#6', 1318.510: 'E6', 1396.913: 'F6',
                     1479.978: 'F#6', 1567.982: 'G6', 1661.219: 'G#6', 1760.000: 'A6', 1864.655: 'A#6', 1975.533: 'B6',
                     2093.005: 'C7', 2217.461: 'C#7', 2349.318: 'D7', 2489.016: 'D#7', 2637.020: 'E7', 2793.826: 'F7',
                     2959.955: 'F#7', 3135.963: 'G7', 3322.438: 'G#7', 3520.000: 'A7', 3729.310: 'A#7', 3951.066: 'B7',
                     4186.009: 'C8', 4434.922: 'C#8', 4698.636: 'D8', 4978.032: 'D#8', 5274.041: 'E8', 5587.652: 'F8',
                     5919.911: 'F#8', 6271.927: 'G8', 6644.875: 'G#8', 7040.000: 'A8', 7458.620: 'A#8', 7902.133: 'B8'}
    # A3    C6 1046
    return interval_Dict[fre_key]


# 양자화 해주는 함수
def scale(note):
    fre_array = np.array(
        [32.7032, 34.6478, 36.7081, 38.8909, 41.2034, 43.6535, 46.2493, 48.9994, 51.9130, 55.0000, 58.2705, 61.7354,
         65.4064, 69.2957, 73.4162, 77.7817, 82.4069, 87.3071, 92.4986, 97.9989, 103.8262, 110.0000, 116.5409, 123.4708,
         130.8128, 138.5913, 146.8324, 155.5635, 164.8138, 174.6141, 184.9972, 195.9977, 207.6523, 220.0000, 266.0819,
         246.9417, 261.6256, 277.1826, 293.6648, 311.1270, 329.6276, 349.2282, 369.9944, 391.9954, 415.3047, 440.0000,
         466.1638, 493.8833, 523.2511, 554.3653, 587.3295, 622.2540, 659.2551, 698.4565, 739.9888, 783.9909, 830.6094,
         880.0000, 932.3275, 987.7666, 1108.502, 1108.731, 1174.659, 1244.508, 1318.510, 1396.913, 1479.978, 1567.982,
         1661.219, 1760.000, 1864.655, 1975.533, 2093.005, 2217.461, 2349.318, 2489.016, 2637.020, 2793.826, 2959.955,
         3135.963, 3322.438, 3520.000, 3729.310, 3951.066, 4186.009, 4434.922, 4698.636, 4978.032, 5274.041, 5587.652,
         5919.911, 6271.927, 6644.875, 7040.000, 7458.620, 7902.133])
    sound_arr = []
    freq_arr = []
    freq_idx_arr = []
    for im in note:
        a = find_nearest(fre_array, im)
        freq_arr.append(a)
        b = find_nearest_idx(fre_array, im)
        freq_idx_arr.append(b)
        sound_arr.append(find_interval(a))
    return sound_arr, freq_arr, freq_idx_arr


# 배수로 감쇄하는 함수
def multiple_freq_decrease(y_, origin_y_, peak_):
    if len(peak_) == 0:
        return -999
    x, x_interval = np.linspace(0, 44100 / 2, 2048 / 2, retstep=True)  # x는 주파수 영역

    for i in range(len(peak_) - 1):  # 모든 피크에 대해서
        if x[peak_[0]] < 100:  # C1~B2
            print('감지불가구간 : C1~B2')

        elif x[peak_[0]] < 214:  # C3~A3
            y_[peak_[0]] = y_[peak_[0]] * 3  # 저주파값 너무 낮아서 증폭시켜본것
            for j in range(2, 6):  # 기준 피크로 부터 2배수는 자신의 1배만큼 감쇄하다가 뒤로갈수록 적게 감쇄 5배수경우 6/5배 감쇄
                if (peak_[i] * j + 1) < 512:
                    y_[peak_[i] * j - 1] = (origin_y_[peak_[i] * j - 1]) - abs(origin_y_[peak_[i]] * (2 / j))
                    y_[peak_[i] * j] = (origin_y_[peak_[i] * j]) - abs(origin_y_[peak_[i]] * (2 / j))
                    y_[peak_[i] * j + 1] = (origin_y_[peak_[i] * j + 1]) - abs(origin_y_[peak_[i]] * (2 / j))
                    y_[peak_[i] * j + 2] = (origin_y_[peak_[i] * j + 2]) - abs(origin_y_[peak_[i]] * (2 / j))

        elif x[peak_[0]] < 391:  # B3~G4
            for j in range(2, 6):  # 기준 피크로 부터 2배수는 자신의 4배만큼 감쇄하다가 뒤로갈수록 적게 감쇄 5배수경우 8/5배 감쇄
                if (peak_[i] * j + 1) < 512:
                    y_[peak_[i] * j - 2] = (origin_y_[peak_[i] * j - 2]) - abs(origin_y_[peak_[i]] * (8 / j))
                    y_[peak_[i] * j - 1] = (origin_y_[peak_[i] * j - 1]) - abs(origin_y_[peak_[i]] * (8 / j))
                    y_[peak_[i] * j] = (origin_y_[peak_[i] * j]) - abs(origin_y_[peak_[i]] * (8 / j))
                    y_[peak_[i] * j + 1] = (origin_y_[peak_[i] * j + 1]) - abs(origin_y_[peak_[i]] * (8 / j))
                    y_[peak_[i] * j + 2] = (origin_y_[peak_[i] * j + 2]) - abs(origin_y_[peak_[i]] * (8 / j))
                    y_[peak_[i] * j + 3] = (y_[peak_[i] * j + 3]) - abs(y_[peak_[i]] * (8 / j))
                    y_[peak_[i] * j + 4] = (y_[peak_[i] * j + 4]) - abs(y_[peak_[i]] * (8 / j))

        else:  # A4~C7
            for j in range(2, 6):  # 기준 피크로 부터 4배수 까지 감쇄하는데 이때 감쇄하는 값의 양쪽 값과 자신을 감쇄
                # if (peak_[i] * j + 1) < 512:
                # print('hell')
                y_[peak_[i] * j - 2] = (origin_y_[peak_[i] * j - 2]) - abs(origin_y_[peak_[i]] ** ((1) ** (j - 1)))
                y_[peak_[i] * j - 1] = (origin_y_[peak_[i] * j - 1]) - abs(origin_y_[peak_[i]] ** ((1) ** (j - 1)))
                y_[peak_[i] * j] = (origin_y_[peak_[i] * j]) - abs(origin_y_[peak_[i]] * ((1) ** (j - 1)))
                y_[peak_[i] * j + 1] = (origin_y_[peak_[i] * j + 1]) - abs(origin_y_[peak_[i]] * ((1) ** (j - 1)))
                y_[peak_[i] * j + 2] = (origin_y_[peak_[i] * j + 2]) - abs(origin_y_[peak_[i]] * ((1) ** (j - 1)))


def move_threshold(now_rmse_):
    new_threshold = 0
    if now_rmse_ < 10000:
        new_threshold = now_rmse_ * 1000 * 0.3
    else:
        new_threshold = now_rmse_ * 1000 * 0.25

    return new_threshold


def IsIt_correct(three_matrix_, matching_gyename_):
    count = 0
    for i in range(0, len(matching_gyename_)):
        count = count + three_matrix_.count(matching_gyename_[i])

    if count / len(three_matrix_) >= 0.5:
        return 1
    else:
        return -999


# matching하는 쓰레드 함수
def matching():
    global melody_sheet
    global real_note
    global sheet_match_point
    global note_match_point
    global matching_gyename
    global wait_matching_gyename
    global match_matrix
    global _class1


    while (1):
        if len(real_note) > 0:
            print("여기서 출발", melody_sheet)
            break
        # print("기다리는 중")

    matching_gyename = real_note[0]
    print("여긴 여기 ", melody_sheet)

    while (1):
        # print("matching", melody_sheet)
        if sheet_match_point == len(melody_sheet) - 3:
            return -1000
        else:
            if len(real_note) > 1:
                if len(real_note) > note_match_point + 1:

                    if len(wait_matching_gyename) > 0:
                        match_matrix.append(melody_sheet[sheet_match_point + 3])  # 악보 상에서 4개 묶기
                        wait_matching_gyename.append(matching_gyename)  # 기다린 음이랑 다음 음 2개 묶기

                        try:  # 안친거! 안쳐서 틀렸음!
                            a = match_matrix.index(wait_matching_gyename[0])
                            b = match_matrix.index(wait_matching_gyename[1])
                            if (b - a) == 1:  # match_matrix에 그 2개 묶은게 있음
                                if a == 1:
                                    sheet_match_point = sheet_match_point + 1
                                    matching_gyename = wait_matching_gyename[0]
                                    # print('1개 안침')
                                elif a == 2:
                                    sheet_match_point = sheet_match_point + 2
                                    matching_gyename = wait_matching_gyename[0]
                                    # print('2개 안침')
                                else:
                                    print('망했음.')
                                match_matrix = []
                                wait_matching_gyename = []

                            else:
                                print('  x   : ', melody_sheet[sheet_match_point])
                                # lock.acquire()
                                abc = MyWindow()
                                ERRORCLASS.error_present(QWidget, sheet_match_point, -999)
                                # lock.release()
                                matching_gyename = wait_matching_gyename[1]
                                wait_matching_gyename = []
                                real_note = []
                                match_matrix = []
                                # sheet_match_point = sheet_match_point + 1
                                note_match_point = 0

                            # 악보에 return하는 표시해야 함!!

                            # return (sheet_match_point - 1)  # match_point index를 갖는 곳에(악보에) 틀림 표시
                        except ValueError:  # 음을 틀렸음!
                            print('  x   :', melody_sheet[sheet_match_point])
                            lock.acquire()
                            abc = MyWindow()
                            ERRORCLASS.error_present(QWidget, sheet_match_point, -999)
                            lock.release()
                            matching_gyename = wait_matching_gyename[1]
                            wait_matching_gyename = []
                            real_note = []
                            match_matrix = []
                            # sheet_match_point = sheet_match_point + 1
                            note_match_point = 0

                        # return (sheet_match_point - 1)
                    else:
                        for i in range(0, 3):
                            match_matrix.append(melody_sheet[sheet_match_point + i])

                        if IsIt_correct(match_matrix[0], matching_gyename) == 1:
                            print('  O   :', match_matrix[0])

                            # lock.acquire()
                            abc = MyWindow()
                            ERRORCLASS.error_present(QWidget, sheet_match_point, 323)
                            # lock.release()
                            sheet_match_point = sheet_match_point + 1
                            note_match_point = note_match_point + 1
                            match_matrix = []

                            matching_gyename = real_note[note_match_point]
                            # return -1
                        else:
                            # print('기다려 : ', matching_gyename)
                            wait_matching_gyename.append(matching_gyename)
                            matching_gyename = real_note[note_match_point + 1]
                            # return -1


def audio_read():
    global start_flag
    print("들어옴")

    CHUNK = 2048
    RATE = 44100
    T = 1.0 / RATE
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    keep_rmse = 0
    keep_keep_rmse = 0
    keep_keep_keeep_rmse = 0
    keep_gyename = 0
    gye_name1 = 0

    press_point_x_list = []
    press_point_y_list = []
    press_point_count = 0
    rmse_list = []

    before_origin_y = 0
    before_decrease_y = 0
    before_threshold = 0
    before_peaks = []
    x_interval = 0
    keep_peaks = 0
    keep_peaks1 = 0
    now_rmse_all_list = []

    while(1):
        if start_flag == 1:
            break

    while (1):
        # for i in range(0, 10000):
        lock.acquire()
        data = np.fromstring(stream.read(CHUNK), dtype=np.int16)  # 마이크에서 데이터를 읽어옴 (데이터 길이 1024)
        lock.release()
        n = len(data)
        now_rmse = np.linalg.norm(data - 0) / np.sqrt(n)
        rmse_list.append(now_rmse)
        if now_rmse > 2000:  # 피아노 소리가 들리지 않을 때는 계산하지 않음 (들어온 데이터의 크기로 분석)

            n = len(data)

            x, x_interval = np.linspace(0, 44100 / 2, n / 2, retstep=True)  # x는 주파수 영역
            # data = librosa.autocorrelate(data, max_size=512)  # 잡음을 줄이기 위한 autocorrelation - noise reduction
            y = fft(data, n)  # 푸리에 변환

            y = np.absolute(y)
            y = y[range(int(n / 2))]
            origin_y = copy.copy(y)  # y값은 함수(..decrease)에 의해 변환되기 때문에 원래 y값을 미리 저장한다.

            # peak 값을 찾기 위한 임계점을 유동적으로 하기 위한 기준 잡기
            max_peak = 0
            std_peaks, _ = find_peaks(y, height=1500)  # 1500을 넘는 peak값을 찾는다. (max를 찾기 위한 표준 peak들)

            if len(std_peaks) > 0 and now_rmse > 4000:
                if keep_keep_rmse < keep_rmse and keep_rmse > now_rmse and keep_keep_keeep_rmse < keep_rmse and \
                        np.abs(keep_keep_keeep_rmse - keep_rmse) > 1000:
                    # press_point_x_list.append(i)
                    # press_point_y_list.append(keep_rmse)
                    lock.acquire()
                    # print('gye:', keep_gyename[0])
                    real_note.append(keep_gyename[0])
                    # print('real_note : ', real_note)
                    lock.release()

                    # plt.plot(keep_gyename[1],)
                    # plt.plot(x, before_origin_y, 'b*')
                    # plt.plot(x, before_origin_y, 'g')
                    # plt.plot(before_peaks * x_interval, y[before_peaks], "rx")
                    # plt.plot(x, before_decrease_y, 'r--')
                    #
                    # std_y = np.ones(int(n / 2)) * before_threshold
                    # plt.plot(x, std_y)
                    # plt.annotate('threshold : %d' % (before_threshold), xy=(11, 10), xytext=(4000, 7500), size=10, ha='right',
                    #              va='center')
                    # plt.annotate('%s' % str(gye_name1), xy=(11, 10), xytext=(4000, 10000000), size=10, ha='right', va='center')
                    # plt.annotate('rmse : %s' % str(keep_rmse), xy=(11, 10), xytext=(4000, 20000000), size=10, ha='right',
                    #              va='center')
                    #
                    # str_keep_peaks = str(keep_peaks) + str(scale(keep_peaks * x_interval)[0])
                    # str_keep_peaks1 = str(keep_peaks1) + str(scale(keep_peaks1 * x_interval)[0])
                    # plt.annotate('before_peaks : %s' % str_keep_peaks, xy=(11, 10), xytext=(4000, 24000000), size=10, ha='right',
                    #              va='center')
                    # plt.annotate('after_peaks : %s' % str_keep_peaks1, xy=(11, 10), xytext=(4000, 22000000), size=10, ha='right',
                    #              va='center')
                    # plt.xlim(0, 4000)
                    # plt.ylim(0, 30000000)
                    # plt.show()
                    # now_rmse_all_list.append(keep_rmse)

                max_peak = np.max(y[std_peaks])  # std_peaks에 있는 값들 중에서 가장 큰 값을 찾는다.
                std_threshold = 0.35 * 1e7  # max_peak을 이용하여 임계값을 설정한다.
                peaks, _ = find_peaks(y, height=std_threshold)  # 임계값을 넘는 peak만 음으로 인식한다.
                keep_peaks = peaks
                gye_name = scale(peaks * x_interval)
                #  하모닉 음을 줄이기 위한 부분(치지 않은 음인데 친 음의 배수 라서 튄 계이름들)
                if not gye_name[0]:
                    continue
                else:
                    multiple_freq_decrease(y, origin_y, peaks)

                    peaks1, _ = find_peaks(y, height=std_threshold)
                    keep_peaks1 = peaks1
                    # print('peaks :  ', peaks1)
                    gye_name1 = scale(peaks1 * x_interval)
                    keep_gyename = gye_name1

                before_decrease_y = y
                before_origin_y = origin_y
                before_threshold = std_threshold
                before_peaks = copy.copy(peaks)

        keep_keep_keeep_rmse = keep_keep_rmse
        keep_keep_rmse = keep_rmse
        keep_rmse = now_rmse
    stream.stop_stream()
    print('빠져나옴')
    stream.close()
    p.terminate()


my_thread1 = threading.Thread(target=matching)
my_thread2 = threading.Thread(target=audio_read)

my_thread2.start()
my_thread1.start()

# if __name__ == "__main__":
app = QApplication(sys.argv)
# myWindow = MyWindow()
my_gui = MyWindow()
my_thread3 = threading.Thread(target=MyWindow)
# _class1 = ERRORCLASS()
my_thread3.start()
my_gui.show()


app.exec_()
print("다끔")



