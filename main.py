import copy
from tkinter import *
letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
numbers = ["1", "2", "3", "4", "5", "6", '7', "8"]
pieces_on_the_board_objects = [[None for _ in range(8)] for _ in range(8)]
pieces_on_the_board_objects_simulation = None
piece_items_in_canvas = [[None for _ in range(8)] for _ in range(8)]
square_items_in_canvas = [[None for _ in range(8)] for _ in range(8)]
square_size = 40
drag_data = {"item": None, "x": None, "y": None, "startX": None, "startY": None, "rectangle": None}
black_pieces = []
white_pieces = []
pieces_vertical_y_plus = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)]
pieces_vertical_y_minus = [(0, -1), (0, -2), (0, -3), (0, -4), (0, -5), (0, -6), (0, -7), ]
pieces_horizontal_x_plus = [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]
pieces_horizontal_x_minus = [(-1, 0), (-2, 0), (-3, 0), (-4, 0), (-5, 0), (-6, 0), (-7, 0)]
pieces_diagonal_y_plus_x_plus = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)]
pieces_diagonal_y_minus_x_plus = [(1, -1), (2, -2), (3, -3), (4, -4), (5, -5), (6, -6), (7, -7)]
pieces_diagonal_y_plus_x_minus = [(-1, 1), (-2, 2), (-3, 3), (-4, 4), (-5, 5), (-6, 6), (-7, 7)]
pieces_diagonal_y_minus_x_minus = [(-1, -1), (-2, -2), (-3, -3), (-4, -4), (-5, -5), (-6, -6), (-7, -7)]
kings_delta_x_y = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
knight_delta_x_y = [(2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (1, 2), (-1, 2)]
squares_attacked_by_white_pieces = [[False for _ in range(8)] for _ in range(8)]
squares_attacked_by_black_pieces = [[False for _ in range(8)] for _ in range(8)]
previous_moves = []
text_letters_canvas_items = [None, None, None, None, None, None, None, None]
text_numbers_canvas_items = [None, None, None, None, None, None, None, None]
who_is_on_bottom_of_the_board = "white"
turn = "white"
chosen_piece = None
make_moves = True


def add_to_list_of_possible_moves_and_attacked_squares(x, y, deltaX, deltaY, pieces_on_the_board_objects_data):
    global squares_attacked_by_white_pieces
    global squares_attacked_by_black_pieces
    global pieces_on_the_board_objects
    global pieces_on_the_board_objects_simulation
    if 0 < x + deltaX < 9 and 0 < y + deltaY < 9:
        pieces_on_the_board_objects_data[x - 1][y - 1].possible_moves.append((deltaX, deltaY))
        if pieces_on_the_board_objects[x - 1][y - 1].color == "white":
            if pieces_on_the_board_objects[x - 1][y - 1].type == "Pawn":
                if deltaX == 0:
                    pass
                elif deltaX != 0:
                    squares_attacked_by_white_pieces[x + deltaX - 1][y + deltaY - 1] = True
            else:
                squares_attacked_by_white_pieces[x + deltaX - 1][y + deltaY - 1] = True
        elif pieces_on_the_board_objects[x - 1][y - 1].color == "black":
            if pieces_on_the_board_objects[x - 1][y - 1].type == "Pawn":
                if deltaX == 0:
                    pass
                elif deltaX != 0:
                    squares_attacked_by_black_pieces[x + deltaX - 1][y + deltaY - 1] = True
            else:
                squares_attacked_by_black_pieces[x + deltaX - 1][y + deltaY - 1] = True


def add_to_attacked_squares_only(x, y, deltaX, deltaY):
    global squares_attacked_by_white_pieces
    global squares_attacked_by_black_pieces
    if 0 < x + deltaX < 9 and 0 < y + deltaY < 9:
        if pieces_on_the_board_objects[x - 1][y - 1].color == "white":
            squares_attacked_by_white_pieces[x + deltaX - 1][y + deltaY - 1] = True
        elif pieces_on_the_board_objects[x - 1][y - 1].color == "black":
            squares_attacked_by_black_pieces[x + deltaX - 1][y + deltaY - 1] = True


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


def return_the_symbol_based_on_the_name_of_the_piece(name_of_the_piece, color):
    piece_symbol = None
    if color == "white":
        if name_of_the_piece == "pawn":
            piece_symbol = chr(0x2659)
        if name_of_the_piece == "knight":
            piece_symbol = chr(0x2658)
        if name_of_the_piece == "bishop":
            piece_symbol = chr(0x2657)
        if name_of_the_piece == "rook":
            piece_symbol = chr(0x2656)
        if name_of_the_piece == "queen":
            piece_symbol = chr(0x2655)
        if name_of_the_piece == "king":
            piece_symbol = chr(0x2657)
    else:
        if name_of_the_piece == "pawn":
            piece_symbol = chr(0x265F)
        if name_of_the_piece == "knight":
            piece_symbol = chr(0x265E)
        if name_of_the_piece == "bishop":
            piece_symbol = chr(0x265D)
        if name_of_the_piece == "rook":
            piece_symbol = chr(0x265C)
        if name_of_the_piece == "queen":
            piece_symbol = chr(0x265B)
        if name_of_the_piece == "king":
            piece_symbol = chr(0x265A)
    return piece_symbol


def return_top_left_tip_of_the_square(x, y):
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
        if j * square_size <= y_coordinates < j * square_size + square_size: y = 9 - j
    return x, y


def change_piece_on_the_square(x, y, piece_symbol, setting_pieces, startX, startY, color, enPassant, castling):
    global pieces_on_the_board
    global previous_moves
    piece_name = return_name_color_of_the_piece(piece_symbol)
    do_not_interfere = False
    canvas.itemconfig(piece_items_in_canvas[x - 1][y - 1], text=piece_symbol,
                      font=('Arial', int(square_size / 2)),
                      tags=("piece", x, y, piece_name, color))
    if setting_pieces and startX is None and startY is None:
        canvas.tag_bind("piece", '<ButtonPress-1>', on_drag_start)
        canvas.tag_bind("piece", '<B1-Motion>', on_drag_motion)
        canvas.tag_bind("piece", '<ButtonRelease-1>', on_drag_stop)
    else:
        canvas.itemconfig(piece_items_in_canvas[startX - 1][startY - 1], text=" ", font=('Arial', int(square_size / 2)),
                          tags=(x, y))
        if pieces_on_the_board_objects[x - 1][y - 1] is not None:
            if pieces_on_the_board_objects[x - 1][y - 1].color == "black":
                black_pieces.remove(pieces_on_the_board_objects[x - 1][y - 1])
            elif pieces_on_the_board_objects[x - 1][y - 1].color == "white":
                white_pieces.remove(pieces_on_the_board_objects[x - 1][y - 1])
            previous_moves.append({"x": x, "y": y, "startX": startX, "startY": startY,
                                   "colorOfTheMovedPiece": pieces_on_the_board_objects[startX - 1][startY - 1].color,
                                   "typeOfTheMovedPiece": pieces_on_the_board_objects[startX - 1][startY - 1].type,
                                   "capturedPieceType": pieces_on_the_board_objects[x - 1][y - 1].type})
        else:
            if enPassant == True:
                if pieces_on_the_board_objects[startX - 1][startY - 1].color == "white":
                    black_pieces.remove(pieces_on_the_board_objects[x - 1][y - 2])
                    pieces_on_the_board_objects[x - 1][y - 2] = None
                    canvas.itemconfig(piece_items_in_canvas[x - 1][y - 2], text=" ",
                                      font=('Arial', int(square_size / 2)),
                                      tags=("piece", x, y, piece_name, color))
                elif pieces_on_the_board_objects[startX - 1][startY - 1].color == "black":
                    white_pieces.remove(pieces_on_the_board_objects[x - 1][y])
                    pieces_on_the_board_objects[x - 1][y] = None
                    canvas.itemconfig(piece_items_in_canvas[x - 1][y], text=" ",
                                      font=('Arial', int(square_size / 2)),
                                      tags=("piece", x, y, piece_name, color))
                previous_moves.append({"x": x, "y": y, "startX": startX, "startY": startY,
                                       "colorOfTheMovedPiece": pieces_on_the_board_objects[startX - 1][
                                           startY - 1].color,
                                       "typeOfTheMovedPiece": pieces_on_the_board_objects[startX - 1][
                                           startY - 1].type,
                                       "capturedPieceType": "Pawn"})
            if castling == True:
                if color == "white":
                    rook_symbol = chr(0x2656)
                elif color == "black":
                    rook_symbol = chr(0x265C)
                if (2, 0) in pieces_on_the_board_objects[startX - 1][startY - 1].possible_moves and x - startX == 2:
                    canvas.itemconfig(piece_items_in_canvas[x - 2][y - 1], text=rook_symbol,
                                      font=('Arial', int(square_size / 2)),
                                      tags=("piece", x, y, return_name_color_of_the_piece(rook_symbol), color))
                    canvas.itemconfig(piece_items_in_canvas[x][y - 1], text=" ",
                                      font=('Arial', int(square_size / 2)),
                                      tags=(x, y))
                    pieces_on_the_board_objects[x - 2][y - 1] = pieces_on_the_board_objects[x][y - 1]
                    pieces_on_the_board_objects[x - 2][y - 1].x_L = x - 1
                    pieces_on_the_board_objects[x][y - 1] = None
                elif (-2, 0) in pieces_on_the_board_objects[startX - 1][startY - 1].possible_moves and x - startX == -2:
                    canvas.itemconfig(piece_items_in_canvas[x][y - 1], text=rook_symbol,
                                      font=('Arial', int(square_size / 2)),
                                      tags=("piece", x, y, return_name_color_of_the_piece(rook_symbol), color))
                    canvas.itemconfig(piece_items_in_canvas[x - 3][y - 1], text=" ",
                                      font=('Arial', int(square_size / 2)),
                                      tags=(x, y))
                pieces_on_the_board_objects[x][y - 1] = pieces_on_the_board_objects[x - 3][y - 1]
                pieces_on_the_board_objects[x][y - 1].x_L = x + 1
                pieces_on_the_board_objects[x - 3][y - 1] = None
        if pieces_on_the_board_objects[startX - 1][startY - 1].type == "Pawn":
            if pieces_on_the_board_objects[startX - 1][startY - 1].color == "white":
                if y == 8 and startY == 7:
                    white_pieces.remove(pieces_on_the_board_objects[startX - 1][startY - 1])
                    piece = create_destroy_piece_choice_menu("white", True)
                    if piece == "queen":
                        queen = Queen("white", x, y)
                        pieces_on_the_board_objects[x - 1][y - 1] = queen
                    elif piece == "rook":
                        rook = Rook("white", x, y)
                        pieces_on_the_board_objects[x - 1][y - 1] = rook
                    elif piece == "bishop":
                        bishop = Bishop("white", x, y)
                        pieces_on_the_board_objects[x - 1][y - 1] = bishop
                    elif piece == "knight":
                        knight = Knight("white", x, y)
                        pieces_on_the_board_objects[x - 1][y - 1] = knight
                    if pieces_on_the_board_objects[x - 1][y - 1] == None:
                        previous_moves.append({"x": x, "y": y, "startX": startX, "startY": startY,
                                               "colorOfTheMovedPiece": pieces_on_the_board_objects[startX - 1][
                                                   startY - 1].color,
                                               "typeOfTheMovedPiece": pieces_on_the_board_objects[startX - 1][
                                                   startY - 1].type,
                                               "capturedPieceType": None})
                    else:
                        previous_moves.append({"x": x, "y": y, "startX": startX, "startY": startY,
                                               "colorOfTheMovedPiece": pieces_on_the_board_objects[startX - 1][
                                                   startY - 1].color,
                                               "typeOfTheMovedPiece": pieces_on_the_board_objects[startX - 1][
                                                   startY - 1].type,
                                               "capturedPieceType": pieces_on_the_board_objects[x - 1][y - 1].type})
                    canvas.itemconfig(piece_items_in_canvas[x - 1][y - 1],
                                      text=return_the_symbol_based_on_the_name_of_the_piece(piece,
                                                                                            pieces_on_the_board_objects[
                                                                                                startX - 1][
                                                                                                startY - 1].color),
                                      font=('Arial', int(square_size / 2)))
                    pieces_on_the_board_objects[startX - 1][startY - 1] = None
                    do_not_interfere = True
            else:
                if y == 1 and startY == 2:
                    piece = create_destroy_piece_choice_menu("black", True)
                    black_pieces.remove(pieces_on_the_board_objects[startX - 1][startY - 1])
                    if piece == "queen":
                        queen = Queen("black", x, y)
                        pieces_on_the_board_objects[x - 1][y - 1] = queen
                    elif piece == "rook":
                        rook = Rook("black", x, y)
                        pieces_on_the_board_objects[x - 1][y - 1] = rook
                    elif piece == "bishop":
                        bishop = Bishop("black", x, y)
                        pieces_on_the_board_objects[x - 1][y - 1] = bishop
                    elif piece == "knight":
                        knight = Knight("black", x, y)
                        pieces_on_the_board_objects[x - 1][y - 1] = knight
                    if pieces_on_the_board_objects[x - 1][y - 1] == None:
                        previous_moves.append({"x": x, "y": y, "startX": startX, "startY": startY,
                                               "colorOfTheMovedPiece": pieces_on_the_board_objects[startX - 1][
                                                   startY - 1].color,
                                               "typeOfTheMovedPiece": pieces_on_the_board_objects[startX - 1][
                                                   startY - 1].type,
                                               "capturedPieceType": None})
                    else:
                        previous_moves.append({"x": x, "y": y, "startX": startX, "startY": startY,
                                               "colorOfTheMovedPiece": pieces_on_the_board_objects[startX - 1][
                                                   startY - 1].color,
                                               "typeOfTheMovedPiece": pieces_on_the_board_objects[startX - 1][
                                                   startY - 1].type,
                                               "capturedPieceType": pieces_on_the_board_objects[x - 1][y - 1].type})
                    canvas.itemconfig(piece_items_in_canvas[x - 1][y - 1],
                                      text=return_the_symbol_based_on_the_name_of_the_piece(piece,
                                                                                            pieces_on_the_board_objects[
                                                                                                startX - 1][
                                                                                                startY - 1].color),
                                      font=('Arial', int(square_size / 2)))
                    pieces_on_the_board_objects[startX - 1][startY - 1] = None
                    do_not_interfere = True
        if do_not_interfere == False:
            previous_moves.append({"x": x, "y": y, "startX": startX, "startY": startY,
                                   "colorOfTheMovedPiece": pieces_on_the_board_objects[startX - 1][startY - 1].color,
                                   "typeOfTheMovedPiece": pieces_on_the_board_objects[startX - 1][startY - 1].type,
                                   "capturedPieceType": None})
            pieces_on_the_board_objects[x - 1][y - 1] = pieces_on_the_board_objects[startX - 1][startY - 1]
            pieces_on_the_board_objects[x - 1][y - 1].x_L = x
            pieces_on_the_board_objects[x - 1][y - 1].y_N = y
            pieces_on_the_board_objects[startX - 1][startY - 1] = None
def check_situation_of_the_king(color):
    situation_of_the_king = None
    global squares_attacked_by_white_pieces
    global squares_attacked_by_black_pieces
    if color == "white":
        for object in white_pieces:
            object.define_possible_moves(pieces_on_the_board_objects)
            if object.type == "King":
                king_object = object
        for object in black_pieces:
            object.define_possible_moves(pieces_on_the_board_objects)
        if squares_attacked_by_black_pieces[king_object.x_L - 1][king_object.y_N - 1] == True:
            for object in white_pieces:
                for x,y in object.possible_moves:
                    pieces_on_the_board_objects_simulation = copy.deepcopy(pieces_on_the_board_objects)
                    pieces_on_the_board_objects_simulation[object.x_L +  x -  1][object.y_N + y - 1] = pieces_on_the_board_objects_simulation[object.x_L - 1][object.y_N - 1]
                    pieces_on_the_board_objects_simulation[object.x_L +  x -  1][object.y_N + y - 1].x_L = object.x_L + x
                    pieces_on_the_board_objects_simulation[object.x_L +  x -  1][object.y_N + y - 1].y_N = object.y_N + y
                    pieces_on_the_board_objects_simulation[object.x_L - 1][object.y_N - 1] = None
                    squares_attacked_by_white_pieces = [[False for _ in range(8)] for _ in range(8)]
                    squares_attacked_by_black_pieces = [[False for _ in range(8)] for _ in range(8)]
                    for i in range(8):
                        for j in range(8):
                            if pieces_on_the_board_objects_simulation[i][j] is not None:
                                if pieces_on_the_board_objects_simulation[i][j].color == "black":
                                    pieces_on_the_board_objects_simulation[i][j].define_possible_moves(pieces_on_the_board_objects_simulation)
                                if pieces_on_the_board_objects_simulation[i][j].color == "white":
                                    if pieces_on_the_board_objects_simulation[i][j].type == "King":
                                        king_object = pieces_on_the_board_objects_simulation[i][j]
                    if squares_attacked_by_black_pieces[king_object.x_L - 1][king_object.y_N - 1] is False:
                        situation_of_the_king = "check"
                        break
                if squares_attacked_by_black_pieces[king_object.x_L - 1][king_object.y_N - 1] is False:
                    situation_of_the_king = "check"
                    break
            if situation_of_the_king == None:
                situation_of_the_king = "checkmate"
        else:
            situation_of_the_king = "safe"
        print(situation_of_the_king)
    elif color == "black":
        for object in black_pieces:
            object.define_possible_moves(pieces_on_the_board_objects)
            if object.type == "King":
                king_object = object
        for object in white_pieces:
            object.define_possible_moves(pieces_on_the_board_objects)
        if squares_attacked_by_white_pieces[king_object.x_L - 1][king_object.y_N - 1] == True:
            for object in black_pieces:
                for x,y in object.possible_moves:
                    pieces_on_the_board_objects_simulation = copy.deepcopy(pieces_on_the_board_objects)
                    if pieces_on_the_board_objects_simulation[object.x_L +  x -  1][object.y_N + y - 1] is not None:
                        pieces_on_the_board_objects_simulation[object.x_L +  x -  1][object.y_N + y - 1] = None
                    pieces_on_the_board_objects_simulation[object.x_L +  x -  1][object.y_N + y - 1] = pieces_on_the_board_objects_simulation[object.x_L - 1][object.y_N - 1]
                    pieces_on_the_board_objects_simulation[object.x_L +  x -  1][object.y_N + y - 1].x_L = object.x_L + x
                    pieces_on_the_board_objects_simulation[object.x_L +  x -  1][object.y_N + y - 1].y_N = object.y_N + y
                    pieces_on_the_board_objects_simulation[object.x_L - 1][object.y_N - 1] = None
                    squares_attacked_by_white_pieces = [[False for _ in range(8)] for _ in range(8)]
                    squares_attacked_by_black_pieces = [[False for _ in range(8)] for _ in range(8)]
                    for i in range(8):
                        for j in range(8):
                            if pieces_on_the_board_objects_simulation[i][j] is not None:
                                if pieces_on_the_board_objects_simulation[i][j].color == "white":
                                    pieces_on_the_board_objects_simulation[i][j].define_possible_moves(pieces_on_the_board_objects_simulation)
                                if pieces_on_the_board_objects_simulation[i][j].color == "black":
                                    if pieces_on_the_board_objects_simulation[i][j].type == "King":
                                        king_object = pieces_on_the_board_objects_simulation[i][j]
                    if squares_attacked_by_white_pieces[king_object.x_L - 1][king_object.y_N - 1] is False:
                        situation_of_the_king = "check"
                        break
                if squares_attacked_by_white_pieces[king_object.x_L - 1][king_object.y_N - 1] is False:
                    situation_of_the_king = "check"
                    break
            if situation_of_the_king == None:
                situation_of_the_king = "checkmate"
        else:
            situation_of_the_king = "safe"
        print(situation_of_the_king)





class Pawn():
    def __init__(self, color, x_L, y_N):
        self.color = color
        self.x_L = x_L
        self.y_N = y_N
        self.piece_id = piece_items_in_canvas[x_L - 1][y_N - 1]
        self.possible_moves = []
        self.type = "Pawn"
        self.enPassant = False
        if self.color == "white":
            self.symbol = chr(0x2659)
            white_pieces.append(self)
        else:
            self.symbol = chr(0x265F)
            black_pieces.append(self)
        change_piece_on_the_square(x_L, y_N, self.symbol, True, None,
                                   None, self.color, False, False)

    def define_possible_moves(self, pieces_on_the_board_objects_data):
        self.possible_moves = []
        self.enPassant = False
        try:
            last_move = previous_moves[len(previous_moves) - 1]
        except IndexError:
            pass
        if self.color == "white":
            if len(previous_moves) != 0:
                if (last_move["x"] == self.x_L - 1 or last_move["x"] == self.x_L + 1 and last_move["y"] == self.y_N
                        and last_move["startX"] == last_move["x"] and last_move["startY"] == 7
                        and last_move["colorOfTheMovedPiece"] != self.color and last_move[
                            "typeOfTheMovedPiece"] == "Pawn"
                        and last_move["capturedPieceType"] == None):
                    self.enPassant = True
                    add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, last_move["x"] - self.x_L, 1, pieces_on_the_board_objects_data)
        else:
            if len(previous_moves) != 0:
                if (last_move["x"] == self.x_L - 1 or last_move["x"] == self.x_L + 1 and last_move["y"] == self.y_N
                        and last_move["startX"] == last_move["x"] and last_move["startY"] == 2
                        and last_move["colorOfTheMovedPiece"] != self.color and last_move[
                            "typeOfTheMovedPiece"] == "Pawn"
                        and last_move["capturedPieceType"] == None):
                    self.enPassant = True
                    add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, last_move["x"] - self.x_L,
                                                                       -1, pieces_on_the_board_objects_data)
        try:

            if self.color == "white":
                if pieces_on_the_board_objects_data[self.x_L + 0 - 1][self.y_N + 1 - 1] is None:
                    add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, 0, 1, pieces_on_the_board_objects_data)
                    if self.y_N == 2:
                        if pieces_on_the_board_objects_data[self.x_L + 0 - 1][self.y_N + 2 - 1] is None:
                            add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, 0, 2, pieces_on_the_board_objects_data)
                if (pieces_on_the_board_objects_data[self.x_L - 1 - 1][self.y_N + 1 - 1] is not None
                        and pieces_on_the_board_objects_data[self.x_L - 1 - 1][self.y_N + 1 - 1].color != self.color):
                    add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, -1, 1, pieces_on_the_board_objects_data)
                add_to_attacked_squares_only(self.x_L, self.y_N, -1, 1)
                if (pieces_on_the_board_objects_data[self.x_L + 1 - 1][self.y_N + 1 - 1] is not None
                        and pieces_on_the_board_objects_data[self.x_L + 1 - 1][self.y_N + 1 - 1].color != self.color):
                    add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, 1, 1, pieces_on_the_board_objects_data)
                add_to_attacked_squares_only(self.x_L, self.y_N, 1, 1)


            elif self.color == "black":
                if pieces_on_the_board_objects_data[self.x_L + 0 - 1][self.y_N - 1 - 1] is None:
                    add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, 0, - 1, pieces_on_the_board_objects_data)
                    if self.y_N == 7:
                        if pieces_on_the_board_objects_data[self.x_L + 0 - 1][self.y_N - 2 - 1] is None:
                            add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, 0, - 2, pieces_on_the_board_objects_data)
                if (pieces_on_the_board_objects_data[self.x_L - 1 - 1][self.y_N - 1 - 1] is not None
                        and pieces_on_the_board_objects_data[self.x_L - 1 - 1][self.y_N - 1 - 1].color != self.color):
                    add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, -1, -1, pieces_on_the_board_objects_data)
                add_to_attacked_squares_only(self.x_L, self.y_N, -1, -1)
                if (pieces_on_the_board_objects_data[self.x_L + 1 - 1][self.y_N - 1 - 1] is not None
                        and pieces_on_the_board_objects_data[self.x_L + 1 - 1][self.y_N - 1 - 1].color != self.color):
                    add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, 1, -1, pieces_on_the_board_objects_data)
                add_to_attacked_squares_only(self.x_L, self.y_N, 1, -1)
        except IndexError:
            pass


