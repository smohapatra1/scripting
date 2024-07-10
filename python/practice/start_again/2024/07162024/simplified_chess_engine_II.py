# #   https://www.hackerrank.com/challenges/simplified-chess-engine-ii/problem?isFullScreen=true

# Chess is a very popular game played by hundreds of millions of people. Nowadays, we have chess engines such as Stockfish and Komodo to help us analyze games. These engines are very powerful pieces of well-developed software that use intelligent ideas and algorithms to analyze positions and sequences of moves, as well as to find tactical ideas. Consider the following simplified version of chess:

# Board:
# It's played on a  board between two players named Black and White.
# Rows are numbered from  to , where the top row is  and the bottom row is .
# Columns are lettered from  to , where the leftmost column is  and the rightmost column is .
# Pieces and Movement:
# White initially has  pieces and Black initially has  pieces.
# There are no Kings on the board. Each player initially has exactly  Queen, at most  Pawns, at most  Rooks, and at most  minor pieces (i.e., a Bishop and/or Knight).
# White's Pawns move up the board, while Black's Pawns move down the board.
# Each move made by any player counts as a single move.
# Each piece's possible moves are the same as in classical chess, with the following exceptions:
# Pawns cannot move two squares forward.
# The en passant move is not possible.
# Promotion:
# Pawns promote to either a Bishop, Knight, or Rook when they reach the back row (promotion to a Queen is not allowed).
# The players must perform promotions whenever possible. This means White must promote their Pawns when they reach any cell in the top row, and Black must promote their Pawns when they reach any cell in the bottom row.
# Objective:
# The goal of the game is to capture the opponent’s Queen without losing your own.
# There will never be a draw or tie scenario like you might see in classical chess.
# Given  and the layout of pieces for  games, implement a very basic engine for our simplified version of chess that determines whether or not White can win in  moves (regardless of how Black plays) if White always moves first. For each game, print YES on a new line if White can win in  moves; otherwise, print NO.

# Input Format

# The first line contains an integer, , denoting the number of games. The subsequent lines describe each game in the following format:

# The first line contains three space-separated integers describing the respective values of  (the number of white pieces),  (the number of black pieces), and  (the maximum number of moves we want to know if White can win in).
# The  subsequent lines describe each chess piece in the form t c r, where  is a character  denoting the type of piece (where  is Queen,  is Knight,  is Bishop,  is Rook, and  is a Pawn), and  and  denote the respective column and row on the board where the figure is located (where  and ). These inputs are given as follows:
# Each of the first  lines describes the type and location of a White piece.
# Each of the subsequent  lines describes the type and location of a Black piece.
# Constraints

# Each player has exactly  Queen, at most  Pawns, at most  Rooks, and at most  minor pieces (i.e., a Bishop and/or Knight).
# It is guaranteed that the initial location of each chess piece is distinct.
# No pawn is initially placed in a row where it would promote.
# Output Format

# For each of the  games of simplified chess, print whether or not White can win in  moves on a new line. If it's possible, print YES; otherwise, print NO instead.

# Sample Input 0

# 1
# 2 1 1
# Q B 1
# P B 3
# Q A 4
# Sample Output 0

# YES
# Explanation 0

# We play the following  game of simplified chess:

# image

# White wins by moving their Pawn to  and capturing Black's Queen, so we print YES on a new line.


#!/bin/python3

import math
import os
import random
import re
import sys


