import cv2
import numpy as np
import tensorflow as tf

def find_grid(image):
    image = cv2.resize(image,(900,900))
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    gray = cv2.bitwise_not(gray)
    model = tf.keras.models.load_model("digits-ocr.h5")
    numbers =[]
    rows = np.vsplit(gray,9)
    for row in rows:
        cols = np.hsplit(row,9)
        for box in cols:
            box = cv2.resize(box,(30,30))/255.0
            box = box[1:29,1:29]
            kernel = np.ones((3,3))
            box = cv2.dilate(box,kernel)
            white = np.sum(box>0)
            if(white == 0):
                numbers.append(0)
                continue
            box = box.reshape(-1,28,28,1)
            prediction = model.predict(box)
            numbers.append(np.argmax(prediction))
    return np.array(numbers).reshape((9,9))
