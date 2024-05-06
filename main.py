import streamlit as st
import requests

api_key = "K3F5shJkjBV1G1eei9bFSo6Sdjeci45AarMNa4AB"
url = ("https://api.nasa.gov/planetary/apod?api_key=K3F5shJkjBV1G1eei9bFSo6Sdjeci45AarMNa4AB")

response = requests.get(url)
content = response.json()

image_response = requests.get(content["url"])
with open("image.jpg", "wb") as file:
    file.write(image_response.content)

st.title(content["title"])
st.text("")

st.image("image.jpg")

st.write(content["explanation"])