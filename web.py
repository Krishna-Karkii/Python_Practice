import streamlit as st
import plotly.express as px
from backend import get_data

st.header("Weather forecaster web")

place = st.text_input("Place")
days = st.slider("Choose days to forecast", min_value=1, max_value=5,
                 help="Slide to how many days to forecast")
option = st.selectbox("Select a Format: ", ("Temperature", "Sky"))

if place:
    if option == "Temperature":
        try:
            st.subheader(f"{option} for {days} days at {place}")
            data, dates = get_data(place, days, option)
            figure = px.line(x=dates, y=data, labels={"x": "dates", "y": "Temperature"})
            st.plotly_chart(figure)
        except KeyError:
            st.subheader("Please Enter a Valid Name of Place!")

    else:
        try:
            datas, dates = get_data(place, days, option)
            image_paths = []
            for data in datas:
                image_paths.append(f"images/{data.lower()}.png")
            new_datas = [data + 2*"\n" + dates[index] for index, data in enumerate(datas)]
            st.image(image_paths, width=115, caption=new_datas)

        except KeyError:
            st.subheader("Please Enter a Valid Name of Place!")
