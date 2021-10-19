"""
===============================================================================
ENGR 13300 Fall 2021

Program Description
    Finds the location of earth. Gives coordinates and saves to a file.

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
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndimage
from image_import import getDimensions, getDataType

def grayscale(img):
    img = img.copy()
    img = (img/255).astype(np.float64)
    gray = np.dot(img[...,:3], [0.299, 0.587, 0.114])
    return gray

def gaussian(img):
    gauss = ndimage.filters.gaussian_filter(img, 1.067, order=0)
    return gauss

def edge_detection(img):
    dx = ndimage.sobel(img, 0)
    dy = ndimage.sobel(img, 1)
    mag = np.hypot(dx, dy)
    return mag

def findEarth(img):
    coords = np.where(img == np.amax(img))
    yearth = int(coords[0])
    xearth = int(coords[1])
    return xearth, yearth

def centerEarth(img, x, y):
    centered = img[y-50:y+51, x-50:x+51]
    return centered

def main():
    fileName = input('Name of file with earth in it: ')
    img = plt.imread(fileName)[:,:,:3]
    fileOutput = input('Name of output file: ')

    if('\\' in fileName):
        fileName = fileName[fileName.index("\\")+1:]
    
    gray = grayscale(img)
    plt.imsave(f"Earth\\gray_{fileName}", gray, cmap="gray")

    gauss = gaussian(gray)
    plt.imsave(f"Earth\\gauss_{fileName}", gauss, cmap="gray")

    edge = edge_detection(gauss)
    plt.imsave(f"Earth\\edge_{fileName}", edge, cmap="gray")

    x, y = findEarth(edge)
    print(f'\nEarth located in {x}, {y}')
    earthCentered = centerEarth(img, x, y)
    plt.imsave(f"{fileOutput}", earthCentered)


if __name__ == '__main__':
    main()

