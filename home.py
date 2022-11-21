import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
image = Image.open('kasir.png')

html = components.html(
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




st.image(image, caption='Sunrise by the mountains',html)
