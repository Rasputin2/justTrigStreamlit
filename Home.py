import time

import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon=":smiley:",
    layout="wide"
)

st.title("Just Trig!")
st.header("Where You Learn to Love Trigonometry.")

intro_p1 = "If you are sitting in your trigonometry class cursing the Pythagoras's name, then this is the website for you.  As the name suggests, Just Trig focuses solely on trigonometry - from basic - to intermediate - to advanced."

intro_p2 = "We start with the most important question of all - why should I learn this stuff?  We move on from there in easily digestible increments.  Each page shown on the left sidebar reflects a discrete topic.  You can just click on the link on the left sidebar and take it from there.  Each topic is followed by a quiz.  We recommend that you do not move ahead to a subsequent topic before getting ALL (100%) of the questions right on each quiz.  We also recommend that if you get something wrong on a quiz, you step away for a while, think about something else, and then retake the quiz.  This advice is based on the neuroscience of 'chunking' - the idea that the operating system of your brain keeps processing and memorizing information even after you are consciously focused on that task."


def write_intro():
    for word in intro_p1.split():
        yield word + " "
        time.sleep(0.02)

    for word in intro_p2.split():
        yield word + " "
        time.sleep(0.02)


st.write([word for word in intro_p1.split()])
