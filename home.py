import streamlit as st

st.write("""
# HOME
""")

dataframe = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
})
st.experimental_show(dataframe)
