import cv2
import numpy as np
from matplotlib import pyplot as plt
from pprint import pprint
from collections import Counter
import glob
import os.path


img_gray = cv2.imread('Images/summer2.png',0)
img_rgb = cv2.imread('Images/summer2.png')

#cv2.imshow('ori',img_gray)


# sharpening. 이미지를 더 분명하게
kernel_sharpen = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])

img = cv2.filter2D(img_gray,-1,kernel_sharpen)


#(그레이스케일 이미지, 임계값, 최댓값, 임계값 종류)
#100 이하면 0으로, 100 이상이면 최댓값으로.
ret, dst = cv2.threshold(img,80,255,cv2.THRESH_BINARY)
#cv2.imshow('binary',dst)




#y축 훑어서 리스트에 문자로 넣어주자
prev = 0
cnt = 1
rle = []
rle_res =[]

for x in range(0,int(dst.shape[1]),1):
    for y in range(0,int(dst.shape[0]),1):
        color = dst.item(y,x)
        
        if color==255: #흰색이면 0
            rle.append(0)
        elif color==0: #검정색이면 1
            rle.append(1)
            
    for i in range(len(rle)):  #rle 리스트를 rle 압축한 후 숫자만 뽑아낸다.
        if i == 0:
            prev = rle[0]
            continue
        if prev == rle[i]:
            cnt = cnt + 1
            if i == len(rle):
                rle_res.append(cnt)
        else:
            rle_res.append(cnt)
            cnt = 1
        prev = rle[i]
    del rle
    rle = []

c = Counter(rle_res)
mode = c.most_common()

line_h=mode[0][0]
line_s=mode[1][0]




#리사이징
standard = 6 #기준값

#value = line_s/standard

value = (standard/line_s)

resize = cv2.resize(dst,dsize=(0,0),fx=value,fy=value,interpolation=cv2.INTER_AREA)
resize2 = cv2.resize(img_rgb,dsize=(0,0),fx=value,fy=value,interpolation=cv2.INTER_AREA)



#y축 훑어서 리스트에 문자로 넣어주자
prev = 0
cnt = 1
rle = []
rle_res =[]

for x in range(0,int(resize.shape[1]),1):
    for y in range(0,int(resize.shape[0]),1):
        color = resize.item(y,x)
        
        if color==255: #흰색이면 0
            rle.append(0)
        elif color==0: #검정색이면 1
            rle.append(1)
            
    for i in range(len(rle)):  #rle 리스트를 rle 압축한 후 숫자만 뽑아낸다.
        if i == 0:
            prev = rle[0]
            continue
        if prev == rle[i]:
            cnt = cnt + 1
            if i == len(rle):
                rle_res.append(cnt)
        else:
            rle_res.append(cnt)
            cnt = 1
        prev = rle[i]
    del rle
    rle = []

c = Counter(rle_res)
mode = c.most_common()

line_h=mode[0][0]
line_s=mode[1][0]





#오선 읽고 위치 저장

# 히스토그램으로 오선 찾기(흑백)(y,x)
h = np.zeros((resize.shape[0],600),dtype=np.uint8)
h_x=0
histo_len = []
for y in range(0,int(resize.shape[0]),1):
    for x in range(0,int(resize.shape[1]),1):
        b = resize[y,x]
        if b == 0:
            cv2.line(h,(h_x,y),(h_x,y),(255,255,255),1)
            h_x = h_x+1
    x=0
    #검정색 몇개 있는지 저장된 배열
    histo_len.append(h_x-1)
    h_x=0


x_histo = []
for i in range(0,resize.shape[0],1):
    if histo_len[i] > 433:      
        x_histo.append(i)
        for x in range(0,resize.shape[1],1):
            resize[i,x]=255        




staff_line = []
first_last =[]
#오선 추출하기
for i in range(0,len(x_histo),1):
    if i ==0:
        staff_line.append(x_histo[i])
        continue
    if x_histo[i]-x_histo[i-1] < line_s-3:
        continue
    staff_line.append(x_histo[i])


for i in range(0,len(staff_line),1):
    if i % 5==0:
        a =staff_line[i]
    elif i%5==4:
        b =staff_line[i]
        first_last.append([a,b])





# rgb
# 글씨 지우기
flag=1
i=0
first = first_last[i][0]-17
last = first_last[i][1]+13
for y in range(0,resize2.shape[0],1):
    if y == last :
        flag = 1
        if i == 4:
            last = first_last[i][1]+17
        else:
            last = first_last[i][1]+13
    if y == first:
        flag = 0
        i = i + 1
        if i == len(first_last):
            break
        first = first_last[i][0]-17
    if flag ==1:
        cv2.line(resize2,(0,y),(resize2.shape[1],y),(255,255,255),1)

