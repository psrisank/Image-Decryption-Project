"""
===============================================================================
ENGR 13300 Fall 2021

Program Description
    Uses the original encrypt/decrypt method to encrypt or decrypt a file. Uses user defined string.

Assignment Information
    Assignment:     Team Python Project
    Author:         Pranav Srisankar, psrisank@purdue.edu
    Team ID:        LC5 - 15

Contributor:   Abhiram Saridena, asariden@purdue.edu
               Arihan Srirangapatnam, asrirang@purdue.edu
               Erik Waller, ewaller@purdue.edu
    My contributor(s) helped me:
    [yes] understand the assignment expectations without
        telling me how they will approach it.
    [yes] understand different ways to think about a solution
        without helping me plan my solution.
    [yes] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.

ACADEMIC INTEGRITY STATEMENT
I have not used source code obtained from any other unauthorized
source, either modified or unmodified. Neither have I provided
access to my code to another. The project I am submitting
is my own original work.
===============================================================================
"""
import matplotlib.pyplot as plt
import numpy as np
from image_import import getDimensions

def keygen(fileName,ikey):
    dimensions = getDimensions(fileName)
    ikeylen = len(ikey) - ikey.count(" ")
    key = np.ones(dimensions, np.uint8)
    i, j, k = np.indices(dimensions)
    key = i*j
    modarray = np.full(dimensions, (ikeylen))
    key = np.mod(key, modarray)
    key = np.multiply(key, (2**8//ikeylen))
    key = key.astype(np.uint8)
    return key

def cipher(fileName, key):
    img = plt.imread(fileName)[:,:,:3] 
    decrypted_image = np.bitwise_xor(img, key)
    return decrypted_image

def main():
    ikey = input("Enter initial key: ")
    fileName = input("Enter image name: ")
    outputName = input("Enter output file name:")

    # Key Generator
    keyarray = keygen(fileName, ikey)

    cipherimg = cipher(fileName, keyarray)
    # Encrypt/Decrypt image
    plt.imsave(f'{outputName}', cipherimg)

if __name__ == '__main__':
    main()


