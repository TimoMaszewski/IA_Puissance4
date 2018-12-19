from player import Player
from copy import deepcopy
import math
import random
import numpy

class AIPlayer(Player):
    """This player should implement a heuristic along with a min-max and alpha
    beta search to """
    def __init__(self):
        super().__init__()
        self.name = "Timo MASZEWSKI et Niels HENDRICKX"

    def getColumn(self, board):
        return self.alphabeta(board)

    def alphabeta(self, board, profondeurmax=3):
        c = self.color
        def heuristic(board):

            score = 0
            for i in range(6):
                row = board.getRow(i)
                for j in range(0, 4):
                    if c not in row[j:j+4]:
                        q = sum(row[j:j+4])
                        score -= 10**abs(q)
                    if -c not in row[j:j+4]:
                        q = sum(row[j:j+4])
                        score += 5**abs(q)
            for j in range(7):
                col = board.getCol(j)
                for i in range(0,3):
                    if c not in col[i:i+4]:
                        q = sum(col[i:i+4])
                        score -= 10**abs(q)
                    if -c not in col[i:i+4]:
                        q = sum(col[i:i+4])
                        score += 5**abs(q)
            for j in range(8):
                for bool in [True, False]:
                    diag = board.getDiagonal(bool, j)
                    k = len(diag)
                    if k >= 4:
                        for p in range(0,k-3):
                            if c not in diag[p:p+4]:
                                q = sum(diag[p:p+4])
                                score -= 10**abs(q)
                            if -c not in diag[p:p+4]:
                                q = sum(diag[p:p+4])
                                score += 5**abs(q)
            return score


        def maxvalue(board, alpha, beta, hauteur):
            if hauteur>=profondeurmax:
                return heuristic(board)
            v = -100000
            for action in board.getPossibleColumns():
                boardcopy = deepcopy(board)
                boardcopy.play(self.color, action)
                v = max(v, minvalue(boardcopy, alpha, beta, hauteur+1))
                if v>=beta:
                    return v
                alpha = max(alpha,v)
            return v

        def minvalue(board, alpha, beta, hauteur):
            if hauteur>=profondeurmax:
                return heuristic(board)
            v = 100000
            for action in board.getPossibleColumns():
                boardcopy = deepcopy(board)
                boardcopy.play(-self.color, action)
                v = min(v, maxvalue(boardcopy, alpha, beta, hauteur+1))
                if v<=alpha:
                    return v
                beta = min(beta,v)
            return v

        meilleur_score = -100000
        beta = 100000
        coup = None
        for action in board.getPossibleColumns():
            boardcopy = deepcopy(board)
            boardcopy.play(self.color, action)
            v = minvalue(boardcopy, meilleur_score, beta, 1)
            if v>meilleur_score:
                meilleur_score = v
                coup = action
        return coup



