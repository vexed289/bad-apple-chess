import subprocess

subprocess.run([
    "ffmpeg",
    "-framerate", "30",
    "-i", "chessImgs/frame%d.png",
    "-i", "bad apple.mp3",
    "-c:v", "libx264",
    "-pix_fmt", "yuv420p",
    "-c:a", "aac",
    "-shortest",
    "bad apple in chess.mp4"
])

# just put this here for documentations sake