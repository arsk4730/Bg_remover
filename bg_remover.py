from rembg import remove
from PIL import Image
import streamlit as st
import io

# Web App का Title
st.title("🔥 AI Background Remover")

# Image Upload Option
uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Image Read करो
    input_image = Image.open(uploaded_file)
    st.image(input_image, caption="Original Image", use_column_width=True)

    # Remove Background
    output_image = remove(input_image)

    # Show Processed Image
    st.image(output_image, caption="Background Removed", use_column_width=True)

    # Download Button
    img_bytes = io.BytesIO()
    output_image.save(img_bytes, format="PNG")
    img_bytes.seek(0)
    st.download_button(label="Download Image", data=img_bytes, file_name="bg_removed.png", mime="image/png")
