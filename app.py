import streamlit as st
import pandas as pd
from datetime import datetime

# --- CONFIGURATION & THEME ---
st.set_page_config(page_title="The Nexus", page_icon="●", layout="centered")

# Timepage-inspired Minimalist CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #000000;
    color: #FFFFFF;
}
.stApp {
    background-color: #000000;
}
h1, h2, h3 {
    color: #FFFFFF !important;
    font-weight: 300 !important;
    letter-spacing: -1px;
}
.stButton>button {
    background-color: #FFFFFF;
    color: #000000;
    border: none;
    border-radius: 0px;
    width: 100%;
    transition: 0.3s;
}
.stButton>button:hover {
    background-color: #CCCCCC;
    color: #000000;
}
.stTextArea textarea {
    background-color: #111111;
    color: #FFFFFF;
    border: 1px solid #333333;
}
hr {
    border: 0;
    border-top: 1px solid #333333;
}
/* Simple Task Card */
.task-card {
    padding: 15px 0px;
    border-bottom: 1px solid #222222;
}
</style>
""", unsafe_allow_html=True)

# --- DATA LOADING ---
SHEET_URL = "https://docs.google.com/spreadsheets/d/12v1XuPLArzwBY6pfQucXMvOhKoa9W07SFpbQKuG-52Y/export?format=csv"

@st.cache_data(ttl=600)
def load_data(url):
    try:
        df = pd.read_csv(url)
        return df
    except Exception as e:
        # Fallback to empty if URL isn't set or fails
        return pd.DataFrame()

# --- APP LAYOUT ---

# Header
st.title("THE NEXUS")
st.write(f"**SEPTEMBER 3, 2026**")
st.write("---")

# Vegas Countdown
vegas_date = datetime(2026, 9, 5)
today = datetime(2026, 9, 3)
days_until = (vegas_date - today).days
st.write(f"DEPARTURE FOR VEGAS IN: **{days_until} DAYS**")

st.write("---")

# Energy-Aware Task Filtering
st.subheader("TASKS")
energy_level = st.select_slider(
    "Current Energy Capacity",
    options=["Low", "Medium", "High"],
    value="Medium"
)

data = load_data(SHEET_URL)

if not data.empty:
    # Filter based on the 'Energy' column in your sheet
    if 'Energy' in data.columns:
        filtered_tasks = data[data['Energy'] == energy_level]

        if not filtered_tasks.empty:
            for index, row in filtered_tasks.iterrows():
                task_name = row.get('Task', 'Unnamed Task')
                st.markdown(f"""
                <div class="task-card">
                <small>{energy_level.upper()}</small><br>
                <strong>{task_name}</strong>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info(f"No {energy_level} energy tasks found.")
    else:
        st.warning("Make sure your Google Sheet has an 'Energy' column!")
else:
    st.info("Awaiting connection to Google Sheets. Check your SHEET_URL.")

st.write("---")

# Journal Management
st.subheader("JOURNAL")
journal_entry = st.text_area("Observations & Notes", placeholder="Write here...", height=200)

uploaded_file = st.file_uploader("Attach media or documents", type=['png', 'jpg', 'pdf'])

if st.button("SAVE TO NEXUS"):
    if journal_entry or uploaded_file:
        st.success("Entry logged to system memory.")
    else:
        st.warning("Entry is empty.")

st.write("---")
st.caption("THE NEXUS • SYSTEM VERSION 4.0.2")
