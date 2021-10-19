"""
===============================================================================
ENGR 13300 Fall 2021

Program Description
    retrieves image dimensions and datatype

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

# Takes in image array, returns dimensions as a tuple
def getDimensions(fileName):
    image = plt.imread(fileName)[:,:,:3]
    return image.shape

# Takes in image ndarray, returns data type
def getDataType(fileName):
    image = plt.imread(fileName)[:,:,:3]
    return image.dtype

def main():
    # Asks for file input
    image_in = input("Enter color image file name: ")
    img = plt.imread(image_in)[:,:,3]
    # If the data type of image isn't uint8, converts to it and saves as tiff
    if (getDataType(image_in) == np.float32):
        img = (img*255).astype(np.uint8)
        plt.imsave(f'{image_in[:len(image_in) - 4]}.tiff')

if __name__ == '__main__':
    main()

