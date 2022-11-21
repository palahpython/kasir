import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

image = Image.open('kasir.png')
image1 = Image.open('text-kasir.png')

st.image(image,image1, caption=None, width=100, use_column_width=None, clamp=False, channels="RGB", output_format="auto")


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