def validmoves(piece,posx,posy,whites,blacks,b):
    if piece=="R":
        L=[]
        i=1
        while posx+i<4 and not (posx+i,posy) in whites:
            L+=[("R",posx+i,posy)]
            if (posx+i,posy) in blacks:
                break
            i+=1
        i=1
        while posx-i>=0 and not (posx-i,posy) in whites:
            L+=[("R",posx-i,posy)]
            if (posx-i,posy) in blacks:
                break
            i+=1
        i=1
        while posy+i<4 and not (posx,posy+i) in whites:
            L+=[("R",posx,posy+i)]
            if (posx,posy+i) in blacks:
                break
            i+=1
        i=1
        while posy-i>=0 and not (posx,posy-i) in whites:
            L+=[("R",posx,posy-i)]
            if (posx,posy-i) in blacks:
                break
            i+=1
        return(L)
    elif piece=="B":
        L=[]
        i=1
        while posx+i<4 and posy+i<4 and not (posx+i,posy+i) in whites:
            L+=[("B",posx+i,posy+i)]
            if (posx+i,posy+i) in blacks:
                break
            i+=1
        i=1
        while posx-i>=0 and posy+i<4 and not (posx-i,posy+i) in whites:
            L+=[("B",posx-i,posy+i)]
            if (posx-i,posy+i) in blacks:
                break
            i+=1
        i=1
        while posx+i<4 and posy-i>=0 and not (posx+i,posy-i) in whites:
            L+=[("B",posx+i,posy-i)]
            if (posx+i,posy-i) in blacks:
                break
            i+=1
        i=1
        while posx-i>=0 and posy-i>=0 and not (posx-i,posy-i) in whites:
            L+=[("B",posx-i,posy-i)]
            if (posx-i,posy-i) in blacks:
                break
            i+=1
        return(L)
    elif piece=="Q":
        return([("Q",z[1],z[2]) for z in validmoves("R",posx,posy,whites,blacks,b)+validmoves("B",posx,posy,whites,blacks,b)])
    elif piece=="N":
        return([("N",z[0],z[1]) for z in [(posx+2,posy+1),(posx+2,posy-1),(posx+1,posy+2),(posx+1,posy-2),(posx-1,posy+2),(posx-1,posy-2),(posx-2,posy+1),(posx-2,posy-1)] if not z in whites and 0<=z[0]<=3 and 0<=z[1]<=3])
    elif piece=="P":
        posy+=1-2*b
        l=[]
        for i in [-1,1]:
            if 0<=posx+i<=3 and (posx+i,posy) in blacks:
                l+=[(posx+i,posy)]
        if not (posx,posy) in whites+blacks:
            l+=[(posx,posy)]
        if posy in [0,3]:
            return([("N",x[0],x[1]) for x in l]+[("B",x[0],x[1]) for x in l]+[("R",x[0],x[1]) for x in l])
        else:
            return([("P",x[0],x[1]) for x in l])

def simplifiedChessEngine(whites, blacks, moves,b):
    if moves==0:
        if b:
            return("YES")
        else:
            return("NO")
    else:
        wh=[(x[1],x[2]) for x in whites]
        bl=[(x[1],x[2]) for x in blacks]
        i,j=[z[1:] for z in blacks if z[0]=="Q"][0]
        l=sum([validmoves(x[0],x[1],x[2],wh,bl,b) for x in whites],[])
        if (i,j) in [x[1:] for x in l]:
            return("YES")
        else:
            nextmove=[];nextmove2=[]
            for i in range(len(whites)):
                for t in validmoves(whites[i][0],whites[i][1],whites[i][2],wh,bl,b):
                    if (t[1],t[2]) in bl:
                        nextmove.append((i,t))
                    else:
                        nextmove2.append((i,t))
            for x in nextmove+nextmove2:
                i,t=x[0],x[1]            
                piece,posx,posy=whites[i]
                taken=[z for z in blacks if (z[1],z[2])==t[1:]]
                blacks=[z for z in blacks if not z in taken]
                whites[i]=t
                if simplifiedChessEngine(blacks,whites,moves-1,1-b)=="NO":
                    whites[i]=(piece,posx,posy)
                    blacks+=taken
                    return("YES")
                else:
                    whites[i]=(piece,posx,posy)
                    blacks+=taken
            return("NO")
if __name__ == '__main__':
    g = int(input())

    for g_itr in range(g):
        wbm = input().split()

        w = int(wbm[0])

        b = int(wbm[1])

        m = int(wbm[2])

        whites = []

        for _ in range(w):
            whites.append(input().rstrip().split())

        blacks = []

        for _ in range(b):
            blacks.append(input().rstrip().split())
        
        whites=[[x[0],ord(x[1])-65,int(x[2])-1] for x in whites]
        blacks=[[x[0],ord(x[1])-65,int(x[2])-1] for x in blacks]

        result = simplifiedChessEngine(whites, blacks, m,0)
        print(result)       


# if __name__ == '__main__':
#     g = int(input().strip())

#     for g_itr in range(g):
#         first_multiple_input = input().rstrip().split()

#         w = int(first_multiple_input[0])

#         b = int(first_multiple_input[1])

#         m = int(first_multiple_input[2])

#         white = []

#         for _ in range(w):
#             white.append(input().rstrip().split())

#         black = []

#         for _ in range(b):
#             black.append(input().rstrip().split())

#         # Write your code here
