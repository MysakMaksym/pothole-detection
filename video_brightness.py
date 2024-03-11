import cv2
import numpy as np

def calculate_video_brightness(video_path):
    cap = cv2.VideoCapture(video_path)
    
    total_brightness = 0
    frame_count = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Convert the frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Calculate the average brightness of the frame
        brightness = np.mean(gray_frame)

        # Accumulate the brightness values
        total_brightness += brightness
        frame_count += 1

    cap.release()

    # Calculate the average brightness across all frames
    average_brightness = total_brightness / frame_count

    return average_brightness

# Example usage:
video_path = 'test_video.mp4'
brightness_threshold = 100  # You can adjust this threshold based on your requirements

average_brightness = calculate_video_brightness(video_path)
print(average_brightness)
if average_brightness < brightness_threshold:
    print("The video is dark. You may want to increase brightness.")
else:
    print("The video is bright enough.")
