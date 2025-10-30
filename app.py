# app.py (Streamlit dashboard)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Game Performance Analyzer", layout="wide")
st.title("🎮 Game Performance Analyzer")

df = pd.read_csv("data/game_performance.csv")
st.sidebar.header("Filters")
game = st.sidebar.selectbox("Game", options=["All"] + sorted(df['Game'].unique().tolist()))
hardware = st.sidebar.selectbox("Hardware", options=["All"] + sorted(df['Hardware'].unique().tolist()))

filtered = df.copy()
if game != "All":
    filtered = filtered[filtered['Game']==game]
if hardware != "All":
    filtered = filtered[filtered['Hardware']==hardware]

st.subheader("Summary")
st.write(filtered.describe())

st.subheader("Avg FPS by Hardware")
fig, ax = plt.subplots()
filtered.groupby('Hardware')['AvgFPS'].mean().sort_values(ascending=False).plot(kind='bar', ax=ax)
ax.set_ylabel("Avg FPS")
st.pyplot(fig)

st.subheader("Load Time (ms) by Game")
fig2, ax2 = plt.subplots()
filtered.groupby('Game')['LoadTimeMs'].mean().plot(kind='bar', ax=ax2)
ax2.set_ylabel("Load Time (ms)")
st.pyplot(fig2)
