import cv2

def getFrames(path: str):
    video = cv2.VideoCapture(path)
    if not video.isOpened():
        raise FileNotFoundError()
    
    try:
        while True:
            success, frame = video.read()
            if not success:
                break
            yield frame
    finally:
        video.release()


def convertFrames(frames):
    for frame in frames:
        yield cv2.resize(frame, (8, 8))

def showFrames(frames):
    video = cv2.namedWindow("video")
    for frame in frames:
        cv2.imshow("video", frame)
        cv2.waitKey(16) # bcos 1000/60fps

def downloadFrames(frames):
    for frameCount, frame in enumerate(frames, start=1):
        cv2.imwrite(f"frames/frame{frameCount}.png", frame)
