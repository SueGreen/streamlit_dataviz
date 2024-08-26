import streamlit as st
from pathlib import Path
import shutil
from PIL import Image
import os
from io import BytesIO
import requests
import zipfile

st.title('Hello')
st.write('World')

# Sample data
data = [
    {"name": "imgs/images_sunset.jpeg"},
    {"name": "imgs/images_sunrise.jpg"},
]


# Function to save all images in a zip file
def save_images():
    Path("images").mkdir(parents=True, exist_ok=True)

    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zf:
        for idx, row in enumerate(data):
            img_filename = Path(row['name'])
            img = Image.open(img_filename)
            img.save(img_filename)
            zf.write(img_filename, os.path.basename(img_filename))

    zip_buffer.seek(0)
    return zip_buffer


# Button to save all images
if st.button("Download All Images"):
    zip_buffer = save_images()
    st.download_button(
        "Download Zip", 
        data=zip_buffer, 
        file_name="images.zip", 
        mime="application/zip"
    )


for idx in range(len(data)):
    col1, col2 = st.columns([1, 1])
    img_filename = Path(data[idx].get("name")).name
    col1.write(img_filename)
    with col2:
        img_path = Path('imgs') / img_filename
        img = Image.open(img_path)
        st.image(img, caption=img_filename, use_column_width=True)

