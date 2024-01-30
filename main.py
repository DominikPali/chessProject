import copy
from tkinter import *
import time
letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8"]
pieces_on_the_board_objects = [[None for _ in range(8)] for _ in range(8)]
pieces_on_the_board_objects_simulation = None
piece_items_in_canvas = [[None for _ in range(8)] for _ in range(8)]
square_items_in_canvas = [[None for _ in range(8)] for _ in range(8)]
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
list_of_situations_on_the_board = []
text_letters_canvas_items = [None, None, None, None, None, None, None, None]
text_numbers_canvas_items = [None, None, None, None, None, None, None, None]
who_is_on_bottom_of_the_board = "white"
turn = "white"
chosen_piece = None
make_moves = True
situation_of_white_king_global = None
situation_of_black_king_global = None
white_pieces_material = 0
black_pieces_material = 0
pieces_captured_by_black_pieces = []
pieces_captured_by_white_pieces = []
canvas_items_pieces_captured_by_black_pieces = []
canvas_items_pieces_captured_by_white_pieces = []
player1 = ""
player2 = ""
player1_score = 0
player2_score = 0
players_names_associated_with_color = {}
white_pieces_position = 0
black_pieces_position = 0
pawns_position_evaluation_data = [[0,  0,  0,  0,  0,  0,  0,  0],[50, 50, 50, 50, 50, 50, 50, 50],[10, 10, 20, 30, 30, 20, 10, 10],[5,  5, 10, 25, 25, 10,  5,  5],[0,  0,  0, 20, 20,  0,  0,  0],[5, -5,-10,  0,  0,-10, -5,  5],[5, 10, 10,-20,-20, 10, 10,  5],[0,  0,  0,  0,  0,  0,  0,  0]]
knights_position_evaluation_data = [[-50,-40,-30,-30,-30,-30,-40,-50],[-40,-20,  0,  0,  0,  0,-20,-40],[-30,  0, 10, 15, 15, 10,  0,-30],[-30,  5, 15, 20, 20, 15,  5,-30],[-30,  0, 15, 20, 20, 15,  0,-30],[-30,  5, 10, 15, 15, 10,  5,-30],[-40,-20,  0,  5,  5,  0,-20,-40],[-50,-40,-30,-30,-30,-30,-40,-50]]
bishops_position_evaluation_data = [[-20,-10,-10,-10,-10,-10,-10,-20],[-10,  0,  0,  0,  0,  0,  0,-10],[-10,  0,  5, 10, 10,  5,  0,-10],[-10,  5,  5, 10, 10,  5,  5,-10],[-10,  0, 10, 10, 10, 10,  0,-10],[-10, 10, 10, 10, 10, 10, 10,-10],[-10,  5,  0,  0,  0,  0,  5,-10],[-20,-10,-10,-10,-10,-10,-10,-20]]
rooks_position_evaluation_data = [[0,  0,  0,  0,  0,  0,  0,  0],[5, 10, 10, 10, 10, 10, 10,  5],[-5,  0,  0,  0,  0,  0,  0, -5],[-5,  0,  0,  0,  0,  0,  0, -5],[-5,  0,  0,  0,  0,  0,  0, -5],[-5,  0,  0,  0,  0,  0,  0, -5],[-5,  0,  0,  0,  0,  0,  0, -5],[0,  0,  0,  5,  5,  0,  0,  0]]
queens_position_evaluation = [[-20,-10,-10, -5, -5,-10,-10,-20],[-10,  0,  0,  0,  0,  0,  0,-10],[-10,  0,  5,  5,  5,  5,  0,-10],[-5,  0,  5,  5,  5,  5,  0, -5],[0,  0,  5,  5,  5,  5,  0, -5],[-10,  5,  5,  5,  5,  5,  0,-10],[-10,  0,  5,  0,  0,  0,  0,-10],[-20,-10,-10, -5, -5,-10,-10,-20]]
kings_position_evaluation = [[-30,-40,-40,-50,-50,-40,-40,-30],[-30,-40,-40,-50,-50,-40,-40,-30],[-30,-40,-40,-50,-50,-40,-40,-30],[-30,-40,-40,-50,-50,-40,-40,-30],[-20,-30,-30,-40,-40,-30,-30,-20],[-10,-20,-20,-20,-20,-20,-20,-10],[20, 20,  0,  0,  0,  0, 20, 20],[20, 30, 10,  0,  0, 10, 30, 20]]

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
        if name_of_the_piece == "Pawn":
            piece_symbol = chr(0x2659)
        if name_of_the_piece == "Knight":
            piece_symbol = chr(0x2658)
        if name_of_the_piece == "Bishop":
            piece_symbol = chr(0x2657)
        if name_of_the_piece == "Rook":
            piece_symbol = chr(0x2656)
        if name_of_the_piece == "Queen":
            piece_symbol = chr(0x2655)
        if name_of_the_piece == "King":
            piece_symbol = chr(0x2654)
    else:
        if name_of_the_piece == "Pawn":
            piece_symbol = chr(0x265F)
        if name_of_the_piece == "Knight":
            piece_symbol = chr(0x265E)
        if name_of_the_piece == "Bishop":
            piece_symbol = chr(0x265D)
        if name_of_the_piece == "Rook":
            piece_symbol = chr(0x265C)
        if name_of_the_piece == "Queen":
            piece_symbol = chr(0x265B)
        if name_of_the_piece == "King":
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
def return_x_y_of_the_square_black_on_bottom(x_coordinates, y_coordinates):
    x, y = return_x_y_of_the_square(x_coordinates, y_coordinates)
    x = 9 - x
    y = 9 - y
    return x, y
def adjust_indexing_by_substraction(value):
    if who_is_on_bottom_of_the_board == "white":
        return value*2
    else:
        return 7
