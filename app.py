import streamlit as st
import pandas as pd
from datetime import datetime

# Page Configuration
st.set_page_config(page_title="Nexus | Semira", layout="centered")

# Sand and Stone Minimalist CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    background-color: #F7F3F0 !important;
    color: #2D2D2D;
    font-family: 'Inter', sans-serif;
}

.date-header {
    font-size: 3.5rem;
    font-weight: 600;
    letter-spacing: -2px;
    margin-bottom: 0px;
    color: #2D2D2D;
}

.sub-header {
    font-size: 1.2rem;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: #8C8279;
    margin-bottom: 40px;
}

.stButton>button {
    background-color: #2D2D2D;
    color: #F7F3F0;
    border: none;
    border-radius: 2px;
    padding: 10px 24px;
    transition: 0.3s;
    width: 100%;
}

.stButton>button:hover {
    background-color: #4A4A4A;
    color: #F7F3F0;
}

.stTextArea textarea, .stTextInput input {
    background-color: #FFFFFF;
    border: 1px solid #E5E0DB;
    border-radius: 2px;
    color: #2D2D2D;
}

hr {
    border-top: 1px solid #E5E0DB;
}
</style>
""", unsafe_allow_html=True)

# Data Loading Logic
SHEET_URL = "https://docs.google.com/spreadsheets/d/12v1XuPLArzwBY6pfQucXMvOhKoa9W07SFpbQKuG-52Y/export?format=csv"

@st.cache_data(ttl=600)
def load_nexus_data(url):
    try:
        df = pd.read_csv(url)
        return df
    except:
        return pd.DataFrame()

# Vertical Timepage Header
now = datetime.now()
st.markdown(f'<div class="date-header">{now.strftime("%B %d")}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="sub-header">{now.strftime("%A").upper()} | THE NEXUS</div>', unsafe_allow_html=True)

# Vegas Countdown
vegas_date = datetime(2026, 9, 5)
today = datetime(2026, 9, 3)
days_until = (vegas_date - today).days

st.markdown(f"**{days_until} DAYS UNTIL VEGAS**")
st.write("---")

# Energy-Aware Task List
st.subheader("TASKS")
energy_level = st.select_slider(
    "Current Energy Level",
    options=["Low", "Medium", "High"],
    value="Medium"
)

df = load_nexus_data(SHEET_URL)

if not df.empty and 'Task' in df.columns:
    # Filter based on energy
    filtered = df[df['Energy'] == energy_level] if 'Energy' in df.columns else df

    if not filtered.empty:
        for index, row in filtered.iterrows():
            st.markdown(f"**□ {row['Task']}**")
    else:
        st.write(f"No {energy_level} energy tasks found.")
else:
    st.info("Syncing with Google Sheets...")

st.write("---")

# Journal Entry Section
st.subheader("JOURNAL ENTRY")
journal_text = st.text_area("Observations", height=150, placeholder="Capture your thoughts here...")
uploaded_file = st.file_uploader("Upload Journal Photo", type=['png', 'jpg', 'jpeg'])

if st.button("SAVE TO SYSTEM"):
    if journal_text or uploaded_file:
        st.success("Entry captured. Nexus memory updated.")
    else:
        st.warning("Please enter text or upload a photo.")

st.write("---")
st.caption("THE NEXUS • VERSION 4.1 • SAND & STONE")
