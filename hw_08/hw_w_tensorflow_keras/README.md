## How to use

First unzip the data.zip file this is going to create a folder called data at the same level as ntbk folder

## Setup tensorflow on your system (only if using your own system)

If you have a gpu available, to use it you have to review commands for:

• Install cuda compiler (system wide):
  – sudo apt install nvidia-cuda-toolkit
  
• Install tensorflow and cuda (on your virtual environment):
  – pip install tensorflow[and-cuda]


Later depending on which version you install you may have to fix keras imports as the version of keras has changed
unless you specifically use the version in the lectures you have to fix the imports to use a newer version,
what I did was use prefix:
  - from keras._tf_keras.keras.
  
Now after the last dot you can import specific packages like:
  - from keras._tf_keras.keras.preproccessing
  - from keras._tf_keras.keras.applications
  - from keras._tf_keras.keras.layers

You get it now.

Using the previous setup it is possible to use a pre-trained model to try out the notebook in the lectures
using the homework data.