def change_piece_on_the_square(x, y, piece_symbol, setting_pieces, startX, startY, color, enPassant, castling):
    global pieces_on_the_board
    global previous_moves
    global white_pieces_material
    global black_pieces_material
    global pieces_captured_by_white_pieces
    global pieces_captured_by_black_pieces
    piece_name = return_name_color_of_the_piece(piece_symbol)
    do_not_interfere = False
    canvas.itemconfig(piece_items_in_canvas[adjust_indexing_by_substraction(x - 1)-(x - 1)][adjust_indexing_by_substraction(y - 1)-(y - 1)], text=piece_symbol,
                      font=('Arial', int(square_size / 2)),
                      tags=("piece", x, y, piece_name, color))
    if setting_pieces and startX is None and startY is None:
        canvas.tag_bind("piece", '<ButtonPress-1>', on_drag_start)
        canvas.tag_bind("piece", '<B1-Motion>', on_drag_motion)
        canvas.tag_bind("piece", '<ButtonRelease-1>', on_drag_stop)
    else:
        canvas.itemconfig(piece_items_in_canvas[adjust_indexing_by_substraction(startX - 1)-(startX - 1)][adjust_indexing_by_substraction(startY - 1)-(startY - 1)], text=" ", font=('Arial', int(square_size / 2)),
                          tags=(x, y))
        if pieces_on_the_board_objects[x - 1][y - 1] is not None:
            if pieces_on_the_board_objects[x - 1][y - 1].color == "black":
                if enPassant == False:
                    black_pieces.remove(pieces_on_the_board_objects[x - 1][y - 1])
                    white_pieces_material += pieces_on_the_board_objects[x - 1][y - 1].value
                    pieces_captured_by_white_pieces.append(pieces_on_the_board_objects[x - 1][y - 1].symbol)
            elif pieces_on_the_board_objects[x - 1][y - 1].color == "white":
                if enPassant == False:
                    white_pieces.remove(pieces_on_the_board_objects[x - 1][y - 1])
                    black_pieces_material += pieces_on_the_board_objects[x - 1][y - 1].value
                    pieces_captured_by_black_pieces.append(pieces_on_the_board_objects[x - 1][y - 1].symbol)
            previous_moves.append({"x": x, "y": y, "startX": startX, "startY": startY,
                                   "colorOfTheMovedPiece": pieces_on_the_board_objects[startX - 1][startY - 1].color,
                                   "typeOfTheMovedPiece": pieces_on_the_board_objects[startX - 1][startY - 1].type,
                                   "capturedPieceType": pieces_on_the_board_objects[x - 1][y - 1].type})
        else:
            if enPassant == True:
                if pieces_on_the_board_objects[startX - 1][startY - 1].color == "white":
                    black_pieces.remove(pieces_on_the_board_objects[x - 1][y - 2])
                    white_pieces_material += pieces_on_the_board_objects[x - 1][y - 2].value
                    pieces_captured_by_white_pieces.append(pieces_on_the_board_objects[x - 1][y - 2].symbol)
                    pieces_on_the_board_objects[x - 1][y - 2] = None
                    canvas.itemconfig(piece_items_in_canvas[adjust_indexing_by_substraction(x - 1)-(x - 1)][adjust_indexing_by_substraction(y - 1)-(y - 1)], text=" ",
                                      font=('Arial', int(square_size / 2)),
                                      tags=("piece", x, y, piece_name, color))
                elif pieces_on_the_board_objects[startX - 1][startY - 1].color == "black":
                    white_pieces.remove(pieces_on_the_board_objects[x - 1][y])
                    black_pieces_material += pieces_on_the_board_objects[x - 1][y].value
                    pieces_captured_by_black_pieces.append(pieces_on_the_board_objects[x - 1][y].symbol)
                    pieces_on_the_board_objects[x - 1][y] = None
                    canvas.itemconfig(piece_items_in_canvas[adjust_indexing_by_substraction(x - 1)-(x - 1)][adjust_indexing_by_substraction(y - 1)-(y - 1)], text=" ",
                                      font=('Arial', int(square_size / 2)),
                                      tags=("piece", x, y, piece_name, color))
                previous_moves.append({"x": x, "y": y, "startX": startX, "startY": startY,
                                       "colorOfTheMovedPiece": pieces_on_the_board_objects[startX - 1][
                                           startY - 1].color,
                                       "typeOfTheMovedPiece": pieces_on_the_board_objects[startX - 1][
                                           startY - 1].type,
                                       "capturedPieceType": "Pawn"})
            elif castling == True:
                if color == "white":
                    rook_symbol = chr(0x2656)
                elif color == "black":
                    rook_symbol = chr(0x265C)
                previous_moves.append({"x": x, "y": y, "startX": startX, "startY": startY,
                                       "colorOfTheMovedPiece": pieces_on_the_board_objects[startX - 1][
                                           startY - 1].color,
                                       "typeOfTheMovedPiece": pieces_on_the_board_objects[startX - 1][startY - 1].type,
                                       "capturedPieceType": None})
                if (2, 0) in pieces_on_the_board_objects[startX - 1][startY - 1].possible_moves and x - startX == 2:
                    canvas.itemconfig(piece_items_in_canvas[adjust_indexing_by_substraction(x - 1)-(x - 1)][adjust_indexing_by_substraction(y - 1)-(y - 1)], text=rook_symbol,
                                      font=('Arial', int(square_size / 2)),
                                      tags=("piece", x, y, return_name_color_of_the_piece(rook_symbol), color))
                    canvas.itemconfig(piece_items_in_canvas[adjust_indexing_by_substraction(x - 1)-(x - 1)][adjust_indexing_by_substraction(y - 1)-(y - 1)], text=" ",
                                      font=('Arial', int(square_size / 2)),
                                      tags=(x, y))
                    pieces_on_the_board_objects[x - 2][y - 1] = pieces_on_the_board_objects[x][y - 1]
                    pieces_on_the_board_objects[x - 2][y - 1].x_L = x - 1
                    pieces_on_the_board_objects[x][y - 1] = None
                    pieces_on_the_board_objects[x - 1][y - 1] = pieces_on_the_board_objects[startX - 1][startY - 1]
                    pieces_on_the_board_objects[x - 1][y - 1].x_L = x
                    pieces_on_the_board_objects[startX - 1][startY - 1] = None
                elif (-2, 0) in pieces_on_the_board_objects[startX - 1][startY - 1].possible_moves and x - startX == -2:
                    canvas.itemconfig(piece_items_in_canvas[adjust_indexing_by_substraction(x - 1)-(x - 1)][adjust_indexing_by_substraction(y - 1)-(y - 1)], text=rook_symbol,
                                      font=('Arial', int(square_size / 2)),
                                      tags=("piece", x, y, return_name_color_of_the_piece(rook_symbol), color))
                    canvas.itemconfig(piece_items_in_canvas[adjust_indexing_by_substraction(x - 1)-(x - 1)][adjust_indexing_by_substraction(y - 1)-(y - 1)], text=" ",
                                      font=('Arial', int(square_size / 2)),
                                      tags=(x, y))
                    pieces_on_the_board_objects[x][y - 1] = pieces_on_the_board_objects[x - 3][y - 1]
                    pieces_on_the_board_objects[x][y - 1].x_L = x + 1
                    pieces_on_the_board_objects[x - 3][y - 1] = None
                    pieces_on_the_board_objects[x - 1][y - 1] = pieces_on_the_board_objects[startX - 1][startY - 1]
                    pieces_on_the_board_objects[x - 1][y - 1].x_L = x
                    pieces_on_the_board_objects[startX - 1][startY - 1] = None
                do_not_interfere = True
        if castling is False and enPassant == False:
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
                        canvas.itemconfig(piece_items_in_canvas[adjust_indexing_by_substraction(x - 1)-(x - 1)][adjust_indexing_by_substraction(y - 1)-(y - 1)],
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
                        canvas.itemconfig(piece_items_in_canvas[adjust_indexing_by_substraction(x - 1)-(x - 1)][adjust_indexing_by_substraction(y - 1)-(y - 1)],
                                          text=return_the_symbol_based_on_the_name_of_the_piece(piece,
                                                                                                pieces_on_the_board_objects[
                                                                                                    startX - 1][
                                                                                                    startY - 1].color),
                                          font=('Arial', int(square_size / 2)))
                        pieces_on_the_board_objects[startX - 1][startY - 1] = None
                        do_not_interfere = True
        if do_not_interfere == False:
            if pieces_on_the_board_objects[x - 1][y - 1] is None:
                previous_moves.append({"x": x, "y": y, "startX": startX, "startY": startY,
                                       "colorOfTheMovedPiece": pieces_on_the_board_objects[startX - 1][startY - 1].color,
                                       "typeOfTheMovedPiece": pieces_on_the_board_objects[startX - 1][startY - 1].type,
                                       "capturedPieceType": None})
            pieces_on_the_board_objects[x - 1][y - 1] = pieces_on_the_board_objects[startX - 1][startY - 1]
            pieces_on_the_board_objects[x - 1][y - 1].x_L = x
            pieces_on_the_board_objects[x - 1][y - 1].y_N = y
            pieces_on_the_board_objects[startX - 1][startY - 1] = None
def check_whether_the_move_will_affect_kings_situation(object, x, y):
    global pieces_on_the_board_objects_simulation
    global squares_attacked_by_white_pieces
    global squares_attacked_by_black_pieces
    can_make_this_move = None
    do_not_interfere = False
    king_object = None
    pieces_on_the_board_objects_simulation = copy.deepcopy(pieces_on_the_board_objects)
    if object.color == "white":
        if object.type == "Pawn":
            if object.enPassant == True and x == 1 or x == -1 and y == 1:
                pieces_on_the_board_objects_simulation[object.x_L + x - 1][object.y_N + y - 1] = \
                    pieces_on_the_board_objects_simulation[object.x_L - 1][object.y_N - 1]
                pieces_on_the_board_objects_simulation[object.x_L + x - 1][object.y_N + y - 1].x_L = object.x_L + x
                pieces_on_the_board_objects_simulation[object.x_L + x - 1][object.y_N + y - 1].y_N = object.y_N + y
                pieces_on_the_board_objects_simulation[object.x_L - 1][object.y_N - 1] = None
                pieces_on_the_board_objects_simulation[object.x_L + x - 1][object.y_N + y - 2] = None
                do_not_interfere = True
            else:
                pass
        if do_not_interfere == False:
            pieces_on_the_board_objects_simulation[object.x_L + x - 1][object.y_N + y - 1] = pieces_on_the_board_objects_simulation[object.x_L - 1][object.y_N - 1]
            pieces_on_the_board_objects_simulation[object.x_L + x - 1][object.y_N + y - 1].x_L = object.x_L + x
            pieces_on_the_board_objects_simulation[object.x_L + x - 1][object.y_N + y - 1].y_N = object.y_N + y
            pieces_on_the_board_objects_simulation[object.x_L - 1][object.y_N - 1] = None
        squares_attacked_by_black_pieces = [[False for _ in range(8)] for _ in range(8)]
        for i in range(8):
            for j in range(8):
                if pieces_on_the_board_objects_simulation[i][j] is not None:
                    if pieces_on_the_board_objects_simulation[i][j].color == "black":
                        pieces_on_the_board_objects_simulation[i][j].define_possible_moves(
                            pieces_on_the_board_objects_simulation)
                    if pieces_on_the_board_objects_simulation[i][j].color == "white":
                        if pieces_on_the_board_objects_simulation[i][j].type == "King":
                            king_object = pieces_on_the_board_objects_simulation[i][j]
        if squares_attacked_by_black_pieces[king_object.x_L - 1][king_object.y_N - 1] is True:
            can_make_this_move = False
    elif object.color == "black":
        if object.type == "Pawn":
            if object.enPassant == True and x == 1 or x == -1 and y == -1:
                pieces_on_the_board_objects_simulation[object.x_L + x - 1][object.y_N + y - 1] = \
                pieces_on_the_board_objects_simulation[object.x_L - 1][object.y_N - 1]
                pieces_on_the_board_objects_simulation[object.x_L + x - 1][object.y_N + y - 1].x_L = object.x_L + x
                pieces_on_the_board_objects_simulation[object.x_L + x - 1][object.y_N + y - 1].y_N = object.y_N + y
                pieces_on_the_board_objects_simulation[object.x_L - 1][object.y_N - 1] = None
                pieces_on_the_board_objects_simulation[object.x_L + x - 1][object.y_N + y] = None
                do_not_interfere = True
            else:
                pass
        if do_not_interfere == False:
            pieces_on_the_board_objects_simulation[object.x_L + x - 1][object.y_N + y - 1] = pieces_on_the_board_objects_simulation[object.x_L - 1][object.y_N - 1]
            pieces_on_the_board_objects_simulation[object.x_L + x - 1][object.y_N + y - 1].x_L = object.x_L + x
            pieces_on_the_board_objects_simulation[object.x_L + x - 1][object.y_N + y - 1].y_N = object.y_N + y
            pieces_on_the_board_objects_simulation[object.x_L - 1][object.y_N - 1] = None
        squares_attacked_by_white_pieces = [[False for _ in range(8)] for _ in range(8)]
        for i in range(8):
            for j in range(8):
                if pieces_on_the_board_objects_simulation[i][j] is not None:
                    if pieces_on_the_board_objects_simulation[i][j].color == "white":
                        pieces_on_the_board_objects_simulation[i][j].define_possible_moves(pieces_on_the_board_objects_simulation)
                    if pieces_on_the_board_objects_simulation[i][j].color == "black":
                        if pieces_on_the_board_objects_simulation[i][j].type == "King":
                            king_object = pieces_on_the_board_objects_simulation[i][j]
        if squares_attacked_by_white_pieces[king_object.x_L - 1][king_object.y_N - 1] is True:
            can_make_this_move = False
    if can_make_this_move is not False:
        can_make_this_move = True
    return can_make_this_move
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
                    do_not_interfere = False
                    pieces_on_the_board_objects_simulation = copy.deepcopy(pieces_on_the_board_objects)
                    if object.type == "Pawn":
                        if object.enPassant == True and x == 1 or x == -1 and y == 1:
                            pieces_on_the_board_objects_simulation[object.x_L + x - 1][object.y_N + y - 1] = \
                            pieces_on_the_board_objects_simulation[object.x_L - 1][object.y_N - 1]
                            pieces_on_the_board_objects_simulation[object.x_L + x - 1][object.y_N + y - 1].x_L = object.x_L + x
                            pieces_on_the_board_objects_simulation[object.x_L + x - 1][object.y_N + y - 1].y_N = object.y_N + y
                            pieces_on_the_board_objects_simulation[object.x_L - 1][object.y_N - 1] = None
                            pieces_on_the_board_objects_simulation[object.x_L + x - 1][object.y_N + y - 2] = None
                            do_not_interfere = True
                        else:
                            pass
                    if do_not_interfere == False:
                        pieces_on_the_board_objects_simulation[object.x_L + x - 1][object.y_N + y - 1] = \
                        pieces_on_the_board_objects_simulation[object.x_L - 1][object.y_N - 1]
                        pieces_on_the_board_objects_simulation[object.x_L + x - 1][object.y_N + y - 1].x_L = object.x_L + x
                        pieces_on_the_board_objects_simulation[object.x_L + x - 1][object.y_N + y - 1].y_N = object.y_N + y
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
                    do_not_interfere = False
                    pieces_on_the_board_objects_simulation = copy.deepcopy(pieces_on_the_board_objects)
                    if object.type == "Pawn":
                        if object.enPassant == True and x == 1 or x == -1 and y == -1:
                            pieces_on_the_board_objects_simulation[object.x_L + x - 1][object.y_N + y - 1] = pieces_on_the_board_objects_simulation[object.x_L - 1][object.y_N - 1]
                            pieces_on_the_board_objects_simulation[object.x_L + x - 1][object.y_N + y - 1].x_L = object.x_L + x
                            pieces_on_the_board_objects_simulation[object.x_L + x - 1][object.y_N + y - 1].y_N = object.y_N + y
                            pieces_on_the_board_objects_simulation[object.x_L - 1][object.y_N - 1] = None
                            pieces_on_the_board_objects_simulation[object.x_L + x - 1][object.y_N + y] = None
                            do_not_interfere = True
                        else:
                            pass
                    if do_not_interfere == False:
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
    return situation_of_the_king
def check_whether_stalemate():
    stalemate = True
    white_material = 0
    black_material = 0
    stalemate_material = True
    stalemate_moves = True
    stalemate_situation = True
    if turn == "white":
        for object in white_pieces:
            object.define_possible_moves(pieces_on_the_board_objects)
            if object.possible_moves != []:
                stalemate_moves = False
            if object.type != "King":
                white_material += object.value
    elif turn == "black":
        for object in black_pieces:
            object.define_possible_moves(pieces_on_the_board_objects)
            if object.possible_moves != []:
                stalemate_moves = False
            if object.type != "King":
                black_material += object.value
    if (black_material > 5 or any(obj.type == "Pawn" for obj in black_pieces)) or (white_material > 5 or any(obj.type == "Pawn" for obj in white_pieces)):
        stalemate_material = False
    for situation in list_of_situations_on_the_board:
        same_situations = 0
        for situation2 in list_of_situations_on_the_board:
            if situation == situation2:
                same_situations += 1
        if same_situations < 2:
            stalemate_situation = False
    if stalemate_moves == False and stalemate_material == False and stalemate_situation == False:
        stalemate = False
    return stalemate
def draw_situation_on_the_board():
    situation_on_the_board = [[None for _ in range(8)] for _ in range(8)]
    for i in range(8):
        for j in range(8):
            if pieces_on_the_board_objects[i][j] is not None:
                if pieces_on_the_board_objects[i][j].color == "white":
                    if pieces_on_the_board_objects[i][j].type == "King":
                        situation_on_the_board[i][j] = "WKing"
                    elif pieces_on_the_board_objects[i][j].type == "Queen":
                        situation_on_the_board[i][j] = "WQueen"
                    elif pieces_on_the_board_objects[i][j].type == "Rook":
                        situation_on_the_board[i][j] = "WRook"
                    elif pieces_on_the_board_objects[i][j].type == "Bischop":
                        situation_on_the_board[i][j] = "WBischop"
                    elif pieces_on_the_board_objects[i][j].type == "Knight":
                        situation_on_the_board[i][j] = "WKnight"
                    elif pieces_on_the_board_objects[i][j].type == "Pawn":
                        situation_on_the_board[i][j] = "WPawn"
                elif pieces_on_the_board_objects[i][j].color == "black":
                    if pieces_on_the_board_objects[i][j].type == "King":
                        situation_on_the_board[i][j] = "BKing"
                    elif pieces_on_the_board_objects[i][j].type == "Queen":
                        situation_on_the_board[i][j] = "BQueen"
                    elif pieces_on_the_board_objects[i][j].type == "Rook":
                        situation_on_the_board[i][j] = "BRook"
                    elif pieces_on_the_board_objects[i][j].type == "Bischop":
                        situation_on_the_board[i][j] = "BBischop"
                    elif pieces_on_the_board_objects[i][j].type == "Knight":
                        situation_on_the_board[i][j] = "BKnight"
                    elif pieces_on_the_board_objects[i][j].type == "Pawn":
                        situation_on_the_board[i][j] = "BPawn"
    return situation_on_the_board
class Pawn():
    def __init__(self, color, x_L, y_N):
        self.color = color
        self.x_L = x_L
        self.y_N = y_N
        self.piece_id = piece_items_in_canvas[x_L - 1][y_N - 1]
        self.possible_moves = []
        self.type = "Pawn"
        self.enPassant = False
        self.value = 1
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
                        and last_move["colorOfTheMovedPiece"] != self.color
                        and last_move["capturedPieceType"] == None):
                    if last_move["typeOfTheMovedPiece"] == "Pawn":
                        if self.y_N == 5:
                            self.enPassant = True
                            add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, last_move["x"] - self.x_L, 1, pieces_on_the_board_objects_data)
        else:
            if len(previous_moves) != 0:
                if (last_move["x"] == self.x_L - 1 or last_move["x"] == self.x_L + 1 and last_move["y"] == self.y_N
                        and last_move["startX"] == last_move["x"] and last_move["startY"] == 2
                        and last_move["colorOfTheMovedPiece"] != self.color
                        and last_move["capturedPieceType"] == None):
                    if last_move["typeOfTheMovedPiece"] == "Pawn":
                        if self.y_N == 4:
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
        self.value = 3
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
        self.value = 3
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
        self.value = 5
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
        self.value = 9
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
                    add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, deltaX, deltaY,pieces_on_the_board_objects_data)
                elif pieces_on_the_board_objects_data[self.x_L + deltaX - 1][self.y_N + deltaY - 1] is not None:
                    if pieces_on_the_board_objects_data[self.x_L + deltaX - 1][self.y_N + deltaY - 1].color != self.color:
                        add_to_list_of_possible_moves_and_attacked_squares(self.x_L, self.y_N, deltaX, deltaY,pieces_on_the_board_objects_data)
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
                        if(pieces_on_the_board_objects_data[self.x_L + 1 - 1][self.y_N - 1] is not None
                            or pieces_on_the_board_objects_data[self.x_L + 2 - 1][self.y_N - 1] is not None):
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
                                or pieces_on_the_board_objects_data[self.x_L - 2 - 1][self.y_N - 1] is not None
                                or pieces_on_the_board_objects_data[self.x_L - 3 - 1][self.y_N - 1] is not None):
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
def wait_for_players_names():
    players_names_entered = BooleanVar(value=False)
    global player1
    global player2
    def button_clicked():
        if input1.get() != "" and input2.get() != "" and input1.get() != input2.get():
            players_names_entered.set(True)

    def on_entry_click1(event):
        if input1.get() == "Enter the name of the first player":
            input1.delete(0, END)
    def on_entry_click2(event):
        if input2.get() == "Enter the name of the second player":
            input2.delete(0, END)
    input1 = Entry(window, width=int(square_size/3*2))
    input1.pack()
    input2 = Entry(window, width=int(square_size/3*2))
    input2.pack()
    input1.insert(0, "Enter the name of the first player")
    input2.insert(0, "Enter the name of the second player")
    input1.bind("<FocusIn>", on_entry_click1)
    input2.bind("<FocusIn>", on_entry_click2)
    submit_players_names_button = Button(window, text="Submit", command=button_clicked)
    submit_players_names_button.pack()
    window.wait_variable(players_names_entered)
    player1 = str(input1.get())
    player2 = str(input2.get())
    input1.destroy()
    input2.destroy()
    submit_players_names_button.destroy()
    global players_names_associated_with_color
    players_names_associated_with_color = {player1:"white", player2:"black"}
