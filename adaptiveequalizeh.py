import cv2
from grabscreen import grab_screen
import time
import numpy as np

def equalizeAdH(img):
    # convert image from RGB to HSV
    img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    img_hsv[:, :, 2] = clahe.apply(img_hsv[:, :, 2])
    # convert image back from HSV to RGB
    img_output = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2RGB)

    return img_output

while (True):
    last_time = time.time()
    screen = grab_screen(region=(0, 40, 1000, 600))
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)

    adaptiveequalize = equalizeAdH(screen)

    cv2.imshow('Adaptive Equalize Histogram', adaptiveequalize)
    #cv2.imshow('window', screen)
    print("fps: {}".format(1 / (time.time() - last_time)))

    if cv2.waitKey(25) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break