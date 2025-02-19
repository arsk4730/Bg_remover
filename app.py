import streamlit as st
import cv2
import numpy as np
import rembg
from PIL import Image

st.title("Background Remover App")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img_array = np.array(image)

    st.image(image, caption="Original Image", use_column_width=True)

    # Remove background
    output = rembg.remove(img_array)

    # Convert to PIL image
    output_image = Image.fromarray(output)

    st.image(output_image, caption="Background Removed", use_column_width=True)

    # Download button
    st.download_button(
        label="Download Image",
        data=output_image.tobytes(),
        file_name="bg_removed.png",
        mime="image/png"
    )
