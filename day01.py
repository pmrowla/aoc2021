#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2021 day 1 module."""


def process(puzzle_input, verbose=False):
    p1 = 0
    p2 = 0

    total = 0
    last_total = 0
    for i, n in enumerate(puzzle_input):
        if i > 0 and n > puzzle_input[i - 1]:
            p1 += 1
        total += n
        if i >= 2:
            if i > 2:
                total -= puzzle_input[i - 3]
                if total > last_total:
                    p2 += 1
            last_total = total

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
        puzzle_input = [int(line.strip()) for line in fileinput.input(args.infile) if line.strip()]
        p1, p2 = process(puzzle_input, verbose=args.verbose)
        print(f'Part one: {p1}')
        print(f'Part two: {p2}')
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
