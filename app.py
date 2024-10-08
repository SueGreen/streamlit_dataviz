import streamlit as st
from pathlib import Path
from PIL import Image
from io import BytesIO
import pandas as pd
import zipfile

# st.set_page_config(layout='wide')
st.title('Hello')
st.write('World')

data = {
    "name": [
        "sunset.jpeg",
        "sunrise.jpg",
        "daylight.jpeg",
        "night.jpeg",
    ]
}
data = pd.DataFrame.from_dict(data)

st.dataframe(data)

# Function to save all images in a zip file
def save_images():
    Path("output").mkdir(parents=True, exist_ok=True)

    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zf:
        for idx in range(len(data)):
            row = data.iloc[idx]
            img_filepath = Path('imgs') / row['name']
            img = Image.open(img_filepath)
            img.save(img_filepath)
            zf.write(img_filepath, img_filepath.name)

        df_filepath = Path('data.csv')
        data.to_csv(df_filepath)
        zf.write(df_filepath, df_filepath.name)
    zip_buffer.seek(0)
    return zip_buffer


# Button to save all images
zip_buffer = save_images()
st.write('---')
st.download_button(
    "Download All Data (Zip)", 
    data=zip_buffer, 
    file_name="daytimes_data.zip", 
    mime="application/zip"
)
st.write('---')


for idx in range(len(data)):
    col1, col2 = st.columns([1, 1])
    img_filename = Path(data.iloc[idx]["name"])
    col1.write(img_filename)
    with col2:
        img_path = Path('imgs') / img_filename
        img = Image.open(img_path)
        st.image(img, caption=img_filename, use_column_width=True)

