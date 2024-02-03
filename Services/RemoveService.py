import cv2
from rembg import remove

def remove_background(image_path):
    image_name = image_path.split('\\')[-1]
    output_image_path = './uploads\\' + image_name.split('.')[0] + '_no_bg.png'

    input = cv2.imread(image_path)
    output = remove(input)
    cv2.imwrite(output_image_path, output)

    return output_image_path