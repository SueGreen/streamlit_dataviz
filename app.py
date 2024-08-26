import streamlit as st
from pathlib import Path


st.title('Hello')
st.write('World')



if st.button('Save img', type='primary'):
    save_dir = Path('Saved')
    Path(save_dir).mkdir(parents=True, exist_ok=True)
    img_path = Path('images_sunset.jpeg')
    shutil.copy(img_path, save_dir)
    st.success(f"Saved at '{save_dir}'.")
    

