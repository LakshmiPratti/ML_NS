# Deep Learning Programming Assignment

## Process flow

- Importing Libraries
- Preparing the Dataset
- Model Building
- Model Fitting
- Evaluate the model
- Analyzing the model
- Predicting the test data

## Description 
- A dataset containing images having 4 digits with labels are the sum of those four digits is given and we have to train our model such that it predicts the sum of those four digits in test datase.
- Trained a CNN (Convolutional Neural Network) on the dataset, which contains a total of 30,000 images containing 4 handwritten digits from 0-9 in each image formatted as 168×40-pixel images.
- Splitted the dataset into train and test data with size 24,000 and 6,000 respectively.
- Preprocessed the input data by reshaping the image and scaling the pixel values between 0 and 1.
- Designed the neural network, here it is Sequential which is prebuilt in keras. Imported Dense layer, which will be used to predict the labels, then the Dropout layer which reduces overfitting , and then Flatten, which will help to convert a 3-d Array to 1-d.
- Trained the model.
- Trained model architecture and weights were saved. 

### How to run    
 ```bash
#If running on your local machine
python3 code.py

```

### Importing Libraries

```python
import keras
from keras.models import Sequential
from keras.models import model_from_json
from keras.layers import Conv2D, MaxPooling2D
from keras.optimizers import RMSprop, Adam, SGD
from keras.layers import Dense, Dropout, Flatten

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

```
