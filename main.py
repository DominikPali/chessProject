from tkinter import *
letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8"]
pieces_on_the_board = [[None for _ in range(8)] for _ in range(8)]
piece_items_in_canvas = [[None for _ in range(8)] for _ in range(8)]
square_items_in_canvas = [[None for _ in range(8)] for _ in range(8)]
square_size = 40
drag_data = {"item":None, "x":None, "y":None, "startX":None, "startY":None}

def return_name_color_of_the_piece(piece_symbol):
    if piece_symbol == "0x265A": return "blackKing"
    if piece_symbol == "0x265B": return "blackQueen"
    if piece_symbol == "0x265C": return "blackRook"
    if piece_symbol == "0x265D": return "blackBishop"
    if piece_symbol == "0x265E": return "blackKnight"
    if piece_symbol == "0x265F": return "blackPawn"
    if piece_symbol == "0x2654": return "whiteKing"
    if piece_symbol == "0x2655": return "whiteQueen"
    if piece_symbol == "0x2656": return "whiteRook"
    if piece_symbol == "0x2657": return "whiteBishop"
    if piece_symbol == "0x2658": return "whiteKnight"
    if piece_symbol == '0x2659': return "whitePawn"

def return_top_left_tip_of_the_square(x,y):
    right_x = 0
    right_y = 0
    for i in range(9):
        if i * square_size <= x < i * square_size + square_size: right_x = i * square_size
    for j in range(9):
        if j * square_size <= y < j * square_size + square_size: right_y = j * square_size
    return right_x, right_y
def return_x_y_of_the_square(x_coordinates, y_coordinates):
    x = 0
    y = 0
    for i in range(9):
        if i * square_size <= x_coordinates < i * square_size + square_size: x = i
    for j in range(9):
        if j * square_size <= y_coordinates < j * square_size + square_size: y = 9-j
    return x, y


def change_piece_on_the_square(x, y, piece_symbol):
    piece_name = return_name_color_of_the_piece(piece_symbol)
    canvas.itemconfig(piece_items_in_canvas[x-1][y-1], text=piece_symbol, font=('Arial', int(square_size/2)), tags=("piece", x, y, piece_name))
    canvas.tag_bind("piece", '<ButtonPress-1>', on_drag_start)
    canvas.tag_bind("piece", '<B1-Motion>', on_drag_motion)
    canvas.tag_bind("piece", '<ButtonRelease-1>', on_drag_stop)

class Pawn():
    def __init__(self, color, x_L, y_N):
        self.color = color
        self.x_L = x_L
        self.y_N = y_N
        self.piece_id = piece_items_in_canvas[x_L - 1][y_N - 1]
        if color == "white":
            self.symbol = chr(0x2659)
        else:
            self.symbol = chr(0x265F)
        change_piece_on_the_square(x_L, y_N, self.symbol)


class Bishop():
    def __init__(self, color, x_L, y_N):
        self.color = color
        self.x_L = x_L
        self.y_N = y_N
        if color == "white":
            self.symbol = chr(0x2657)
        else:
            self.symbol = chr(0x265D)
        change_piece_on_the_square(x_L, y_N, self.symbol)

class Knight():
    def __init__(self, color, x_L, y_N):
        self.color = color
        self.x_L = x_L
        self.y_N = y_N
        if color == "white":
            self.symbol = chr(0x2658)
        else:
            self.symbol = chr(0x265E)
        change_piece_on_the_square(x_L, y_N, self.symbol)

class Rook():
    def __init__(self, color, x_L, y_N):
        self.color = color
        self.x_L = x_L
        self.y_N = y_N
        if color == "white":
            self.symbol = chr(0x2656)
        else:
            self.symbol = chr(0x265C)
        change_piece_on_the_square(x_L, y_N, self.symbol)

class Queen():
    def __init__(self, color, x_L, y_N):
        self.color = color
        self.x_L = x_L
        self.y_N = y_N
        if color == "white":
            self.symbol = chr(0x2655)
        else:
            self.symbol = chr(0x265B)
        change_piece_on_the_square(x_L, y_N, self.symbol)

class King():
    def __init__(self, color, x_L, y_N):
        self.color = color
        self.x_L = x_L
        self.y_N = y_N
        if color == "white":
            self.symbol = chr(0x2654)
        else:
            self.symbol = chr(0x265A)
        change_piece_on_the_square(x_L, y_N, self.symbol)

