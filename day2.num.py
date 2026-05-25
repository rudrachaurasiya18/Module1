import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load Image
image =mpimg.imread("sample.jpg")

# Show Original Shape
print("Image Shape:", image.shape)

# -----------------------------
# Convert RGB to Grayscale
# -----------------------------

grayscale = np.mean(image[:, :, :3], axis=2)

# -----------------------------
# Increase Brightness
# -----------------------------

bright_image = np.clip(image + 50, 0, 255)

# -----------------------------
# Decrease Brightness
# -----------------------------

dark_image = np.clip(image - 50, 0, 255)

# -----------------------------
# Flip Horizontally
# -----------------------------

flip_horizontal = np.fliplr(image)

# -----------------------------
# Flip Vertically
# -----------------------------

flip_vertical = np.flipud(image)

# -----------------------------
# Crop Image
# -----------------------------

cropped = image[100:400, 100:400]

# -----------------------------
# Display Images
# -----------------------------

plt.figure(figsize=(15, 10))

# Original
plt.subplot(2, 4, 1)
plt.imshow(image)
plt.title("Original")
plt.axis("off")

# Grayscale
plt.subplot(2, 4, 2)
plt.imshow(grayscale, cmap='gray')
plt.title("Grayscale")
plt.axis("off")

# Bright
plt.subplot(2, 4, 3)
plt.imshow(bright_image.astype(np.uint8))
plt.title("Bright")
plt.axis("off")

# Dark
plt.subplot(2, 4, 4)
plt.imshow(dark_image.astype(np.uint8))
plt.title("Dark")
plt.axis("off")

# Horizontal Flip
plt.subplot(2, 4, 5)
plt.imshow(flip_horizontal)
plt.title("Horizontal Flip")
plt.axis("off")

# Vertical Flip
plt.subplot(2, 4, 6)
plt.imshow(flip_vertical)
plt.title("Vertical Flip")
plt.axis("off")

# Cropped
plt.subplot(2, 4, 7)
plt.imshow(cropped)
plt.title("Cropped")
plt.axis("off")

plt.tight_layout()
plt.show()