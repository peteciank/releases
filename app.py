import streamlit as st
from PIL import Image
import io
import random

# Function to generate a random configuration of boxes
def generate_boxes(num_boxes):
    boxes = [{'id': i, 'size': random.uniform(0.1, 0.5), 'position': {'x': random.uniform(0, 1), 'y': random.uniform(0, 1)}}
             for i in range(num_boxes)]
    return boxes

# Streamlit app
def main():
    st.title("Box Game")

    # Create a bigger box (Epic)
    epic_box_image = Image.new('RGB', (400, 400), color='orange')
    st.image(epic_box_image, caption="Epic Box")

    # Get the number of boxes from the user
    num_boxes = st.slider("Select the number of Feature Boxes:", min_value=1, max_value=10, value=5)

    # Generate random boxes
    boxes = generate_boxes(num_boxes)

    # Display Feature Boxes
    for box in boxes:
        box_image = Image.new('RGB', (int(box['size'] * 400), int(box['size'] * 400)), color='violet')
        st.image(box_image, caption="Feature")

    # Create a Release Box (Green)
    release_box_image = Image.new('RGB', (400, 400), color='green')
    st.image(release_box_image, caption="Release Box")

    # Arrow buttons for movement
    st.sidebar.markdown("# Controls")
    selected_box_id = st.sidebar.radio("Select a Feature Box:", [box['id'] for box in boxes], index=0)

    col1, col2, col3 = st.sidebar.columns(3)
    if col2.button("↑"):
        for box in boxes:
            if box['id'] == selected_box_id:
                box['position']['y'] = max(0, box['position']['y'] - 0.1)
        st.experimental_rerun()

    if col1.button("←"):
        for box in boxes:
            if box['id'] == selected_box_id:
                box['position']['x'] = max(0, box['position']['x'] - 0.1)
        st.experimental_rerun()

    if col3.button("→"):
        for box in boxes:
            if box['id'] == selected_box_id:
                box['position']['x'] = min(1 - box['size'], box['position']['x'] + 0.1)
        st.experimental_rerun()

    if col2.button("↓"):
        for box in boxes:
            if box['id'] == selected_box_id:
                box['position']['y'] = min(1 - box['size'], box['position']['y'] + 0.1)
        st.experimental_rerun()

    # Render the updated boxes
    for box in boxes:
        x_pos = int(box['position']['x'] * 400)
        y_pos = int(box['position']['y'] * 400)
        box_image = Image.new('RGB', (int(box['size'] * 400), int(box['size'] * 400)), color='violet')
        epic_box_image.paste(box_image, (x_pos, y_pos))

    st.image(epic_box_image, caption="Epic Box with Feature Boxes")

if __name__ == "__main__":
    main()
