import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

image = Image.open('kasir.png')
image1 = Image.open('text-kasir.png')

img = st.image(image, caption=None, width=100, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
img1 = st.image(image1, caption=None, width=100, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
st.write(img,"",img1)


components.html(
    """
    <table>
    <tr>
    <td>HOME</td>
    <td>|<td>
    <td>Help</td>
    </tr>
    </table>
    """,
    height=600,
)
