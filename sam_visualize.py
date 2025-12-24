import cv2
import torch
import matplotlib.pyplot as plt
from segment_anything import sam_model_registry, SamAutomaticMaskGenerator

# Load image
image = cv2.imread("CF142.JPG")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Load SAM model
sam = sam_model_registry["vit_b"](
    checkpoint="sam_vit_b_01ec64.pth"
)
sam.to(device="cpu")

# Automatic mask generator
mask_generator = SamAutomaticMaskGenerator(
    sam,
    points_per_side=32,
    pred_iou_thresh=0.86,
    stability_score_thresh=0.92,
    min_mask_region_area=1000,
)

# Generate masks
masks = mask_generator.generate(image_rgb)

print(f"Total masks generated: {len(masks)}")

# Visualize masks
plt.figure(figsize=(6,6))
plt.imshow(image_rgb)
for mask in masks:
    m = mask["segmentation"]
    plt.contour(m, colors='yellow', linewidths=0.5)
plt.title("SAM Generated Masks")
plt.axis("off")
plt.show()