class Bishop():
    def __init__(self, color, x_L, y_N):
        self.color = color
        self.x_L = x_L
        self.y_N = y_N
        self.possible_moves = []
        self.type = "Bishop"
        if color == "white":
            self.symbol = chr(0x2657)
            white_pieces.append(self)
        else:
            self.symbol = chr(0x265D)
            black_pieces.append(self)
        change_piece_on_the_square(x_L, y_N, self.symbol, True, None,
                                   None, self.color, False, False)

    def define_possible_moves(self, pieces_on_the_board_objects_data):
        self.possible_moves = []
        for tuple in pieces_diagonal_y_minus_x_minus:
            deltaX, deltaY = tuple
            try:
                if pieces_on_the_board_objects_data[self.x_L + deltaX - 1][self.y_N + deltaY - 1] is None:
                    add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, deltaX, deltaY,
                                                                       pieces_on_the_board_objects_data)
                elif pieces_on_the_board_objects_data[self.x_L + deltaX - 1][self.y_N + deltaY - 1] is not None:
                    if pieces_on_the_board_objects_data[self.x_L + deltaX - 1][
                        self.y_N + deltaY - 1].color != self.color:
                        add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, deltaX, deltaY,
                                                                           pieces_on_the_board_objects_data)
                    elif pieces_on_the_board_objects_data[self.x_L + deltaX - 1][
                        self.y_N + deltaY - 1].color == self.color:
                        add_to_attacked_squares_only(self.x_L, self.y_N, deltaX, deltaY)
                    break
                else:
                    break
            except IndexError:
                pass
        for tuple in pieces_diagonal_y_minus_x_plus:
            deltaX, deltaY = tuple
            try:
                if pieces_on_the_board_objects_data[self.x_L + deltaX - 1][self.y_N + deltaY - 1] is None:
                    add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, deltaX, deltaY,
                                                                       pieces_on_the_board_objects_data)
                elif pieces_on_the_board_objects_data[self.x_L + deltaX - 1][self.y_N + deltaY - 1] is not None:
                    if pieces_on_the_board_objects_data[self.x_L + deltaX - 1][
                        self.y_N + deltaY - 1].color != self.color:
                        add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, deltaX, deltaY,
                                                                           pieces_on_the_board_objects_data)
                    elif pieces_on_the_board_objects_data[self.x_L + deltaX - 1][
                        self.y_N + deltaY - 1].color == self.color:
                        add_to_attacked_squares_only(self.x_L, self.y_N, deltaX, deltaY)
                    break
                else:
                    break
            except IndexError:
                pass
        for tuple in pieces_diagonal_y_plus_x_minus:
            deltaX, deltaY = tuple
            try:
                if pieces_on_the_board_objects_data[self.x_L + deltaX - 1][self.y_N + deltaY - 1] is None:
                    add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, deltaX, deltaY,
                                                                       pieces_on_the_board_objects_data)
                elif pieces_on_the_board_objects_data[self.x_L + deltaX - 1][self.y_N + deltaY - 1] is not None:
                    if pieces_on_the_board_objects_data[self.x_L + deltaX - 1][
                        self.y_N + deltaY - 1].color != self.color:
                        add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, deltaX, deltaY,
                                                                           pieces_on_the_board_objects_data)
                    elif pieces_on_the_board_objects_data[self.x_L + deltaX - 1][
                        self.y_N + deltaY - 1].color == self.color:
                        add_to_attacked_squares_only(self.x_L, self.y_N, deltaX, deltaY)
                    break
                else:
                    break
            except IndexError:
                pass
        for tuple in pieces_diagonal_y_plus_x_plus:
            deltaX, deltaY = tuple
            try:
                if pieces_on_the_board_objects_data[self.x_L + deltaX - 1][self.y_N + deltaY - 1] is None:
                    add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, deltaX, deltaY,
                                                                       pieces_on_the_board_objects_data)
                elif pieces_on_the_board_objects_data[self.x_L + deltaX - 1][self.y_N + deltaY - 1] is not None:
                    if pieces_on_the_board_objects_data[self.x_L + deltaX - 1][
                        self.y_N + deltaY - 1].color != self.color:
                        add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, deltaX, deltaY,
                                                                           pieces_on_the_board_objects_data)
                    elif pieces_on_the_board_objects_data[self.x_L + deltaX - 1][
                        self.y_N + deltaY - 1].color == self.color:
                        add_to_attacked_squares_only(self.x_L, self.y_N, deltaX, deltaY)
                    break
                else:
                    break
            except IndexError:
                pass


