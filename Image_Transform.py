import streamlit as st
import cv2
import numpy as np

# Function to perform affine transformations
def apply_affine_transformation(image, transformation_type, transformation_value):
    height, width = image.shape[:2]
    if transformation_type == 'Translation':
        translation_matrix = np.float32([[1, 0, transformation_value[0]], [0, 1, transformation_value[1]])
        transformed_image = cv2.warpAffine(image, translation_matrix, (width, height))
    elif transformation_type == 'Rotation':
        rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), transformation_value, 1)
        transformed_image = cv2.warpAffine(image, rotation_matrix, (width, height))
    elif transformation_type == 'Scaling':
        scaling_matrix = np.float32([[transformation_value, 0, 0], [0, transformation_value, 0]])
        transformed_image = cv2.warpAffine(image, scaling_matrix, (width, height))
    elif transformation_type == 'Shearing':
        transformed_image = transformed_image = cv2.warpAffine(image, shearing_matrix, (width, height))
    else:
        transformed_image = image
    return transformed_image

# Streamlit app
st.title('Image Transformation App')

# Upload an image
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image = cv2.imdecode(np.fromstring(uploaded_image.read(), np.uint8), cv2.IMREAD_COLOR)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Select transformation type
    transformation_type = st.selectbox("Select Transformation Type", ["Translation", "Rotation", "Scaling", "Flipping"])

    # Set transformation value
    if transformation_type == 'Translation':
        transformation_value = st.slider("Select Translation (x, y)", -100, 100, (0, 0))
    elif transformation_type == 'Rotation':
        transformation_value = st.slider("Select Rotation (degrees)", -180, 180, 0)
    elif transformation_type == 'Scaling':
        transformation_value = st.slider("Select Scaling Factor", 0.1, 3.0, 1.0)
    else:
        transformation_value = None

    if st.button("Apply Transformation"):
        transformed_image = apply_affine_transformation(image, transformation_type, transformation_value)
        st.image(transformed_image, caption='Transformed Image', use_column_width=True)