window = Tk()
square_size = int(window.winfo_screenheight()/18)
window.attributes('-fullscreen', True)
window.configure(bg="#4a4a4a")
wait_for_players_names()
title_label = Label(window, text="Chess", font=('Impact', int(square_size*1.5)), bg="#4a4a4a", fg="#ffffff")
title_label.pack()
player_on_the_top_of_the_board_label = Label(window, text=player2, font=("Oswald", int(square_size/2)), bg="#4a4a4a", fg="#ffffff")
player_on_the_top_of_the_board_label.pack()
chessLabel = Label(window, bg="#4a4a4a")
chessLabel.pack(anchor="n")
score_label = Label(window, text="Score: " + player1 + ": " + str(player1_score) + " ; " + player2 + ": " + str(player2_score), font=("Impact", int(square_size/2)), bg="#4a4a4a", fg="#ffffff")
score_label.place(x=int(square_size * 3.5), y=int(square_size*3))
materialLabelTop = Label(chessLabel, bg="#4a4a4a", font=int(square_size * 0.75))
materialLabelTop.pack()
canvas_material_top = Canvas(materialLabelTop, height=square_size, bg="#4a4a4a", width=square_size*9)
canvas_material_top.pack()
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
    global adjust_indexing
    if players_names_associated_with_color[player1] == "white":
        key_with_value_black = player2
        key_with_value_white = player1
    else:
        key_with_value_black = player1
        key_with_value_white = player2
    if who_is_on_bottom_of_the_board == "white":
        for i in range(8):
            canvas.itemconfig(text_letters_canvas_items[i], text=letters[7 - i],
                              font=('Arial', int(square_size / 2)))
            canvas.itemconfig(text_numbers_canvas_items[i], text=numbers[i],
                              font=('Arial', int(square_size / 2)))
        for i in range(8):
            for j in range(8):
                canvas.itemconfig(piece_items_in_canvas[i][j], text=" ",
                                  font=('Arial', int(square_size / 2)),
                                  tags=(i+1, j+1))
        for i in range(8):
            for j in range(8):
                if pieces_on_the_board_objects[i][j] is not None:
                    canvas.itemconfig(piece_items_in_canvas[7-i][7-j],
                                      text=return_the_symbol_based_on_the_name_of_the_piece(pieces_on_the_board_objects[i][j].type, pieces_on_the_board_objects[i][j].color),
                                      font=('Arial', int(square_size / 2)),
                                      tags=("piece", i + 1, j + 1))
                    canvas.tag_bind("piece", '<ButtonPress-1>', on_drag_start)
                    canvas.tag_bind("piece", '<B1-Motion>', on_drag_motion)
                    canvas.tag_bind("piece", '<ButtonRelease-1>', on_drag_stop)
        who_is_on_bottom_of_the_board = "black"
        player_on_the_bottom_of_the_board_label.config(text=key_with_value_black)
        player_on_the_top_of_the_board_label.config(text=key_with_value_white)
    elif who_is_on_bottom_of_the_board == "black":
        for j in range(8):
            canvas.itemconfig(text_letters_canvas_items[j], text=letters[j],
                              font=('Arial', int(square_size / 2)))
            canvas.itemconfig(text_numbers_canvas_items[j], text=numbers[7 - j],
                              font=('Arial', int(square_size / 2)))
        for i in range(8):
            for j in range(8):
                canvas.itemconfig(piece_items_in_canvas[i][j], text=" ",
                                  font=('Arial', int(square_size / 2)),
                                  tags=(i+1, j+1))
        for i in range(8):
            for j in range(8):
                if pieces_on_the_board_objects[i][j] is not None:
                    canvas.itemconfig(piece_items_in_canvas[i][j],
                                      text=return_the_symbol_based_on_the_name_of_the_piece(pieces_on_the_board_objects[i][j].type, pieces_on_the_board_objects[i][j].color),
                                      font=('Arial', int(square_size / 2)),
                                      tags=("piece", i + 1, j + 1))
                    canvas.tag_bind("piece", '<ButtonPress-1>', on_drag_start)
                    canvas.tag_bind("piece", '<B1-Motion>', on_drag_motion)
                    canvas.tag_bind("piece", '<ButtonRelease-1>', on_drag_stop)
        who_is_on_bottom_of_the_board = "white"
        player_on_the_bottom_of_the_board_label.config(text=key_with_value_white)
        player_on_the_top_of_the_board_label.config(text=key_with_value_black)
