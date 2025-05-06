import cv2
import os

# Function to extract frames from a video at 2x speed
def video_to_image_sequence(video_path, output_folder, speed_factor=2):
    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Unable to open video file.")
        return

    # Get the original frame rate of the video
    original_fps = int(cap.get(cv2.CAP_PROP_FPS))
    skip_frames = int(original_fps / speed_factor)

    frame_count = 0
    image_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Save only the frames corresponding to 2x speed
        if frame_count % skip_frames == 0:
            image_path = os.path.join(output_folder, f"frame_{image_count:04d}.png")
            cv2.imwrite(image_path, frame)
            image_count += 1

        frame_count += 1

    cap.release()
    print(f"Frames saved to {output_folder}")

# Usage
video_path = "path/to/your/video.mp4"  # Replace with your video file path
output_folder = "output_images"        # Replace with your desired output folder
video_to_image_sequence(video_path, output_folder)
