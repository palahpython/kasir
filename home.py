import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
image = Image.open('kasir.png')
image0 = Image.open('text-kasir.png')

with tab1:
   st.header("A cat")
   st.image('image, width=200)

with tab2:
   st.header("A dog")
   st.image('image0', width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)


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
