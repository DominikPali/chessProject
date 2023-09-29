from tkinter import *
letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8"]
pieces_on_the_board_objects = [[None for _ in range(8)] for _ in range(8)]
piece_items_in_canvas = [[None for _ in range(8)] for _ in range(8)]
square_items_in_canvas = [[None for _ in range(8)] for _ in range(8)]
pieces_on_the_board = [[None for _ in range(8)] for _ in range(8)]
square_size = 40
drag_data = {"item":None, "x":None, "y":None, "startX":None, "startY":None}
kings_delta_x_y = [(0, 1),(1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

def add_to_list_of_possible_moves(x,y, deltaX, deltaY):
    if 0 < x + deltaX < 9 and 0 < y + deltaY < 9:
        pieces_on_the_board_objects[x - 1][y - 1].possible_moves.append((deltaX, deltaY))
    print(pieces_on_the_board_objects[4][6])
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
    if piece_symbol == "0x2659": return "whitePawn"
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
def change_piece_on_the_square(x, y, piece_symbol, setting_pieces, startX, startY, color):
    global pieces_on_the_board
    piece_name = return_name_color_of_the_piece(piece_symbol)
    canvas.itemconfig(piece_items_in_canvas[x - 1][y - 1], text=piece_symbol, font=('Arial', int(square_size / 2)),
                      tags=("piece", x, y, piece_name, color))
    pieces_on_the_board[x-1][y-1] = piece_name
    if setting_pieces and startX is None and startY is None:
        canvas.tag_bind("piece", '<ButtonPress-1>', on_drag_start)
        canvas.tag_bind("piece", '<B1-Motion>', on_drag_motion)
        canvas.tag_bind("piece", '<ButtonRelease-1>', on_drag_stop)
    else:
        canvas.itemconfig(piece_items_in_canvas[startX - 1][startY - 1], text=" ", font=('Arial', int(square_size / 2)),
                          tags=(x, y))
        pieces_on_the_board_objects[x-1][y-1] = pieces_on_the_board_objects[startX-1][startY-1]
        pieces_on_the_board_objects[x-1][y-1].x_L = x
        pieces_on_the_board_objects[x-1][y-1].y_N = y
        pieces_on_the_board_objects[startX - 1][startY - 1] = None
class Pawn():
    def __init__(self, color, x_L, y_N):
        self.color = color
        self.x_L = x_L
        self.y_N = y_N
        self.piece_id = piece_items_in_canvas[x_L - 1][y_N - 1]
        self.possible_moves = []
        if self.color == "white":
            self.symbol = chr(0x2659)
        else:
            self.symbol = chr(0x265F)
        change_piece_on_the_square(x_L, y_N, self.symbol, True, None, None, self.color)
    def define_possible_moves(self):
        try:
            if self.color == "white":
                if pieces_on_the_board_objects[self.x_L + 0 - 1][self.y_N + 1 - 1] is None:
                    add_to_list_of_possible_moves(self.x_L, self.y_N, 0, 1)
                    if self.y_N == 2:
                        if pieces_on_the_board_objects[self.x_L + 0 - 1][self.y_N + 2 - 1] is None:
                            add_to_list_of_possible_moves(self.x_L, self.y_N, 0, 2)
                if pieces_on_the_board_objects[self.x_L - 1 - 1][self.y_N + 1 - 1] is not None:
                    if pieces_on_the_board_objects[self.x_L - 1 - 1][self.y_N + 1 - 1].color == "black":
                        add_to_list_of_possible_moves(self.x_L, self.y_N, -1, 1)
                if pieces_on_the_board_objects[self.x_L + 1 - 1][self.y_N + 1 - 1] is not None:
                    if pieces_on_the_board_objects[self.x_L + 1 - 1][self.y_N + 1 - 1].color == "black":
                        add_to_list_of_possible_moves(self.x_L, self.y_N, 1, 1)

            elif self.color == "black":
                if pieces_on_the_board_objects[self.x_L + 0 - 1][self.y_N - 1 - 1] is None:
                    add_to_list_of_possible_moves(self.x_L, self.y_N, 0, -1)
                    if self.y_N == 7:
                        if pieces_on_the_board_objects[self.x_L + 0 - 1][self.y_N - 2 - 1] is None:
                            add_to_list_of_possible_moves(self.x_L, self.y_N, 0, -2)
                if pieces_on_the_board_objects[self.x_L - 1 - 1][self.y_N - 1 - 1] is not None:
                    if pieces_on_the_board_objects[self.x_L - 1 - 1][self.y_N - 1 - 1].color == "white":
                        add_to_list_of_possible_moves(self.x_L, self.y_N, -1, -1)
                if pieces_on_the_board_objects[self.x_L + 1 - 1][self.y_N - 1 - 1] is not None:
                    if pieces_on_the_board_objects[self.x_L + 1 - 1][self.y_N - 1 - 1].color == "white":
                        add_to_list_of_possible_moves(self.x_L, self.y_N, 1, -1)
        except IndexError:
            pass


class Bishop():
    def __init__(self, color, x_L, y_N):
        self.color = color
        self.x_L = x_L
        self.y_N = y_N
        self.possible_moves = []
        if color == "white":
            self.symbol = chr(0x2657)
        else:
            self.symbol = chr(0x265D)
        change_piece_on_the_square(x_L, y_N, self.symbol, True, None, None, self.color)

class Knight():
    def __init__(self, color, x_L, y_N):
        self.color = color
        self.x_L = x_L
        self.y_N = y_N
        self.possible_moves = []
        if color == "white":
            self.symbol = chr(0x2658)
        else:
            self.symbol = chr(0x265E)
        change_piece_on_the_square(x_L, y_N, self.symbol, True, None, None, self.color)

class Rook():
    def __init__(self, color, x_L, y_N):
        self.color = color
        self.x_L = x_L
        self.y_N = y_N
        self.possible_moves = []
        if color == "white":
            self.symbol = chr(0x2656)
        else:
            self.symbol = chr(0x265C)
        change_piece_on_the_square(x_L, y_N, self.symbol, True, None, None, self.color)

class Queen():
    def __init__(self, color, x_L, y_N):
        self.color = color
        self.x_L = x_L
        self.y_N = y_N
        self.possible_moves = []
        if color == "white":
            self.symbol = chr(0x2655)
        else:
            self.symbol = chr(0x265B)
        change_piece_on_the_square(x_L, y_N, self.symbol, True, None, None, self.color)

class King():
    def __init__(self, color, x_L, y_N):
        self.color = color
        self.x_L = x_L
        self.y_N = y_N
        self.possible_moves = []
        if color == "white":
            self.symbol = chr(0x2654)
        else:
            self.symbol = chr(0x265A)
        change_piece_on_the_square(x_L, y_N, self.symbol, True, None, None, self.color)

    def define_possible_moves(self):
        for tuple in kings_delta_x_y:
            deltaX, deltaY = tuple
            try:
                if (pieces_on_the_board_objects[self.x_L + deltaX - 1][self.y_N + deltaY - 1] is None
                    or pieces_on_the_board_objects[self.x_L + deltaX - 1][self.y_N + deltaY - 1] is not None
                    and pieces_on_the_board_objects[self.x_L + deltaX - 1][self.y_N + deltaY - 1].color != self.color):
                    add_to_list_of_possible_moves(self.x_L, self.y_N, deltaX, deltaY)
            except IndexError:
                pass




def start_function():
    for i in range(8):
        pawnW = Pawn("white",i+1, 2)
        pieces_on_the_board_objects[i][1] = pawnW
        pawnB = Pawn("black", i+1, 7)
        pieces_on_the_board_objects[i][6] = pawnB
    rookW1 = Rook("white",1,1)
    pieces_on_the_board_objects[0][0] = rookW1
    rookW2 = Rook("white", 8, 1)
    pieces_on_the_board_objects[7][0] = rookW2
    rookB1 = Rook("black", 1, 8)
    pieces_on_the_board_objects[0][7] = rookB1
    rookB2 = Rook("black", 8, 8)
    pieces_on_the_board_objects[7][7] = rookB2

    knightW1 = Knight("white",2,1)
    pieces_on_the_board_objects[1][0] = knightW1
    knightW2 = Knight("white", 7, 1)
    pieces_on_the_board_objects[6][0] = knightW2
    knightB1 = Knight("black", 2, 8)
    pieces_on_the_board_objects[1][7] = knightB1
    knightB2 = Knight("black", 7, 8)
    pieces_on_the_board_objects[6][7] = knightB2

    bishopW1 = Bishop("white",3,1)
    pieces_on_the_board_objects[2][0] = bishopW1
    bishopW2 = Bishop("white", 6, 1)
    pieces_on_the_board_objects[5][0] = bishopW2
    bishopB1 = Bishop("black", 3, 8)
    pieces_on_the_board_objects[2][7] = bishopB1
    bishopB2 = Bishop("black", 6, 8)
    pieces_on_the_board_objects[5][7] = bishopB2

    queenW = Queen("white", 4, 1)
    pieces_on_the_board_objects[3][0] = queenW
    queenB = Queen("black", 4, 8)
    pieces_on_the_board_objects[3][7] = queenB

    kingW = King("white", 5, 1)
    pieces_on_the_board_objects[4][0] = kingW
    kingB = King("black", 5, 8)
    pieces_on_the_board_objects[4][7] = kingB


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
        canvas.create_text(x1 - int(square_size/2), y1 - int(square_size/2), font=("Arial", int(square_size/2)), text=8-j)
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
    row, col = return_x_y_of_the_square(event.x, event.y)
    closest_item = piece_items_in_canvas[row-1][col-1]
    item_tags = canvas.gettags(closest_item)
    if "piece" in item_tags:
        drag_data["item"] = closest_item
        drag_data["x"] = event.x
        drag_data["y"] = event.y
        drag_data["startX"], drag_data["startY"] = return_top_left_tip_of_the_square(event.x, event.y)
        drag_data["startX"] += square_size/2
        drag_data["startY"] += square_size/2
    canvas.tag_raise(closest_item)

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
    change_piece = False
    x, y = return_x_y_of_the_square(drag_data["x"], drag_data["y"])
    print(str(x) + "  is x")
    print(str(y) + "  is y")
    startX, startY = return_x_y_of_the_square(drag_data["startX"], drag_data["startY"])
    print(str(startX) + "  is startX")
    print(str(startY) + "  is startY")
    if x != startX or y != startY:
        pieces_on_the_board_objects[startX-1][startY-1].define_possible_moves()
        for tuple in pieces_on_the_board_objects[startX-1][startY-1].possible_moves:
            deltaX, deltaY = tuple
            print(str(deltaX) + " is deltaX    " + str(deltaY) + " is deltaY")
            if x == startX + deltaX and y == startY + deltaY:
                change_piece = True
    if change_piece:
        change_piece_on_the_square(x, y, pieces_on_the_board_objects[startX-1][startY-1].symbol, False,
                                startX, startY, pieces_on_the_board_objects[startX-1][startY-1].color)
        pieces_on_the_board_objects[x - 1][y - 1].possible_moves = []
        canvas.tag_raise(piece_items_in_canvas[x-1][y-1])
    drag_data = {"item": None, "x" : None, "y" : None, "startX" : None, "startY" : None}

canvas = Canvas(boardLabels, height=square_size*9)
canvas.pack()

create_chess_board()
start_function()
window.mainloop()