class Knight():
    def __init__(self, color, x_L, y_N):
        self.color = color
        self.x_L = x_L
        self.y_N = y_N
        self.possible_moves = []
        self.type = "Knight"
        if color == "white":
            self.symbol = chr(0x2658)
            white_pieces.append(self)
        else:
            self.symbol = chr(0x265E)
            black_pieces.append(self)
        change_piece_on_the_square(x_L, y_N, self.symbol, True, None,
                                   None, self.color, False, False)

    def define_possible_moves(self, pieces_on_the_board_objects_data):
        self.possible_moves = []
        for tuple in knight_delta_x_y:
            deltaX, deltaY = tuple
            try:
                if pieces_on_the_board_objects_data[self.x_L + deltaX - 1][self.y_N + deltaY - 1] is None:
                    add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, deltaX, deltaY, pieces_on_the_board_objects_data)
                elif pieces_on_the_board_objects_data[self.x_L + deltaX - 1][self.y_N + deltaY - 1] is not None:
                    if pieces_on_the_board_objects_data[self.x_L + deltaX - 1][self.y_N + deltaY - 1].color != self.color:
                        add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, deltaX, deltaY, pieces_on_the_board_objects_data)
                    elif pieces_on_the_board_objects_data[self.x_L + deltaX - 1][self.y_N + deltaY - 1].color == self.color:
                        add_to_attacked_squares_only(self.x_L, self.y_N, deltaX, deltaY)
            except IndexError:
                pass


