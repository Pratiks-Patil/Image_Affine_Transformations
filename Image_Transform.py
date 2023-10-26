import streamlit as st
import cv2
import numpy as np

# Function to perform a translation transformation
def apply_translation(image, translation_value):
    height, width = image.shape[:2]
    translation_matrix = np.float32([[1, 0, translation_value[0]], [0, 1, translation_value[1]], [0, 0, 1]])
    transformed_image = cv2.warpAffine(image, translation_matrix, (width, height), flags=cv2.INTER_LINEAR)
    return transformed_image

# Function to select transformation type
def select_transformation_type():
    transformation_type = st.selectbox("Select Transformation Type", ["Translation", "Rotation", "Scaling", "Shearing"])
    return transformation_type

# Function to set transformation value
def set_transformation_value(transformation_type):
    if transformation_type == 'Translation':
        transformation_value = st.slider("Select Translation (x, y)", -100, 100, (0, 0))
    elif transformation_type == 'Rotation':
        transformation_value = st.slider("Select Rotation (degrees)", -180, 180, 0)
    elif transformation_type == 'Scaling':
        transformation_value = st.slider("Select Scaling Factor", 0.1, 3.0, 1.0)
    else:
        transformation_value = st.slider("Select Shearing Value", -1.0, 1.0, 0.0)
    return transformation_value

# Function to apply transformation
def apply_transformation(image, transformation_type, transformation_value):
    if transformation_type == 'Translation':
        transformed_image = apply_translation(image, transformation_value)
    elif transformation_type == 'Rotation':
        transformed_image = apply_rotation(image, transformation_value)
    elif transformation_type == 'Scaling':
        transformed_image = apply_scaling(image, transformation_value)
    else:
        transformed_image = apply_shearing(image, transformation_value)
    return transformed_image

# Streamlit app
st.title('Image Transformation App')

# Upload an image
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image = cv2.imdecode(np.frombuffer(uploaded_image.read(), np.uint8), cv2.IMREAD_COLOR)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Select transformation type
    transformation_type = select_transformation_type()

    # Set transformation value
    transformation_value = set_transformation_value(transformation_type)

    if st.button("Apply Transformation"):
        transformed_image = apply_transformation(image, transformation_type, transformation_value)
        st.image(transformed_image, caption='Transformed Image', use_column_width=True)
