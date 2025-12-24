import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image
img = cv2.imread("CF142.JPG")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Initialize mask
h, w = gray.shape
region = np.zeros((h, w), dtype=np.uint8)

# Choose seed point (bottom center - near foot)
seed_x, seed_y = int(w/2), int(h*0.75)
seed_value = gray[seed_y, seed_x]

# Threshold for similarity
threshold = 10

# Stack for region growing
stack = [(seed_x, seed_y)]

while stack:
    x, y = stack.pop()
    if region[y, x] == 0:
        if abs(int(gray[y, x]) - int(seed_value)) < threshold:
            region[y, x] = 255
            # Check neighbors
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < w and 0 <= ny < h:
                    stack.append((nx, ny))

# Display
plt.imshow(region, cmap='gray')
plt.title("Region Growing Segmentation")
plt.axis("off")
plt.show()
