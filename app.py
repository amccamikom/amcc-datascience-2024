import streamlit as st
from utils import (
    load_data, filter_data, plot_bar_chart, plot_line_chart,
    plot_boxplot, plot_area_chart, plot_scatter_plot,
    plot_heatmap, plot_pie_chart, plot_bar_chart_multi_col
)

st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")
st.title("🚴‍♀️ Bike Sharing Dashboard")
st.markdown("Explore insights from hourly bike rental data.")

df = load_data()
filtered_df = filter_data(df)

with st.expander("📄 Filtered Data Preview"):
    st.dataframe(filtered_df.head(20), height=250)

tab1, tab2, tab3 = st.tabs(["📊 Overview", "⏱️ Temporal", "🌦️ Weather Factors"])

# ========== TAB 1: OVERVIEW ==========
with tab1:
    col1, col2 = st.columns(2)
    with col1:
        plot_bar_chart(filtered_df, 'season', 'cnt', "Total Rentals by Season")
        with st.container():
            st.markdown("**🔍 Insight:**")
            st.markdown("""
            - Musim panas memiliki jumlah peminjaman tertinggi dibanding musim lain.
            - Peminjaman menurun drastis saat musim dingin.
            - Musim gugur tetap tinggi, menandakan preferensi pengguna di cuaca sedang.
            """)
    with col2:
        plot_pie_chart(filtered_df, 'season', 'cnt', "Rental Proportion by Season")
        with st.container():
            st.markdown("**🔍 Insight:**")
            st.markdown("""
            - Summer dan Fall menyumbang lebih dari 60% total peminjaman.
            - Musim semi berkontribusi paling sedikit.
            - Distribusi menunjukkan pola musiman yang konsisten tiap tahun.
            """)

    col3, col4 = st.columns(2)
    with col3:
        plot_bar_chart_multi_col(filtered_df, ['casual', 'registered'], "Total Rentals: Casual vs Registered")
        with st.container():
            st.markdown("**🔍 Insight:**")
            st.markdown("""
            - Pengguna terdaftar mendominasi peminjaman sepeda.
            - Perbedaan signifikan antara jumlah pengguna casual dan registered.
            - Strategi peningkatan user terdaftar dapat berdampak besar.
            """)
    with col4:
        plot_bar_chart_multi_col(filtered_df, ['temp', 'atemp', 'hum', 'windspeed'], "Average Weather Conditions")
        with st.container():
            st.markdown("**🔍 Insight:**")
            st.markdown("""
            - Temperatur rata-rata berada di kisaran ideal untuk bersepeda.
            - Kelembaban cukup tinggi namun tetap banyak peminjaman.
            - Kecepatan angin rendah mendukung kenyamanan pengguna.
            """)

# ========== TAB 2: TEMPORAL ==========
with tab2:
    col5, col6 = st.columns(2)
    with col5:
        plot_line_chart(filtered_df, 'dteday', 'cnt', "Daily Rental Trend")
        with st.container():
            st.markdown("**🔍 Insight:**")
            st.markdown("""
            - Tren peminjaman meningkat secara signifikan selama musim panas.
            - Ada penurunan drastis saat musim dingin.
            - Pola tren mengikuti kalender musiman.
            """)
    with col6:
        plot_area_chart(filtered_df, ['mnth', 'season'], 'cnt', "Monthly Rentals by Season")
        with st.container():
            st.markdown("**🔍 Insight:**")
            st.markdown("""
            - Bulan-bulan musim panas menunjukkan puncak aktivitas.
            - Kombinasi bulan dan musim memperlihatkan pola peminjaman berulang.
            - Musim dingin menurun drastis meski berada di awal/tengah tahun.
            """)

    plot_bar_chart(filtered_df, 'hr', 'cnt', "Hourly Rental Patterns")
    with st.container():
        st.markdown("**🔍 Insight:**")
        st.markdown("""
        - Jam sibuk pagi (sekitar 8:00) dan sore (sekitar 17:00-18:00) paling padat.
        - Aktivitas ini sesuai dengan jam berangkat dan pulang kerja.
        - Malam hari dan dini hari menunjukkan penurunan tajam.
        """)

# ========== TAB 3: WEATHER ==========
with tab3:
    col7, col8 = st.columns(2)
    with col7:
        plot_scatter_plot(filtered_df, 'temp', 'cnt', 'season', "Temperature vs Rentals")
        with st.container():
            st.markdown("**🔍 Insight:**")
            st.markdown("""
            - Semakin tinggi suhu, semakin tinggi jumlah peminjaman.
            - Efek ini konsisten di semua musim kecuali musim dingin.
            - Titik tertinggi terlihat antara 25-30°C.
            """)
    with col8:
        plot_boxplot(filtered_df, 'weathersit', 'cnt', "Boxplot: Rentals by Weather Condition")
        with st.container():
            st.markdown("**🔍 Insight:**")
            st.markdown("""
            - Cuaca cerah menunjukkan jumlah peminjaman tertinggi.
            - Cuaca buruk (hujan/salju) secara drastis menurunkan jumlah pengguna.
            - Mist (kabut) memiliki variasi tertinggi antar data.
            """)

    plot_heatmap(filtered_df, ['temp', 'atemp', 'hum', 'windspeed', 'casual', 'registered', 'cnt'], "Correlation Heatmap")
    with st.container():
        st.markdown("**🔍 Insight:**")
        st.markdown("""
        - Temperatur memiliki korelasi positif yang kuat dengan total peminjaman.
        - Registered users menunjukkan korelasi paling tinggi terhadap `cnt`.
        - Kelembaban dan kecepatan angin cenderung memiliki korelasi negatif lemah.
        """)
