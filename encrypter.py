"""
===============================================================================
ENGR 13300 Fall 2021

Program Description
    Enrypts and Decrypts a file given a key string, utilizing pseudo random numbers.

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

def histogram(fileName):
    image = plt.imread(fileName)
    #plot the intensity histogram of the red channel 
    plt.hist(image[:,:,0].reshape(image.shape[0]*image.shape[1]),bins=np.arange(2**8+1))
    plt.show()

def keygen(fileName, ikey):
    dimensions = getDimensions(fileName)
    ikeylen = len(ikey) - ikey.count(" ")
    s = [ikeylen]
    counter=0
    key = np.ones(dimensions, dtype=np.uint8)
    for i in range(len(key)):
        for j in range(len(key[i])):
            if (counter>0):
                s.append((1103515245*s[counter-1]+12345)%(2**31))
            key[i][j] = s[counter]
            counter+=1
    return key


def cipher(fileName, key):
    img = plt.imread(fileName)[:,:,:3] 
    ciphered_img = np.bitwise_xor(img, key)
    return ciphered_img

def compare():
    img1 = input("Enter name of first image: ")
    img2 = input("Enter name of second image: ")

    histogram(img1)
    histogram(img2)

def main():
    ikey = input("Enter initial key: ")
    fileName = input("Enter image name: ")
    outputName = input("Enter output file name: ")

    img = plt.imread(fileName)[:,:,:3]

    # Key Generator
    keyarray = keygen(fileName, ikey)

    cipherimg = cipher(fileName, keyarray)
    # Encrypt/Decrypt image
    plt.imsave(f'{outputName}', cipherimg)

    comp = input(f'Would you like to compare your encrypted image with its original encryption?')
    if (comp.lower() == 'yes'):
        compare() 


if __name__ == '__main__':
    main()

