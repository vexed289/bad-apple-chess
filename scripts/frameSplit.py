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
    video = cv2.namedWindow("video")
    for frame in frames:
        cv2.imshow("video", frame)
        cv2.waitKey(16) # bcos 1000/60fps

def downloadFrames(frames, format: str='png'):
    for frameCount, frame in enumerate(frames, start=1):
        cv2.imwrite(f"frames/frame{frameCount}.{format}", frame)

def convertChess(frame: cv2.typing.MatLike):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    chars = np.where(gray != 0, 'r', 'Q')
    return '/'.join(''.join(row) for row in chars) + " w - - 0 1"

#downloadFrames(getFrames("bad apple.mp4"))

converted = convertFrames(getFrames("bad apple.mp4"))

res = []

for item in converted:
    res.append(convertChess(item))

with open("chess.txt", 'w') as out:
    out.write('\n'.join(res))
