import cv2
import numpy as np
import matplotlib.pyplot as plt
from segment_anything import sam_model_registry, SamAutomaticMaskGenerator

# ------------------ LOAD IMAGE ------------------ #
image = cv2.imread("3.jpeg")
if image is None:
    raise FileNotFoundError("CF142.JPG not found!")

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
h, w, _ = image_rgb.shape

# Convert to HSV for skin detection
image_hsv = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2HSV)

# ------------------ LOAD SAM MODEL ------------------ #
sam = sam_model_registry["vit_b"](checkpoint="sam_vit_b_01ec64.pth")
sam.to(device="cpu")

mask_generator = SamAutomaticMaskGenerator(
    sam,
    min_mask_region_area=800
)

# Generate masks
masks = mask_generator.generate(image_rgb)

# ------------------ FOOT MASK SELECTION ------------------ #
foot_mask = np.zeros((h, w), dtype=np.uint8)

# Sort masks by area (largest first)
masks = sorted(masks, key=lambda x: x["area"], reverse=True)

selected = 0

for mask in masks:
    seg = mask["segmentation"].astype(np.uint8)

    ys, xs = np.where(seg == 1)
    if len(xs) == 0:
        continue

    # Bounding box and centroid
    x_min, x_max = xs.min(), xs.max()
    y_min, y_max = ys.min(), ys.max()
    cx = int(xs.mean())
    cy = int(ys.mean())

    box_h = y_max - y_min
    box_w = x_max - x_min

    # Skin color consistency check
    skin_pixels = image_hsv[seg == 1]
    skin_ratio = np.mean(
        (skin_pixels[:, 1] > 30) & (skin_pixels[:, 2] > 50)
    )

    # Selection rules
    if (
        skin_ratio > 0.3 and            # skin-like region
        cy > h * 0.45 and cy < h * 0.85 and  # foot position (not floor)
        box_h > 0.6 * box_w             # foot + ankle shape
    ):
        foot_mask[seg == 1] = 255
        selected += 1

    if selected == 2:  # two feet
        break

# ------------------ MASK POLISHING ------------------ #
kernel = np.ones((7, 7), np.uint8)

# Fill small holes
foot_mask = cv2.morphologyEx(foot_mask, cv2.MORPH_CLOSE, kernel)

# Remove small noise
foot_mask = cv2.morphologyEx(foot_mask, cv2.MORPH_OPEN, kernel)

# Keep only largest connected components (two feet)
num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(foot_mask)

clean_mask = np.zeros_like(foot_mask)

# Skip background label 0
areas = stats[1:, cv2.CC_STAT_AREA]
largest = np.argsort(areas)[-2:] + 1

for lbl in largest:
    clean_mask[labels == lbl] = 255

foot_mask = clean_mask

# ------------------ FINAL OUTPUT ------------------ #
result = cv2.bitwise_and(image_rgb, image_rgb, mask=foot_mask)

plt.figure(figsize=(6, 6))
plt.imshow(result)
plt.title("Final Foot Segmentation Output")
plt.axis("off")
plt.show()



