"""This Python script is taken from Introduction to Deep Learning and Tensorflow, part 2. This is training a basic Convolutional Neural Network for MNIST classification."""

# Load all libraries and helper functions 
import tensorflow as tf
import numpy as np
import sys
import pandas as pd
import os
import urllib
print("TensorFlow version %s is loaded." % tf.__version__)

print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))

# Load the mnist dataset built into TensorFlow
mnist = tf.keras.datasets.mnist
(inputs_train, labels_train), (inputs_test, labels_test) = mnist.load_data()

# Squash the training data to values that range between 0 and 1.
inputs_train, inputs_test = inputs_train / 255.0, inputs_test / 255.0

# TensorFlow networks take inputs with shape (number of samples, height, width, channels)
# The current shape for the inputs are (number of samples, height, width)
# We therefore need to add an extra dimension at the end
inputs_train = np.expand_dims(inputs_train, axis=-1)
inputs_test = np.expand_dims(inputs_test, axis=-1)

# Print shapes of all our data as a sanity check
print('inputs_train shape: ',inputs_train.shape)
print('labels_train shape: ',labels_train.shape)
print('inputs_test shape: ',inputs_test.shape)
print('labels_test shape: ',labels_test.shape)

# Use tf.data to batch and shuffle the dataset:
train_ds = tf.data.Dataset.from_tensor_slices((inputs_train, labels_train)).shuffle(10000).batch(32)
test_ds = tf.data.Dataset.from_tensor_slices((inputs_test, labels_test)).batch(32)

# Example of a very simple Conv Net
class MyConvNet(tf.keras.Model):
  def __init__(self):
    # This function runs whenever you create an instance of your model.
    # Since it only runs once, you should initialise all your trainable variables here. Basically any layer that contains "weights" in your model.
    super(MyConvNet, self).__init__()
    self.conv1 = tf.keras.layers.Conv2D(32, 3, activation='relu')
    self.flatten = tf.keras.layers.Flatten()
    self.dense1 = tf.keras.layers.Dense(64, activation='relu')
    self.dense2 = tf.keras.layers.Dense(10)

  def call(self, x):
    # This function runs every time you call the model: output = model(input).
    # Since it runs frequently, you should NOT initialise any trainable variables here.
    # If you do so, those weights will be re-initialised at every call, hence defeating the purpose of the training process.
    x = self.conv1(x)
    x = self.flatten(x)
    x = self.dense1(x)
    return self.dense2(x)

# Create an instance of the model
model = MyConvNet()

# We use SparseCategoricalCrossentropy as the loss function and Adam as the gradient descent function.
loss_function = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
optimizer = tf.keras.optimizers.Adam(learning_rate=1e-7)

# We create the x_loss and x_accuracy objects to help keep track of model performance during training. 
# The loss and accuracy values at each step of the training process are aggregated in the objects and can be printed out at the end of each training epoch.
train_loss = tf.keras.metrics.Mean(name='train_loss')
train_accuracy = tf.keras.metrics.SparseCategoricalAccuracy(name='train_accuracy')
test_loss = tf.keras.metrics.Mean(name='test_loss')
test_accuracy = tf.keras.metrics.SparseCategoricalAccuracy(name='test_accuracy')


# The function train_step executes the forward and backward propagation of a single batch of images during the training process.
# As the TensorFlow documentation puts it, when you annotate a function with tf.function, you can still call it like any other function. 
# But it will be compiled into a graph, which means you get the benefits of faster execution, running on GPU or TPU, or exporting to SavedModel.
@tf.function
def train_step(images, labels):
  with tf.GradientTape() as tape:
    # training=True is only needed if there are layers with different behavior during training versus inference (e.g. Dropout).
    # It is best to include it if you are ever unsure. True during training, False during validation / testing / inference.
    predictions = model(images, training=True)
    train_step_loss = loss_function(labels, predictions)
  # Determine the gradients for each trainable variable (weights) based on the loss function
  gradients = tape.gradient(train_step_loss, model.trainable_variables)
  # Apply the optimiser to the gradients to perform gradient descent
  optimizer.apply_gradients(zip(gradients, model.trainable_variables))
  train_loss(train_step_loss)
  train_accuracy(labels, predictions)

# The function test_step executes the inference (forward propagation) of a single batch of testing image.
def test_step(images, labels, confusion_matrix):
  # training=True is only needed if there are layers with different behavior during training versus inference (e.g. Dropout).
  # It is best to include it if you are ever unsure. True during training, False during validation / testing / inference.
  predictions = model(images, training=False)
  test_step_loss = loss_function(labels, predictions)
  test_loss(test_step_loss)
  test_accuracy(labels, predictions)
  pred_class = np.argmax(predictions.numpy(), axis=-1)
  for i in range(labels.shape[0]):
    confusion_matrix[labels[i],pred_class[i]] += 1


max_epochs = 20
for epoch in range(max_epochs):
  # Reset the metrics at the start of the next epoch
  train_loss.reset_states()
  train_accuracy.reset_states()
  test_loss.reset_states()
  test_accuracy.reset_states()
  confusion_matrix = np.zeros((10,10))

  # Perform training across the entire train set
  for inputs, labels in train_ds:
    train_step(inputs, labels)

  # Perform testing across the entire test set
  for test_inputs, test_labels in test_ds:
    test_step(test_inputs, test_labels, confusion_matrix)

  template = 'Epoch {}, Loss: {}, Accuracy: {}, Test Loss: {}, Test Accuracy: {}'
  print(template.format(epoch+1,
                        train_loss.result(),
                        train_accuracy.result()*100,
                        test_loss.result(),
                        test_accuracy.result()*100))
  print('Confusion matrix: rows represent labels, columns represent predictions')
  print(np.asarray(confusion_matrix,np.int32))
