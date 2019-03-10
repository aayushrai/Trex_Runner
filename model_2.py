from keras.models import Sequential
from keras.layers import Dense,Conv2D,MaxPooling2D,Flatten,Activation,Dropout
from keras.preprocessing.image import ImageDataGenerator

img_gen = ImageDataGenerator(rescale=1/255)


model = Sequential()
model.add(Conv2D(filters=32,kernel_size=(3,3),input_shape=(80, 270,3),activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(filters=32,kernel_size=(3,3),input_shape=(80, 270,3),activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(filters=64,kernel_size=(3,3),input_shape=(80, 270,3),activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(128))
model.add(Activation("relu"))
model.add(Dropout(.4))
model.add(Dense(2))
model.add(Activation("sigmoid"))

model.compile(loss="categorical_crossentropy",optimizer="adam",metrics=["accuracy"])

train_image_gen = img_gen.flow_from_directory("Data_2",target_size=(80,270),batch_size= 5)
print(train_image_gen.class_indices)
results = model.fit_generator(train_image_gen,epochs=30,steps_per_epoch=65)
model.save("model\\trex_6.h5")
