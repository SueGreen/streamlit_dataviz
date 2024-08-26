import streamlit as st
from pathlib import Path
from PIL import Image
from io import BytesIO
import pandas as pd
import zipfile

st.title('Hello')
st.write('World')

# Sample data
data = [
    {"name": "imgs/sunset.jpeg"},
    {"name": "imgs/sunrise.jpg"},
    {"name": "imgs/daylight.jpeg"},
    {"name": "imgs/night.jpeg"},
]
# data = pd.DataFrame.from_dict(data)


# Function to save all images in a zip file
def save_images():
    Path("images").mkdir(parents=True, exist_ok=True)

    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zf:
        for idx, row in enumerate(data):
            img_filename = Path(row['name'])
            img = Image.open(img_filename)
            img.save(img_filename)
            zf.write(img_filename, img_filename.name)

    zip_buffer.seek(0)
    return zip_buffer


# Button to save all images
zip_buffer = save_images()
st.write('---')
st.download_button(
    "Download All Images (Zip)", 
    data=zip_buffer, 
    file_name="images.zip", 
    mime="application/zip"
)
st.write('---')


for idx in range(len(data)):
    col1, col2 = st.columns([1, 1])
    img_filename = Path(data[idx].get("name")).name
    col1.write(img_filename)
    with col2:
        img_path = Path('imgs') / img_filename
        img = Image.open(img_path)
        st.image(img, caption=img_filename, use_column_width=True)

