#!/usr/bin/python

import sys
import os
import time
import random
import math


key_size = 0
message = ""
order = []
encoded = ""
decoded = ""
matrix = []
row = 0
col = 0
key = ""


def fill_matrix_e(row, col):
    global matrix
    message_index = 0
    for r in range(row):
        matrix.append([])
        for c in range(col):
            matrix[r].append(message[message_index])
            message_index += 1


def fill_matrix_d(row,col):
    global matrix
    message_index = 0
    for r0 in range(row):
        matrix.append([])
    for o in order:
        r1 = key.index(o)
        for c in range(col):
            matrix[r1].append(message[message_index])
            message_index += 1


def print_matrix(mtx, rw, cl):
    for r in range(rw):
        for c in range(cl):
            print mtx[r][c],
        print ""


def get_key():
    global key_size, key, order
    key = raw_input("What is the key word >>> ")
    key_size = len(key)
    order = sorted(key)


def read_in_message_e():
    global message, row
    message = raw_input("What is the message >>> ")
    get_key()
    row = len(message)/key_size
    left_over = len(message) % key_size
    if left_over != 0:
        fillers = key_size - left_over
        for i in range(fillers):
            ran = random.SystemRandom()
            ascii_num = int(math.floor(95 * ran.random()) + 32)
            message += chr(ascii_num)

        row += 1
        fill_matrix_e(row, key_size)

    else:
        fill_matrix_e(row, key_size)


def read_in_message_d():
    global message, col
    message = raw_input("What is the message >>> ")
    get_key()
    col = len(message) / key_size
    fill_matrix_d(key_size, col)


def encode_message():
    global encoded
    read_in_message_e()
    for c in range(key_size):
        for r in range(row):
            cl = key.index(order[c])
            encoded += matrix[r][cl]

    print encoded


def decode_message():
    global decoded
    read_in_message_d()
    for c in range(col):
        for r in range(key_size):
            decoded += matrix[r][c]

    print decoded


def main():
    answer = int(raw_input("Would you like to Encrypt [1] or Decrpyt [2] >>> "))
    if answer == 2:
        decode_message()
    else:
        encode_message()


if __name__ == '__main__':
    main()