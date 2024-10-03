import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

# Dataset
all_data_df = pd.read_csv("dashboard/all_data.csv")
all_data_df.reset_index(inplace=True)

# Sidebar
with st.sidebar:
    # Title
    st.title("Bike Sharing Dashboard")
    # Logo
    st.image("dashboard/bike.png")

# Title
st.header("Bike Sharing Dashboard :bike:")

# 1. Data Visualisasi Pengguna Terdaftar dan Kasual Berdasarkan Musim
st.subheader("Perbedaan Pengguna Sepeda Terdaftar dan Kasual Berdasarkan Musim")
seasonal_avg = all_data_df.groupby('season_x').agg({
    'casual_y': 'mean',
    'registered_y': 'mean'
}).reset_index()
seasonal_avg.columns = ['season', 'casual_avg', 'registered_avg']
fig, ax = plt.subplots(figsize=(30, 14))
sns.barplot(x='season', y='casual_avg', data=seasonal_avg, color='skyblue', label='Casual Users')
sns.barplot(x='season', y='registered_avg', data=seasonal_avg, color='lightgreen', label='Registered Users', alpha=0.7)
ax.set_title('Perbandingan Rata-Rata Penyewaan Pengguna Terdaftar dan Kasual Berdasarkan Musim', fontsize=36)
ax.set_xlabel('Musim', fontsize=26)
ax.set_ylabel('Rata-Rata Jumlah Penyewaan', fontsize=26)
ax.tick_params(axis='both', labelsize=22)
ax.legend(loc='upper right')
st.pyplot(plt)

# 2. Data Visualisasi Pola Penggunaan Sepeda Dalam Seminggu
st.subheader("Pola Penggunaan Sepeda Dalam Seminggu")
fig, ax = plt.subplots(figsize=(8, 6))
sns.boxplot(x='weekday_x', y='cnt_x', data=all_data_df)
ax.set_title('Distribusi Penggunaan Sepeda Berdasarkan Hari dalam Seminggu')
ax.set_xlabel('Hari dalam Seminggu (0: Minggu, 6: Sabtu)')
ax.set_ylabel('Total Penggunaan Sepeda')
ax.grid(True)
st.pyplot(fig)

# 3. Tren Penggunaan Sepeda Dalam 24 Jam
hourly_usage = all_data_df.groupby('hr')['cnt_x'].mean().reset_index()
st.subheader("Tren Penggunaan Sepeda Dalam 24 Jam")
fig, ax = plt.subplots(figsize=(35, 14))
sns.lineplot(x='hr', y='cnt_x', data=hourly_usage, marker='o', color='blue')
ax.set_title('Rata-rata Penyewaan Sepeda Berdasarkan Jam dalam Sehari', fontsize=36)
ax.set_xlabel('Jam (0-23)', fontsize=26)
ax.set_ylabel('Jumlah Rata-rata Penyewaan Sepeda', fontsize=26)
ax.tick_params(axis='both', labelsize=22)
ax.grid(True)
st.pyplot(fig)


# Copyright
st.caption('Copyright (C) Aldi Musneldi 2024')
