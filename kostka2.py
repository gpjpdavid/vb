#!/usr/bin/env python3

"""
Emulace hraci kostky
version: 1.0.0
Program pro generovani nahodnych cisel od 1 do poctu sten kostky.
"""

import random


def main(pocet_sten):
    return random.randint(1, pocet_sten)


if __name__ == '__main__':
    print(main(6))