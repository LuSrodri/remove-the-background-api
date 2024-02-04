import cv2
from rembg import remove, new_session

def remove_background(image_path):
    image_name = image_path.split('\\')[-1]
    output_image_path = './uploads\\' + image_name.split('.')[0] + '_no_bg.png'

    input = cv2.imread(image_path)
    model_name = "silueta"
    session = new_session(model_name)
    output = remove(input, session=session, post_process_mask=True)
    cv2.imwrite(output_image_path, output)

    return output_image_path