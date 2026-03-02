from frameSplit import writeFENs
from chessConvert import getPNG
from videoCompile import compileVid

if __name__ == "__main__":
    video = "assets/bad apple.mp4"
    audio = "assets/bad apple.mp3"
    chessWrite = "assets/chess.txt"

    writeFENs(video, chessWrite)
    getPNG(chessWrite)
    compileVid(FENsrc="chessImgs", audio=audio, result="bad apple in chess.mp4")