for y in range(last,resize2.shape[0],1):
    cv2.line(resize2,(0,y),(resize2.shape[1],y),(255,255,255),1)


# 음표 템플릿
note_2 = cv2.imread('Images/2.png')
note_2 = cv2.resize(note_2,dsize=(0,0), fx=0.3,fy=0.3,interpolation=cv2.INTER_AREA)

threshold = 0.6

w, h,a = note_2.shape
res = cv2.matchTemplate(resize2, note_2, cv2.TM_CCOEFF_NORMED)
loc = np.where(res >= threshold)


for pt in zip(*loc[::-1]):
    cv2.line(resize2,(int(pt[0]+(w/2)),int(pt[1]+(h/2))),(int(pt[0]+(w/2)),int(pt[1]+(h/2))),(0,0,0),7)


for m in range(0,len(loc[0])-1,1):
    for n in range(0,len(loc[0])-1,1):
        if loc[1][m] == loc[1][n]:
            if loc[0][n]-loc[0][m]<line_s+2 and loc[0][n]-loc[0][m]>line_s-1:            
                cv2.line(resize2,(loc[1][n]-3,loc[0][n]+2),(loc[1][m]+11,loc[0][n]+2),(255,255,255),1)



note_on = cv2.imread('Images/on.png')

w, h,a = note_on.shape
res = cv2.matchTemplate(resize2, note_on, cv2.TM_CCOEFF_NORMED)
threshold = 0.61
loc = np.where(res >= threshold)


for pt in zip(*loc[::-1]):
    cv2.line(resize2,(int(pt[0]+(w/2)),int(pt[1]+(h/2))),(int(pt[0]+(w/2)),int(pt[1]+(h/2))),(0,0,0),6)


# 음표 따오기

# sharpening. 이미지를 더 분명하게
kernel_sharpen = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])

img2 = cv2.filter2D(resize2,-1,kernel_sharpen)


_, img = cv2.threshold(img2, 30, 255, cv2.THRESH_BINARY)
img = 255 - img;
img = 255 - cv2.erode(img, np.ones((3,3)), iterations=2)


# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Filter by Area.
params.filterByArea = True
params.minArea = 0.01

params.filterByConvexity = False

params.minDistBetweenBlobs = 0.1 #사이 간격 ->얘 하면 화음 인식

# Create a detector with the parameters
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3 :
    detector = cv2.SimpleBlobDetector(params)
else : 
    detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs.
keypoints = detector.detect(img)

