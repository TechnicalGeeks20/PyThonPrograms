import cv2
import time
import os
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
year=input("Enter Year of study : ")
section=input("Enter Section : ")
id=input("Enter ID : ")
name=input("Enter Name : ")
dataFolder="Dataset"
path=os.path.join(os.path.join(dataFolder,year),section)
try:
    os.makedirs("{}\\".format(path)+id+'.'+name)
    path=os.path.join(path,id+'.'+name)
    print(path)
    cap = cv2.VideoCapture(0)
    i=0
    while i<80:
        _, img = cap.read()
        grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(grayImage, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi_color = img[y:y + h, x:x + w]
            roi_gray=grayImage[y:y+h,x:x+w]
            print(str(i)+" Object found. Saving locally.") 
            cv2.imwrite("{}\\".format(path)+str(id)+"."+str(i)+'.jpg',roi_gray) 
            i=i+1
        cv2.imshow('img', img)
        k = cv2.waitKey(30) & 0xff
        if k==27:
            break
        time.sleep(1)
    cap.release()
except:
    print("File already exist")



