#!usr/bin/python3

# Importing Libraries
import keras
from keras.models import Sequential
from keras.models import model_from_json
from keras.layers import Conv2D, MaxPooling2D
from keras.optimizers import RMSprop, Adam, SGD
from keras.layers import Dense, Dropout, Flatten

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

from google.colab import drive
drive.mount('/content/drive')

"""# **Loading all three datasets and concatenating them**"""

# Loading all three datasets and concatenating them
td0=np.load('/content/drive/MyDrive/Assign1/Data/data0.npy')
tl0=np.load('/content/drive/MyDrive/Assign1/Data/lab0.npy')
td1=np.load('/content/drive/MyDrive/Assign1/Data/data1.npy')
tl1=np.load('/content/drive/MyDrive/Assign1/Data/lab1.npy')
td2=np.load('/content/drive/MyDrive/Assign1/Data/data2.npy')
tl2=np.load('/content/drive/MyDrive/Assign1/Data/lab2.npy')
td = np.concatenate([td0, td1, td2], axis=0)
tl = np.concatenate([tl0,tl1,tl2], axis=0)

"""# **Splitting the datset for training and testing**"""

# Train and Test Data Split
x_train, x_test, y_train, y_test = train_test_split(td, tl, test_size=0.2)


train_new_model = True

if train_new_model:
# Preprocessing the input data
  num_of_trainImgs = x_train.shape[0] 
  num_of_testImgs = x_test.shape[0] 
  img_width = 168
  img_height = 40

# Reshaping the images
  x_train = x_train.reshape(x_train.shape[0], img_height, img_width, 1)
  x_test = x_test.reshape(x_test.shape[0], img_height, img_width, 1)
  test = test.reshape(test.shape[0], img_height, img_width, 1)
  input_shape = (img_height, img_width,1)
 
  x_train = x_train.astype('float32')
  x_test = x_test.astype('float32')

# Normalize inputs from 0-255 to 0-1
  x_train /= 255
  x_test /= 255

# Converting the class vectors to binary class
  num_classes = 37
  y_train = keras.utils.to_categorical(y_train, num_classes)
  y_test = keras.utils.to_categorical(y_test, num_classes)
  
 model = Sequential()
  model.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=input_shape))
  model.add(Conv2D(32, (3, 3), activation='relu'))
  model.add(MaxPooling2D((2,2)))
  model.add(Dropout(0.2)) 

  model.add(Conv2D(64, (3,3), padding='same', activation='relu'))
  model.add(Conv2D(64, (3,3), activation='relu'))
  model.add(MaxPooling2D((2,2)))
  model.add(Dropout(0.2)) 

  model.add(Conv2D(128, (3,3), padding='same', activation='relu'))
  model.add(Conv2D(128, (3,3), activation='relu'))
  model.add(Activation('relu'))
  model.add(MaxPooling2D((2,2)))
  model.add(Dropout(0.2)) 

#### Fully-Connected Layer ####
  model.add(Flatten())
  model.add(Dense(1024, activation='relu'))
  model.add(Dropout(0.2))
  model.add(Dense(512, activation='relu'))
  model.add(Dense(128, activation='relu'))
  model.add(Dense(64, activation='relu'))
  model.add(Dropout(0.2))
  model.add(Dense(num_classes, activation='softmax'))
  model.summary()

# Defining Optimizer
  optimizerAdam = Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0, amsgrad=False)
# Compiling the model
  model.compile(optimizer = optimizerAdam , loss = "categorical_crossentropy", metrics=["accuracy"])
  
# Fitting the model  
  history = model.fit(x_train, y_train,
          batch_size=128,
          epochs=25,
          verbose=False,
          validation_data=(x_test, y_test))

# Serialize model to json
  json_model = model.to_json()

# Save the model architecture to JSON file
  with open('Trained_model.json', 'w') as json_file:
      json_file.write(json_model)

# Saving model.add(Dropout(0.3))the weights of the model
  model.save_weights('Trained_weights.h5')

# Evaluate the model
  score = model.evaluate(x_test, y_test, verbose=1)
  print("%s: %.1f%%" % (model.metrics_names[0], score[0]))
  print("%s: %.1f%%" % (model.metrics_names[1], score[1]*100))


else:
# Load json and create model
  json_file = open('Trained_model.json', 'r')
  loaded_model_json = json_file.read()
  json_file.close()
  loaded_model = model_from_json(loaded_model_json)

# Load weights into new model
  loaded_model.load_weights("Trained_weights.h5")
  print("Loaded model from disk")
 
# Evaluate loaded model on test data
  #loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
  #score = loaded_model.evaluate(x_test, y_test, verbose=1)
  #print("%s: %.1f%%" % (loaded_model.metrics_names[0], score[0]))
  #print("%s: %.1f%%" % (loaded_model.metrics_names[1], score[1]*100))

  prediction = loaded_model.predict_classes(test)
  np.save('prediction', prediction)
  

"""# **Model Accuracy and Loss plots**"""

# Analyzing the model
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
