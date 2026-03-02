import subprocess
def compileVid(FENsrc: str, audio: str, result: str):

    subprocess.run([
        "ffmpeg",
        "-framerate", "30",
        "-i", f"{FENsrc}/frame%d.png",
        "-i", f"{audio}",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-shortest",
        f"{result}"
    ])
    print(f"video compiled to {result}")
# just put this here for documentations sake