class Rook():
    def __init__(self, color, x_L, y_N):
        self.color = color
        self.x_L = x_L
        self.y_N = y_N
        self.possible_moves = []
        self.type = "Rook"
        if color == "white":
            self.symbol = chr(0x2656)
            white_pieces.append(self)
        else:
            self.symbol = chr(0x265C)
            black_pieces.append(self)
        change_piece_on_the_square(x_L, y_N, self.symbol, True, None, None,
                                   self.color, False, False)

    def define_possible_moves(self, pieces_on_the_board_objects_data):
        self.possible_moves = []
        for tuple in pieces_vertical_y_plus:
            deltaX, deltaY = tuple
            try:
                if pieces_on_the_board_objects_data[self.x_L + deltaX - 1][self.y_N + deltaY - 1] is None:
                    add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, deltaX, deltaY,
                                                                       pieces_on_the_board_objects_data)
                elif pieces_on_the_board_objects_data[self.x_L + deltaX - 1][self.y_N + deltaY - 1] is not None:
                    if pieces_on_the_board_objects_data[self.x_L + deltaX - 1][
                        self.y_N + deltaY - 1].color != self.color:
                        add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, deltaX, deltaY,
                                                                           pieces_on_the_board_objects_data)
                    elif pieces_on_the_board_objects_data[self.x_L + deltaX - 1][
                        self.y_N + deltaY - 1].color == self.color:
                        add_to_attacked_squares_only(self.x_L, self.y_N, deltaX, deltaY)
                    break
                else:
                    break
            except IndexError:
                pass
        for tuple in pieces_vertical_y_minus:
            deltaX, deltaY = tuple
            try:
                if pieces_on_the_board_objects_data[self.x_L + deltaX - 1][self.y_N + deltaY - 1] is None:
                    add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, deltaX, deltaY,
                                                                       pieces_on_the_board_objects_data)
                elif pieces_on_the_board_objects_data[self.x_L + deltaX - 1][self.y_N + deltaY - 1] is not None:
                    if pieces_on_the_board_objects_data[self.x_L + deltaX - 1][
                        self.y_N + deltaY - 1].color != self.color:
                        add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, deltaX, deltaY,
                                                                           pieces_on_the_board_objects_data)
                    elif pieces_on_the_board_objects_data[self.x_L + deltaX - 1][
                        self.y_N + deltaY - 1].color == self.color:
                        add_to_attacked_squares_only(self.x_L, self.y_N, deltaX, deltaY)
                    break
                else:
                    break
            except IndexError:
                pass
        for tuple in pieces_horizontal_x_plus:
            deltaX, deltaY = tuple
            try:
                if pieces_on_the_board_objects_data[self.x_L + deltaX - 1][self.y_N + deltaY - 1] is None:
                    add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, deltaX, deltaY,
                                                                       pieces_on_the_board_objects_data)
                elif pieces_on_the_board_objects_data[self.x_L + deltaX - 1][self.y_N + deltaY - 1] is not None:
                    if pieces_on_the_board_objects_data[self.x_L + deltaX - 1][
                        self.y_N + deltaY - 1].color != self.color:
                        add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, deltaX, deltaY,
                                                                           pieces_on_the_board_objects_data)
                    elif pieces_on_the_board_objects_data[self.x_L + deltaX - 1][
                        self.y_N + deltaY - 1].color == self.color:
                        add_to_attacked_squares_only(self.x_L, self.y_N, deltaX, deltaY)
                    break
                else:
                    break
            except IndexError:
                pass
        for tuple in pieces_horizontal_x_minus:
            deltaX, deltaY = tuple
            try:
                if pieces_on_the_board_objects_data[self.x_L + deltaX - 1][self.y_N + deltaY - 1] is None:
                    add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, deltaX, deltaY,
                                                                       pieces_on_the_board_objects_data)
                elif pieces_on_the_board_objects_data[self.x_L + deltaX - 1][self.y_N + deltaY - 1] is not None:
                    if pieces_on_the_board_objects_data[self.x_L + deltaX - 1][
                        self.y_N + deltaY - 1].color != self.color:
                        add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, deltaX, deltaY,
                                                                           pieces_on_the_board_objects_data)
                    elif pieces_on_the_board_objects_data[self.x_L + deltaX - 1][
                        self.y_N + deltaY - 1].color == self.color:
                        add_to_attacked_squares_only(self.x_L, self.y_N, deltaX, deltaY)
                    break
                else:
                    break
            except IndexError:
                pass


