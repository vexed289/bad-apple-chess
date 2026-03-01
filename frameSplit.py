import cv2

def convertFrame(frame): # convert frame to size 8x8
    return cv2.resize(frame, (8, 8))

def readFrames(): # read frames and put in file
    
    video = cv2.VideoCapture("bad apple.mp4")

    frameCount = 1
    success = True
    #fps = video.get(cv2.CAP_PROP_FPS)
    #delay = int(1000 / fps)
    while success:
        success, frame = video.read()
        #cv2.namedWindow("video")
        if success:
            """
            cv2.imshow("video", frame)
            cv2.waitKey(delay)
            cv2.destroyWindow(f"frame{frameCount}")
            """
            cv2.imwrite(f"frames/frame{frameCount}.png", frame)
            frameCount+=1

    video.release()
    #cv2.destroyAllWindows()
    return

def showFrames():
    video = cv2.VideoCapture("bad apple.mp4")

    frameCount = 1
    success = True
    fps = video.get(cv2.CAP_PROP_FPS)
    delay = int(1000 / fps)
    cv2.namedWindow("video")
    while success:
        success, frame = video.read()
        if success:
            cv2.imshow("video", frame)
            cv2.waitKey(delay)

            frameCount+=1
    cv2.destroyAllWindows()
readFrames()