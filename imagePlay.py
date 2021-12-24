# operations save image download 
import streamlit as st
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

def main():
    selected_box = st.sidebar.selectbox('Select from dropdown', ('Play with Images', 'About the App'))   
    if selected_box == 'About the App':
        about() 
    if selected_box == 'Play with Images':
        play_with_images()

def about():
    st.title("Welcome to ImagePlay!")
    st.caption("An web application to perform basic image processing operations")
    with st.expander("About"):
        st.write("""""")
    with st.expander("Supported Operations"):
        st.write("Following operations are supported by the web app currently")
        st.markdown("""
        * Image Negative 
        * Channel Swapping
        * Fourier Domain
        * Image Sharpening
        * Image Smoothing
        * Contrast Enhancement
        * Grayscale
        * Image Resizing
        * Crop Image
        * Channel Splitting
        * Plot Histogram
        * Rotate Image
        * Flip Image""")
    with st.expander("Created By"):
        st.write("""Pranjali Bajpai - 2018EEB1243""")

def play_with_images():
    st.title("Welcome to ImagePlay!")
    st.caption("An web application to perform basic image processing operations")
    file = st.file_uploader("Please upload an image file", type=["jpg", "png"])
    operationType = st.radio("Select one of the operations", ('Image Negative', 'Channel Swapping', 'Fourier Domain', 'Image Sharpening', 'Image Smoothing', 'Contrast Enhancement', 'Grayscale', 'Image Resizing', 'Crop Image', 'Channel Splitting', 'Plot Histogram', 'Rotate Image', 'Flip Image'))
    if file is None:
        st.text("Please upload an image file to continue")
    else:
        image = Image.open(file)
        if operationType == 'Image Negative':
            image_negative(image)
        elif operationType == 'Channel Swapping':
            channel_swapping(image)
        elif operationType == 'Fourier Domain':
            fourier_domain(image)
        elif operationType == 'Image Sharpening':
            image_sharpening(image)
        elif operationType == 'Image Smoothing':
            image_smoothing(image)
        elif operationType == 'Contrast Enhancement':
            contrast_enhancement(image)
        elif operationType == 'Grayscale':
            grayscale(image)
        elif operationType == 'Image Resizing':
            image_resizing(image)
        elif operationType == 'Crop Image':
            channel_swapping(image)
        elif operationType == 'Channel Splitting':
            channel_splitting(image)
        elif operationType == 'Plot Histogram':
            plot_histogram(image)
        elif operationType == 'Rotate Image':
            rotate_image(image)
        elif operationType == 'Flip Image':
            flip_image(image)

# Function to generate photographic negative image of input image
def ImNegative(image):
    image = image.convert('L') # Convert to grayscale image
    x, y = image.size # Size of image
    L = 256 # Intensity levels in image
    negativeIm = image.copy() # Make a copy of the input image
    
    # Traverse over every pixel
    for i in range (0, x-1): 
        for j in range (0, y-1):
            currentVal = image.getpixel((i, j)) # Get Current Pixel Intensity value
            negativeVal = L-1-currentVal # Apply negative transformation
            negativeIm.putpixel((i, j), negativeVal) # Put the new Pixel at (i, j) position
    
    return negativeIm

def image_negative(image):
    if image.mode != 'RGB':
        st.text("Please upload RGB image")
    else:
        st.text("Uploaded Image")
        st.image(image)
        with st.spinner('Wait for it...'):
            negativeIm = ImNegative(image)
            st.text("Image Negative")
            st.image(negativeIm)
            if(st.button("Download Negative Image")):
                negativeIm.save('negativeIm.png')
                st.success("Image Downloaded successfully!")

def channel_splitting(image):
    if image.mode != 'RGB':
        st.text("Please upload RGB image")
    else:
        st.text("Uploaded Image")
        st.image(image)
        with st.spinner('Wait for it...'):
            imageR, imageG, imageB = image.split()
            x, y=image.size
            Rchannel = np.zeros((y, x, 3), dtype = "uint8")
            Bchannel = np.zeros((y, x, 3), dtype = "uint8")
            Gchannel = np.zeros((y, x, 3), dtype = "uint8")
            # Create individual components image
            Rchannel[:, :, 0]= imageR;
            Bchannel[:, :, 1]= imageB;
            Gchannel[:, :, 2]= imageG;
            # Convert array to image
            Rchannel = Image.fromarray(Rchannel) 
            Bchannel = Image.fromarray(Bchannel) 
            Gchannel = Image.fromarray(Gchannel) 
            
            st.text("Red channel")
            st.image(Rchannel)
            st.text("Green channel")
            st.image(Gchannel)
            st.text("Blue channel")
            st.image(Bchannel)
            if(st.button("Download Image")):
                Rchannel.save('Rchannel.png')
                Gchannel.save('Gchannel.png')
                Bchannel.save('Bchannel.png')
                st.success("Image Downloaded successfully!")


if __name__ == "__main__":
    main()