class Queen():
    def __init__(self, color, x_L, y_N):
        self.color = color
        self.x_L = x_L
        self.y_N = y_N
        self.possible_moves = []
        self.type = "Queen"
        if color == "white":
            self.symbol = chr(0x2655)
            white_pieces.append(self)
        else:
            self.symbol = chr(0x265B)
            black_pieces.append(self)
        change_piece_on_the_square(x_L, y_N, self.symbol, True, None, None,
                                   self.color, False, False)

    def define_possible_moves(self, pieces_on_the_board_objects_data):
        self.possible_moves = []
        self.possible_moves = []
        for tuple in pieces_vertical_y_plus:
            deltaX, deltaY = tuple
            try:
                if pieces_on_the_board_objects_data[self.x_L + deltaX - 1][self.y_N + deltaY - 1] is None:
                    add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, deltaX, deltaY,
                                                                       pieces_on_the_board_objects_data)
                elif pieces_on_the_board_objects_data[self.x_L + deltaX - 1][self.y_N + deltaY - 1] is not None:
                    if pieces_on_the_board_objects_data[self.x_L + deltaX - 1][
                        self.y_N + deltaY - 1].color != self.color:
                        add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, deltaX, deltaY,
                                                                           pieces_on_the_board_objects_data)
                    elif pieces_on_the_board_objects_data[self.x_L + deltaX - 1][
                        self.y_N + deltaY - 1].color == self.color:
                        add_to_attacked_squares_only(self.x_L, self.y_N, deltaX, deltaY)
                    break
                else:
                    break
            except IndexError:
                pass
        for tuple in pieces_vertical_y_minus:
            deltaX, deltaY = tuple
            try:
                if pieces_on_the_board_objects_data[self.x_L + deltaX - 1][self.y_N + deltaY - 1] is None:
                    add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, deltaX, deltaY,
                                                                       pieces_on_the_board_objects_data)
                elif pieces_on_the_board_objects_data[self.x_L + deltaX - 1][self.y_N + deltaY - 1] is not None:
                    if pieces_on_the_board_objects_data[self.x_L + deltaX - 1][
                        self.y_N + deltaY - 1].color != self.color:
                        add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, deltaX, deltaY,
                                                                           pieces_on_the_board_objects_data)
                    elif pieces_on_the_board_objects_data[self.x_L + deltaX - 1][
                        self.y_N + deltaY - 1].color == self.color:
                        add_to_attacked_squares_only(self.x_L, self.y_N, deltaX, deltaY)
                    break
                else:
                    break
            except IndexError:
                pass
        for tuple in pieces_horizontal_x_plus:
            deltaX, deltaY = tuple
            try:
                if pieces_on_the_board_objects_data[self.x_L + deltaX - 1][self.y_N + deltaY - 1] is None:
                    add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, deltaX, deltaY,
                                                                       pieces_on_the_board_objects_data)
                elif pieces_on_the_board_objects_data[self.x_L + deltaX - 1][self.y_N + deltaY - 1] is not None:
                    if pieces_on_the_board_objects_data[self.x_L + deltaX - 1][
                        self.y_N + deltaY - 1].color != self.color:
                        add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, deltaX, deltaY,
                                                                           pieces_on_the_board_objects_data)
                    elif pieces_on_the_board_objects_data[self.x_L + deltaX - 1][
                        self.y_N + deltaY - 1].color == self.color:
                        add_to_attacked_squares_only(self.x_L, self.y_N, deltaX, deltaY)
                    break
                else:
                    break
            except IndexError:
                pass
        for tuple in pieces_horizontal_x_minus:
            deltaX, deltaY = tuple
            try:
                if pieces_on_the_board_objects_data[self.x_L + deltaX - 1][self.y_N + deltaY - 1] is None:
                    add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, deltaX, deltaY,
                                                                       pieces_on_the_board_objects_data)
                elif pieces_on_the_board_objects_data[self.x_L + deltaX - 1][self.y_N + deltaY - 1] is not None:
                    if pieces_on_the_board_objects_data[self.x_L + deltaX - 1][
                        self.y_N + deltaY - 1].color != self.color:
                        add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, deltaX, deltaY,
                                                                           pieces_on_the_board_objects_data)
                    elif pieces_on_the_board_objects_data[self.x_L + deltaX - 1][
                        self.y_N + deltaY - 1].color == self.color:
                        add_to_attacked_squares_only(self.x_L, self.y_N, deltaX, deltaY)
                    break
                else:
                    break
            except IndexError:
                pass
        for tuple in pieces_diagonal_y_minus_x_minus:
            deltaX, deltaY = tuple
            try:
                if pieces_on_the_board_objects_data[self.x_L + deltaX - 1][self.y_N + deltaY - 1] is None:
                    add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, deltaX, deltaY,
                                                                       pieces_on_the_board_objects_data)
                elif pieces_on_the_board_objects_data[self.x_L + deltaX - 1][self.y_N + deltaY - 1] is not None:
                    if pieces_on_the_board_objects_data[self.x_L + deltaX - 1][
                        self.y_N + deltaY - 1].color != self.color:
                        add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, deltaX, deltaY,
                                                                           pieces_on_the_board_objects_data)
                    elif pieces_on_the_board_objects_data[self.x_L + deltaX - 1][
                        self.y_N + deltaY - 1].color == self.color:
                        add_to_attacked_squares_only(self.x_L, self.y_N, deltaX, deltaY)
                    break
                else:
                    break
            except IndexError:
                pass
        for tuple in pieces_diagonal_y_minus_x_plus:
            deltaX, deltaY = tuple
            try:
                if pieces_on_the_board_objects_data[self.x_L + deltaX - 1][self.y_N + deltaY - 1] is None:
                    add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, deltaX, deltaY,
                                                                       pieces_on_the_board_objects_data)
                elif pieces_on_the_board_objects_data[self.x_L + deltaX - 1][self.y_N + deltaY - 1] is not None:
                    if pieces_on_the_board_objects_data[self.x_L + deltaX - 1][
                        self.y_N + deltaY - 1].color != self.color:
                        add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, deltaX, deltaY,
                                                                           pieces_on_the_board_objects_data)
                    elif pieces_on_the_board_objects_data[self.x_L + deltaX - 1][
                        self.y_N + deltaY - 1].color == self.color:
                        add_to_attacked_squares_only(self.x_L, self.y_N, deltaX, deltaY)
                    break
                else:
                    break
            except IndexError:
                pass
        for tuple in pieces_diagonal_y_plus_x_minus:
            deltaX, deltaY = tuple
            try:
                if pieces_on_the_board_objects_data[self.x_L + deltaX - 1][self.y_N + deltaY - 1] is None:
                    add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, deltaX, deltaY,
                                                                       pieces_on_the_board_objects_data)
                elif pieces_on_the_board_objects_data[self.x_L + deltaX - 1][self.y_N + deltaY - 1] is not None:
                    if pieces_on_the_board_objects_data[self.x_L + deltaX - 1][
                        self.y_N + deltaY - 1].color != self.color:
                        add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, deltaX, deltaY,
                                                                           pieces_on_the_board_objects_data)
                    elif pieces_on_the_board_objects_data[self.x_L + deltaX - 1][
                        self.y_N + deltaY - 1].color == self.color:
                        add_to_attacked_squares_only(self.x_L, self.y_N, deltaX, deltaY)
                    break
                else:
                    break
            except IndexError:
                pass
        for tuple in pieces_diagonal_y_plus_x_plus:
            deltaX, deltaY = tuple
            try:
                if pieces_on_the_board_objects_data[self.x_L + deltaX - 1][self.y_N + deltaY - 1] is None:
                    add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, deltaX, deltaY,
                                                                       pieces_on_the_board_objects_data)
                elif pieces_on_the_board_objects_data[self.x_L + deltaX - 1][self.y_N + deltaY - 1] is not None:
                    if pieces_on_the_board_objects_data[self.x_L + deltaX - 1][
                        self.y_N + deltaY - 1].color != self.color:
                        add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, deltaX, deltaY,
                                                                           pieces_on_the_board_objects_data)
                    elif pieces_on_the_board_objects_data[self.x_L + deltaX - 1][
                        self.y_N + deltaY - 1].color == self.color:
                        add_to_attacked_squares_only(self.x_L, self.y_N, deltaX, deltaY)
                    break
                else:
                    break
            except IndexError:
                pass


