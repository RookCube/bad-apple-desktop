import cv2
import numpy as np
import os
import shutil
import time
from PIL import Image

waitSecond = 1  # render time
dirPath = "C:/Users/timyr/Desktop"
blackImg = "black.png"
whiteImg = "white.png"


def delete_all():
    for filename in os.listdir(dirPath):
        if filename != "desktop.ini":
            try:
                os.remove(dirPath + "/" + filename)
            except:
                print("bruh")


def replace(where, whiteOrBlackMake):
    try:
        why = where + ".png"
        # check that image correct color
        if np.sum((Image.open(why).load())[0, 0]) + 100 > whiteOrBlackMake / 3:
            if whiteOrBlackMake > 255:
                print(why, "dont replace")
            else:
                shutil.copyfile(blackImg, why)
        else:
            print(why, "replace")
            if whiteOrBlackMake > 255:
                shutil.copyfile(whiteImg, why)
            else:
                print(why, "dont replace")
        # without check
        # if whiteOrBlackMake > 255:
        #     shutil.copyfile(whiteImg, why)
        # else:
        #     shutil.copyfile(blackImg, why)
    except:
        print("blink")


def make_matrix():
    for p in range(20):
        for k in range(10):
            shutil.copy(blackImg, dirPath + "/" + str(p) + "-" + str(k) + ".png")


ans = input("icon or image:")
delete_all()
make_matrix()
cap = cv2.VideoCapture('ha-3.mp4')
capOriginal = cv2.VideoCapture('ha.mp4')
# if ans == "icon":
#     while cap.isOpened():
#         ret, frame = cap.read()
#         if ret:
#             delete_all()
#             for i in range(len(frame)):
#                 for o in range(len(frame[i])):
#                     path = dirPath + "/" + str(i) + "-" + str(o)
#             cv2.imshow('bad apple', frame)
#
#             # Press Q on keyboard to  exit
#             if cv2.waitKey(25) & 0xFF == ord('q'):
#                 break
#
#         # Break the loop
#         else:
#             break
while cap.isOpened():
    ret, frame = cap.read()
    frameOr = capOriginal.read()[1]
    if ret:
        wait = time.time()
        for i in range(len(frame)):
            for o in range(len(frame[i])):
                path = dirPath + "/" + str(o) + "-" + str(i)
                replace(path, np.sum((frame[i])[o]))
        wait2 = time.time()
        trig = wait2-wait

        if trig < waitSecond:
            time.sleep(waitSecond - trig)
        else:
            print("bruh2")
            break
        image2 = cv2.putText(frameOr, str(trig), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2,
                             cv2.LINE_AA)  # put text on img
        cv2.imshow('bad apple', image2)

        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break
# When everything done, release the video capture object
cap.release()
capOriginal.release()
# Closes all the frames
cv2.destroyAllWindows()
