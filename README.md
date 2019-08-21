# webcamCapture
Data capture tool for Jabra Panacast

## Getting started:
### Prereq:
stuff you need from pip:
```
pip install opencv-python
```
```
python3+
```
### Usage:
When running the script, you will need a total of 4 parameters.
1. Webcamcap.py
2. -cam
3. camNum
4. mode

Example Usages:
```
python WebcamCap.py -cam 1 -cycle
python WebcamCap.py -cam 0 -keypress
```
You must define the camera number and mode when running the script.

Modes:
```
-cycle: when prompted enter total number of images followed by time interval between.
This mode will allow you to set a cycle to take X number of images every Y seconds. Good tool to run and let it sit for some time.
```
```
-keypress: Given a live feed, choose when to save images.
This mode will allow you to press the space bar to choose when you want to take photos.
```

Additional Usage:
All your images will be saved in a folder called images for ease of zipping & organization.

