from Constants import BLACK_PAWN, WHITE_PAWN
from Board import Board
from Player import Player
from random import random

SCORE_MAX = 10000
SCORE_MIN = -10000
SCORE_THREE = 100
"""The AIPlayer class inherits Player
   it has a new attribute pos_score in order to store the value of each Tile
"""


class AIPlayer(Player):
    def __init__(self, playerNumber: int = 0, color: bool = WHITE_PAWN) -> None:
        Player.__init__(self, playerNumber, color)
        self.pos_score = [[1, 2, 1], [2, 3, 2], [1, 2, 1]]


"""
    here are some actions that AIPlayer can do as humain
"""


# the AIPlayer do the place circle action
def placeCircularPawn(self, board:Board, x: int = 0, y: int = 0) -> int:
    playNumber = self.getPlayerNumber
    board.placeCircularPawn(playNumber, x, y)


# the AIPlayer do the move circle action
def moveCircularPawn(self, board:Board , pre_tile, next_x, next_y) -> int:
    playNumber = self.getPlayerNumber
    board.moveCircularPawn(playNumber, pre_tile, next_x, next_y)


# the AIPlayer do the move square action
def moveSquarePawn(self, board:Board, x: int = 0, y: int = 0) -> int:
    tile = board[x][y]
    diff = math.fabs(tile.idTile - board.emptyTile.idTile)

    if ([board.emptyTile, tile] == board.squarePawnMoved):
        return -1

    if (diff == 1 or diff == 3):
        board.twoSquarePawnsMoved = None
        board.squarePawnMoved = [tile, board.emptyTile]
        squarePawn = tile.getSquarePawn()
        tile.setSquarePawn(None)
        board.emptyTile.setSquarePawn(squarePawn)
        board.emptyTile = tile
        return 0
    else:
        return -2


#
def isMove2SquarePawnsPossible(board:Board) -> bool:
    return board.emptyTile.idTile != 5


def move2SquarePawns(self, board:Board, x: list = [0, 0], y: list = [0, 0]) -> int:
    firstTile = board[int(x[0]), int(y[0])]
    secondTile = board[int(x[1]), int(y[1])]

    board.squarePawnMoved = None

    if (not board.isMove2SquarePawnsPossible()):
        return -1

    if ([firstTile, secondTile] == board.twoSquarePawnsMoved):
        return -2

    diff = math.fabs(firstTile.idTile - board.emptyTile.idTile)
    if (diff != 1 and diff != 3):
        return -3

    diff = math.fabs(firstTile.idTile - secondTile.idTile)
    if (diff != 1 and diff != 3):
        return -4

    if (not ((secondTile.x == firstTile.x and secondTile.x == board.emptyTile.x) or
             (secondTile.y == firstTile.y and secondTile.y == board.emptyTile.y))):
        return -5

    board.twoSquarePawnsMoved = None
    firstSquarePawn = firstTile.getSquarePawn()
    secondSquarePawn = secondTile.getSquarePawn()
    firstTile.setSquarePawn(secondSquarePawn)
    secondTile.setSquarePawn(None)
    board.emptyTile.setSquarePawn(firstSquarePawn)

    board.twoSquarePawnsMoved = [firstTile, board.emptyTile]
    board.emptyTile = secondTile


"""These functions below is to help us choose the best step and choose the action to execute according to the situation
   We use the founction 'Evaluate' to evaluate the score(This score is determined by the scores of yourself and your opponent on the current board) of each Tile
   We use the function 'Renew_Score' to update the score and sort it in descending order
   We use a function 'findBestStep' to generate a tree at the depth of 4, and use alpha-bete to find the best choice based on the next situation
   After completing the determination of the best step, we use the function 'play' to use the appropriate action function and play it
"""
# the AIPlayer chose the best way to play after evalue this tiles
"""def play(self, board:Board):
    x, y = self.findBestStep(board, self.getPlayerNumber, 4)
    if (self.isCircularPawnAvailable):
        self.placeCircularPawn(board, x, y)
"""            
# renew the score of every tile in list moves
def Renew_Score(self, board:Board, turn):
    scores = []
    for y in range(3):
        for x in range(3):
            if not board[y][x].getPlyernumber():
                score = self.pos_score[y][x]
                moves.append((score, x, y))
    scores.sort(reverse=True)
    return moves


