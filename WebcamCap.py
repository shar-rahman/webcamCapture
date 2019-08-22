import cv2
import sys
import os
import time

#TO-DO
# - live view for cycle mode

# show args
def printUsage():
    print("\nUsage: python WebcamCap.py -cam 1 -cycle")
    print("       python WebCamCap.py -cam 0 -keypress")
    print("       python WebCamCap.py -cam <num> <mode -keypress or -cycle>")
    print("Required params:")
    print("\n-cam       :set camera number (panacast is usually 0 or 1)")
    print("           usage: -cam 2\n")
    print("----------")
    print("-cycle     :engange cycle mode")
    print("           usage: -cycle\n")
    print("        OR\n")
    print("-keypress  :engage keypress mode")
    print("           usage: press <space> to capture an image instead of time incrementing")
    print("----------")
    print("\nMust select one of two modes: -cycle or -keypress!\n")
    exit(-1)

# input validation
if len(sys.argv) is 1 or len(sys.argv) > 4: printUsage()
if sys.argv[1] != "-cam": printUsage()
if int(sys.argv[2]) < 0 or int(sys.argv[2]) > 10: printUsage()
if sys.argv[3] != "-keypress" and sys.argv[3] != "-cycle": printUsage()

# check if cam exists
isLive = True
try:
    camNum = int(sys.argv[2])
except Exception as e:
    print("Camera number not found")
    isLive = False

Menu = True
# mode selection
if sys.argv[3] == "-keypress": 
    usingCycle = False
    cycles = -2
    timeInterval = 0
    print("Press <space> to take a photo, <esc> to exit.\n")
elif sys.argv[3] == "-cycle":
    usingCycle = True
    print("Live view not available for cycle mode.")
    print("Enter 5 10 to take a photo every 10 seconds for a total of 5 photos\n")
    while Menu:
        userInput = input("Enter # of images followed by time interval between (seconds): ")
        cycleUsage = userInput.split()
        cycles = int(cycleUsage[0])
        timeInterval = int(cycleUsage[1])
        if cycles < 1 or timeInterval < 1:
            print("Invalid input try for cycle or time interval. Must be positive integer above 0.")
        else: Menu = False
else: printUsage()



cap = cv2.VideoCapture(camNum, cv2.CAP_DSHOW)
vidH = 1080
vidW = 3840
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, vidH)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, vidW)
cv2.namedWindow("capture", cv2.WINDOW_NORMAL)
cv2.resizeWindow("capture", (960, 270))
#if cam exists, will output vid to window

if isLive:
    # create image folder
    if not os.path.exists("images/"): os.makedirs("images/")

    intervalNum = 0
    holdTime = int(time.time())
    while cap.isOpened() and cycles != intervalNum:
        ret,image = cap.read()
        ret,save = cap.read()
        if not ret: break
        if usingCycle: # -cycle mode
            saveName = "images/%d_%d.png" % (holdTime, intervalNum)
            cv2.imwrite(saveName, image)
            cv2.imshow("capture", image)
            print("Image %s saved!" % saveName)
            intervalNum = intervalNum + 1
            cv2.waitKey(timeInterval*1000)
        else: # -keypress mode
            key = cv2.waitKey(1)
            if key % 256 == 32:  
                saveName = "images/%d_%d.png" % (holdTime, intervalNum)
                cv2.imwrite(saveName, save)
                print("Image %s saved!" % saveName)
                intervalNum = intervalNum + 1
            if key % 256 == 27: break
        cv2.imshow("capture", cv2.resize(image, (vidW, vidH)))

print("Closing Camera feed")
cap.release()
print("Closing windows")
cv2.destroyAllWindows()