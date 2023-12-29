import cv2
import time
import handtrackingmodule as htm
import random

win = 0
losses = 0
tie = 0
wCam, hCam = 1600, 900

pTime = 0
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
initialTime = 0
timer = 0
stateResult = False
startGame = False

detector = htm.handDetector(detectionCon=0.75)  # handtracking
tipIds = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    # print(lmList)

    movelist = ["ROCK", "SCISSORS", "PAPER", "Invalid"]
    computermovelist = ["ROCK", "SCISSORS", "PAPER"]


    cv2.putText(img, f'ROCK PAPER SCISSORS  ', (450, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)
    cv2.putText(img, f'GAME SCORES', (500, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)



    if startGame:



        if stateResult is False:
            timer = time.time() - initialTime
            cv2.putText(img, str(int(timer)), (605, 435), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)

            if timer > 3:
                stateResult = True
                timer = 0





    # checking if fingers are opened or closed
                if len(lmList) != 0:
                    fingers = []
                    if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:  # lmlist[thumb no][y postion]
                        fingers.append(1)
                    else:
                        fingers.append(0)
                    for Id in range(1, 5):
                        if lmList[tipIds[Id]][2] < lmList[tipIds[Id] - 2][2]:  # lmlist[other 4 fingers no][y postion]
                            fingers.append(1)
                        else:
                            fingers.append(0)
                        # print(fingers)
                    totalFingers = fingers.count(1)
                    print(totalFingers)








                    if totalFingers == 2 or totalFingers == 3:
                        playermove = movelist[1]
                        
                    elif totalFingers == 5:
                        playermove = movelist[2]

                    elif totalFingers == 0:
                        playermove = movelist[0]

                    else:
                        print("invalid")
                        playermove = movelist[3]


                    if computermove == playermove:
                        print("its a tie ")
                        tie = tie + 1
                    elif playermove == "ROCK" and computermove == "SCISSORS":
                        print("you win")
                        win = win + 1
                    elif playermove == "ROCK" and computermove == "PAPER":
                        print("YOU LOSE ")
                        losses = losses + 1
                    elif playermove == "PAPER" and computermove == "ROCK":
                        print("you win ")
                        win = win + 1
                    elif playermove == "PAPER" and computermove == "SCISSORS":
                        print("you lose")
                        losses = losses + 1
                    elif playermove == "SCISSORS" and computermove == "PAPER":
                        print("you win")
                        win = win + 1

                    elif playermove == "SCISSORS" and computermove == "ROCK":
                        print("you lose")
                        losses = losses + 1
                    elif playermove == "Invalid":
                        print("invalid you lose")
                        losses = losses + 1



    if stateResult:
        cv2.putText(img, f'WIN: {win}  LOSE: {losses}  TIES: {tie}', (450, 150), cv2.FONT_HERSHEY_COMPLEX, 1,
                    (255, 0, 0), 2)
        cv2.putText(img, f'BOT CHOICE: {computermove}', (900, 700), cv2.FONT_HERSHEY_COMPLEX, 1,
                    (255, 0, 0), 2)
        cv2.putText(img, f'YOUR CHOICE: {playermove}',(40, 700), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)











    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'fps: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)
    cv2.imshow("Image", img)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

    if key == ord('s'):
        startGame = True
        initialTime = time.time()
        stateResult = False
        computermove = random.choice(computermovelist)


cap.release()
cv2.destroyAllWindows()





