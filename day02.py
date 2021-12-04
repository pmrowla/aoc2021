#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2021 day 2 module."""

from typing import NamedTuple


class Position(NamedTuple):
    pos: int
    depth: int
    aim: int


def move(pos: Position, direction: str, distance: int) -> Position:
    return {
        "forward": lambda pos: Position(pos.pos + distance, pos.depth + pos.aim * distance, pos.aim),
        "down": lambda pos: Position(pos.pos, pos.depth, pos.aim - distance),
        "up": lambda pos: Position(pos.pos, pos.depth, pos.aim + distance),
    }[direction](pos)


def process(puzzle_input, verbose=False):
    p1 = 0
    p2 = 0

    pos = Position(0, 0, 0)
    for line in puzzle_input:
        direction, distance = line.split()
        pos = move(pos, direction, int(distance))

    p1 = abs(pos.pos * pos.aim)
    p2 = abs(pos.pos * pos.depth)
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
        puzzle_input = (line for line in fileinput.input(args.infile) if line.strip())
        p1, p2 = process(puzzle_input, verbose=args.verbose)
        print(f'Part one: {p1}')
        print(f'Part two: {p2}')
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
