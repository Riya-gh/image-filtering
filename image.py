import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image from your laptop
image_path = r"C:\users\tirum\OneDrive\Pictures\blurred image.jpg"  # Update this with your image path
image = cv2.imread(image_path)
sharpening_kernel = np.array([[-1, -1, -1], 
                              [-1,  9, -1], 
                              [-1, -1, -1]])

# Apply the sharpening filter
sharpened_image = cv2.filter2D(image, -1, sharpening_kernel)


# Convert images from BGR to RGB (for correct color display in Matplotlib)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
filtered_image_rgb = cv2.cvtColor( sharpened_image, cv2.COLOR_BGR2RGB)

# Display the original and blurred image side by side
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(filtered_image_rgb)
plt.title("filtered image")
plt.axis("off")

plt.show()
