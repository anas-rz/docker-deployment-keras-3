import streamlit as st
from PIL import Image
import numpy as np

from keras.preprocessing import image
from keras.applications.imagenet_utils import decode_predictions
from model import mixer_b16_224

model = mixer_b16_224(pretrained=True)


def load_and_preprocess(image_file):
    img = image.load_img(image_file, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


st.title("Image Classification App")
st.write("Upload an image to classify:")

uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image")

    try:
        processed_image = load_and_preprocess(uploaded_file)
        prediction = model.predict(processed_image)
        prediction = decode_predictions(prediction, top=1)[0][0][1]
        st.success(f"Classified as: {prediction}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
        uploaded_file = None
