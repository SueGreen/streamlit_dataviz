import streamlit as st
from pathlib import Path
import shutil
from PIL import Image

st.title('Hello')
st.write('World')



#if st.button('Save img', type='primary'):
#    save_dir = Path('Saved')
#    Path(save_dir).mkdir(parents=True, exist_ok=True)
#    img_path = Path('images_sunset.jpeg')
#    shutil.copy(img_path, save_dir)
#    st.success(f"Saved at '{save_dir}'.")
#    

#with open(Path("imgs.zip"), "rb") as file:
#    btn = st.download_button(
#        label="Download data",
#        data=file,
#        file_name=Path("imgs.zip"),
#        #mime="image/jpeg",
#    )



import streamlit as st
import os
from PIL import Image
from io import BytesIO
import requests
import zipfile

# Sample data
data = [
    {"name": "imgs/images_sunset.jpeg"},
]

## Function to download and display high-quality images
#def download_image(url):
#    response = requests.get(url)
#    img = Image.open(BytesIO(response.content))
#    return img

# Function to save all images in a zip file
def save_images():
    if not os.path.exists("images"):
        os.makedirs("images")

    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zf:
        for idx, row in enumerate(data):
            #img = download_image(row["image_url"])
            #img_filename = f"images/{row['name'].replace(' ', '_').lower()}.png"
            img_filename = Path(row['name'])
            img = Image.open(img_filename)
            img.save(img_filename)
            zf.write(img_filename, os.path.basename(img_filename))

    zip_buffer.seek(0)
    return zip_buffer


# Button to save all images
if st.button("Download All Images"):
    zip_buffer = save_images()
    st.download_button("Download Zip", data=zip_buffer, file_name="images.zip", mime="application/zip")



