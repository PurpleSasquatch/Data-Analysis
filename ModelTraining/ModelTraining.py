from tensorflow import keras
import tensorflow as tf
import cv2
from keras.preprocessing.image import ImageDataGenerator
import pickle

loadfilename = r'download/Generated_Model.sav'
loaded_model = pickle.load(open(loadfilename, 'rb'))
result = loaded_model.score(X_test, Y_test)
print(result)

batch_size = 16

loadfilename = r'download/Training_Images_Preprocessed.sav'
PreprocessedTrainingImages = pickle.load(open(loadfilename, 'rb'))

loadfilename = r'download/Testing_Images_Preprocessed.sav'
PreprocessedTestingImages = pickle.load(open(loadfilename, 'rb'))
## Replace with loading files from volume
train_image_gen = image_gen.flow_from_directory(PreprocessedTrainingImages,
                                               target_size=image_shape[:2],
                                               batch_size=batch_size,
                                               class_mode='binary')


test_image_gen = image_gen.flow_from_directory(PreprocessedTestingImages,
                                               target_size=image_shape[:2],
                                               batch_size=batch_size,
                                               class_mode='binary')

train_image_gen.class_indices

import warnings
warnings.filterwarnings('ignore')

from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

results = model.fit_generator(train_image_gen,epochs=10,
                              steps_per_epoch=150,
                              validation_data=test_image_gen,
                             validation_steps=12)

results.history['val_accuracy']
plt.plot(results.history['val_accuracy'])
train_image_gen.class_indices

savefilename = r'download/Trained_Model.sav'
pickle.dump(model, open(savefilename, 'wb'))
