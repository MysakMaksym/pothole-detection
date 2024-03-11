import cv2

def adjust_brightness_contrast(input_video_path, output_video_path, brightness=0, contrast=1):
    cap = cv2.VideoCapture(input_video_path)
    
    # Get the frames per second (fps), width, and height of the input video
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # Create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            break
        
        # Adjust brightness and contrast
        frame = cv2.convertScaleAbs(frame, alpha=contrast, beta=brightness)
        
        # Write the modified frame to the output video
        out.write(frame)
        
        cv2.imshow('Adjusted Video', frame)
        
        if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
            break
    
    cap.release()
    out.release()
    cv2.destroyAllWindows()

# Example usage:
input_video_path = 'test_video.mp4'
output_video_path = f'output_{input_video_path}'
brightness_value = 40  # Adjust as needed (positive values increase brightness)
contrast_value = 6   # Adjust as needed (values > 1 increase contrast, values < 1 decrease contrast)

adjust_brightness_contrast(input_video_path, output_video_path, brightness=brightness_value, contrast=contrast_value)
