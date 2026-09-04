import streamlit as st
import pandas as pd

#--- PAGE CONFIG ---
st.set_page_config(page_title="The Nexus", page_icon="🏜️", layout="wide")

#--- CUSTOM CSS (Sand and Stone Aesthetic) ---
st.markdown(f"""
<style>
/* Main background and text */
.stApp {{ background-color: #f4f1ea; color: #4a4a4a; }}
/* Headers */
h1, h2, h3 {{ color: #4a4a4a !important; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }}
/* Buttons */
.stButton>button {{ background-color: #d4a373; color: white; border-radius: 8px; border: none; padding: 0.5rem 1rem; }}
.stButton>button:hover {{ background-color: #bc8a5f; color: white; }}
/* Sidebar */
[data-testid="stSidebar"] {{ background-color: #e9e5d9; }}
/* Progress bar color */
.stProgress > div > div > div > div {{ background-color: #d4a373; }}
</style>
""", unsafe_allow_html=True)

#--- INITIAL DATA ---
def get_daily_tasks():
    return pd.DataFrame([
        {"Task": "Work: Project Plan (Gemini/SSH)", "Energy": "High", "Status": "Pending"},
        {"Task": "Work: Manager Sync & Invites", "Energy": "Medium", "Status": "Pending"},
        {"Task": "Content: Scripting (Aug 14-25)", "Energy": "High", "Status": "Pending"},
        {"Task": "Personal: Vegas Packing", "Energy": "Medium", "Status": "Pending"},
        {"Task": "Personal: Baby Meal Prep", "Energy": "Medium", "Status": "Pending"},
        {"Task": "Content: Scheduling for Next Week", "Energy": "Low", "Status": "Pending"},
    ])

def get_subway_data():
    return [
        {"Line": "Work: Project Kickoff", "Station": "Plan Draft", "Progress": 20, "Status": "🟡"},
        {"Line": "Content: Sep 14-25", "Station": "Scripting", "Progress": 10, "Status": "🟡"},
        {"Line": "Personal: Vegas Trip", "Station": "Packing", "Progress": 40, "Status": "🟢"},
    ]

#--- NAVIGATION ---
st.sidebar.title("🚉 Nex")
page = st.sidebar.radio("Navigate to:", ["Daily Ticket", "Subway Routes", "Signal Box"])

#--- DAILY TICKET PAGE ---
if page == "Daily Ticket":
    st.title("Your Daily Ticket")
    energy_filter = st.select_slider("Current Energy Unit", options=["Low", "Medium", "High"], value="Medium")
    st.divider()
    tasks = get_daily_tasks()
    filtered_tasks = tasks[tasks['Energy'] == energy_filter]
    st.subheader(f"Optimal Tasks for {energy_filter} Energy:")
    
    for index, row in filtered_tasks.iterrows():
        st.checkbox(f"{row['Task']}", key=f"task_{index}")
        
    st.divider()
    st.caption("Nex Tip: Focus on Work priorities first, then Content, then Personal.")

#--- SUBWAY ROUTES PAGE ---
elif page == "Subway Routes":
    st.title("Strategic Roadmap")
    subway_data = get_subway_data()
    for route in subway_data:
        st.subheader(f"Route: {route['Line']}")
        c1, c2 = st.columns([4, 1])
        with c1:
            st.progress(route['Progress'] / 100)
        with c2:
            st.write(f"{route['Status']} Current: {route['Station']}")
        st.write("---")

#--- SIGNAL BOX ---
elif page == "Signal Box":
    st.title("Signal Box (Blockers)")
    st.error("**Blocker:** Content Shooting is 'Blocked' by Vegas Trip Prep. Complete Baby Meals to clear.")
    st.warning("**Note:** Project Plan needs Manager 'Go-Ahead' session tomorrow.")
    if st.button("Resolve Blocker with First Principles"):
        st.write("Nex: 'If you had to pack in 15 minutes, what is the absolute essential outfit selection?'")

#--- FOOTER ---
st.sidebar.markdown("---")
st.sidebar.caption("System: Sand & Stone v1.0")
st.sidebar.button("Emergency Hibernation (3 Left)")