def update_pieces_captured_by_white_and_black_pieces():
    global canvas_material_bottom
    global canvas_material_top
    last_x0_black = 0
    last_x0_white = 0
    if black_pieces_material != 0:
        for i in canvas_items_pieces_captured_by_black_pieces:
            canvas_material_top.delete(i)
        for j, symbol in enumerate(pieces_captured_by_black_pieces):
            x0 = j*int(square_size/3) + int(square_size/2)
            y0 = int(square_size/4)
            piece = canvas_material_top.create_text(x0, y0 + int(square_size / 4), text=symbol, font=("Arial", int(square_size / 2)))
            canvas_items_pieces_captured_by_black_pieces.append(piece)
            last_x0_black = x0
        piece2 = canvas_material_top.create_text(last_x0_black + int(square_size / 2) + int(square_size / 4),
                                                 int(square_size / 2), text="+" + str(black_pieces_material),
                                                 font=("Arial", int(square_size / 2)))
        canvas_items_pieces_captured_by_black_pieces.append(piece2)
    if white_pieces_material != 0:
        for i in canvas_items_pieces_captured_by_white_pieces:
            canvas_material_bottom.delete(i)
        for i, symbol in enumerate(pieces_captured_by_white_pieces):
            x0 = i*int(square_size/3) + int(square_size/2)
            y0 = int(square_size/4)
            piece = canvas_material_bottom.create_text(x0, y0 + int(square_size / 4), text=symbol, font=("Arial", int(square_size / 2)))
            canvas_items_pieces_captured_by_white_pieces.append(piece)
            last_x0_white = x0
        piece = canvas_material_bottom.create_text(last_x0_white + int(square_size / 2) + int(square_size/4), int(square_size/2), text="+" + str(white_pieces_material),
                                                   font=("Arial", int(square_size / 2)))
        canvas_items_pieces_captured_by_white_pieces.append(piece)
