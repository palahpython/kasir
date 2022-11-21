import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
image = Image.open('kasir.png')
st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")


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
