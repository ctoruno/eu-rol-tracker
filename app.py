"""
Project:        EU Copilot App
Module Name:    Master app script
Author:         Carlos Alberto Toruño Paniagua
Date:           October 19th, 2023
Description:    This module contains the home page code for the EU Copilot App
This version:   October 23rd, 2023
"""

import streamlit as st
import pandas as pd

# Page config
st.set_page_config(
    page_title = "Home",
    page_icon  = "house"
)

# Reading CSS styles
with open("styles.css") as stl:
    st.markdown(f"<style>{stl.read()}</style>", 
                unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>EU Rule of Law Tracker</h1>", 
            unsafe_allow_html=True)
st.markdown(
    """
    <p class='jtext'>
    Welcome to the EU Rule of Law Tracker, a pilot project aimed at systematically tracking, classifying, 
    and analyzing social and political events related to the rule of law across the 27 member states 
    of the European Union. This initiative makes use of news articles archives and Large Language Models 
    (LLM) in order to produce a systematized database for researchers to assess and validate perceptions 
    on the rule of Law in the targeted countries.
    </p>

    <p class='jtext'>
    For a in-depth description of the conceptual framework, extraction, translation, classification, and
    analysis of the data, please feel free to check the <a href='https://ctoruno.github.io/eu-rol-tracker/'
    target= '_blank'>Methodological Manuscript in this link</a>
    </p>
    """,
    unsafe_allow_html = True
)