import datetime
import cv2
import streamlit as st
import time
st.header("Live Web-Cam")
button = st.button("Open-cam")

if button:
    image = st.image([])
    camera = cv2.VideoCapture(0)
    time.sleep(1)
    while True:
        current_time = datetime.datetime.now()
        current_time = current_time.strftime('%A')
        current_day = time.strftime("%b %d,%Y %H:%M:%S")
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        cv2.putText(frame, text=current_day, org=(25, 30),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(255, 30, 30),
                    thickness=2, lineType=cv2.LINE_AA)
        cv2.putText(frame, text=current_time, org=(25, 60),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(255, 255, 255),
                    thickness=2, lineType=cv2.LINE_AA)
        image.image(frame)
