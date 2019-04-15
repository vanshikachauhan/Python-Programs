from tkinter import *

root=Tk()

def printname():
    #declare headers
    from keras.datasets import mnist
    from keras import models
    from keras import layers
    from keras.utils import to_categorical
    #loading mnist data sets

    (train_image,train_lebels),(test_image,test_lebels)=mnist.load_data()


    train_image=train_image.reshape((60000,28*28))
    train_image=train_image.astype('float32')/255
    test_image=test_image.reshape((10000,28*28))
    test_image=test_image.astype('float32')/255


    #declare model architecture
    model=models.Sequential()
    #define the model layers
    model.add(layers.Dense(60,activation='relu',input_shape=(28*28,)))

    model.add(layers.Dense(30,activation='relu'))
    model.add(layers.Dense(10,activation='softmax'))

    #compile the program

    model.compile(optimizer='sgd',loss='categorical_crossentropy',metrics=['accuracy'])



    train_lebels= to_categorical(train_lebels)
    test_lebels= to_categorical(test_lebels)
    #fiting the data
    model.fit(train_image,train_lebels,epochs=3,batch_size=500)


def evaluate():
    #evaluate model on test data
    Score=model.evaluate(test_image,test_lebels,verbose=1)
    print("test accuracy:",Score[1]*100)
    model.save('2dense.h5')






















button=Button(root,text="clickme",command=printname)
button.pack()

button=Button(root,text="clickme",command=evaluate)
button.pack()

root.mainloop()#it does not let the window close

