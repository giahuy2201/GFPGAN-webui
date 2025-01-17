import cv2

def resize_image(image, max_size=720):
    """
    Resize the image so both sides are less than or equal to max_size while maintaining the aspect ratio
    """
    height, width = image.shape[:2]

    # Check if resizing is necessary
    if height <= max_size and width <= max_size:
        return image  # No resizing needed

    # Calculate the scaling factor
    scale_factor = min(max_size / height, max_size / width)

    # Calculate new dimensions
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)

    # Resize the image
    resized_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)
    return resized_image