# -*- coding: utf-8 -*-
"""
Created on Wed May  8 14:21:47 2024

@author: Morteza
"""
import cv2
import numpy as np

# Create a Macbeth Color Checker image
def create_macbeth_image(width, height):
    # Macbeth Color Checker colors in sRGB
    macbeth_colors = [
        [115, 82, 68], [194, 150, 130], [98, 122, 157], [87, 108, 67], [133, 128, 177],
        [103, 189, 170], [214, 126, 44], [80, 91, 166], [193, 90, 99], [94, 60, 108],
        [157, 188, 64], [224, 163, 46], [56, 61, 150], [70, 148, 73], [175, 54, 60],
        [231, 199, 31], [187, 86, 149], [8, 133, 161], [243, 243, 242], [200, 200, 200],
        [160, 160, 160], [122, 122, 121], [85, 85, 85], [52, 52, 52]
    ]
    
    macbeth_image = np.zeros((height, width, 3), dtype=np.uint8)
    patch_width = width // 6
    patch_height = height // 4
    
    for i, color in enumerate(macbeth_colors):
        col_start = (i % 6) * patch_width
        col_end = col_start + patch_width
        row_start = (i // 6) * patch_height
        row_end = row_start + patch_height
        macbeth_image[row_start:row_end, col_start:col_end] = color
    
    return macbeth_image

# Create a window
cv2.namedWindow('Changing Gamma', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Changing Gamma', 1920, 1080)

# Define image size
image_width = 1920
image_height = 1080

# Create a Macbeth Color Checker image
image = create_macbeth_image(image_width, image_height)

# Slow down the frame rate
delay = 500  # in milliseconds

for gamma in np.arange(0, 6.1, 0.1):
    # Apply gamma correction
    corrected_image = np.uint8(((image / 255.0) ** (1 / gamma)) * 255.0)
    
    # Display gamma value on the image
    text = "Gamma: {:.1f}".format(gamma)
    cv2.putText(corrected_image, text, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 10, cv2.LINE_AA)
    cv2.putText(corrected_image, text, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 0), 5, cv2.LINE_AA)
    
    # Display the image
    cv2.imshow('Changing Gamma', corrected_image)
    
    # Wait for a specific amount of time
    cv2.waitKey(delay)

# Close all OpenCV windows
cv2.destroyAllWindows()