class King():
    def __init__(self, color, x_L, y_N):
        self.color = color
        self.x_L = x_L
        self.y_N = y_N
        self.type = "King"
        self.possible_moves = []
        self.castling_queens_side = True
        self.castling_kings_side = True
        self.castling = True
        if color == "white":
            self.symbol = chr(0x2654)
            white_pieces.append(self)
        else:
            self.symbol = chr(0x265A)
            black_pieces.append(self)
        change_piece_on_the_square(x_L, y_N, self.symbol, True, None, None,
                                   self.color, False, False)

    def define_possible_moves(self, pieces_on_the_board_objects_data):
        self.possible_moves = []
        self.castling = True
        self.castling_queens_side = True
        self.castling_kings_side = True
        for tuple in kings_delta_x_y:
            deltaX, deltaY = tuple
            try:
                if pieces_on_the_board_objects_data[self.x_L + deltaX - 1][self.y_N + deltaY - 1] is None:
                    add_to_attacked_squares_only(self.x_L, self.y_N, deltaX, deltaY)
                    if (self.color == "white" and squares_attacked_by_black_pieces[self.x_L + deltaX - 1][
                        self.y_N + deltaY - 1] == False
                            or self.color == "black" and squares_attacked_by_white_pieces[self.x_L + deltaX - 1][
                                self.y_N + deltaY - 1] == False):
                        add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, deltaX, deltaY, pieces_on_the_board_objects_data)
                elif pieces_on_the_board_objects_data[self.x_L + deltaX - 1][self.y_N + deltaY - 1] is not None:
                    if pieces_on_the_board_objects_data[self.x_L + deltaX - 1][self.y_N + deltaY - 1].color != self.color:
                        if (self.color == "white" and squares_attacked_by_black_pieces[self.x_L + deltaX - 1][
                            self.y_N + deltaY - 1] == False
                                or self.color == "black" and squares_attacked_by_white_pieces[self.x_L + deltaX - 1][
                                    self.y_N + deltaY - 1] == False):
                            add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, deltaX, deltaY, pieces_on_the_board_objects_data)
                    elif pieces_on_the_board_objects_data[self.x_L + deltaX - 1][self.y_N + deltaY - 1].color == self.color:
                        add_to_attacked_squares_only(self.x_L, self.y_N, deltaX, deltaY)
            except IndexError:
                pass
        try:
            if len(previous_moves) > 0:
                for i in range(len(previous_moves)):
                    if previous_moves[i]["colorOfTheMovedPiece"] == self.color and previous_moves[i][
                        "typeOfTheMovedPiece"] == "King":
                        self.castling = False
                    else:
                        pass
                if self.castling == True:
                    for i in range(len(previous_moves)):
                        if previous_moves[i]["colorOfTheMovedPiece"] == self.color and previous_moves[i][
                            "typeOfTheMovedPiece"] == "Rook" and previous_moves[i]["startX"] == 8:
                            self.castling_kings_side = False
                        else:
                            pass
                    if self.castling_kings_side == True:
                        if (pieces_on_the_board_objects_data[self.x_L + 1 - 1][self.y_N - 1] is not None
                                and pieces_on_the_board_objects_data[self.x_L + 2 - 1][self.y_N - 1] is not None):
                            self.castling_kings_side = False
                        else:
                            if self.color == "white":
                                if (squares_attacked_by_black_pieces[self.x_L + 1 - 1][self.y_N - 1] is False
                                        and squares_attacked_by_black_pieces[self.x_L + 2 - 1][self.y_N - 1] is False):
                                    add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, 2, 0, pieces_on_the_board_objects_data)
                                else:
                                    self.castling_kings_side = False
                            elif self.color == "black":
                                if (squares_attacked_by_white_pieces[self.x_L + 1 - 1][self.y_N - 1] is False
                                        and squares_attacked_by_white_pieces[self.x_L + 2 - 1][self.y_N - 1] is False):
                                    add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, 2, 0, pieces_on_the_board_objects_data)
                                else:
                                    self.castling_kings_side = False

                    for i in range(len(previous_moves)):
                        if previous_moves[i]["colorOfTheMovedPiece"] == self.color and previous_moves[i][
                            "typeOfTheMovedPiece"] == "Rook" and previous_moves[i]["startX"] == 1:
                            self.castling_queens_side = False
                        else:
                            pass
                    if self.castling_queens_side == True:
                        if (pieces_on_the_board_objects_data[self.x_L - 1 - 1][self.y_N - 1] is not None
                                and pieces_on_the_board_objects_data[self.x_L - 2 - 1][self.y_N - 1] is not None
                                and pieces_on_the_board_objects_data[self.x_L - 3 - 1][self.y_N - 1] is not None):
                            self.castling_queens_side = False
                        else:
                            if self.color == "white":
                                if (squares_attacked_by_black_pieces[self.x_L - 1 - 1][self.y_N - 1] is False
                                        and squares_attacked_by_black_pieces[self.x_L - 2 - 1][self.y_N - 1] is False):
                                    add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, -2, 0, pieces_on_the_board_objects_data)
                                else:
                                    self.castling_queens_side = False
                            elif self.color == "black":
                                if (squares_attacked_by_white_pieces[self.x_L - 1 - 1][self.y_N - 1] is False
                                        and squares_attacked_by_black_pieces[self.x_L - 2 - 1][self.y_N - 1] is False):
                                    add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, -2, 0, pieces_on_the_board_objects_data)
                                else:
                                    self.castling_queens_side = False
            if self.castling_kings_side == True or self.castling_queens_side == True:
                self.castling = True
        except IndexError:
            pass


