import streamlit as st
from pathlib import Path
import shutil

st.title('Hello')
st.write('World')



#if st.button('Save img', type='primary'):
#    save_dir = Path('Saved')
#    Path(save_dir).mkdir(parents=True, exist_ok=True)
#    img_path = Path('images_sunset.jpeg')
#    shutil.copy(img_path, save_dir)
#    st.success(f"Saved at '{save_dir}'.")
#    

with open(Path("imgs.zip"), "rb") as file:
    btn = st.download_button(
        label="Download data",
        data=file,
        file_name=Path("imgs.zip"),
        #mime="image/jpeg",
    )