def start_function():
    for i in range(8):
        pawnW = Pawn("white",i+1, 2)
        pieces_on_the_board[i][1] = pawnW
        pawnB = Pawn("black", i+1, 7)
        pieces_on_the_board[i][7] = pawnB
    rookW1 = Rook("white",1,1)
    pieces_on_the_board[0][0] = rookW1
    rookW2 = Rook("white", 8, 1)
    pieces_on_the_board[7][0] = rookW2
    rookB1 = Rook("black", 1, 8)
    pieces_on_the_board[0][7] = rookB1
    rookB2 = Rook("black", 8, 8)
    pieces_on_the_board[7][7] = rookB2

    knightW1 = Knight("white",2,1)
    pieces_on_the_board[1][0] = knightW1
    knightW2 = Knight("white", 7, 1)
    pieces_on_the_board[6][0] = knightW2
    knightB1 = Knight("black", 2, 8)
    pieces_on_the_board[1][7] = knightB1
    knightB2 = Knight("black", 7, 8)
    pieces_on_the_board[6][7] = knightB2

    bishopW1 = Bishop("white",3,1)
    pieces_on_the_board[3][0] = bishopW1
    bishopW2 = Bishop("white", 6, 1)
    pieces_on_the_board[5][0] = bishopW2
    bishopB1 = Bishop("black", 3, 8)
    pieces_on_the_board[2][7] = bishopB1
    bishopB2 = Bishop("black", 6, 8)
    pieces_on_the_board[5][7] = bishopB2

    queenW = Queen("white", 4, 1)
    pieces_on_the_board[3][0] = queenW
    queenB = Queen("black", 4, 8)
    pieces_on_the_board[3][7] = queenB

    kingW = King("white", 5, 1)
    pieces_on_the_board[4][0] = kingW
    kingB = King("black", 5, 8)
    pieces_on_the_board[4][7] = kingB


window = Tk()
window.attributes('-fullscreen', True)
window.configure(bg="#4a4a4a")

titleLabel = Label(window, text="Chess", font=("Impact", 100), fg="#fff", bg="#4a4a4a")
titleLabel.pack(anchor="n", pady=50)

chessLabel = Label(window, bg="#4a4a4a")
chessLabel.pack(anchor="n", pady=50)

materialLabelTop = Label(chessLabel, text="Here white's captured pieces will be shown", font=30)
materialLabelTop.pack()

boardLabels = Label(chessLabel, bg="#4a4a4a")
boardLabels.pack()

def create_chess_board():
    global square_items_in_canvas
    global piece_items_in_canvas
    for i in range(8):
        x0 = i * square_size + square_size
        x1 = x0 + square_size
        y0 = 0
        y1 = y0 + square_size
        canvas.create_rectangle(x0, y0, x1, y1, fill="#fff")
        canvas.create_text(x1-int(square_size/2), y1-int(square_size/2), font=("Arial", int(square_size/2)), text=letters[i])
    for j in range(8):
        x0 = 0
        x1 = x0 + square_size
        y0 = j * square_size + square_size
        y1 = y0 + square_size
        canvas.create_rectangle(x0, y0, x1, y1, fill="#fff")
        canvas.create_text(x1 - square_size / 2, y1 - square_size / 2, font=("Arial", int(square_size/2)), text=8-j)
    for i in range(8):
        for j in range(8):
            x0 = i * square_size + square_size
            y0 = j * square_size + square_size
            x1 = x0 + square_size
            y1 = y0 + square_size

            color = "#b5b897" if (i+j) % 2 == 0 else "#484a3c"

            square_item = canvas.create_rectangle(x0, y0, x1, y1, fill=color, tags="square")
            square_items_in_canvas[i][7-j] = square_item
            piece_item = canvas.create_text(x0+int(square_size/2), y0 + int(square_size/2), text=" ")
            piece_items_in_canvas[i][7-j] = piece_item
def on_drag_start(event):
    global drag_data
    closest_item = canvas.find_closest(event.x, event.y)[0]
    item_tags = canvas.gettags(closest_item)
    if "square" in item_tags:
        col = (event.x - square_size) // square_size
        row = 7 - (event.y - square_size) // square_size
        piece_item = piece_items_in_canvas[col + 1][8 - row]
        if piece_item:
            closest_item = piece_item
            item_tags = canvas.gettags(closest_item)
    if "piece" in item_tags:
        drag_data['item'] = closest_item
        drag_data["x"] = event.x
        drag_data["y"] = event.y
        drag_data["startX"], drag_data["startY"] = return_top_left_tip_of_the_square(event.x, event.y)
        drag_data["startX"] += square_size/2
        drag_data["startY"] += square_size/2

    canvas.tag_raise(closest_item)
    print("x value: " + str(event.x))
    print("y value: " + str(event.y))
    print(return_x_y_of_the_square(event.x, event.y))

def on_drag_motion(event):
    if drag_data["item"]:
        deltaX = event.x - drag_data["x"]
        deltaY = event.y - drag_data["y"]
        canvas.move(drag_data["item"], deltaX, deltaY)
        drag_data["x"] = event.x
        drag_data["y"] = event.y
    canvas.tag_raise(drag_data["item"])
def on_drag_stop(event):
    global drag_data
    canvas.coords(drag_data["item"], drag_data["startX"], drag_data["startY"])

    canvas.tag_raise(drag_data["item"])
    drag_data = {"item": None, "x" : None, "y" : None, "startX" : None, "startY" : None}

canvas = Canvas(boardLabels, height=square_size*9)
canvas.pack()

create_chess_board()
start_function()
window.mainloop()