# fine the best position at depth
def findBestStep(self, board:Board, turn, depth, alpha=SCORE_MIN, beta=SCORE_MAX) -> int:
    score = self.Evaluate(board, turn)

    if depth <= 0 or score == SCORE_THREE:
        return score
    scores = self.Renew_Score(board, turn)
    bestmove = None

    for _, y, x in scores:
        # set the present tile of the player turn
        if board[x][y].SquarePawn:
            board[x][y].setCircularPawn(CircularPawn(turn, self.color, Board[y][x].idTile, x, y))
        else:
            board[x][y].setSquarePawn.setNewCircular(turn, self.color, Board[y][x].idTile, x, y)

        if turn == 1:
            op_turn = 0
        else:
            op_turn = 1

        score = -self.findBestStep(board, op_turn, depth - 1, -beta, -alpha)

        board[x][y].getCircularPawn.PlayerNumber = None
        self.beta += 1

        if score > alpha:
            bestmove = (x, y)
            if alpha >= beta:
                break
    if depth == 4 and bestmove:
        self.bestmove = bestmove
    x, y = self.bestmove
    return (x, y)


# the founction to evaluate the score of every tile
def Evaluate(self, board:Board, turn):
    if turn == 0:
        mine = 1
        opponent = 2
    else:
        mine = 2
        opponent = 1
    record = [[[0,0]for x in range(3)]for y in range(3)]
    for x in range(3):
        for y in range(3):
            if not board[x][y].getPlyernumber():
                mscore[x][y] = self.evaluatescore(board, x, y, mine, opponent)
                oscore[x][y] = self.evaluatescore(board, x, y, opponent, mine)
            else:
                mscore[x][y] = oscore[x][y]
    return (mscore - oscore)