# Draw blobs
img_point = cv2.drawKeypoints(resize2, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

#Write image
#cv2.imwrite("treble_staff.jpg", img_point)

#cv2.imshow('asdfasdf',img_point)


right = []
left = []

pop_arr=[]
pop_arr2 = []

k = 0

first = first_last[k][0] -17
last = first_last[k][1] + 13

all_key=[]
dlfma=[]

# 계이름 함수
melody_=[]
melody_all = []


dic_mel={1:'B3',2:'C4',3:'D4',4:'E4',5:'F4',6:'G4',7:'A4',8:'B4',9:'C5',10:'D5',11:'E5',12:'F5',13:'G5',14:'A5',15:'B5',16:'C6',31:'D2',32:'E2',33:'F2',34:'G2',35:'A2',36:'B2',37:'C3',38:'D3',39:'E3',40:'F3',41:'G3',42:'A3',43:'B3',44:'C4',45:'D4',46:'E4'}

def melody(axis_y,first2,last2):
    calcu = (last2 - first2) / 8
    if axis_y > (last2 + (3*calcu))-2 and axis_y < (last2 + (3*calcu))+2:
        melody_.append(1)
    elif axis_y > (last2 + (2*calcu))-2 and axis_y < (last2 +(2*calcu))+2:
        melody_.append(2)
    elif axis_y > (last2 + (1*calcu))-2 and axis_y < (last2 +(1*calcu))+2:
        melody_.append(3)
    elif axis_y > (last2)-2 and axis_y < (last2)+2:
        melody_.append(4)
    elif axis_y > (last2 - (1*calcu))-2 and axis_y < (last2 - (1*calcu))+2:
        melody_.append(5)   
    elif axis_y > (last2 - (2*calcu))-2 and axis_y < (last2 - (2*calcu))+2:
        melody_.append(6)
    elif axis_y > (last2 - (3*calcu))-2 and axis_y < (last2 - (3*calcu))+2:
        melody_.append(7)
    elif axis_y > (last2 - (4*calcu))-2 and axis_y < (last2 - (4*calcu))+2:
        melody_.append(8)   
    elif axis_y > (last2 - (5*calcu))-2 and axis_y < (last2 - (5*calcu))+2:
        melody_.append(9)
    elif axis_y > (last2 - (6*calcu))-2 and axis_y < (last2 - (6*calcu))+2:
        melody_.append(10)
    elif axis_y > (last2 - (7*calcu))-2 and axis_y < (last2 - (7*calcu))+2:
        melody_.append(11)
    elif axis_y > (first2)-2 and axis_y < (first2)+2:
        melody_.append(12)
    elif axis_y > (first2 - (1*calcu))-2 and axis_y < (first2- (1*calcu))+2:
        melody_.append(13)
    elif axis_y > (first2 - (2*calcu))-2 and axis_y < (first2 - (2*calcu))+2:
        melody_.append(14)
    elif axis_y > (first2 - (3*calcu))-2 and axis_y < (first2 - (3*calcu))+2:
        melody_.append(15)
    elif axis_y > (first2 - (4*calcu))-2 and axis_y < (first2 - (4*calcu))+2:
        melody_.append(16)
    else:
        melody_.append(1111111111111111)




def melody2(axis_y,first2,last2):
    calcu = (last2 - first2) / 8
    if axis_y > (last2 + (3*calcu))-2 and axis_y < (last2 + (3*calcu))+2:
        melody_.append(31)
    elif axis_y > (last2 + (2*calcu))-2 and axis_y < (last2 +(2*calcu))+2:
        melody_.append(32)
    elif axis_y > (last2 + (1*calcu))-2 and axis_y < (last2 +(1*calcu))+2:
        melody_.append(33)
    elif axis_y > (last2)-2 and axis_y < (last2)+2:
        melody_.append(34)
    elif axis_y > (last2 - (1*calcu))-2 and axis_y < (last2 - (1*calcu))+2:
        melody_.append(35)   
    elif axis_y > (last2 - (2*calcu))-2 and axis_y < (last2 - (2*calcu))+2:
        melody_.append(36)
    elif axis_y > (last2 - (3*calcu))-2 and axis_y < (last2 - (3*calcu))+2:
        melody_.append(37)
    elif axis_y > (last2 - (4*calcu))-2 and axis_y < (last2 - (4*calcu))+2:
        melody_.append(38)   
    elif axis_y > (last2 - (5*calcu))-2 and axis_y < (last2 - (5*calcu))+2:
        melody_.append(39)
    elif axis_y > (last2 - (6*calcu))-2 and axis_y < (last2 - (6*calcu))+2:
        melody_.append(40)
    elif axis_y > (last2 - (7*calcu))-2 and axis_y < (last2 - (7*calcu))+2:
        melody_.append(41)
    elif axis_y > (first2)-2 and axis_y < (first2)+2:
        melody_.append(42)
    elif axis_y > (first2 - (1*calcu))-2 and axis_y < (first2- (1*calcu))+2:
        melody_.append(43)
    elif axis_y > (first2 - (2*calcu))-2 and axis_y < (first2 - (2*calcu))+2:
        melody_.append(44)
    elif axis_y > (first2 - (3*calcu))-2 and axis_y < (first2 - (3*calcu))+2:
        melody_.append(45)
    elif axis_y > (first2 - (4*calcu))-2 and axis_y < (first2 - (4*calcu))+2:
        melody_.append(46)
    else:
        melody_.append(22222222)

    


for i in range(len(keypoints)-1,-1,-1):
    if keypoints[i].pt[1] > first and keypoints[i].pt[1] < last:
        if k%2 == 0:
            right.append([int(keypoints[i].pt[0]),int(keypoints[i].pt[1])])
        else:
            left.append([int(keypoints[i].pt[0]),int(keypoints[i].pt[1])]) 

    else:
        if k%2 ==0:
            right.sort()
            for n in range(0,len(right),1):
                if n == len(right)-1:
                    break
                if abs(right[n+1][0] - right[n][0]) < 4 and abs(right[n+1][1] - right[n][1]) < 4:
                    pop_arr.append(n)
                elif n!=0 and abs(right[n+1][0] - right[n-1][0]) < 4 and abs(right[n+1][1] - right[n-1][1]) < 4:
                    pop_arr.append(n-1)
                    
            
            pop_arr.sort()        
            a = np.array(pop_arr)
            if len(pop_arr)!=0:
                for n in range(0,len(pop_arr),1):
                    right.pop(a[n])
                    a = a-1

            dlfma.extend(right)
            del right
            right =[]
            del pop_arr
            pop_arr=[]
            del(a)
            
        elif k%2==1:
            left.sort()
            for n in range(0,len(left),1):
                if n == len(left)-1:
                    break
                if abs(left[n+1][0] - left[n][0]) < 3 and abs(left[n+1][1] - left[n][1]) < 3:
                    pop_arr2.append(n)
                elif n!=0 and abs(left[n+1][0] - left[n-1][0]) < 3 and abs(left[n+1][1] - left[n-1][1]) < 3:
                    pop_arr2.append(n-1)
            if k==1:        
                for n in range(0,len(left),1):
                    if n == len(left)-1:
                        break
                    if abs(left[n+1][0] - left[n][0]) < 3 and abs(left[n+1][1] - left[n][1]) < 3:
                        pop_arr2.append(n)
                    elif n!=0 and abs(left[n+1][0] - left[n-1][0]) < 3 and abs(left[n+1][1] - left[n-1][1]) < 3:
                        pop_arr2.append(n-1)
            
            pop_arr2.sort()  
            b = np.array(pop_arr2)
            if len(pop_arr2)!=0:
                for n in range(0,len(pop_arr2),1):
                    left.pop(b[n])
                    b = b-1
            
            dlfma.extend(left)
            del left
            left =[]
            del pop_arr2
            pop_arr2=[]
            del(b)
            
            dlfma.sort()
            dlfma.append(99999)
            all_key.extend(dlfma)
            del dlfma
            dlfma =[]

        if k == (len(first_last)*2) -1:
            break
        
        k = k+1
        first = first_last[k][0] -17
        last = first_last[k][1] +13
        if keypoints[i].pt[1] > first and keypoints[i].pt[1] < last:
            if k%2 == 0:
                right.append([int(keypoints[i].pt[0]),int(keypoints[i].pt[1])])
            else:
                left.append([int(keypoints[i].pt[0]),int(keypoints[i].pt[1])]) 


left.sort()
for n in range(0,len(left),1):
    if n == len(left)-1:
        break
    if abs(left[n+1][0] - left[n][0]) < 3 and abs(left[n+1][1] - left[n][1]) < 3:
        pop_arr2.append(n)
    elif n!=0 and abs(left[n+1][0] - left[n-1][0]) < 3 and abs(left[n+1][1] - left[n-1][1]) < 3:
        pop_arr2.append(n-1)
        
if len(pop_arr2)!=0:
    pop_arr2.sort()
    b = np.array(pop_arr2)
    for n in range(0,len(pop_arr2),1):
        left.pop(b[n])
        b= b-1

dlfma.extend(left)
dlfma.sort()
all_key.extend(dlfma)


k=0
#melody
for q in range(0,len(all_key),1):
    if (all_key[q]==99999):
        k=k+2
        if k ==8:
            break
    else:
        first = first_last[k][0]
        last = first_last[k][1]
        first2 = first_last[k+1][0]
        last2 = first_last[k+1][1]
        if first-17 <= all_key[q][1] and last+13 >= all_key[q][1]:
            melody(all_key[q][1],first,last)
        else :
            melody2(all_key[q][1],first2,last2)

#99999빼기
b = (all_key.index(99999))
all_key.pop(b)
b = (all_key.index(99999))
all_key.pop(b)
b = (all_key.index(99999))
all_key.pop(b)


for i in range(0,len(all_key),1):
    cv2.line(resize2,(all_key[i][0],all_key[i][1]),(all_key[i][0],all_key[i][1]),(0,255,255),3)

#cv2.imshow('after',resize2)

            

flag = 0
temp2=[]
for u in range(0,len(melody_),1):
    for z, p in dic_mel.items():
        if melody_[u] == z and flag == 0:
            if u != len(all_key)-1 and (abs(all_key[u][0] - all_key[u+1][0]) <3 ):
                temp2.append(dic_mel[z])
                flag =1
            else:
                melody_all.append([dic_mel[z]])
        elif melody_[u] == z and flag ==1:
            temp2.append(dic_mel[z])
            if u != len(all_key)-1 and (abs(all_key[u][0] - all_key[u+1][0]) <3 ):
                flag =2
            else:
                melody_all.append(temp2)
                flag =0
                del temp2
                temp2=[]
        elif melody_[u] ==z and flag ==2:
            temp2.append(dic_mel[z])
            melody_all.append(temp2)
            flag =0
            del temp2
            temp2=[]



