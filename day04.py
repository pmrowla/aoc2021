#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2021 day 4 module."""

from collections import OrderedDict
from typing import NamedTuple


class Tile(NamedTuple):
    n: int
    marked: bool = False


def parse_input(lines):
    rolls = [int(n) for n in lines[0].split(',')]
    boards = []
    for i in range(2, len(lines), 6):
        if len(lines) - i < 6:
            break
        board = []
        for j in range(5):
            board.append([Tile(int(n)) for n in lines[i + j].split()])
        boards.append(board)
    return rolls, boards


def mark(board, num):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j].n == num:
                board[i][j] = Tile(num, True)
                return


def win(board):
    for i in range(len(board)):
        if (
            all(tile.marked for tile in board[i])
            or all(row[i].marked for row in board)
        ):
            return True
    return False


def score(board):
    return sum(
        sum(tile.n for tile in row if not tile.marked)
        for row in board
    )


def process(puzzle_input, verbose=False):
    p1 = None
    p2 = None

    rolls, boards = parse_input(list(puzzle_input))
    wins = OrderedDict()
    for roll in rolls:
        for i, board in enumerate(boards):
            mark(board, roll)
            if win(board):
                if i not in wins:
                    total = score(board) * roll
                    wins[i] = total
                    if p1 is None:
                        p1 = total
    _, p2 = wins.popitem(last=True)

    return p1, p2


def main():
    """Main entry point."""
    import argparse
    import fileinput

    parser = argparse.ArgumentParser()
    parser.add_argument('infile', help='input file to read ("-" for stdin)')
    parser.add_argument('-v', '--verbose', '-d', '--debug',
                        action='store_true', dest='verbose', help='verbose output')
    args = parser.parse_args()
    try:
        puzzle_input = (line.strip() for line in fileinput.input(args.infile))
        p1, p2 = process(puzzle_input, verbose=args.verbose)
        print(f'Part one: {p1}')
        print(f'Part two: {p2}')
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
