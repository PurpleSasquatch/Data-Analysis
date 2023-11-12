from tensorflow import keras
from keras.preprocessing.image import ImageDataGenerator
import pickle

#Preprocess the train images dataset by rotating skewing and zooming in on the images
image_gen = ImageDataGenerator(rotation_range=30, # rotate the image 30 degrees
                               width_shift_range=0.1, # Shift the pic width by a max of 10%
                               height_shift_range=0.1, # Shift the pic height by a max of 10%
                               rescale=1/255, # Rescale the image by normalzing it.
                               shear_range=0.2, # Shear means cutting away part of the image (max 20%)
                               zoom_range=0.2, # Zoom in by 20% max
                               horizontal_flip=True, # Allo horizontal flipping
                               fill_mode='nearest' # Fill in missing pixels with the nearest filled value
                              )

#apply image gen to directories
Malaria_Test_Preproccessed = image_gen.flow_from_directory(r"download/Malaria_categorised/test")
Malaria_Train_Preproccessed = image_gen.flow_from_directory(r"download/Malaria_categorised/train")

#reshape images
image_shape = (150,150,3)

savefilename = r'/app/data/Training_Images_Preprocessed.sav'
pickle.dump(Malaria_Train_Preproccessed, open(savefilename, 'wb'))

savefilename =  r'/app/data/Testing_Images_Preprocessed.sav'
pickle.dump(Malaria_Test_Preproccessed, open(savefilename, 'wb'))
