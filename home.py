import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
image = Image.open('kasir.png')

st.image(image, caption='Sunrise by the mountains')
# bootstrap 4 collapse example
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
