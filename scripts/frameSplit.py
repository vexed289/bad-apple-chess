import cv2
import numpy as np


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
    cv2.namedWindow("video")
    for frame in frames:
        cv2.imshow("video", frame)
        cv2.waitKey(33) # bcos 1000/30fps
    cv2.destroyAllWindows()

def downloadFrames(frames, format: str='png', destinationFolder: str='frames'):
    for frameCount, frame in enumerate(frames, start=1):
        cv2.imwrite(f"{destinationFolder}/frame{frameCount}.{format}", frame)

def convertChess(frames):
    for frame in frames:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        chars = np.where(gray != 0, 'r', 'Q')
        yield '/'.join(''.join(row) for row in chars) + " w - - 0 1"
    

def writeFENs(fname: str, write: str):
    print(f"FEN write started from {fname} to {write}")
    res = convertChess(convertFrames(getFrames(fname)))

    with open(write, 'w') as out:
        out.write('\n'.join(res))
    print("FENs written")