def start_function():
    for i in range(8):
        pawnW = Pawn("white", i + 1, 2)
        pieces_on_the_board_objects[i][1] = pawnW
        pawnB = Pawn("black", i + 1, 7)
        pieces_on_the_board_objects[i][6] = pawnB
    rookW1 = Rook("white", 1, 1)
    pieces_on_the_board_objects[0][0] = rookW1
    rookW2 = Rook("white", 8, 1)
    pieces_on_the_board_objects[7][0] = rookW2
    rookB1 = Rook("black", 1, 8)
    pieces_on_the_board_objects[0][7] = rookB1
    rookB2 = Rook("black", 8, 8)
    pieces_on_the_board_objects[7][7] = rookB2

    knightW1 = Knight("white", 2, 1)
    pieces_on_the_board_objects[1][0] = knightW1
    knightW2 = Knight("white", 7, 1)
    pieces_on_the_board_objects[6][0] = knightW2
    knightB1 = Knight("black", 2, 8)
    pieces_on_the_board_objects[1][7] = knightB1
    knightB2 = Knight("black", 7, 8)
    pieces_on_the_board_objects[6][7] = knightB2

    bishopW1 = Bishop("white", 3, 1)
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

chessLabel = Label(window, bg="#4a4a4a")
chessLabel.pack(anchor="n", pady=int(square_size * 1.25))

materialLabelTop = Label(chessLabel, text="Here white's captured pieces will be shown", font=int(square_size * 0.75))
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
        text_letters = canvas.create_text(x1 - int(square_size / 2), y1 - int(square_size / 2),
                                          font=("Arial", int(square_size / 2)), text=letters[i])
        text_letters_canvas_items[i] = text_letters
    for j in range(8):
        x0 = 0
        x1 = x0 + square_size
        y0 = j * square_size + square_size
        y1 = y0 + square_size
        canvas.create_rectangle(x0, y0, x1, y1, fill="#fff")
        text_numbers = canvas.create_text(x1 - int(square_size / 2), y1 - int(square_size / 2),
                                          font=("Arial", int(square_size / 2)), text=8 - j)
        text_numbers_canvas_items[j] = text_numbers
    for i in range(8):
        for j in range(8):
            x0 = i * square_size + square_size
            y0 = j * square_size + square_size
            x1 = x0 + square_size
            y1 = y0 + square_size

            color = "#b5b897" if (i + j) % 2 == 0 else "#484a3c"

            square_item = canvas.create_rectangle(x0, y0, x1, y1, fill=color, tags="square")
            square_items_in_canvas[i][7 - j] = square_item
            piece_item = canvas.create_text(x0 + int(square_size / 2), y0 + int(square_size / 2), text=" ")
            piece_items_in_canvas[i][7 - j] = piece_item


def reverse_the_board():
    global who_is_on_bottom_of_the_board
    if who_is_on_bottom_of_the_board == "white":
        for i in range(8):
            canvas.itemconfig(text_letters_canvas_items[i], text=letters[7 - i],
                              font=('Arial', int(square_size / 2)))
            canvas.itemconfig(text_numbers_canvas_items[i], text=numbers[i],
                              font=('Arial', int(square_size / 2)))

        who_is_on_bottom_of_the_board = "black"
    elif who_is_on_bottom_of_the_board == "black":
        for j in range(8):
            canvas.itemconfig(text_letters_canvas_items[j], text=letters[j],
                              font=('Arial', int(square_size / 2)))
            canvas.itemconfig(text_numbers_canvas_items[j], text=numbers[7 - j],
                              font=('Arial', int(square_size / 2)))
            who_is_on_bottom_of_the_board = "white"


def on_drag_start(event):
    global drag_data
    row, col = return_x_y_of_the_square(event.x, event.y)
    closest_item = piece_items_in_canvas[row - 1][col - 1]
    item_tags = canvas.gettags(closest_item)
    if "piece" in item_tags and make_moves == True:
        drag_data["item"] = closest_item
        drag_data["x"] = event.x
        drag_data["y"] = event.y
        drag_data["startX"], drag_data["startY"] = return_top_left_tip_of_the_square(event.x, event.y)
        drag_data["startX"] += square_size / 2
        drag_data["startY"] += square_size / 2
        drag_data["rectangle"] = None

    canvas.tag_raise(closest_item)


def on_drag_motion(event):
    global drag_data
    if drag_data["item"]:
        if drag_data["rectangle"] is not None:
            canvas.delete(drag_data["rectangle"])
            drag_data["rectangle"] = None
        deltaX = event.x - drag_data["x"]
        deltaY = event.y - drag_data["y"]
        canvas.move(drag_data["item"], deltaX, deltaY)
        drag_data["x"] = event.x
        drag_data["y"] = event.y
        x0, y0 = return_top_left_tip_of_the_square(event.x, event.y)
        x1 = x0 + square_size
        y1 = y0 + square_size
        rectangle = canvas.create_rectangle(x0, y0, x1, y1, outline='white', width=1, fill='')
        drag_data["rectangle"] = rectangle
        canvas.tag_raise(drag_data["rectangle"])
    canvas.tag_raise(drag_data["item"])


