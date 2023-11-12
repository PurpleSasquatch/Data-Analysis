import numpy as np
from tensorflow.keras.utils import load_img, img_to_array

loadfilename = r'app/data/Trained_Model.sav'
loaded_model = pickle.load(open(loadfilename, 'rb'))

loadfilename = r'app/data/Trained_Model.sav'
loaded_model = pickle.load(open(loadfilename, 'rb'))

# Display the image
Glass1 = cv2.imread(r'/app/dataset/Malaria_Test/Parasitized/C100P61ThinF_IMG_20150918_144104_cell_162.png')
Glass1 = cv2.cvtColor(Glass1,cv2.COLOR_BGR2RGB)
plt.imshow(Glass1)

glass_imgfile = r'/app/dataset/Malaria_Test/Uninfected/C100P61ThinF_IMG_20150918_144104_cell_144.png'
glassimg = load_img(glass_imgfile, target_size=(150, 150))
glassimg = img_to_array(glassimg)
glassimg = np.expand_dims(glassimg, axis=0)
glassimg= glassimg/255

prediction_prob = model.predict(glassimg)

def glasssortable(test):
    if test > 0.5: label = 'Table'
    else: label = 'Glass'
    return(label)

print(f'Prediction of image is a :', glasssortable(prediction_prob[0]), prediction_prob[0] )

table1 = cv2.imread( r'/app/dataset/Malaria_Train/Positive_Result_001')
table1 = cv2.cvtColor(table1,cv2.COLOR_BGR2RGB)
plt.imshow(table1)

table_imgfile = r'/app/dataset/Malaria_Train/Negtative_Result_001'

tableimg = load_img(table_imgfile, target_size=(150, 150))
tableimg = img_to_array(tableimg)

tableimg = np.expand_dims(tableimg, axis=0)
tableimg= tableimg/255
prediction_prob = model.predict(tableimg)
print(f'Prediction of image is a :', glasssortable(prediction_prob[0]), prediction_prob[0] )
