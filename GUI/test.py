from keras import Input
from keras.models import load_model
import numpy as np
from keras.preprocessing.image import load_img
import keras.preprocessing.image as im
img_size = (224, 224)


model = load_model("vggNet-00017--0.1318.h5")


def get_result(image):
    img_data = load_img(image, target_size=img_size)
    img_data = im.img_to_array(img_data)
    img_data = np.expand_dims(img_data, axis=0)
    predic = model.predict(img_data)
    return (1 - float(predic[0]))*100


if __name__ == '__main__':
    nomal_lit = list()
    ab_lit = list()
    for i in range(1, 7):
        img_data = load_img('images/no'+str(i)+'.jpg', target_size=img_size)
        img_data = im.img_to_array(img_data)
        img_data = np.expand_dims(img_data, axis=0)
        predic = model.predict(img_data)
        nomal_lit.append(predic[0])
    for i in range(1, 7):
        img_data = load_img('images/ab'+str(i)+'.jpg', target_size=img_size)
        img_data = im.img_to_array(img_data)
        img_data = np.expand_dims(img_data, axis=0)
        predic = model.predict(img_data)
        ab_lit.append(predic[0])
    print('--test -- ')
    print('normal')
    print(nomal_lit)
    print('abnormal')
    print(ab_lit)