def on_drag_stop(event):
    global drag_data
    global squares_attacked_by_black_pieces
    global squares_attacked_by_white_pieces
    global turn
    canvas.coords(drag_data["item"], drag_data["startX"], drag_data["startY"])
    change_piece = False
    canvas.delete(drag_data["rectangle"])
    x, y = return_x_y_of_the_square(drag_data["x"], drag_data["y"])
    startX, startY = return_x_y_of_the_square(drag_data["startX"], drag_data["startY"])
    if pieces_on_the_board_objects[startX - 1][startY - 1].type == "King":
        squares_attacked_by_white_pieces = [[False for _ in range(8)] for _ in range(8)]
        squares_attacked_by_black_pieces = [[False for _ in range(8)] for _ in range(8)]
        if pieces_on_the_board_objects[startX - 1][startY - 1].color == "white":
            for object in black_pieces:
                object.define_possible_moves(pieces_on_the_board_objects)
        elif pieces_on_the_board_objects[startX - 1][startY - 1].color == "black":
            for object in white_pieces:
                object.define_possible_moves(pieces_on_the_board_objects)
    if x != startX or y != startY:
        pieces_on_the_board_objects[startX - 1][startY - 1].define_possible_moves(pieces_on_the_board_objects)
        for tuple in pieces_on_the_board_objects[startX - 1][startY - 1].possible_moves:
            deltaX, deltaY = tuple
            if x == startX + deltaX and y == startY + deltaY:
                change_piece = True
    if change_piece:
        if pieces_on_the_board_objects[startX - 1][startY - 1].color == turn:
            deltaX2 = x - startX
            deltaY2 = y - startY
            if pieces_on_the_board_objects[startX - 1][startY - 1].type == "Pawn":
                if pieces_on_the_board_objects[startX - 1][startY - 1].enPassant == True:
                    if pieces_on_the_board_objects[startX - 1][
                        startY - 1].color == "white" and deltaY2 == 1 and deltaX2 == - 1 or deltaX2 == 1:
                        change_piece_on_the_square(x, y, pieces_on_the_board_objects[startX - 1][startY - 1].symbol,
                                                   False,
                                                   startX, startY,
                                                   pieces_on_the_board_objects[startX - 1][startY - 1].color, True,
                                                   False)
                    elif pieces_on_the_board_objects[startX - 1][
                        startY - 1].color == "black" and deltaY2 == -1 and deltaX2 == - 1 or deltaX2 == 1:
                        change_piece_on_the_square(x, y, pieces_on_the_board_objects[startX - 1][startY - 1].symbol,
                                                   False,
                                                   startX, startY,
                                                   pieces_on_the_board_objects[startX - 1][startY - 1].color, True,
                                                   False)
                    else:
                        change_piece_on_the_square(x, y, pieces_on_the_board_objects[startX - 1][startY - 1].symbol,
                                                   False,
                                                   startX, startY,
                                                   pieces_on_the_board_objects[startX - 1][startY - 1].color, False,
                                                   False)
                else:
                    change_piece_on_the_square(x, y, pieces_on_the_board_objects[startX - 1][startY - 1].symbol, False,
                                               startX, startY,
                                               pieces_on_the_board_objects[startX - 1][startY - 1].color,
                                               False, False)
                if turn == "white":
                    turn = "black"
                else:
                    turn = "white"
            elif pieces_on_the_board_objects[startX - 1][startY - 1].type == "King":
                if pieces_on_the_board_objects[startX - 1][
                    startY - 1].castling == True and deltaX2 == - 2 or deltaX2 == 2:
                    change_piece_on_the_square(x, y, pieces_on_the_board_objects[startX - 1][startY - 1].symbol, False,
                                               startX, startY,
                                               pieces_on_the_board_objects[startX - 1][startY - 1].color,
                                               False, True)
                else:
                    change_piece_on_the_square(x, y, pieces_on_the_board_objects[startX - 1][startY - 1].symbol, False,
                                               startX, startY,
                                               pieces_on_the_board_objects[startX - 1][startY - 1].color,
                                               False, False)
                if turn == "white":
                    turn = "black"
                else:
                    turn = "white"
            else:
                change_piece_on_the_square(x, y, pieces_on_the_board_objects[startX - 1][startY - 1].symbol, False,
                                           startX, startY, pieces_on_the_board_objects[startX - 1][startY - 1].color,
                                           False, False)
                if turn == "white":
                    turn = "black"
                else:
                    turn = "white"
            canvas.tag_raise(piece_items_in_canvas[x - 1][y - 1])
    else:
        pass
        squares_attacked_by_white_pieces = [[False for _ in range(8)] for _ in range(8)]
        squares_attacked_by_black_pieces = [[False for _ in range(8)] for _ in range(8)]
        drag_data = {"item": None, "x": None, "y": None, "startX": None, "startY": None}


def create_destroy_piece_choice_menu(color, create):
    global queen_button
    global rook_button
    global bishop_button
    global knight_button
    global pawn_promotion_menu_label
    global make_moves
    piece_selected = BooleanVar(value=False)
    label = Label(window)
    label.pack

    def chose_queen():
        global chosen_piece
        chosen_piece = "queen"
        destroy_buttons()
        piece_selected.set(True)

    def chose_rook():
        global chosen_piece
        chosen_piece = "rook"
        destroy_buttons()
        piece_selected.set(True)

    def chose_bishop():
        global chosen_piece
        chosen_piece = "bishop"
        destroy_buttons()
        piece_selected.set(True)

    def chose_knight():
        global chosen_piece
        chosen_piece = "knight"
        destroy_buttons()
        piece_selected.set(True)

    def destroy_buttons():
        queen_button.destroy()
        rook_button.destroy()
        bishop_button.destroy()
        knight_button.destroy()

    if create == True:
        if color == "white":
            queen_button = Button(pawn_promotion_menu_label, text=chr(0x2655), font=("Arial", int(square_size / 2)),
                                  command=chose_queen)
            queen_button.pack(side=LEFT)
            rook_button = Button(pawn_promotion_menu_label, text=chr(0x2656), font=("Arial", int(square_size / 2)),
                                 command=chose_rook)
            rook_button.pack(side=LEFT)
            bishop_button = Button(pawn_promotion_menu_label, text=chr(0x2657), font=("Arial", int(square_size / 2)),
                                   command=chose_bishop)
            bishop_button.pack(side=LEFT)
            knight_button = Button(pawn_promotion_menu_label, text=chr(0x2658), font=("Arial", int(square_size / 2)),
                                   command=chose_knight)
            knight_button.pack(side=LEFT)
        else:
            queen_button = Button(pawn_promotion_menu_label, text=chr(0x265B), font=("Arial", int(square_size / 2)),
                                  command=chose_queen)
            queen_button.pack(side=LEFT)
            rook_button = Button(pawn_promotion_menu_label, text=chr(0x265C), font=("Arial", int(square_size / 2)),
                                 command=chose_rook)
            rook_button.pack(side=LEFT)
            bishop_button = Button(pawn_promotion_menu_label, text=chr(0x265D), font=("Arial", int(square_size / 2)),
                                   command=chose_bishop)
            bishop_button.pack(side=LEFT)
            knight_button = Button(pawn_promotion_menu_label, text=chr(0x265E), font=("Arial", int(square_size / 2)),
                                   command=chose_knight)
            knight_button.pack(side=LEFT)
        make_moves = False
        label.wait_variable(piece_selected)
        make_moves = True
        return chosen_piece
    else:
        destroy_buttons()


canvas = Canvas(boardLabels, height=square_size * 9)
canvas.pack()
pawn_promotion_menu_label = Label(window, text="Here will be menu", font=('Arial', int(square_size / 2)), bg="white",
                                  fg="black")
pawn_promotion_menu_label.pack()
test_button = Button(window, text="Check king's situation", command=lambda: check_situation_of_the_king("white"))
test_button.pack()
create_chess_board()
start_function()
window.mainloop()