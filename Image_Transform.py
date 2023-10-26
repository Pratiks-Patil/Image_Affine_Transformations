import streamlit as st
import cv2
import numpy as np

# Function to perform a translation transformation
def apply_translation(image, translation_value):
    height, width = image.shape[:2]
    translation_matrix = np.float32([[1, 0, translation_value[0]], [0, 1, translation_value[1]])
    transformed_image = cv2.warpAffine(image, translation_matrix, (width, height))
    return transformed_image

# Function to perform a rotation transformation
def apply_rotation(image, rotation_angle):
    height, width = image.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), rotation_angle, 1)
    transformed_image = cv2.warpAffine(image, rotation_matrix, (width, height))
    return transformed_image

# Function to perform a scaling transformation
def apply_scaling(image, scaling_factor):
    height, width = image.shape[:2]
    scaling_matrix = np.float32([[scaling_factor, 0, 0], [0, scaling_factor, 0])
    transformed_image = cv2.warpAffine(image, scaling_matrix, (width, height))
    return transformed_image

# Function to perform a shearing transformation
def apply_shearing(image, shearing_value):
    height, width = image.shape[:2]
    shearing_matrix = np.float32([[1, shearing_value, 0], [shearing_value, 1, 0])
    transformed_image = cv2.warpAffine(image, shearing_matrix, (width, height))
    return transformed_image

# Streamlit app
st.title('Image Transformation App')

# Upload an image
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image = cv2.imdecode(np.frombuffer(uploaded_image.read(), np.uint8), cv2.IMREAD_COLOR)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Select transformation type
    transformation_type = st.selectbox("Select Transformation Type", ["Translation", "Rotation", "Scaling", "Shearing"])

    # Set transformation value
    if transformation_type == 'Translation':
        transformation_value = st.slider("Select Translation (x, y)", -100, 100, (0, 0))
    elif transformation_type == 'Rotation':
        transformation_value = st.slider("Select Rotation (degrees)", -180, 180, 0)
    elif transformation_type == 'Scaling':
        transformation_value = st.slider("Select Scaling Factor", 0.1, 3.0, 1.0)
    else:
        transformation_value = st.slider("Select Shearing Value", -1.0, 1.0, 0.0)

    if st.button("Apply Transformation"):
        if transformation_type == 'Translation':
            transformed_image = apply_translation(image, transformation_value)
        elif transformation_type == 'Rotation':
            transformed_image = apply_rotation(image, transformation_value)
        elif transformation_type == 'Scaling':
            transformed_image = apply_scaling(image, transformation_value)
        else:
            transformed_image = apply_shearing(image, transformation_value)

        st.image(transformed_image, caption='Transformed Image', use_column_width=True)
