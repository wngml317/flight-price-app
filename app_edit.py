import streamlit as st


def edit_txt(txt) : 
    html_temp  = f"""
    <h5 style = "text_align:center; font-weight: bold;"> {txt} </h5>
    """
    st.markdown(html_temp, unsafe_allow_html = True)


