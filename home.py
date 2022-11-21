import streamlit as st
import streamlit.components.v1 as components

# bootstrap 4 collapse example
components.html(
    """
    <table>
    <div>HOME</div>
    <div>Info</div>
    </table>
    """,
    height=600,
)
