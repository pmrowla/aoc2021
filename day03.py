#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2021 day 3 module."""

from collections import Counter


def get_common(numbers):
    i = 0
    while len(numbers) > 1 and i < len(numbers[0]):
        common = Counter(num[i] for num in numbers).most_common()
        most = common[0][0]
        least = common[1][0]
        same = common[0][1] == common[1][1]
        yield most, least, same, numbers
        i += 1


def process(puzzle_input, verbose=False):
    p1 = 0
    p2 = 0

    numbers = list(puzzle_input)
    gamma = []
    epsilon = []
    for most, least, _same, _nums in get_common(numbers):
        gamma.append(most)
        epsilon.append(least)
    p1 = int(''.join(gamma), 2) * int(''.join(epsilon), 2)

    o2 = list(numbers)
    for i, (most, _least, same, nums) in enumerate(get_common(o2)):
        val = '1' if same else most
        nums[:] = [n for n in nums if n[i] == val]
        o2 = nums

    co2 = list(numbers)
    for i, (_most, least, same, nums) in enumerate(get_common(co2)):
        val = '0' if same else least
        nums[:] = [n for n in nums if n[i] == val]
        co2 = nums
    p2 = int(o2[0], 2) * int(co2[0], 2)
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
        puzzle_input = (line.strip() for line in fileinput.input(args.infile) if line.strip())
        p1, p2 = process(puzzle_input, verbose=args.verbose)
        print(f'Part one: {p1}')
        print(f'Part two: {p2}')
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