# evaluate the score of tile[x][y]
def evaluatescore(self, board:Board, x, y, mine, opponent):
    score = 0
    if x - 1 < 0 and y - 1 < 0:
        if (board[x + 1][y].getPlyernumber() == mine or board[x + 2][y].getPlayernumber() == mine):
            if (board[x + 1][y].getPlyernumber() == opponent or board[x + 2][y].getPlayernumber() == opponent):
                score+=5
            elif(board[x + 1][y].getPlyernumber() == mine and board[x + 2][y].getPlayernumber() == mine):
                score+=100
            else:
                score+=25
            record[x + 1][y][mine - 1] = score
            record[x + 2][y][mine - 1] = score
        elif (board[x][y + 1].getPlyernumber() == mine or board[x][y + 2].getPlayernumber() == mine):
            if (board[x][y + 1].getPlyernumber() == opponent or board[x][y + 2].getPlayernumber() == opponent):
                score+=5
            elif (board[x][y + 1].getPlyernumber() == mine and board[x][y + 2].getPlayernumber() == mine):
                score+=100
            else:
                score+=25
            record[x][y + 1][mine - 1] = score
            record[x][y + 2][mine - 1] = score
        elif (board[x + 1][y + 1].getPlyernumber() == mine and board[x + 2][y + 2].getPlayernumber() == mine):
            if (board[x + 1][y + 1].getPlyernumber() == opponent and board[x + 2][y + 2].getPlayernumber() == opponent):
                score+=5
            elif (board[x + 1][y + 1].getPlyernumber() == mine and board[x + 2][y + 2].getPlayernumber() == mine):
                score+=100
            else:
                score+=25
            record[x + 1][y + 1][mine - 1] = score
            record[x + 2][y + 2][mine - 1] = score
    elif x - 2 < 0 and y - 1 < 0:
        if(board[x - 1][y].getPlyernumber() == mine or board[x + 1][y].getPlyernumber() == mine):
            if (board[x - 1][y].getPlyernumber() == opponent or board[x + 1][y].getPlyernumber() == opponent):
                score+=5
            elif(board[x - 1][y].getPlyernumber() == mine and board[x + 1][y].getPlyernumber() == mine):
                score+=100
            else:
                score+=25
            record[x - 1][y][mine - 1] = score
            record[x + 1][y][mine - 1] = score
        elif (board[x][y + 1].getPlyernumber() == mine or board[x][y + 2].getPlyernumber() == mine):
            if (board[x][y + 1].getPlyernumber() == opponent or board[x][y + 2].getPlyernumber() == opponent):
                score+=5
            elif(board[x][y + 1].getPlyernumber() == mine and board[x][y + 2].getPlyernumber() == mine):
                score+=100
            else:
                score+=25
            record[x + 1][y + 1][mine - 1] = score
            record[x + 2][y + 2][mine - 1] = score
    elif x - 3 < 0 and y - 1 < 0:
        if (board[x - 1][y].getPlyernumber() == mine or board[x - 2][y].getPlyernumber() == mine):
            if (board[x - 1][y].getPlyernumber() == opponent or board[x - 2][y].getPlyernumber() == opponent):
                score+=5
            elif(board[x - 1][y].getPlyernumber() == mine and board[x - 2][y].getPlyernumber() == mine):
                score+=100
            else:
                score+=25
            record[x - 1][y][mine - 1] = score
            record[x - 2][y][mine - 1] = score
        elif (board[x - 1][y + 1].getPlyernumber() == mine or board[x - 2][y + 2].getPlayernumber() == mine):
            if (board[x - 1][y + 1].getPlyernumber() == opponent or board[x - 2][y + 2].getPlayernumber() == opponent):
                score+=5
            elif (board[x - 1][y + 1].getPlyernumber() == mine and board[x - 2][y + 2].getPlayernumber() == mine):
                score+=100
            else:
                score+=25
            record[x - 1][y + 1][mine - 1] = score
            record[x - 2][y + 2][mine - 1] = score
        elif (board[x][y - 1].getPlyernumber() == mine or board[x][y - 2].getPlayernumber() == mine):
            if (board[x][y - 1].getPlyernumber() == opponent or board[x][y - 2].getPlayernumber() == opponent):
                score+=5
            elif (board[x][y - 1].getPlyernumber() == mine and board[x][y - 2].getPlayernumber() == mine):
                score+=100
            else:
                score+=25
            record[x][y - 1][mine - 1] = score
            record[x][y - 2][mine - 1] = score
    elif x - 1 < 0 and y - 2 < 0:
        if (board[x][y - 1].getPlyernumber() == mine or board[x][y + 1].getPlayernumber() == mine):
            if (board[x][y - 1].getPlyernumber() == opponent or board[x][y + 1].getPlayernumber() == opponent):
                score+=5
            elif (board[x][y - 1].getPlyernumber() == mine and board[x][y + 1].getPlayernumber() == mine):
                score+=100
            else:
                score+=25
            record[x][y - 1][mine - 1] = score
            record[x][y + 1][mine - 1] = score
        elif (board[x + 1][y].getPlyernumber() == mine or board[x + 2][y].getPlayernumber() == mine):
            if (board[x + 1][y].getPlyernumber() == opponent or board[x + 2][y].getPlayernumber() == opponent):
                score+=5
            elif (board[x + 1][y].getPlyernumber() == mine and board[x + 2][y].getPlayernumber() == mine):
                score+=100
            else:
                score+=25
            record[x + 1][y][mine - 1] = score
            record[x + 2][y][mine - 1] = score
    elif x - 2 < 0 and y - 2 < 0:
        if (board[x - 1][y - 1].getPlyernumber() == mine or board[x + 1][y + 1].getPlayernumber() == mine):
            if (board[x - 1][y - 1].getPlyernumber() == opponent or board[x + 1][y + 1].getPlayernumber() == opponent):
                score+=5
            elif (board[x - 1][y - 1].getPlyernumber() == mine and board[x + 1][y + 1].getPlayernumber() == mine):
                score+=100
            else:
                score+=25
            record[x - 1][y - 1][mine - 1] = score
            record[x + 1][y + 1][mine - 1] = score
        elif (board[x][y - 1].getPlyernumber() == mine or board[x][y + 1].getPlayernumber() == mine):
            if (board[x][y - 1].getPlyernumber() == opponent or board[x][y + 1].getPlayernumber() == opponent):
                score+=5
            elif (board[x][y - 1].getPlyernumber() == mine and board[x][y + 1].getPlayernumber() == mine):
                score+=100
            else:
                score+=25
            record[x][y - 1][mine - 1] = score
            record[x][y + 1][mine - 1] = score
        elif (board[x + 1][y - 1].getPlyernumber() == mine or board[x - 1][y + 1].getPlayernumber() == mine):
            if (board[x + 1][y - 1].getPlyernumber() == opponent or board[x - 1][y + 1].getPlayernumber() == opponent):
                score+=5
            elif (board[x + 1][y - 1].getPlyernumber() == mine and board[x - 1][y + 1].getPlayernumber() == mine):
                score+=100
            else:
                score+=25
            record[x + 1][y - 1][mine - 1] = score
            record[x - 1][y + 1][mine - 1] = score
        elif (board[x - 1][y].getPlyernumber() == mine or board[x + 1][y].getPlayernumber() == mine):
            if (board[x - 1][y].getPlyernumber() == opponent or board[x + 1][y].getPlayernumber() == opponent):
                score+=5
            elif (board[x - 1][y].getPlyernumber() == mine and board[x + 1][y].getPlayernumber() == mine):
                score+=100
            else:
                score+=25
            record[x - 1][y][mine - 1] = score
            record[x + 1][y][mine - 1] = score
    elif x - 3 < 0 and y - 2 < 0:
        if (board[x][y - 1].getPlyernumber() == mine or board[x][y + 1].getPlayernumber() == mine):
            if (board[x][y - 1].getPlyernumber() == opponent or board[x][y + 1].getPlayernumber() == opponent):
                score+=5
            elif (board[x][y - 1].getPlyernumber() == mine and board[x][y + 1].getPlayernumber() == mine):
                score+=100
            else:
                score+=25
            record[x][y - 1][mine - 1] = score
            record[x][y + 1][mine - 1] = score
        elif (board[x - 1][y].getPlyernumber() == mine or board[x - 2][y].getPlayernumber() == mine):
            if (board[x - 1][y].getPlyernumber() == opponent or board[x - 2][y].getPlayernumber() == opponent):
                score+=5
            elif (board[x - 1][y].getPlyernumber() == mine and board[x - 2][y].getPlayernumber() == mine):
                score+=100
            else:
                score+=25
            record[x + 1][y][mine - 1] = score
            record[x + 2][y][mine - 1] = score
    elif x - 1 < 0 and y - 3 < 0:
        if (Board[x][y - 1].getPlyernumber() == mine or board[x][y - 2].getPlayernumber() == mine):
            if (board[x][y - 1].getPlyernumber() == opponent or board[x][y - 2].getPlayernumber() == opponent):
                score+=5
            elif (board[x][y - 1].getPlyernumber() == mine and board[x][y - 2].getPlayernumber() == mine):
                score+=100
            else:
                score+=25
            record[x][y - 1][mine - 1] = score
            record[x][y - 2][mine - 1] = score
        elif (board[x + 1][y - 1].getPlyernumber() == mine or board[x + 2][y - 2].getPlayernumber() == mine):
            if (board[x + 1][y - 1].getPlyernumber() == opponent or board[x + 2][y - 2].getPlayernumber() == opponent):
                score+=5
            elif (board[x + 1][y - 1].getPlyernumber() == mine and board[x + 2][y - 2].getPlayernumber() == mine):
                score+=100
            else:
                score+=25
            record[x + 1][y - 1][mine - 1] = score
            record[x + 2][y - 2][mine - 1] = score
        elif (board[x + 1][y].getPlyernumber() == mine or board[x + 2][y].getPlayernumber() == mine):
            if (board[x + 1][y].getPlyernumber() == opponent or board[x + 2][y].getPlayernumber() == opponent):
                score+=5
            elif (board[x + 1][y].getPlyernumber() == mine and board[x + 2][y].getPlayernumber() == mine):
                score+=100
            else:
                score+=25
            record[x + 1][y][mine - 1] = score
            record[x + 2][y][mine - 1] = score
    elif x - 2 < 0 and y - 3 < 0:
        if (board[x - 1][y].getPlyernumber() == mine or board[x + 1][y].getPlayernumber() == mine):
            if (board[x - 1][y].getPlyernumber() == opponent or board[x + 1][y].getPlayernumber() == opponent):
                score+=5
            elif (board[x - 1][y].getPlyernumber() == mine and board[x + 1][y].getPlayernumber() == mine):
                score+=100
            else:
                score+=25
            record[x - 1][y][mine - 1] = score
            record[x + 1][y][mine - 1] = score
        elif (board[x][y - 1].getPlyernumber() == mine or board[x][y - 2].getPlayernumber() == mine):
            if (board[x][y - 1].getPlyernumber() == opponent or board[x][y - 2].getPlayernumber() == opponent):
                score+=5
            elif (board[x][y - 1].getPlyernumber() == mine and board[x][y - 2].getPlayernumber() == mine):
                score+=100
            else:
                score+=25
            record[x][y - 1][mine - 1] = score
            record[x][y - 2][mine - 1] = score
    elif x - 3 < 0 and y - 3 < 0:
        if (board[x - 1][y - 1].getPlyernumber() == mine or board[x - 2][y - 2].getPlayernumber() == mine):
            if (board[x - 1][y - 1].getPlyernumber() == opponent or board[x - 2][y - 2].getPlayernumber() == opponent):
                score+=5
            elif (board[x - 1][y - 1].getPlyernumber() == mine and board[x - 2][y - 2].getPlayernumber() == mine):
                score+=100
            else:
                score+=25
            record[x - 1][y - 1][mine - 1] = score
            record[x - 2][y - 2][mine - 1] = score
        elif (board[x][y - 1].getPlyernumber() == mine or board[x][y - 2].getPlayernumber() == mine):
            if (board[x][y - 1].getPlyernumber() == opponent or board[x][y - 2].getPlayernumber() == opponent):
                score+=5
            elif (board[x][y - 1].getPlyernumber() == mine and board[x][y - 2].getPlayernumber() == mine):
                score+=100
            else:
                score+=25
            record[x][y - 1][mine - 1] = score
            record[x][y - 2][mine - 1] = score
        elif (board[x - 1][y].getPlyernumber() == mine or Board[x - 1][y].getPlayernumber() == mine):
            if (board[x - 1][y].getPlyernumber() == opponent or board[x - 1][y].getPlayernumber() == opponent):
                score+=5
            elif (board[x - 2][y].getPlyernumber() == mine and board[x - 2][y].getPlayernumber() == mine):
                score+=100
            else:
                score+=25
            record[x - 1][y][mine - 1] = score
            record[x - 2][y][mine - 1] = score

                