def on_drag_start(event):
    global drag_data
    if who_is_on_bottom_of_the_board == "white":
        row, col = return_x_y_of_the_square(event.x, event.y)
    else:
        row, col = return_x_y_of_the_square_black_on_bottom(event.x, event.y)
    closest_item = piece_items_in_canvas[adjust_indexing_by_substraction(row - 1)-(row - 1)][adjust_indexing_by_substraction(col - 1)-(col - 1)]
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
    global situation_of_white_king_global
    global situation_of_black_king_global
    global win_label
    canvas.coords(drag_data["item"], drag_data["startX"], drag_data["startY"])
    change_piece = False
    canvas.delete(drag_data["rectangle"])
    if who_is_on_bottom_of_the_board == "white":
        x, y = return_x_y_of_the_square(drag_data["x"], drag_data["y"])
        startX, startY = return_x_y_of_the_square(drag_data["startX"], drag_data["startY"])
    else:
        x, y = return_x_y_of_the_square_black_on_bottom(drag_data["x"], drag_data["y"])
        startX, startY = return_x_y_of_the_square_black_on_bottom(drag_data["startX"], drag_data["startY"])
    deltaX2 = x - startX
    deltaY2 = y - startY
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
                if check_whether_the_move_will_affect_kings_situation(pieces_on_the_board_objects[startX-1][startY-1], deltaX, deltaY) == True:
                    change_piece = True
    if change_piece:
        if pieces_on_the_board_objects[startX - 1][startY - 1].color == turn:
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
            list_of_situations_on_the_board.append(draw_situation_on_the_board())
            if check_situation_of_the_king("white") != "checkmate":
                situation_of_white_king_global = check_situation_of_the_king("white")
                update_pieces_captured_by_white_and_black_pieces()
            elif check_situation_of_the_king("white") == "checkmate":
                situation_of_white_king_global = check_situation_of_the_king("white")
                canvas.destroy()
                boardLabels.destroy()
                materialLabelTop.destroy()
                materialLabelBottom.destroy()
                chessLabel.destroy()
                score_label.destroy()
                title_label.destroy()
                player_on_the_top_of_the_board_label.destroy()
                player_on_the_bottom_of_the_board_label.destroy()
                if players_names_associated_with_color[player1] == "black":
                    player_who_won = player1
                elif players_names_associated_with_color[player2] == "black":
                    player_who_won = player2
                want_to_play_again("black", player_who_won)
            if check_situation_of_the_king("black") != "checkmate":
                situation_of_black_king_global = check_situation_of_the_king("black")
                update_pieces_captured_by_white_and_black_pieces()
            elif check_situation_of_the_king("black") == "checkmate":
                situation_of_black_king_global = check_situation_of_the_king("black")
                canvas.destroy()
                boardLabels.destroy()
                materialLabelTop.destroy()
                materialLabelBottom.destroy()
                chessLabel.destroy()
                score_label.destroy()
                title_label.destroy()
                player_on_the_top_of_the_board_label.destroy()
                player_on_the_bottom_of_the_board_label.destroy()
                if players_names_associated_with_color[player1] == "white":
                    player_who_won = player1
                elif players_names_associated_with_color[player2] == "white":
                    player_who_won = player2
                want_to_play_again("white", player_who_won)
            if check_situation_of_the_king("black") != "checkmate" and check_situation_of_the_king("white") != "checkmate":
                if check_whether_stalemate() == True:
                    canvas.destroy()
                    boardLabels.destroy()
                    materialLabelTop.destroy()
                    materialLabelBottom.destroy()
                    chessLabel.destroy()
                    score_label.destroy()
                    title_label.destroy()
                    player_on_the_top_of_the_board_label.destroy()
                    player_on_the_bottom_of_the_board_label.destroy()
                    want_to_play_again(None, "Nobody")
                else:
                    reverse_the_board()
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
    pawn_promotion_menu_label = Label(window, font=('Arial', int(square_size / 2)),
                                      bg="white",
                                      fg="black")
    pawn_promotion_menu_label.pack()
    label = Label(window)
    label.pack()

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
        pawn_promotion_menu_label.destroy()
        label.destroy()
        return chosen_piece
    else:
        destroy_buttons()
