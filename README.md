# bad-apple-chess

We need to split this into 3 parts:
 - Getting the bad apple video, splitting into frames, converting into 8x8 grid
 - Converting this 8x8 grid into a FEN format by finding which piece to use for which part of the grid
 - Displaying this, and merging all the images together into a video

Part 1:\
~To get the bad apple video, I'll use a yt-dlp wrapper I made a while back and just put the mp4 into this folder~ (done)\
~Then to split it into frames, I could use cv2 like I did in another project. I'll try 5 fps for now because I'm just testing, but I'll increase it later.~ (done but i forgot the 5 fps bit oops)\
~I put all these frames as png/jpg/whatever into a folder called frames~ (done)\
~Then I use some interpolation or whatever to scale each image to 8x8~ (done)\
Since all pixels are black and white, I'll just convert it into binary where 1 is black and 0 is white and put them into a folder called binary.

Part 2:\
With the binary approach this seems easier because I'll just use the largest piece for both black and white\
Then I just add the extra information for the FEN and either make it valid for chess.com (needs king of both colours) or use something else\
After spending 5 seconds searching stuff up, I think I can use https://www.redhotpawn.com/chess/chess-fen-viewer.php and just use their download feature as that will make part 3 easier\
But their background is ugly so I might find something else later

Part 3:\
Merge downloaded pngs together. I don't want to do it manually so I'll try find a good way of doing it automatically
