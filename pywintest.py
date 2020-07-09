import cv2
from grabscreen import grab_screen
import time

while (True):
    last_time = time.time()
    screen = grab_screen(region=(0, 40, 1000, 600))
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
    cv2.imshow('window', screen)
    print("fps: {}".format(1 / (time.time() - last_time)))

    if cv2.waitKey(25) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break