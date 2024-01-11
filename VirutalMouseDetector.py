"""
This project is build using many python packages.
Purpose: This project is build to create an virtual mouse which
         will move and click the objects as usual mouse.
"""
import cv2
import numpy as np
import HandTrackingModule as handTrack
import time
import autopy


class virtualMouse:

    def __init__(self):

        ##################################################
        # Width and height of the camera.
        widthCam, heightCam = 640, 480

        # width and height of screen.
        wScr, hScr = autopy.screen.size()

        # Frame reduction
        frameReduction = 100

        # smoothing the mouse.
        smoothening = 8

        ##################################################

        pLocationX, pLocationY = 0, 0
        cLocationX, cLoactionY = 0, 0
        cam = cv2.VideoCapture(0)
        cam.set(3, widthCam)
        cam.set(4, heightCam)

        detector = handTrack.handDetector(maxHands=1)
        pTime = 0

        while True:

            # 1. find the hand landmarks.
            success, image = cam.read()
            image = detector.findHands(image)
            lists, boundingBox = detector.findPosition(image)

            # 2. Get the tip of the index and the middle finger
            if len(lists) != 0:
                x1, y1 = lists[8][1:]
                x2, y2 = lists[12][1:]

                # 3. check which fingers are up
                fingers = detector.fingersUp()

                cv2.rectangle(image, (frameReduction, frameReduction),
                              (widthCam - frameReduction, heightCam - frameReduction),
                              (255, 0, 255), 2)

                # 4. when index finger then moving mode.
                if fingers[1] == 1 and fingers[2] == 0:
                    # 5. convert the coordinates.
                    x3 = np.interp(x1, (frameReduction, widthCam - frameReduction), (0, wScr))
                    y3 = np.interp(y1, (frameReduction, heightCam - frameReduction), (0, hScr))

                    # 6. smoothen the values
                    cLocationX = pLocationX + (x3 - pLocationX) / smoothening
                    cLoactionY = pLocationY + (y3 - pLocationY) / smoothening

                    # 7. move mouse.
                    autopy.mouse.move(wScr - cLocationX, cLoactionY)
                    cv2.circle(image, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
                    pLocationX, pLocationY = cLocationX, cLoactionY

                # 8. when index & middle finger then clicking mode.
                if fingers[1] == 1 and fingers[2] == 1:
                    # 9. find distance between fingers.
                    # length, img, lineInfo = detector.findDistance(8, 12, image)
                    # if length < 40:
                    #     cv2.circle(image, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                    #
                    #     # 10. click mouse if distance is short.
                    autopy.mouse.click()

            # 11. frame rate.
            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            cv2.putText(image, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

            # 12. display
            cv2.imshow("Image", image)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break


def main():
    vm = virtualMouse()


if __name__ == "__main__":
    main()
