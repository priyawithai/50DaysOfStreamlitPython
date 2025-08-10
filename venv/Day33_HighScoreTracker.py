# HighScoreTracker.py
import streamlit as st
import pandas as pd
import os

# --- App Config ---
st.set_page_config(page_title="High Score Tracker 🏆", page_icon="🎮", layout="centered")
st.title("🎮 High Score Tracker")
st.subheader("Day 33 — AI Python Challenge 🦅  #FlyHighwithAI")

st.markdown("Add your score and see who’s leading the board! 🏆")

FILE_PATH = "highscores.csv"

# --- Load existing scores ---
if os.path.exists(FILE_PATH):
    scores_df = pd.read_csv(FILE_PATH)
else:
    scores_df = pd.DataFrame(columns=["Player", "Score"])

# --- Player Input ---
player_name = st.text_input("👤 Player Name", placeholder="Enter your name")
player_score = st.number_input("🎯 Score", min_value=0, step=1)

if st.button("💾 Save Score"):
    if player_name.strip():
        # Append new score
        new_entry = pd.DataFrame({"Player": [player_name.strip()], "Score": [player_score]})
        scores_df = pd.concat([scores_df, new_entry], ignore_index=True)
        
        # Save to CSV
        scores_df.to_csv(FILE_PATH, index=False)
        st.success(f"✅ Score for '{player_name.strip()}' saved!")
    else:
        st.error("❌ Please enter a player name before saving.")

# --- Display Scoreboard ---
if not scores_df.empty:
    st.markdown("### 🏆 Scoreboard")
    # Sort by highest score first
    sorted_df = scores_df.sort_values(by="Score", ascending=False).reset_index(drop=True)
    
    # Highlight top scorer
    top_scorer = sorted_df.iloc[0]["Player"]
    st.success(f"🥇 Top Scorer: **{top_scorer}** with {sorted_df.iloc[0]['Score']} points!")
    
    st.dataframe(sorted_df, use_container_width=True)
else:
    st.info("No scores yet. Be the first to play! 🎮")

# --- Clear Scoreboard ---
if st.button("🗑️ Clear Scoreboard"):
    scores_df = pd.DataFrame(columns=["Player", "Score"])
    scores_df.to_csv(FILE_PATH, index=False)
    st.warning("📂 Scoreboard has been cleared!")
