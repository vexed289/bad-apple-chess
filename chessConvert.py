import chess
import chess.svg
import cairosvg

f = "chess.txt"

with open(f, 'r') as f: 
    fens=f.readlines()

for i, fen in enumerate(fens, start=1):
    fen = fen.strip()
    board = chess.Board(fen)
    svg = chess.svg.board(board)
    cairosvg.svg2png(bytestring=svg.encode(), write_to=f"chessImgs/frame{i}.png")
    print(f"frame{i}")

