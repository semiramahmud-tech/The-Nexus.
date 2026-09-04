import streamlit as st 
from streamlit_gsheets import GSheetsConnection 
import pandas as pd 
from datetime import datetime 

# --- CONFIGURATION --- 
st.set_page_config(page_title="NEXUS", layout="centered") 

# --- STYLE: TIMEPAGE MINIMALISM --- 
st.markdown(""" 
<style> 
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap'); 

html, body, [data-testid="stAppViewContainer"] {
    background-color: #000000; 
    color: #FFFFFF; 
    font-family: 'Inter', sans-serif; 
} 

/* Headers */ 
h1, h2, h3 {
    font-weight: 300 !important; 
    text-transform: uppercase; 
    letter-spacing: 0.1em; 
    color: #FFFFFF; 
    margin-top: 2rem; 
} 

.date-header {
    font-size: 5rem; 
    font-weight: 900; 
    margin-bottom: 0px; 
    line-height: 1; 
} 

.date-sub {
    font-size: 1.2rem; 
    color: #888; 
    text-transform: uppercase; 
    letter-spacing: 0.3em; 
    margin-bottom: 4rem; 
} 

/* Vertical Timeline */ 
.timeline-container {
    border-left: 1px solid #333; 
    padding-left: 30px; 
    margin-left: 10px; 
} 

.timeline-item {
    margin-bottom: 40px; 
    position: relative; 
} 

.timeline-item::before {
    content: ''; 
    position: absolute; 
    left: -36px; 
    top: 8px; 
    width: 10px; 
    height: 10px; 
    background-color: #FFFFFF; 
    border-radius: 50%; 
} 

/* Input Styling */ 
.stTextInput input, .stTextArea textarea, .stSelectbox [data-baseweb="select"] {
    background-color: #111 !important; 
    color: white !important; 
    border-radius: 0px !important; 
    border: 1px solid #333 !important; 
} 

/* Button Styling */ 
.stButton>button {
    background-color: #FFFFFF; 
    color: #000000; 
    border-radius: 0px; 
    font-weight: 700; 
}
</style>
""", unsafe_allow_html=True)
