import cv2


def convert_to_8bit(image_path, output_path):

    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Image at {image_path} could not be loaded. Check the file path.")

    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    cv2.imwrite(output_path, rgb_image)
    print(f"Image converted to 8-bit RGB and saved to {output_path}")


image_path=r'C:\Users\User\Downloads\obama.jpg'
output_path=r'C:\Users\User\Downloads\result.jpg'
convert_to_8bit(image_path,output_path)