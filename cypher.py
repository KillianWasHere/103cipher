#!/bin/python3
##
## EPITECH PROJECT, 2025
## cypher.py
## File description:
## The 103cipher project
##
import sys

## x = nb_col y = nb_lin
def create_matrix(x, y):
    return [[0 for j in range(x)] for i in range(y)]

def show_matrix_decryption(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j < len(matrix[i]) - 1:
                if matrix[i][j] == 0:
                    print(f"{round(abs(matrix[i][j]), 3)}", end = "\t")
                else:
                    print(f"{round(matrix[i][j], 3)}", end = "\t")
            else:
                if matrix[i][j] == 0:
                    print(f"{round(abs(matrix[i][j]), 3)}", end = "\n")
                else:
                    print(f"{round(matrix[i][j], 3)}", end = "\n")
    return 0

def show_matrix_encryption(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j < len(matrix[i]) - 1:
                if matrix[i][j] == 0:
                    print(f"{abs(matrix[i][j]):.0f}", end = "\t")
                else:
                    print(f"{matrix[i][j]:.0f}", end = "\t")
            else:
                if matrix[i][j] == 0:
                    print(f"{abs(matrix[i][j]):.0f}", end = "\n")
                else:
                    print(f"{matrix[i][j]:.0f}", end = "\n")
    return 0

def mul_mtrx(matrix1, matrix2):
    result_matrix = create_matrix(len(matrix2[0]), len(matrix1))

    for i in range(len(result_matrix)):
        for j in range(len(result_matrix[i])):
            for k in range(len(matrix2)):
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
    return result_matrix

def mul_int_mtrx(nb, mtrx):
    tmp = mtrx

    for i in range(len(tmp)):
        for j in range(len(tmp[i])):
            tmp[i][j] = tmp[i][j] * nb
    return tmp

def wrd_in_mtrx(string):
    lenght = len(string)
    k = 1

    while (pow(k, 2) < lenght):
        k += 1
    mtrx = create_matrix(k, k)
    idx = 0
    for i in range(len(mtrx)):
        for j in range(len(mtrx[i])):
            if (idx < len(string)):
                mtrx[i][j] = ord(string[idx])
                idx += 1
    return mtrx

def wrd_in_n_column_mtrx(string, n):
    lenght = len(string)
    k = 1
    while ((k * n) < lenght):
        k += 1
    mtrx = create_matrix(n, k)
    idx = 0
    for i in range(len(mtrx)):
        for j in range(len(mtrx[i])):
            if (idx < len(string)):
                mtrx[i][j] = ord(string[idx])
                idx += 1
    return mtrx

def int_list_in_n_column_mtrx(int_list, n):
    lenght = len(int_list)
    k = 1
    while ((k * n) < lenght):
        k += 1
    mtrx = create_matrix(n, k)
    idx = 0
    for i in range(len(mtrx)):
        for j in range(len(mtrx[i])):
            if (idx < len(int_list)):
                mtrx[i][j] = int_list[idx]
                idx += 1
    return mtrx

def str_to_int_array(string):
    wrd = string
    nb_space = 0
    int_list = []

    for i in range(len(string)):
        if string[i] == ' ':
            nb_space += 1
    for i in range(nb_space):
        idx = 0
        while wrd[idx] != ' ' or idx == len(wrd) - 1:
            idx += 1
        int_list.append(int(wrd[:idx]))
        wrd = wrd[idx + 1:]
    try:
        int_list.append(int(wrd))
    except ValueError:
        sys.exit(84)
    return int_list

def transpose(mtrx):
    transpo = create_matrix(len(mtrx), len(mtrx[0]))

    for i in range(len(mtrx)):
        for j in range(len(mtrx[i])):
            transpo[j][i] = mtrx[i][j]
    return transpo

def det_mtrx_2by2(mtrx):
    return (mtrx[0][0] * mtrx[1][1]) - (mtrx[0][1] * mtrx[1][0])

def invrt_mtrx_2by2(mtrx):
    det = det_mtrx_2by2(mtrx)
    invrt = mtrx

    if (det == 0):
        sys.exit(84)
    invrt[0][0], invrt[1][1] = invrt[1][1], invrt[0][0]
    invrt[0][1] = -invrt[0][1]
    invrt[1][0] = -invrt[1][0]
    for i in range(len(mtrx)):
        for j in range(len(mtrx[i])):
            invrt[i][j] = invrt[i][j] * (1/det)
    return invrt

def cofactor_mtrx_3by3(mtrx, i, j):
    result = pow((-1), i + j)
    sub_list = []
    sub_mtrx = create_matrix(2, 2)

    for idx in range(len(mtrx)):
        for jdx in range(len(mtrx[idx])):
            if (idx != i) and (jdx != j):
                sub_list.append(mtrx[idx][jdx])
    sub_mtrx[0] = sub_list[:2]
    sub_mtrx[1] = sub_list[2:]
    return result * ((sub_mtrx[0][0] * sub_mtrx[1][1]) - (sub_mtrx[0][1] * sub_mtrx[1][0]))

def det_mtrx_3by3(mtrx):
    result = 0

    for i in range(3):
        result += cofactor_mtrx_3by3(mtrx, 0, i) * mtrx[0][i]
    return result

def invrt_mtrx_3by3(mtrx):
    det = det_mtrx_3by3(mtrx)
    cofactor_mtrx = create_matrix(3, 3)

    if (det == 0):
        return None
    for i in range(len(cofactor_mtrx)):
        for j in range(len(cofactor_mtrx[i])):
            cofactor_mtrx[i][j] = cofactor_mtrx_3by3(mtrx, i, j)
    cofactor_mtrx = transpose(cofactor_mtrx)
    return mul_int_mtrx(1/det, cofactor_mtrx)

def print_help():
    print(f"""USAGE
    ./103cipher message key flag

DESCRIPTION
    message     a message, made of ASCII characters
    key         the encryption key, made of ASCII characters
    flag        0 for the message to be encrypted, 1 to be decrypted""")

def is_strictly_integer(s: str):
    if len(s) == 0:
        return False
    if s[0] == "-":
        s = s[1:]
    return s.isdigit()

def main():
    try:
        if sys.argv[1] == "-h":
            print_help()
            sys.exit(0)
    except IndexError:
        sys.exit(84)

    if len(sys.argv) != 4:
        sys.exit(84)
    if type(sys.argv[1]) != str or type(sys.argv[2]) != str:
        sys.exit(84)
    if len(sys.argv[1]) == 0 or len(sys.argv[2]) == 0:
        sys.exit(84)
    if not(is_strictly_integer(sys.argv[3])):
        sys.exit(84)
    if int(sys.argv[3]) != 0 and int(sys.argv[3]) != 1:
        sys.exit(84)
    
    if sys.argv[3] == '0':
        mat_key = wrd_in_mtrx(sys.argv[2])
        mat_mot = wrd_in_n_column_mtrx(sys.argv[1], len(mat_key))
        mat_mulled = mul_mtrx(mat_mot, mat_key)
        print("Key matrix:")
        show_matrix_encryption(mat_key)
        print("\nEncrypted message:")
        for i in range(len(mat_mulled)):
            for j in range(len(mat_mulled[i])):
                if j == len(mat_mulled[i]) - 1 and i == len(mat_mulled) - 1:
                    print(mat_mulled[i][j], end='')
                else:
                    print(mat_mulled[i][j], end=' ')
        print('')
    elif sys.argv[3] == '1':
        mat_key = wrd_in_mtrx(sys.argv[2])
        if (len(mat_key) == 3):
            mat_key = invrt_mtrx_3by3(mat_key)
        elif (len(mat_key) == 2):
            mat_key = invrt_mtrx_2by2(mat_key)
        elif (len(mat_key) == 1):
            mat_key[0][0] = 1/mat_key[0][0]
        else:
            sys.exit(84)

        if type(mat_key) != list:
            sys.exit(84)
        mat_crypt = int_list_in_n_column_mtrx(str_to_int_array(sys.argv[1]), len(mat_key))
        print("Key matrix:")
        show_matrix_decryption(mat_key)
        mat_mot = mul_mtrx(mat_crypt, mat_key)
        print("\nDecrypted message:")
        for i in range(len(mat_mot)):
            for j in range(len(mat_mot[i])):
                if (int(mat_mot[i][j]) != 0):
                    print(chr(int(round(mat_mot[i][j]))), end = '')
        print('')

if __name__ == "__main__":
    main()
