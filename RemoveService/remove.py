import numpy as np
from sklearn.cluster import KMeans
import cv2
import os

def remove_background(image_path):
    image = cv2.imread(image_path, cv2.COLOR_BGR2RGB)

    image_norm = image.copy()/255

    X = np.ravel(image_norm)

    qtdLinhas = image.shape[0] * image.shape[1]
    X = np.reshape( X, (qtdLinhas,3) )

    model = KMeans(n_clusters=2, max_iter=1, random_state=10)
    model.fit(X)
    pred = model.predict(X)

    cluster = np.argmax(model.cluster_centers_[:,0])

    pred = np.reshape(pred, (image.shape[0], image.shape[1]))

    mask = pred == cluster

    image[mask] = [255, 255, 255]

    image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)

    white_pixels = (image[:,:,0] == 255) & (image[:,:,1] == 255) & (image[:,:,2] == 255)

    image[white_pixels] = [0, 0, 0, 0]

    image_name = image_path.split('\\')[-1]
    new_image_path = './uploads\\' + image_name.split('.')[0] + '_no_bg.png'
    cv2.imwrite(new_image_path, image)

    return new_image_path