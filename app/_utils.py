import cv2

def resize_image(image, max_size=1200):
    """
    Resize the image to half original size while maintaining the aspect ratio
    """
    height, width = image.shape[:2]

    # Check if resizing is necessary
    if height <= max_size and width <= max_size:
        return image  # No resizing needed

    # Set it to half original size
    scale_factor = 0.5

    # Calculate new dimensions
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)

    # Resize the image
    resized_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)
    return resized_image