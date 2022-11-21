import streamlit as st
import streamlit.components.v1 as components

# bootstrap 4 collapse example
components.html(
    """
    <table>
    <tr>
    <div>HOME</div>
    <div>Info</div>
    </tr>
    </table>
    """,
    height=600,
)
