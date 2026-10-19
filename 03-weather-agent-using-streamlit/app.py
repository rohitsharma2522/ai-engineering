import streamlit as st
from weather_agent.prompts import build_greeting_prompt, build_weather_prompt



with st.sidebar:
    st.header("About this project")
    st.markdown(build_greeting_prompt())