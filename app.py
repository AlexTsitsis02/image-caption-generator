import streamlit as st
from PIL import Image
from model import generate_caption

# Streamlit UI
st.title("🖼️ AI Image Caption Generator")
st.write("Upload an image, and the AI will generate a caption for it.")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    caption = generate_caption(uploaded_file)
    
    st.subheader("📝 Generated Caption:")
    st.write(f"**{caption}**")
