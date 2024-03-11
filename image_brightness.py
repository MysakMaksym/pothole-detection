import cv2
import numpy as np

def is_dark(image, threshold=50):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Calculate the average pixel intensity
    average_intensity = np.mean(gray)
    
    # Check if the average intensity is below the threshold
    return average_intensity < threshold

def adjust_brightness_contrast(image, brightness=50, contrast=50):
    # Adjust brightness and contrast using the cv2.addWeighted function
    adjusted_image = cv2.addWeighted(image, 1 + contrast / 100, np.zeros(image.shape, image.dtype), 0, brightness - contrast)
    
    # Clip the pixel values to be in the valid range [0, 255]
    adjusted_image = np.clip(adjusted_image, 0, 255)
    
    return adjusted_image

def process_image(input_path, output_path, brightness=50, contrast=50, dark_threshold=50):
    # Read the input image
    image = cv2.imread(input_path)
    
    # Check if the image is dark
    if is_dark(image, dark_threshold):
        # Adjust brightness and contrast
        adjusted_image = adjust_brightness_contrast(image, brightness, contrast)
        
        # Save the adjusted image
        cv2.imwrite(output_path, adjusted_image)
        print(f"Image adjusted and saved to {output_path}")
    else:
        print("Image is not dark. No adjustment needed.")

# Example usage:
input_image_path = "test_image5.jpg"
output_image_path = "output_image.jpg"
process_image(input_image_path, output_image_path, brightness=70, contrast=30, dark_threshold=50)