def want_to_play_again(who_won, player_who_won):
    win_label = Label(window, text=player_who_won + " won", font=("Impact", int(square_size * 2)),
                      bg="#4a4a4a", fg="white")
    win_label.pack(anchor="n")
    def want_to_play_again():
        continue_th_game_or_not(False)
    def do_not_want_to_play_again():
        continue_th_game_or_not(True)
    def continue_th_game_or_not(window_destroy):
        if window_destroy == True:
            window.destroy()
        elif window_destroy == False:
            global player1_score
            global player2_score
            global players_names_associated_with_color
            global pieces_on_the_board_objects
            if who_won == "white":
                if players_names_associated_with_color[player1] == "white":
                    player1_score += 1
                elif players_names_associated_with_color[player2] == "white":
                    player2_score += 1
            elif who_won == "black":
                if players_names_associated_with_color[player1] == "black":
                    player1_score += 1
                elif players_names_associated_with_color[player2] == "black":
                    player2_score += 1
            global pieces_on_the_board_objects_simulation, piece_items_in_canvas, square_items_in_canvas, drag_data, black_pieces, white_pieces, squares_attacked_by_white_pieces, squares_attacked_by_black_pieces,\
                previous_moves, list_of_situations_on_the_board, text_letters_canvas_items, text_numbers_canvas_items, who_is_on_bottom_of_the_board, turn, chosen_piece, make_moves, situation_of_white_king_global, \
                situation_of_black_king_global, white_pieces_material, black_pieces_material, pieces_captured_by_black_pieces, pieces_captured_by_white_pieces, canvas_items_pieces_captured_by_black_pieces, \
                canvas_items_pieces_captured_by_white_pieces
            pieces_on_the_board_objects = [[None for _ in range(8)] for _ in range(8)]
            pieces_on_the_board_objects_simulation = None
            piece_items_in_canvas = [[None for _ in range(8)] for _ in range(8)]
            square_items_in_canvas = [[None for _ in range(8)] for _ in range(8)]
            drag_data = {"item": None, "x": None, "y": None, "startX": None, "startY": None, "rectangle": None}
            black_pieces = []
            white_pieces = []
            squares_attacked_by_white_pieces = [[False for _ in range(8)] for _ in range(8)]
            squares_attacked_by_black_pieces = [[False for _ in range(8)] for _ in range(8)]
            previous_moves = []
            list_of_situations_on_the_board = []
            text_letters_canvas_items = [None, None, None, None, None, None, None, None]
            text_numbers_canvas_items = [None, None, None, None, None, None, None, None]
            who_is_on_bottom_of_the_board = "white"
            turn = "white"
            chosen_piece = None
            make_moves = True
            situation_of_white_king_global = None
            situation_of_black_king_global = None
            white_pieces_material = 0
            black_pieces_material = 0
            pieces_captured_by_black_pieces = []
            pieces_captured_by_white_pieces = []
            canvas_items_pieces_captured_by_black_pieces = []
            canvas_items_pieces_captured_by_white_pieces = []
            question_label.destroy()
            button_play_again.destroy()
            button_stop_playing.destroy()
            win_label.destroy()
            global chessLabel, score_label, materialLabelTop, canvas_material_top, boardLabels, canvas, materialLabelBottom, canvas_material_bottom,\
                player_on_the_top_of_the_board_label, player_on_the_bottom_of_the_board_label, title_label
            title_label = Label(window, text="Chess", font=('Impact', int(square_size * 1.5)), bg="#4a4a4a",
                                fg="#ffffff")
            title_label.pack()
            player_on_the_top_of_the_board_label = Label(window, text=player1,
                                                         font=("Oswald", int(square_size / 2)), bg="#4a4a4a",
                                                         fg="#ffffff")
            player_on_the_top_of_the_board_label.pack()
            chessLabel = Label(window, bg="#4a4a4a")
            chessLabel.pack(anchor="n")
            score_label = Label(window, text="Score: " + player1 + ": " + str(player1_score) + " ; " + player2 + ": " + str(player2_score),
                                font=("Impact", int(square_size / 2)), bg="#4a4a4a", fg="#ffffff")
            score_label.place(x=int(square_size * 4), y=int(square_size * 1.66))
            materialLabelTop = Label(chessLabel, bg="#4a4a4a", font=int(square_size * 0.75))
            materialLabelTop.pack()
            canvas_material_top = Canvas(materialLabelTop, height=square_size, bg="#4a4a4a", width=square_size * 9)
            canvas_material_top.pack()
            boardLabels = Label(chessLabel, bg="#4a4a4a")
            boardLabels.pack()
            canvas = Canvas(boardLabels, height=square_size * 9, width=square_size * 9)
            canvas.pack()
            materialLabelBottom = Label(chessLabel, text="Here black's captured pieces will be shown",
                                        font=int(square_size * 0.75), bg="#4a4a4a")
            materialLabelBottom.pack()
            canvas_material_bottom = Canvas(materialLabelBottom, height=square_size, bg="#4a4a4a",
                                            width=square_size * 9)
            canvas_material_bottom.pack()
            player_on_the_bottom_of_the_board_label = Label(window, text=player2,
                                                            font=("Oswald", int(square_size / 2)), bg="#4a4a4a",
                                                            fg="#ffffff")
            player_on_the_bottom_of_the_board_label.pack()
            if players_names_associated_with_color[player1] == "black":
                players_names_associated_with_color[player1] = "white"
                players_names_associated_with_color[player2] = "black"
                player_on_the_bottom_of_the_board_label.config(text=player1)
                player_on_the_top_of_the_board_label.config(text=player2)
            elif players_names_associated_with_color[player1] == "white":
                players_names_associated_with_color[player1] = "black"
                players_names_associated_with_color[player2] = "white"
                player_on_the_bottom_of_the_board_label.config(text=player2)
                player_on_the_top_of_the_board_label.config(text=player1)

            player_on_the_bottom_of_the_board_label.pack()
            create_chess_board()
            start_function()
            list_of_situations_on_the_board.append(draw_situation_on_the_board())


    question_label = Label(window, text="Do you want to play again?")
    question_label.pack()
    button_play_again = Button(window, text="Yes", command=want_to_play_again)
    button_play_again.pack()
    button_stop_playing = Button(window, text="No", command=do_not_want_to_play_again)
    button_stop_playing.pack()
canvas = Canvas(boardLabels, height=square_size * 9, width=square_size * 9)
canvas.pack()
create_chess_board()
start_function()
list_of_situations_on_the_board.append(draw_situation_on_the_board())
materialLabelBottom = Label(chessLabel, text="Here black's captured pieces will be shown", font=int(square_size * 0.75), bg="#4a4a4a")
materialLabelBottom.pack()
canvas_material_bottom = Canvas(materialLabelBottom, height=square_size, bg="#4a4a4a", width=square_size * 9)
canvas_material_bottom.pack()
player_on_the_bottom_of_the_board_label = Label(window, text=player1, font=("Oswald", int(square_size/2)), bg="#4a4a4a", fg="#ffffff")
player_on_the_bottom_of_the_board_label.pack()
window.mainloop()