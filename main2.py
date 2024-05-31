import cv2
import os
from cvzone.HandTrackingModule import HandDetector 
import numpy as np

#variable
width,heigth = 1280,720
folderpath = "presentation 3"

#camera setup
cap = cv2.VideoCapture(0)
cap.set(3,width)
cap.set(4,heigth)

#Get the list of presentation images
pathImages = sorted(os.listdir(folderpath),key=len)
#print(pathImages)

#variables
imgNumber = 0
hs , ws = int(120*1), int(213*1)
gestureThreshold = 300
buttonPressed = False
buttonCount = 0
buttonDelay = 5
annotations = [[]]
annotationNumber = 0
annotationStart = False

#Hand Detector
detector = HandDetector(detectionCon=0.8, maxHands=2)


while True:
    #import Images
    success , img = cap.read()
    img = cv2.flip(img, 1)
    pathFullImage = os.path.join(folderpath,pathImages[imgNumber])
    imgCurrent = cv2.imread(pathFullImage)

    hands, img = detector.findHands(img)
    cv2.line(img, (0, gestureThreshold), (width, gestureThreshold), (0,0,0), 10)

     # Keyboard control to change slides
    key = cv2.waitKey(1)
    if key == ord('a') and imgNumber > 0:
        imgNumber -= 1
    elif key == ord('d') and imgNumber < len(pathImages) - 1:
        imgNumber += 1

    if hands and buttonPressed is False:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        cx, cy = hand['center']
        #print(fingers)
        lmList = hand['lmList']
        indexFinger = lmList[8][0], lmList[8][1]
        xval = int(np.interp(lmList[8][0], [width//2, w], [0, width]))  # pointer screen change 
        yval = int(np.interp(lmList[8][1], [130, heigth-130], [0, heigth])) # pointer screen change
        indexFinger = xval, yval




        #if cy <= gestureThreshold:    #if hand is at the height of the face
           # annotationStart = False





           
            # Gesture 1- Left
        if fingers == [1,1,1,0,0]:
                annotationStart = False
                print("Left")
                if imgNumber>0:
                    buttonPressed = True
                    annotations = [[]]
                    annotationNumber = 0
                    
                    imgNumber -= 1
                
        if fingers == [1,0,0,0,0]:
            break
            
            # Gesture 2- Right
        if fingers == [0,0,0,0,1]:
                annotationStart = False
                #print("Right") 
                if imgNumber<len(pathImages)-1:
                    buttonPressed = True
                    annotations = [[]]
                    annotationNumber = 0
                    
                    imgNumber += 1

        # Gesture 3- Pointer
        if fingers == [0,1,1,0,0]:
            cv2.circle(imgCurrent, indexFinger, 8, (0,0,255), cv2.FILLED)
            annotationStart = False

        # Gesture 4- Draw
        if fingers == [0,1,0,0,0]:
            if annotationStart is False:
                annotationStart = True
                annotationNumber += 1
                annotations.append([])
            cv2.circle(imgCurrent, indexFinger, 8, (0,0,255), cv2.FILLED)
            annotations[annotationNumber].append(indexFinger)
        else:
            annotationStart = False

        # Gesture 5- Erase
        if fingers == [0,1,1,1,0]:
            if annotations:
                if annotationNumber >= 0:
                    annotations.pop(-1)
                    annotationNumber -= 1
                    buttonPressed = True
    else:
        annotationStart = False

    
    # ButtonPress is False
    if buttonPressed:
        buttonCount += 1
        if buttonCount > buttonDelay:
            buttonCount = 0
            buttonPressed = False


    for i in range(len(annotations)):
        for j in range(len(annotations[i])):
            if j != 0:
                cv2.line(imgCurrent, annotations[i][j-1], annotations[i][j], (0, 0, 200), 8)


    #Adding Webcam image on slide
    imgSmall = cv2.resize(img,(ws, hs))
    h, w, _ = imgCurrent.shape
    imgCurrent[0:hs, w-ws:w] = imgSmall


    cv2.imshow("Image",img)
    cv2.imshow("Slides",imgCurrent)

    key = cv2.waitKey(1)
    # if key == ord('q'):
    #     break


#Resize all the img size
#Resize webcam Size