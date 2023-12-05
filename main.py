import streamlit as st
import pandas


st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("./images/photo.jpg")

with col2:
    st.title("Wolfler Guzzo Ferreira")
    content = """
    Lorem incididunt consectetur excepteur ea exercitation amet consectetur quis ea aliquip do. Occaecat deserunt velit nisi anim 
    fugiat in aliquip exercitation. Fugiat ea occaecat laboris eiusmod cillum minim. Deserunt fugiat consectetur eu laborum.
    Aute aliquip sint proident minim magna cillum dolore officia. Ex dolore esse amet consequat. Duis pariatur irure Lorem 
    incididunt Lorem magna cupidatat. Veniam in eu incididunt exercitation incididunt ea nostrud. Enim duis magna cupidatat 
    occaecat laboris ut. Quis nisi sunt consectetur irure non aliqua ea Lorem culpa.
    """
    st.info(content)

content2 = """
    Below you can find some of the apps I have built in Python. Feel free to contact me!
    """
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("./images/" + row["image"])
        st.write("[Source Code]({})".format(row['url']))

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("./images/" + row["image"])
        st.write("[Source Code]({})".format(row['url']))
