from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from PIL import Image
import numpy as np
import tensorflow as tf
from io import BytesIO
from keras.models import load_model
from pathlib import Path
# from model import anup.h5 as mode
img_size = 128
# import pickle

BASE_DIR = Path(__file__).resolve(strict=True).parent
print(BASE_DIR, "kdkfhk 233 2442")

# Assuming BASE_DIR is defined correctly and points to the right directory
# model = pickle.load(open("anup.h5", 'rb'))
# model = tf.keras.models.load_model(f"{BASE_DIR}/anup.h5", compile=False)
model = load_model(f"{BASE_DIR}/fmodel.h5", compile=False)


# Load the TensorFlow colorization model (replace 'anup.h5' with your actual model file)


# Image processing and colorization function
def colorize_image(image: Image.Image):
    """
    Preprocesses the input grayscale image, passes it through the TensorFlow model, 
    and returns the colorized image.
    """
      # Set the size based on the input size expected by your model


    a = []

        # Resize the RGB image
    rgb = image.resize((img_size, img_size))

        # Convert to grayscale
    gray = rgb.convert('L')

        # Convert to numpy array, normalize, and reshape grayscale array
    gray_array = np.asarray(gray).reshape(( img_size, img_size, 1)) / 255.0
    a.append(gray_array)
    d= np.asanyarray(a)
        

        # Generate colorized output
    output = model(d[0:]).numpy()

        # Convert output to image format
    color_output = Image.fromarray((output[0] * 255).astype('uint8')).resize((1024, 1024))

    return color_output
   



   
  



